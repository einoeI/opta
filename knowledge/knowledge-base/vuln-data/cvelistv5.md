---
title: "CVEProject/cvelistV5"
url: "https://github.com/CVEProject/cvelistV5/tree/main"
type: dataset
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [2]
version: "main @ 1765ad633eca (2026-11-09); release 2026-11-09_baseline"
license: "CVE Program Terms of Use (no separate open-source license stated)"
---

## Summary
The official CVE List, hosted as CVE Record Format (JSON 5) files on GitHub. Records update about every 7 minutes through the CVE Services API. Consumers can use daily baseline and hourly delta zips, or git. The README documents the container structure (CNA, CVE Program, ADP), which determines where CPE and CVSS enrichment appears.

## Key facts
- Records may be 5.0 or 5.1 in format per their `dataversion` field; validate with the schema that field names.
- CVE Record Format 5.2.0 (2025-10-29) adds Package URL identifiers via `packageURL` on affected items, as a non-breaking change.
- Legacy CSV, HTML, XML and CVRF downloads lost support on 2024-06-30.
- `deltaLog.json` normally retains a rolling 30 days of modification history.
- CVE Program Container holds Program-added references (introduced 2024-07-31).
- The CISA-ADP container adds SSVC, KEV catalog data and Vulnrichment enrichment such as CVSS, CWE and CPE.
- GitHub reports no license for the repo; use is governed by the CVE Program Terms of Use.

## Verbatim
- "This repository is the official CVE List."
- "They are updated regularly (about every 7 minutes) using the official CVE Services API."
- "All support for the legacy CVE content download formats (i.e., CSV, HTML, XML, and CVRF) ended on June 30, 2024."

## Relevance
Offline, ToU-licensed base for CVE data, no NVD dependency (OWASP OT #2). The README's PURL support matters because `research-notes.md` §4 flags CPE gaps; adoption of PURL by CNAs was not measured here.
