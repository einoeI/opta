"""otpa update: live API calls, each saved as a dated snapshot (the only network access).
otpa cves: snapshots + change-notes + components -> devices/<d>/cves.csv, offline, deterministic.

Sources and what they decide:
  override      overrides.csv in the device folder, hand-written with reason + source (wins)
  change-notes  vendor CSV of CVEs still in this firmware            -> Version-candidate
  csaf          vendor CSAF advisories (installed_on firmware range) -> Version-candidate / Not-affected
  osv           OSV.dev per component with a purl                    -> Version-candidate
  circl         CIRCL device search; version range of the CVE record -> Version-candidate / Not-affected
  CVSS: NVD when fetched (`update --cvss`), else the vendor's score from CSAF, else empty.
The highest tier with an opinion decides (vendor > osv > circl); within it, affected wins."""
import json
import os
import re
import time
import urllib.parse

import yaml

from otpa import OtpaError, manifest, sources
from otpa.engagement import device_dir
from otpa.modules.components import catalog_lookup, load_catalog, read_csv, write_csv

COLUMNS = ["cve", "component", "version", "source", "cvss_version", "score", "vector",
           "cvss_source", "reachable", "label", "vendor_fixed_in", "note"]
TIER = {"override": -1, "change-notes": 0, "csaf": 0, "osv": 1, "circl": 2}


def register(sub):
    p = sub.add_parser("update", help="fetch vulnerability data for a device (network)")
    p.add_argument("device")
    p.add_argument("--cvss", action="store_true",
                   help="also fetch NVD CVSS for every CVE (slow without NVD_API_KEY); "
                        "otherwise the vendor's CSAF scores are used where they exist")
    p.set_defaults(run=update)
    p = sub.add_parser("cves", help="build cves.csv for a device from its snapshots (offline)")
    p.add_argument("device")
    p.set_defaults(run=build)


def load_device(dev):
    d = yaml.safe_load((dev / "device.yaml").read_text(encoding="utf-8")) or {}
    missing = [k for k in ("model", "article_no", "firmware") if not d.get(k)]
    if missing:
        raise OtpaError(f"{dev / 'device.yaml'}: missing {', '.join(missing)}")
    return {**d, "article_no": str(d["article_no"]), "firmware": str(d["firmware"])}


def _change_notes(dev, device):
    name = (device.get("evidence_sources") or {}).get("change_notes")
    return dev / name if isinstance(name, str) else None


def _osv_key(c):
    return f"{c['name']}@{c['version']}"


def collect(dev, device, catalog, components):
    """{cve: [(tier, source, label, component, fixed_in, note)]} from local files only."""
    obs = {}

    def add(cve, source, label, component, fixed="", note=""):
        obs.setdefault(cve.upper(), []).append(
            (TIER[source.split(":")[0]], source, label, component, fixed, note))

    model, article, fw = device["model"], device["article_no"], device["firmware"]
    for r in read_csv(dev / "overrides.csv"):
        if r["label"] not in ("Version-candidate", "Not-affected") or not r["reason"] or not r["source_url"]:
            raise OtpaError(f"overrides.csv {r['cve']}: label must be Version-candidate or "
                            "Not-affected, reason and source_url are required")
        add(r["cve"], "override", r["label"], "", r["fixed_in"], f"override: {r['reason']}")
    notes = _change_notes(dev, device)
    for r in read_csv(notes) if notes else []:
        cat = catalog_lookup(catalog, r["component"])
        add(r["cve"], "change-notes", "Version-candidate", cat["name"] if cat else r["component"],
            r.get("first_fixed_in", ""), r.get("note", ""))
    for key, path in sorted(sources.latest_snapshots(dev, "csaf").items()):
        adv = json.loads(path.read_bytes())
        aid = adv.get("document", {}).get("tracking", {}).get("id", key)
        for cve, (label, fixed) in sources.csaf_status(adv, model, article, fw).items():
            note = f"{aid}: known affected" if label == "Version-candidate" else \
                f"{aid}: fixed or not affected in this firmware"
            add(cve, f"csaf:{aid}", label, "firmware", fixed, note)
    records = {}
    for path in sources.latest_snapshots(dev, "circl-search").values():
        for rows in json.loads(path.read_bytes()).get("results", {}).values():
            for cve, rec in rows:
                records.setdefault(cve.upper(), []).append(rec)
    for cve, recs in records.items():
        results = [sources.cve_record_status(r, model, article, fw) for r in recs]
        status = [s for s, _ in results]
        if True in status:
            add(cve, "circl", "Version-candidate", "firmware")
        elif False in status:
            add(cve, "circl", "Not-affected", "firmware", max(f for s, f in results if s is False),
                "CVE record: firmware outside affected versions")
        else:
            add(cve, "circl", "Version-candidate", "firmware", note="CVE record: no usable version range")
    osv = sources.latest_snapshots(dev, "osv")
    for c in components:
        path = osv.get(sources._safe(_osv_key(c)))
        for cve, osv_id, fixed in sources.osv_vulns(json.loads(path.read_bytes())) if path else []:
            add(cve, "osv", "Version-candidate", c["name"], fixed, osv_id if osv_id != cve else "")
    return obs


def merge(observations):
    obs = sorted(observations)
    top = [o for o in obs if o[0] == obs[0][0]]
    label = "Version-candidate" if any(o[2] == "Version-candidate" for o in top) else "Not-affected"
    fixed = {f for o in top if o[2] == label for f in o[4].split("; ") if f}
    return {"component": next((o[3] for o in obs if o[3]), ""),
            "source": ";".join(sorted({o[1] for o in obs})),
            "label": label,
            "vendor_fixed_in": "; ".join(sorted(fixed, key=sources._vkey)),
            "note": "; ".join(sorted({o[5] for o in obs if o[5]}))}


