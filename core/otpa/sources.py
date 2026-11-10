"""Vulnerability sources: HTTP + snapshots (live, `otpa update` only) and pure parsers
(offline, read snapshots). Response shapes were checked against the live APIs on 2026-11-10."""
import csv
import hashlib
import re
import time
import urllib.error
import urllib.request

from otpa import __version__

CIRCL_SEARCH = "https://vulnerability.circl.lu/api/search/{}/{}"
NVD_CVE = "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={}"
OSV_QUERY = "https://api.osv.dev/v1/query"
AFFECTED = ("known_affected", "first_affected", "last_affected")
NOT_AFFECTED = ("fixed", "first_fixed", "known_not_affected")


def http_get(url, data=None, headers=None):
    """GET (or POST when data is given) with backoff on 429/5xx/network errors."""
    req = urllib.request.Request(url, data=data, headers={
        "Accept": "application/json", "Content-Type": "application/json",
        "User-Agent": f"otpa/{__version__}", **(headers or {})})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code != 429 and e.code < 500 or attempt == 3:
                raise
        except urllib.error.URLError:
            if attempt == 3:
                raise
        time.sleep(2 ** (attempt + 1))


# --- snapshots: snapshots/<date>/<source>/<key>.json, listed with SHA-256 in snapshots/index.csv

def _safe(key):
    return re.sub(r"[^A-Za-z0-9._@-]+", "_", key)


