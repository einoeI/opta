---
title: "ICS/OT Security (TeamStarWolf discipline page)"
url: "https://github.com/TeamStarWolf/TeamStarWolf/blob/main/disciplines/ics-ot-security.md"
type: other
trust: secondary
accessed: 2026-11-09
published: 2026-10-21
owasp_ot: [1,4,5,6,7,8,9,10]
version: "commit 149ca1dabf, 2026-10-21; page last corrected 2026-10-13 against ATT&CK v19.2"
license: "MIT (repository)"
---

## Summary
A community learning-path page covering the Purdue model, protocol weaknesses, key incidents, tools, standards and certifications.
It is a good orientation map with a staged learning route.
It has at least one ATT&CK ID error when compared with MITRE, and states no primary sourcing for its incident facts.
The page records "Last reviewed: No review recorded yet".

## Key facts
- Learning stages: Foundation (Purdue, protocols, ATT&CK for ICS); Practitioner (protocol analysis, passive monitoring, OT vulnerability assessment, IEC 62443, NERC CIP); Advanced (adversary emulation, firmware analysis, PLC programming abuse, lab recreation of TTPs).
- Protocol claims: Modbus has no authentication or encryption; DNP3 authentication is optional via SAv5; OPC UA supports X.509 and TLS, which the page says are often disabled for compatibility; BACnet/SC is an optional secure option.
- Its RA-3/RA-5 alignment states "passive scanning only in production" and "consequence-based risk scoring".
- Tools named include GRASSMARLIN (described as archived), Redpoint, s7scan, pymodbus, libiec61850, ICS-pcap, Zeek, ICS-Security-Tools, caldera-ot, binwalk, FACT_core and EMBA.
- Lab-relevant items named: OpenPLC Runtime, ControlThings Platform, MITRE CALDERA for OT.
- Link status on the access date: `mitre/caldera-ot` last commit 2026-09-16; `ITI/ICS-Security-Tools` 2026-11-01; `nsacyber/GRASSMARLIN` showed an archive banner, last commit 2017-08-04.
- ID error against ATT&CK v20.1: the page lists "Denial of Control | T0815"; MITRE has T0813 Denial of Control and T0815 Denial of View. The page also uses "Man in the Middle" for T0830, which MITRE names Adversary-in-the-Middle.

## Verbatim
None needed.

## Relevance
- Use for orientation and tool discovery; take IDs and incident facts from primary sources.
- Inference: "passive scanning only in production" is stricter than ACI EUROPE, which permits controlled active testing under change control.
