---
title: "Nmap NSE scripts for ICS protocols (nmap/nmap scripts/)"
url: "https://github.com/nmap/nmap/tree/master/scripts"
type: tool
trust: primary
accessed: 2026-11-10
published: unknown
owasp_ot: [1, 9]
license: "Nmap Public Source License (per nmap.org)"
version: "master branch, last commit 2026-11-09"
---

# Nmap NSE scripts for ICS protocols

## Summary
Nmap ships NSE scripts that identify ICS devices by speaking their protocol. Each script declares a port rule and NSE categories; the categories (`safe`, `intrusive`, `discovery`, `version`, `broadcast`) are how a runbook separates safe from aggressive probes. Script source files were downloaded and their `portrule` and `categories` lines read on 2026-11-10. The data is captured in `catalog/ot-ports.csv`.

## Key facts
- `s7-info`: TCP 102, categories discovery, version.
- `iec61850-mms`: TCP 102, discovery, intrusive, version.
- `modbus-discover`: 502 (port or service "modbus"), discovery, intrusive.
- `enip-info`: 44818 TCP/UDP, discovery, version.
- `bacnet-info`: 47808 UDP/TCP, discovery, version.
- `fox-info` (Niagara Fox): 1911 and 4911 TCP, discovery, version.
- `omron-info` (FINS): 9600 TCP/UDP, discovery, version.
- `pcworx-info` (Phoenix Contact PC WORX): 1962 TCP, discovery.
- `profinet-cm-lookup`: 34964 UDP, discovery, intrusive.
- `multicast-profinet-discovery`: Layer 2 PROFINET DCP, categories discovery, info, safe, broadcast (no port).
- Most of these scripts were written by Stephen Hilt (Digital Bond) and merged from Redpoint (see knowledge-base/tools/digitalbond-redpoint.md).

## Verbatim
- `portrule = shortport.port_or_service(502, "modbus")` and `categories = {"discovery", "intrusive"}` (modbus-discover.nse)

## Relevance
Maintained source for ICS service identification in the active-discovery step (OWASP OT #1, #9). Note that none of the ICS scripts except `multicast-profinet-discovery` is in the `safe` category, so `--script "<proto> and safe"` selects almost nothing; use the category column of `catalog/ot-ports.csv` to decide which scripts are allowed in safe mode, and run `intrusive` ones on the testbed only.
