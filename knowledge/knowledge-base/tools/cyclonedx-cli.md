---
title: "CycloneDX/cyclonedx-cli"
url: "https://github.com/CycloneDX/cyclonedx-cli"
type: tool
trust: primary
accessed: 2026-11-09
published: 2026-07-23
owasp_ot: [3]
version: "0.33.1 (2026-07-23); main @ b3cfa4b0edc3"
license: "Apache-2.0"
---

## Summary
CLI for CycloneDX BOM analysis, modification, diffing, merging, format conversion, signing and verification. It is built for automation, with stdin/stdout support. It generates no SBOMs from targets.

## Key facts
- Commands: add, analyze, convert, diff, keygen, merge, sign, validate, verify.
- Conversion between CycloneDX XML, JSON, Protobuf, CSV and SPDX JSON v2.3.
- Any `--input-file` command also accepts stdin.
- Used by Phoenix Contact's SBOM workflow for `validate` and `merge --hierarchical`.

## Verbatim
- "Conversion is supported between CycloneDX XML, JSON, Protobuf, CSV, and SPDX JSON v2.3."

## Relevance
`validate` is a cheap quality gate; `diff` compares SBOMs across firmware versions or vendor against generated (OWASP OT #3).
