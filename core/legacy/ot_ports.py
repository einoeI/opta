#!/usr/bin/env python3
"""Look up OT/ICS ports from catalog/ot-ports.csv (each row cites its source).

Usage:
    python3 ot_ports.py 502            # what runs on a port (ranges included)
    python3 ot_ports.py --scope plcnext
    python3 ot_ports.py --selftest     # validates the CSV

From Python:  from ot_ports import load, lookup
"""
import csv
import pathlib
import sys

CSV = pathlib.Path(__file__).resolve().parents[2] / "catalog" / "ot-ports.csv"
TRANSPORTS = {"tcp", "udp", "tcp/udp", "udp/tcp"}


def load(path=CSV):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def lookup(port, rows=None):
    port = int(port)
    return [r for r in rows or load()
            if int(r["port"]) <= port <= int(r["port_end"] or r["port"])]


def selftest():
    rows = load()
    for i, r in enumerate(rows, 2):
        lo, hi = int(r["port"]), int(r["port_end"] or r["port"])
        assert 0 < lo <= hi <= 65535, "line %d: bad port range" % i
        assert r["transport"] in TRANSPORTS, "line %d: transport" % i
        assert r["scope"] in {"generic", "plcnext"}, "line %d: scope" % i
        assert (r["scope"] == "plcnext") == bool(r["state"]), "line %d: state only for vendor rows" % i
        assert r["source_url"].startswith("https://") and r["accessed"], "line %d: source" % i
    assert {r["service"] for r in lookup(50000, rows)} == {"profinet-device"}
    assert not [r for r in rows if r["scope"] == "plcnext" and r["port"] == "502"], "502 is not on the PLCnext list"
    print("selftest ok (%d rows)" % len(rows))


def main(argv):
    if "--selftest" in argv:
        return selftest()
    rows = load()
    if "--scope" in argv:
        scope = argv[argv.index("--scope") + 1]
        rows = [r for r in rows if r["scope"] == scope]
    elif argv:
        rows = lookup(argv[0], rows)
    for r in rows:
        span = r["port"] + ("-" + r["port_end"] if r["port_end"] else "")
        print("%-12s %-8s %-20s %-10s %s  [%s]" % (span, r["transport"], r["service"],
              r["state"] or r["scope"], r["description"], r["nse_scripts"] or "-"))


if __name__ == "__main__":
    main(sys.argv[1:])
