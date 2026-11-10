---
title: "Common Security Advisory Framework Version 2.0 (OASIS Standard)"
url: "https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html"
type: standard
trust: primary
accessed: 2026-11-09
published: 2022-11-18
owasp_ot: [2,3]
version: "2.0 OS (18 November 2022); CSAF 2.1 is at Committee Specification Draft 04 (2026-10-21), not a final standard"
---

## Summary
OASIS standard for machine-readable security advisories in JSON, superseding CVRF 1.2. It defines five document profiles, product status, VEX justification flags, and a distribution model covering provider-metadata, ROLIE feeds and provider roles. CSAF 2.1 exists only as a draft (CSD04, 2026-10-21), so 2.0 remains current.

## Key facts
- Approved as OASIS Standard 18 November 2022; editors Langley Rock, Stefan Hagen, Thomas Schmidt; supersedes CVRF 1.2.
- Five profiles: CSAF Base, Security incident response, Informational Advisory, Security Advisory, VEX (`/document/category` value `csaf_vex`).
- Product status has eight properties: first_affected, first_fixed, fixed, known_affected, known_not_affected, last_affected, recommended, under_investigation.
- VEX profile: each `known_not_affected` item SHALL have an impact statement, either a machine-readable flag or a human-readable threat of category `impact`.
- VEX flag labels: component_not_present, inline_mitigations_already_exist, vulnerable_code_cannot_be_controlled_by_adversary, vulnerable_code_not_in_execute_path, vulnerable_code_not_present.
- Remediation categories: mitigation, no_fix_planned, none_available, vendor_fix, workaround.
- Distribution includes provider-metadata.json at a well-known URL (requirements 7 and 9) and ROLIE feeds (requirements 15 to 17).
- Roles: CSAF publisher, provider, trusted provider, lister, aggregator. Trusted provider adds requirements 18 to 20 (hashes, signatures, public OpenPGP key).
- Consumers retrieving from a trusted provider MUST check hash and signature files before further processing.

## Verbatim
- "The main purpose of the VEX format is to state that and why a certain product is, or is not, affected by a vulnerability."
- "vulnerable_code_not_present: The product is not affected because the code underlying the vulnerability is not present in the product."

## Relevance
Defines how vendor VEX should be parsed: `known_not_affected` plus a flag is the signal that removes a backport false positive (OWASP OT #2). Signature checking applies to trusted providers including Phoenix Contact's.
