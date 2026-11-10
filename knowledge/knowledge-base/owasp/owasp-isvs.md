---
title: "OWASP IoT Security Verification Standard (ISVS)"
url: "https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS"
type: standard
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [3,5,10]
version: "1.0.0-RC2 per README text (commit edfda29ba8, 2026-06-29)"
license: "CC BY-SA 4.0 per README badge; GitHub API reports NOASSERTION"
---

## Summary
An open standard of security requirements for IoT ecosystems, covering design, development and testing.
It is a requirements catalogue rather than a test methodology.
The README describes the content as a release candidate that is not yet final.
Its version signalling is inconsistent, so cite the RC string.

## Key facts
- The README states the current content is release candidate `1.0.0-RC2` and "not yet a finalized standard".
- The same README carries badges for "Version 1.0" and "release date October 2025"; the GitHub releases feed read on the access date showed "Pre-release 1.0RC" dated 2020-12-22 as its entry.
- Requirement chapters: V1 IoT Ecosystem; V2 User Space Application; V3 Software Platform; V4 Communication; V5 Hardware Platform.
- Formats are advertised as PDF, EPUB, DOCX, CSV, JSON and XML.
- Project leads are Aaron Guzman and Cédric Bassem.
- The latest commit is edfda29ba8 on 2026-06-29; the repository's last push is 2026-08-02.

## Verbatim
- "It is **not yet a finalized standard**."

## Relevance
- Inference: useful as a requirements checklist for hardening findings on embedded controllers (V3, V4, V5), paired with ISTG for test steps.
- Do not describe it as a finalized 1.0 standard in project reports.
- Only the README was read; individual requirements were not reviewed.
