#!/usr/bin/env python3
"""Cross-check the vendor's authoritative "affects firmware 2022.0.8" CVE list
against CIRCL Vulnerability-Lookup.

Input CSV (from the official PLCnext AXC F 2152 change notes) lists component
CVEs still present on 2022.0.8 -- i.e. everything fixed in a LATER firmware.
This script:
  1. enriches each CVE with CVSS/severity from CIRCL (lookup by CVE id),
  2. flags which ones a DEVICE-level search (axc f 2152) would catch -- the
     point being almost none, because component CVEs carry no device CPE,
  3. writes an enriched, severity-sorted CSV a pentester can actually use.

Lookups are cached to disk so re-runs are instant and don't hammer the API.
stdlib only.

Usage:
    python3 crosscheck_firmware.py --csv path/to/change-notes.csv
    python3 crosscheck_firmware.py --selftest
"""
import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

VULN = "https://vulnerability.circl.lu/api/vulnerability/"
SEARCH = "https://vulnerability.circl.lu/api/search/"
DEVICE_ALIASES = [  # (vendor, product) keys that resolve to the AXC F 2152
    ("phoenix contact", "axc f 2152 (2404267)"),
    ("phoenixcontact", "axc_f_2152_firmware"),
    ("phoenixcontact", "axc_f_2152"),
]
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "workspace", "devices", "phoenix-contact", "axc-f-2152", "2022.0.8")
CACHE = os.path.join(HERE, "snapshots", "circl_cache.json")
SEV_RANK = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1, "": 0, None: 0}


