---
title: "Awesome IoT & Hardware Security Learning Resources"
url: "https://github.com/jassics/awesome-cybersecurity-learning-resources/blob/main/awesome-iot-hardware-security-learning-resources.md"
type: other
trust: secondary
accessed: 2026-11-09
published: 2026-04-23
owasp_ot: [2,8,10]
version: "commit 3165f1ad1e, 2026-04-23"
license: "GPL-3.0 (repository)"
---

## Summary
A curated link list for IoT, firmware, hardware-interface and radio security.
Its firmware-analysis section is the part most relevant to this project.
Link health below covers GitHub links only and was checked on the access date.
`published` is the file's last commit.

## Key facts
- Sections: Books, Videos, Courses, Labs, Tools (firmware, hardware interfaces, radio, network), Certifications, Blogs/Articles.
- Dead on GitHub (404): `kmkz/IoT-SecurityTools`, `jhdscript/zwave-js-tools`, `abhijithvijayan/awesome-hardware-hacking`.
- Showing an archive banner: `praetorian-inc/DVRF` (last commit 2016-05-18), `jopohl/urh` (last commit 2025-12-19).
- Maintained firmware tools by last commit: `e-m-b-a/emba` 2026-11-03, `fkie-cad/FACT_core` 2026-11-02, `ReFirmLabs/binwalk` 2026-08-11, `pr0v3rbs/FirmAE` 2026-06-24.
- `OWASP/IoTGoat` and `scriptingxss/owasp-fstm` last changed 2025-10-05; `firmadyne/firmadyne` 2024-07-21; `riverloopsec/killerbee` 2022-08-19; `fkie-cad/awesome-embedded-and-iot-security` 2023-10-17.
- The list includes MITRE EMB3D, described there as an embedded-device threat model released in 2024.
- Hardware-interface tools listed include Bus Pirate, JTAGulator, Saleae analyzers, ChipWhisperer and SEGGER J-Link.

## Verbatim
None needed.

## Relevance
- Inference: EMBA, FACT_core, binwalk and FirmAE fit the project's "never scan the live PLC, analyse firmware out-of-band" stance.
- Inference: most radio tooling is out of scope unless a target profile has a wireless interface.
