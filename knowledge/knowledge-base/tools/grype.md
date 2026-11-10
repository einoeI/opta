---
title: "anchore/grype"
url: "https://github.com/anchore/grype"
type: tool
trust: primary
accessed: 2026-11-09
published: 2026-11-09
owasp_ot: [2]
version: "v0.121.3 (2026-11-09); main @ cd1f23eb50df"
license: "Apache-2.0"
---

## Summary
Vulnerability scanner for container images, filesystems and SBOMs, with EPSS/KEV prioritization. It supports VEX filtering through `--vex`. Its capability list covers major distributions, but no Yocto or OpenEmbedded entry was found, and its docs flag CPE matches as needing verification.

## Key facts
- Scans images, directories and SBOMs (`grype sbom:./sbom.json`).
- README lists OpenVEX support; the filter-results docs state OpenVEX and CSAF VEX both work with `--vex`, which accepts multiple files.
- `--only-fixed` and `--only-notfixed` filter by fix state; `.grype.yaml` holds ignore rules.
- Match types: `exact-direct-match` and `exact-indirect-match` are high confidence; `cpe-match` requires verification.
- OS capability list includes Debian and Raspberry Pi OS among others; grep of the page found no Yocto or OpenEmbedded.

## Verbatim
- "Match types in JSON output indicate reliability: exact-direct-match and exact-indirect-match are high confidence, cpe-match requires verification"

## Relevance
Usable with a Syft SBOM, but on Yocto firmware expect CPE matches (inference). Label those Version-candidate and apply vendor CSAF VEX via `--vex` where it exists (OWASP OT #2).