def _cve_key(cve):
    m = re.fullmatch(r"CVE-(\d+)-(\d+)", cve)
    return (0, int(m[1]), int(m[2]), "") if m else (1, 0, 0, cve)


def build(args, argv):
    dev = device_dir(args.workspace, args.device)
    device = load_device(dev)
    components = read_csv(dev / "components.csv")
    versions = {}
    for c in components:
        versions.setdefault(c["name"].casefold(), set()).add(c["version"])
    nvd = sources.latest_snapshots(dev, "nvd")
    vendor_scores = {}
    for key, path in sorted(sources.latest_snapshots(dev, "csaf").items()):
        adv = json.loads(path.read_bytes())
        aid = adv.get("document", {}).get("tracking", {}).get("id", key)
        for cve, scores in sources.csaf_scores(adv).items():
            vendor_scores.setdefault(cve, (scores, f"csaf:{aid}"))
    rows = []
    for cve, obs in collect(dev, device, load_catalog(), components).items():
        row = {"cve": cve, **merge(obs), "reachable": "unknown"}
        row["version"] = "; ".join(sorted(versions.get(row["component"].casefold(), [])))
        path = nvd.get(sources._safe(cve))
        cvss, cvss_source = (sources.nvd_cvss(json.loads(path.read_bytes())), "nvd") if path else ([], "")
        if not cvss:
            cvss, cvss_source = vendor_scores.get(cve, ([], ""))
        for version, score, vector in cvss or [("", "", "")]:
            rows.append(row | {"cvss_version": version, "score": score, "vector": vector,
                               "cvss_source": cvss_source if version else ""})
    rows.sort(key=lambda r: (_cve_key(r["cve"]), r["cvss_version"]))
    out = dev / "cves.csv"
    notes = _change_notes(dev, device)
    with manifest.record(dev, argv) as entry:
        write_csv(out, rows, COLUMNS)
        entry["inputs"] = [p for p in (dev / "device.yaml", dev / "components.csv", dev / "overrides.csv", notes)
                           if p and p.exists()]
        entry["snapshots"] = sorted(str(p.relative_to(dev)) for p in (dev / "snapshots").glob("*/*/*.json"))
        entry["outputs"] = [out]
    labels = [r["label"] for r in {r["cve"]: r for r in rows}.values()]
    print(f"{out}: {len(labels)} CVEs, {labels.count('Version-candidate')} Version-candidate, "
          f"{labels.count('Not-affected')} Not-affected")
    unmapped = [c["name"] for c in components if c["mapped"] == "no"]
    if unmapped:
        print(f"not looked up (unmapped): {', '.join(unmapped)}")


def update(args, argv):
    dev = device_dir(args.workspace, args.device)
    device = load_device(dev)
    today = time.strftime("%Y-%m-%d")
    saved, failed = [], []

    def fetch(source, key, url, data=None, headers=None):
        try:
            body = sources.http_get(url, data, headers)
            saved.append(sources.save_snapshot(dev, source, key, url, body, today))
            return body
        except OSError as e:  # URLError and HTTPError are OSErrors
            failed.append(f"{source} {key}: {e}")
            print(f"failed: {source} {key}: {e}")

    with manifest.record(dev, argv) as entry:
        for vendor, product in device.get("circl_products") or []:
            url = sources.CIRCL_SEARCH.format(urllib.parse.quote(vendor), urllib.parse.quote(product))
            page, pages = 1, 1
            while page <= pages:  # paginated: 10 per page by default
                body = fetch("circl-search", f"{vendor}__{product}__p{page}", f"{url}?per_page=100&page={page}")
                pages = -(-json.loads(body).get("total_count", 0) // 100) if body else 0
                page += 1
                time.sleep(0.25)
        if device.get("csaf_feed"):
            feed = fetch("csaf-feed", "feed", device["csaf_feed"])
            entries = json.loads(feed).get("feed", {}).get("entry", []) if feed else []
            for i, e in enumerate(entries, 1):
                if e.get("id") and e.get("content", {}).get("src"):
                    fetch("csaf", e["id"], e["content"]["src"])
                if i % 25 == 0:
                    print(f"  csaf {i}/{len(entries)}")
        for c in read_csv(dev / "components.csv"):
            if c["purl"]:
                query = {"package": {"purl": c["purl"]}} | ({} if "@" in c["purl"] else {"version": c["version"]})
                fetch("osv", _osv_key(c), sources.OSV_QUERY, json.dumps(query).encode())
        # NVD (CVSS, only with --cvss) for every known CVE that has no NVD snapshot yet.
        cves = {} if not args.cvss else collect(dev, device, load_catalog(), read_csv(dev / "components.csv"))
        have = sources.latest_snapshots(dev, "nvd")
        todo = sorted(c for c in cves if c.startswith("CVE-") and sources._safe(c) not in have)
        key = os.environ.get("NVD_API_KEY")
        if todo:
            print(f"NVD: {len(todo)} CVEs, ~{len(todo) * (1 if key else 7) // 60 + 1} min"
                  + ("" if key else " (set NVD_API_KEY to go 10x faster)"))
        for i, cve in enumerate(todo, 1):
            fetch("nvd", cve, sources.NVD_CVE.format(cve), headers={"apiKey": key} if key else None)
            time.sleep(0.7 if key else 6.5)  # NVD limit: 5 per 30 s without key, 50 with
            if i % 25 == 0:
                print(f"  nvd {i}/{len(todo)}")
        entry["snapshots"] = sorted(str(p.relative_to(dev)) for p in saved)
        if failed:
            entry["failed"] = failed
    print(f"{len(saved)} snapshots saved, {len(failed)} failed")
    return 1 if failed else 0
