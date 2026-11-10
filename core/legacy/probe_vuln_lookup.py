#!/usr/bin/env python3
"""Verification probe: does CIRCL Vulnerability-Lookup cover a given OT device,
and is the vendor's CSAF provider (CERT@VDE for Phoenix Contact) reachable as a
direct fallback?

Two independent checks, stdlib only:
  1. CIRCL public API  -> /api/search/<vendor>/<product>  (the proposed spine)
  2. CERT@VDE CSAF feed -> the authoritative vendor source, as cross-check

Defaults target the testbed's Phoenix Contact AXC F 2152 (article 2404267).
Prints a candidate CVE list (NOT a vulnerability verdict -- version match is
only "version-candidate" until a test reproduces it) and a coverage verdict.

Usage:
    python3 probe_vuln_lookup.py                 # AXC F 2152 defaults
    python3 probe_vuln_lookup.py --vendor "phoenix contact" --product "axc f 2152 (2404267)"
    python3 probe_vuln_lookup.py --selftest      # offline parser check
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request

API = "https://vulnerability.circl.lu/api/search/"
CERTVDE_FEED = ("https://phoenixcontact.csaf-tp.certvde.com"
                "/.well-known/csaf/white/csaf-feed-tlp-white.json")


def _get(url, timeout=30):
    req = urllib.request.Request(url, headers={"Accept": "application/json",
                                               "User-Agent": "ot-pentesting-probe"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def _find_first(obj, key):
    """First value for `key` anywhere in a nested dict/list, else None."""
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        for v in obj.values():
            hit = _find_first(v, key)
            if hit is not None:
                return hit
    elif isinstance(obj, list):
        for v in obj:
            hit = _find_first(v, key)
            if hit is not None:
                return hit
    return None


def extract(cve_id, record):
    """Pull the few fields a tester cares about, defensively across source shapes."""
    cna = record.get("containers", {}).get("cna", {}) if isinstance(record, dict) else {}
    return {
        "id": (cve_id or _find_first(record, "cveId") or "?").upper(),
        "cvss": _find_first(record, "baseScore"),
        "severity": _find_first(record, "baseSeverity"),
        "assigner": _find_first(record, "assignerShortName"),
        "advisory": _find_first(record, "advisory"),
        "title": (cna.get("title")
                  or (cna.get("descriptions") or [{}])[0].get("value")
                  or ""),
    }


def search_circl(vendor, product):
    url = API + urllib.parse.quote(vendor) + "/" + urllib.parse.quote(product)
    data = _get(url)
    results = data.get("results", {})
    findings = {}  # cve_id -> extracted (deduped across sources)
    sources = {}   # cve_id -> set of source names
    for source, rows in results.items():
        for row in rows:
            cve_id, record = row[0], row[1]
            f = extract(cve_id, record)
            findings.setdefault(f["id"], f)
            sources.setdefault(f["id"], set()).add(source)
    for cid, f in findings.items():
        f["sources"] = sorted(sources[cid])
    return url, data.get("total_count"), findings


def check_certvde():
    """Independent reachability + count of the authoritative vendor CSAF feed."""
    try:
        feed = _get(CERTVDE_FEED)
    except Exception as e:  # network/DNS/TLS -- report, don't crash the probe
        return None, f"unreachable: {e}"
    # ROLIE feed: feed.feed.entry is a list of advisory entries
    entries = _find_first(feed, "entry") or []
    return len(entries), "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vendor", default="phoenix contact")
    ap.add_argument("--product", default="axc f 2152 (2404267)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    print(f"# Target: {args.vendor} / {args.product}\n")

    print("## 1. CIRCL Vulnerability-Lookup (proposed spine)")
    try:
        url, total, findings = search_circl(args.vendor, args.product)
    except Exception as e:
        print(f"  ERROR querying CIRCL: {e}")
        return 2
    print(f"  {url}")
    print(f"  total_count={total}  unique CVEs={len(findings)}")
    certvde_assigned = 0
    for f in sorted(findings.values(), key=lambda x: x["id"]):
        cvss = f["cvss"] if f["cvss"] is not None else "-"
        assigner = f["assigner"] or "-"
        if assigner == "CERTVDE":
            certvde_assigned += 1
        adv = f" [{f['advisory']}]" if f["advisory"] else ""
        print(f"    {f['id']:<18} CVSS {str(cvss):<4} {str(f['severity'] or ''):<8} "
              f"src={','.join(f['sources'])} assigner={assigner}{adv}")
        if f["title"]:
            print(f"        {f['title'][:100]}")

    print("\n## 2. CERT@VDE CSAF feed (authoritative vendor source, cross-check)")
    count, status = check_certvde()
    print(f"  {CERTVDE_FEED}")
    print(f"  status={status}" + (f"  advisories_in_feed={count}" if count is not None else ""))

    print("\n## Verdict")
    if findings and certvde_assigned:
        print(f"  COVERED. CIRCL returns {len(findings)} CVEs for this device, "
              f"{certvde_assigned} assigned by CERT@VDE -> the authoritative Phoenix")
        print("  Contact data IS reachable via the public API. Use it as the spine;")
        print("  keep the CERT@VDE feed only as an offline/air-gapped fallback.")
    elif findings:
        print(f"  PARTIAL. CIRCL returns {len(findings)} CVEs but none assigned by")
        print("  CERT@VDE -- pull the CERT@VDE CSAF feed directly to be safe.")
    else:
        print("  NOT COVERED via this vendor/product string. Try another vendor key")
        print("  (browse /api/browse/) or use the CERT@VDE CSAF feed directly.")
    print("\n  NOTE: these are version-CANDIDATES, not confirmed vulnerabilities.")
    return 0


def selftest():
    # Known CVE-2020-12521 (CERT@VDE, PROFINET LLDP DoS) record shape -> fields.
    rec = {"containers": {"cna": {"title": "PROFINET LLDP DoS",
                                  "metrics": [{"cvssV3_1": {"baseScore": 6.5,
                                                            "baseSeverity": "MEDIUM"}}]}},
           "cveMetadata": {"assignerShortName": "CERTVDE"},
           "source": {"advisory": "VDE-2020-049"}}
    f = extract("cve-2020-12521", rec)
    assert f["id"] == "CVE-2020-12521", f
    assert f["cvss"] == 6.5 and f["severity"] == "MEDIUM", f
    assert f["assigner"] == "CERTVDE", f
    assert f["advisory"] == "VDE-2020-049", f
    assert extract("", {})["id"] == "?"  # empty record must not crash
    print("selftest OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
