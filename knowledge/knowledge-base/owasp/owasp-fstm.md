---
title: "OWASP Firmware Security Testing Methodology (FSTM)"
url: "https://scriptingxss.gitbook.io/firmware-security-testing-methodology"
type: standard
trust: secondary
accessed: 2026-11-09
published: 2025-10-05
owasp_ot: [2,9]
version: "master @ ec666e8f8b9f (2025-10-05); tag FSTMV1 (2019-11-01)"
license: "CC-BY-SA-4.0"
---

## Summary
Nine-stage methodology for firmware security assessment, published as a GitBook and at github.com/scriptingxss/owasp-fstm, whose README section on EMBA is the second link. It covers information gathering through binary exploitation. Trust is marked secondary because it is a community methodology, though it sits under OWASP's firmware work.

## Key facts
- Stages: 1 information gathering, 2 obtaining firmware, 3 analyzing firmware, 4 extracting the filesystem, 5 analyzing filesystem contents, 6 emulating firmware, 7 dynamic analysis, 8 runtime analysis, 9 binary exploitation.
- Stage 3 uses `binwalk -E` entropy checks for suspected encryption.
- Stage 4 lists filesystem types squashfs, ubifs, romfs, rootfs, jffs2, yaffs2, cramfs, initramfs; shows carving with dd and `unsquashfs`.
- Notes Binwalk v3 (rewritten in Rust) as faster than Python versions.
- EMBA section lists SBOM generation, cve-bin-tool integration, SBOM VEX support, and tracking of recompiled or modified libraries.
- The EMBA section's install text still names `cve-search` as a dependency.
- EMBArk is described in the text as being in "a very early development stage"; the EMBA README reports EMBArk v0.3.

## Verbatim
- "EMBA is designed as a core firmware analysis tool for penetration testers."

## Relevance
Procedural frame for offline firmware analysis, with the stage boundary that matters here: stages 6-9 are testbed only (OWASP OT #9). The stale EMBA dependency note conflicts with the EMBA book's cve-bin-tool description; prefer EMBA's own docs.
