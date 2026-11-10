---
title: "cisagov/CSAF"
url: "https://github.com/cisagov/CSAF/tree/develop"
type: dataset
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [2,3]
version: "develop @ 92657dd99619 (2026-11-06)"
---

## Summary
CISA's repository of machine-readable IT and OT security advisories in OASIS CSAF 2.0. It also republishes vendor partner CSAFs and includes a CSAF-to-Markdown tool. Provider metadata is linked for CISA's CSAF Trusted Provider role. No license is declared on the repository.

## Key facts
- Default branch is `develop`; 127 stars.
- Advisories are in `csaf_files/IT/white`, `csaf_files/OT/white` and `csaf_files/VA/white`.
- All advisories follow CSAF v2.0, per the README.
- Republished vendor CSAFs retain the original vendor dates and revision history.
- CISA Trusted Provider metadata: https://www.cisa.gov/sites/default/files/csaf/provider-metadata.json
- `tools/csaf2md` converts CSAF v2.0 JSON into Markdown.
- GitHub reports no license (`license: null`); README states none.

## Verbatim
- "These republication CSAFs retain the dates and revision history of the original vendor CSAF."

## Relevance
Confirms CISA CSAF as a machine-readable OT advisory source (`research-notes.md` §4). `csaf_files/OT/white` is the path to ingest (OWASP OT #2). Update cadence is not stated.