def save_snapshot(dev_dir, source, key, url, body, date):
    path = dev_dir / "snapshots" / date / source / f"{_safe(key)}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    index = dev_dir / "snapshots" / "index.csv"
    new = not index.exists()
    with open(index, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        if new:
            w.writerow(["date", "source", "key", "url", "sha256"])
        w.writerow([date, source, key, url, hashlib.sha256(body).hexdigest()])
    return path


def latest_snapshots(dev_dir, source):
    """{key: path} of the newest snapshot per key. Dates are ISO, so name order is time order."""
    found = {}
    for path in sorted((dev_dir / "snapshots").glob(f"*/{source}/*.json")):
        found[path.stem] = path
    return found


# --- versions

def version_tuple(text):
    nums = re.findall(r"\d+", str(text))
    return tuple(int(n) for n in nums) if nums else None


def _vkey(text):
    return version_tuple(text) or (), text


def in_range(version, expr):
    """True/False whether version satisfies expr ("<2022.0.8 LTS", "2022.0.8",
    "vers:intdot/>=1|<2"); None if a version has no digits.
    ponytail: numeric-tuple compare, no pre-release handling; fine for vendor firmware numbers."""
    v = version_tuple(version)
    expr = re.sub(r"^vers:[^/]*/", "", expr.strip())
    ops = {"<": tuple.__lt__, "<=": tuple.__le__, ">": tuple.__gt__, ">=": tuple.__ge__,
           "=": tuple.__eq__, "!=": tuple.__ne__}
    for part in expr.split("|"):
        op, ref = re.match(r"\s*(<=|>=|!=|<|>|=)?\s*(.*)", part).groups()
        ref = version_tuple(ref)
        if v is None or ref is None:
            return None
        if not ops[op or "="](v, ref):
            return False
    return True


# --- parsers

def _branches(node):
    for b in node.get("branches", []):
        yield b
        yield from _branches(b)


def csaf_status(adv, model, article_no, firmware):
    """{cve: (label, fixed_in)} for this device + firmware, from installed_on relationships."""
    tree = adv.get("product_tree", {})
    names = {b["product"]["product_id"]: b for b in _branches(tree) if "product" in b}
    hardware = {pid for pid, b in names.items()
                if b["category"] == "product_name" and (
                    article_no in b["product"].get("product_identification_helper", {}).get("model_numbers", [])
                    or b["name"].casefold() == model.casefold())}
    ours, fixed_versions = set(), {}
    for rel in tree.get("relationships", []):
        if rel.get("category") != "installed_on" or rel["relates_to_product_reference"] not in hardware:
            continue
        fw = names.get(rel["product_reference"])
        if fw is None:
            continue
        pid = rel["full_product_name"]["product_id"]
        if in_range(firmware, fw["name"]):
            ours.add(pid)
        if fw["category"] == "product_version":
            fixed_versions[pid] = fw["name"]
    result = {}
    for vuln in adv.get("vulnerabilities", []):
        status = vuln.get("product_status", {})
        hit = lambda keys: ours & {p for k in keys for p in status.get(k, [])}
        if not vuln.get("cve"):
            continue
        if hit(AFFECTED):
            fixed = sorted({fixed_versions[p] for k in NOT_AFFECTED for p in status.get(k, [])
                            if p in fixed_versions}, key=_vkey)
            result[vuln["cve"]] = ("Version-candidate", "; ".join(fixed))
        elif hit(NOT_AFFECTED):
            result[vuln["cve"]] = ("Not-affected", "")
    return result


def cve_record_status(record, model, article_no, firmware):
    """(in_range, fixed_in) from a CVE 5 record's affected list. in_range is None when the
    record has no version range for this model (common: 'n/a', or only in the description)."""
    results, fixed = [], set()
    for a in record.get("containers", {}).get("cna", {}).get("affected", []):
        product_match = str(a.get("product", "")).casefold() == model.casefold()
        for v in a.get("versions", []):
            label = str(v.get("version", ""))
            if v.get("status") != "affected":
                continue
            if not (product_match or model.casefold() in label.casefold() or article_no in label):
                continue
            parts = []
            if v.get("lessThan"):
                parts.append("<" + v["lessThan"])
                fixed.add(v["lessThan"])
            if v.get("lessThanOrEqual"):
                parts.append("<=" + v["lessThanOrEqual"])
            if product_match and label not in ("0", "*", ""):
                parts.append((">=" if parts else "=") + label)
            if parts:
                results.append(in_range(firmware, "|".join(parts)))
    status = True if True in results else False if False in results else None
    return status, ("; ".join(sorted(fixed, key=_vkey)) if status is False else "")


def nvd_cvss(resp):
    """[(cvss_version, score, vector)] for every CVSS version NVD has, Primary source first."""
    found = {}
    for v in resp.get("vulnerabilities", []):
        for key, metrics in v["cve"].get("metrics", {}).items():
            if key.startswith("cvssMetricV"):
                for m in sorted(metrics, key=lambda m: m.get("type") != "Primary"):
                    d = m["cvssData"]
                    found.setdefault(d["version"], (d["version"], d["baseScore"], d["vectorString"]))
    return sorted(found.values())


def csaf_scores(adv):
    """{cve: [(cvss_version, score, vector)]} as scored by the vendor in a CSAF advisory."""
    out = {}
    for vuln in adv.get("vulnerabilities", []):
        found = {}
        for s in vuln.get("scores", []):
            for key in ("cvss_v2", "cvss_v3", "cvss_v4"):
                d = s.get(key)
                if d and d.get("version") and "baseScore" in d:
                    found.setdefault(d["version"], (d["version"], d["baseScore"], d.get("vectorString", "")))
        if vuln.get("cve") and found:
            out[vuln["cve"]] = sorted(found.values())
    return out


def osv_vulns(resp):
    """[(cve_or_osv_id, osv_id, fixed_versions)], sorted."""
    out = []
    for v in resp.get("vulns", []):
        cve = next((a for a in sorted(v.get("aliases", [])) if a.startswith("CVE-")), v["id"])
        fixed = sorted({e["fixed"] for a in v.get("affected", []) for r in a.get("ranges", [])
                        for e in r.get("events", []) if "fixed" in e}, key=_vkey)
        out.append((cve, v["id"], "; ".join(fixed)))
    return sorted(out)
