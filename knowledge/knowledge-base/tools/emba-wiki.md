---
title: "EMBA wiki (e-m-b-a/emba)"
url: "https://github.com/e-m-b-a/emba/wiki"
type: tool
trust: primary
accessed: 2026-11-09
published: 2026-11-03
owasp_ot: [2,3,9]
version: "v2.0.5 Iced latte edition (2026-11-03); master @ 76d26381b9bf"
license: "GPL-3.0"
---

## Summary
EMBA is a firmware analyzer and SBOM tool for pentesters and product security teams, covering extraction, static and dynamic analysis, SBOM and vulnerability aggregation. Wiki pages read: Home, Feature overview, Usage, SBOM environment, Dependency-Track integration, and EMBA book chapters 1 and 5. It is the only tool reviewed that attempts per-binary CVE verification and outputs VEX, but no page read mentions RAUC.

## Key facts
- README badge: "Research only"; project copyright Siemens AG and Siemens Energy AG.
- Extraction modules: P05 archive (patool), P14 ext mount, P15 UBI, P50 binwalk v3, P55 unblob (generic primary), P60 fallback, P65 package extractor (.deb, .ipk, .apk), plus several vendor-specific decryptors.
- SBOM sources: binaries and libraries (S09), Linux kernel (S24/S25), distribution identification (S06), RPM, Debian and OpenWRT package systems (S08).
- The `sbom-minimal` scan profile excludes binary analysis (S09).
- F15 converts the inventory to a CycloneDX JSON SBOM. F17 uses cve-bin-tool for CVE lookup by component name and version.
- EMBA book: verification modules attempt to confirm whether the vulnerable feature or code path is present in the specific binary, reducing false positives. Output includes VEX JSON and a CycloneDX SBOM with VEX data.
- A wiki page documents uploading CycloneDX SBOMs to Dependency-Track.
- Yocto is not named in the SBOM sources list; `opkg`/`ipk` support is described as OpenWRT.
- A case-insensitive search of the wiki pages read found no match for "rauc".

## Verbatim
- "Beside our binary analysis mechanism as SBOM source EMBA is now able to extract details from the following sources:"
- "*EMBA* is designed as the central firmware analysis and SBOM tool for penetration testers, product security teams, developers and responsible product managers." (README)

## Relevance
Best fit for the `research-notes.md` §7B offline path, and the only one here with verification and VEX output. Inference: unblob/binwalk may reach a RAUC SquashFS payload, but this is unconfirmed (OWASP OT #2, #3, #9).