def _get(url, timeout=30):
    req = urllib.request.Request(url, headers={"Accept": "application/json",
                                               "User-Agent": "ot-pentesting-probe"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def _find_all(obj, key, out):
    if isinstance(obj, dict):
        if key in obj:
            out.append(obj[key])
        for v in obj.values():
            _find_all(v, key, out)
    elif isinstance(obj, list):
        for v in obj:
            _find_all(v, key, out)
    return out


def best_cvss(record):
    """Highest baseScore anywhere in the record, and matching severity."""
    scores = [s for s in _find_all(record, "baseScore", []) if isinstance(s, (int, float))]
    sevs = [s for s in _find_all(record, "baseSeverity", []) if isinstance(s, str)]
    cvss = max(scores) if scores else None
    sev = max(sevs, key=lambda s: SEV_RANK.get(s.upper(), 0)).upper() if sevs else sev_from_score(cvss)
    return cvss, sev


def sev_from_score(cvss):
    if cvss is None:
        return ""
    if cvss >= 9.0:
        return "CRITICAL"
    if cvss >= 7.0:
        return "HIGH"
    if cvss >= 4.0:
        return "MEDIUM"
    return "LOW"


def load_cache():
    try:
        with open(CACHE) as f:
            return json.load(f)
    except Exception:
        return {}


def save_cache(c):
    try:
        with open(CACHE, "w") as f:
            json.dump(c, f)
    except Exception:
        pass


def lookup(cve, cache):
    """Return {found, cvss, severity}. A real 404 is cached as not-found; a
    throttle/network error backs off, retries, and is NOT cached (so re-runs
    retry it instead of poisoning the cache)."""
    cve = cve.upper().strip()
    if cve in cache:
        return cache[cve]
    for attempt in range(4):
        try:
            rec = _get(VULN + urllib.parse.quote(cve))
            cvss, sev = best_cvss(rec) if rec else (None, "")
            cache[cve] = {"found": bool(rec), "cvss": cvss, "severity": sev}
            time.sleep(0.25)  # ponytail: polite pacing; cache makes it one-time
            return cache[cve]
        except urllib.error.HTTPError as e:
            if e.code == 404:  # genuinely not in CIRCL
                cache[cve] = {"found": False, "cvss": None, "severity": ""}
                return cache[cve]
            time.sleep(1.5 * (attempt + 1))  # 429/5xx -> back off
        except Exception:
            time.sleep(1.5 * (attempt + 1))
    return {"found": None, "cvss": None, "severity": ""}  # error, uncached -> retry next run


def device_search_hits():
    """CVE ids a device-level search returns -- the set the CPE/CSAF spine 'sees'."""
    hits = set()
    for vendor, product in DEVICE_ALIASES:
        url = SEARCH + urllib.parse.quote(vendor) + "/" + urllib.parse.quote(product)
        try:
            data = _get(url)
        except Exception:
            continue
        for rows in data.get("results", {}).values():
            for row in rows:
                hits.add(str(row[0]).upper())
    return hits


def read_csv(path):
    with open(path, newline="") as f:
        return [r for r in csv.DictReader(f) if r.get("cve")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=os.path.join(HERE, "change-notes.csv"))
    ap.add_argument("--out", default=os.path.join(HERE, "enriched.csv"))
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    rows = read_csv(args.csv)
    print(f"# Firmware 2022.0.8 cross-check -- {len(rows)} CVEs from vendor change notes\n")

    print("Enriching via CIRCL (cached)...", flush=True)
    cache = load_cache()
    enriched = []
    for i, r in enumerate(rows, 1):
        info = lookup(r["cve"], cache)
        in_circl = {True: "yes", False: "NO", None: "error"}[info["found"]]
        enriched.append({**r,
                         "cvss": info["cvss"] if info["cvss"] is not None else "",
                         "severity": info["severity"],
                         "in_circl": in_circl})
        if i % 50 == 0:
            print(f"  {i}/{len(rows)}", flush=True)
            save_cache(cache)
    save_cache(cache)

    print("\nChecking what a device-level search would catch...", flush=True)
    dev = device_search_hits()
    for e in enriched:
        e["caught_by_device_search"] = "yes" if e["cve"].upper() in dev else "no"

    # Write enriched CSV (the usable pentester output)
    cols = ["cve", "component", "first_fixed_in", "listed_in", "note",
            "cvss", "severity", "in_circl", "caught_by_device_search"]
    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for e in sorted(enriched, key=lambda x: (x["cvss"] if isinstance(x["cvss"], (int, float)) else -1),
                        reverse=True):
            w.writerow({k: e.get(k, "") for k in cols})

    # Summary
    found = sum(1 for e in enriched if e["in_circl"] == "yes")
    caught = sum(1 for e in enriched if e["caught_by_device_search"] == "yes")
    missing = [e["cve"] for e in enriched if e["in_circl"] == "NO"]
    crit = sum(1 for e in enriched if e["severity"] == "CRITICAL")
    high = sum(1 for e in enriched if e["severity"] == "HIGH")

    print("\n## Summary")
    print(f"  CVEs affecting 2022.0.8 (vendor ground truth): {len(enriched)}")
    print(f"  Enriched by CIRCL (found, got CVSS):           {found}  ({found*100//len(enriched)}%)")
    print(f"  CRITICAL: {crit}   HIGH: {high}")
    print(f"  Caught by DEVICE-level search (axc f 2152):    {caught}  <-- the gap")
    if missing:
        print(f"  NOT in CIRCL ({len(missing)}) -> rely on vendor CSV: {', '.join(missing[:8])}"
              + (" ..." if len(missing) > 8 else ""))

    print("\n## Top 15 by CVSS (prioritised, version-CANDIDATES on 2022.0.8)")
    top = sorted(enriched, key=lambda x: (x["cvss"] if isinstance(x["cvss"], (int, float)) else -1),
                 reverse=True)[:15]
    for e in top:
        print(f"    {e['cve']:<18} {str(e['cvss']):<4} {e['severity']:<8} "
              f"{e['component']:<12} fixed_in={e['first_fixed_in']}")

    print(f"\nWrote enriched CSV -> {args.out}")
    print("NOTE: 'affects 2022.0.8' is vendor ground truth; CVSS is context, not a")
    print("confirmed-exploitable verdict. Reproduce before labelling anything Reproduced.")
    return 0


def selftest():
    rec = {"containers": {"cna": {"metrics": [{"cvssV3_1": {"baseScore": 5.5, "baseSeverity": "MEDIUM"}}]},
                          "adp": [{"metrics": [{"cvssV3_1": {"baseScore": 7.5, "baseSeverity": "HIGH"}}]}]}}
    cvss, sev = best_cvss(rec)
    assert cvss == 7.5 and sev == "HIGH", (cvss, sev)      # takes the highest
    assert best_cvss({}) == (None, ""), best_cvss({})      # empty is safe
    assert sev_from_score(9.1) == "CRITICAL" and sev_from_score(None) == ""
    print("selftest OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
