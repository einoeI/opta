---
title: "ICS/OT Security Reference (TeamStarWolf)"
url: "https://github.com/TeamStarWolf/TeamStarWolf/blob/main/ICS_OT_SECURITY_REFERENCE.md"
type: other
trust: secondary
accessed: 2026-11-09
published: 2026-11-03
owasp_ot: [1,2,3,4,5,6,7,8,9,10]
version: "commit 628b642d0c, 2026-11-03; page last corrected 2026-10-13 against ATT&CK v19.2"
license: "MIT (repository)"
---

## Summary
A long community reference on OT architecture, protocols, threat actors, malware case studies, ATT&CK mapping, standards, detection and incident response.
It is dense and practical, with concrete protocol ports, passive-first guidance and OT incident-response ordering.
It contains several errors checkable against MITRE and internal contradictions, so its facts need primary corroboration.
The page records "Last reviewed: No review recorded yet".

## Key facts
- Default ports stated: Modbus TCP 502; DNP3 20000; IEC 61850 MMS 102; EtherNet/IP 44818; OPC UA 4840; BACnet 47808/UDP; IEC 60870-5-104 2404; S7comm and S7comm-Plus 102; GE SRTP 18245.
- Protocol assessment checks include: restricting Modbus write codes 5, 6, 15, 16 to authorised stations; DNP3 SAv5 enabled; OPC UA certificates validated and not NoSecurity; S7 IP allowlisting; BACnet broadcast filtering.
- Passive guidance: "Passive monitoring should always be the first choice"; active scanning can crash PLCs, corrupt process states or trigger safety shutdowns; passive asset discovery described as mandatory.
- The page warns against -T4/-T5, script arguments or UDP scans on live OT networks, while also listing Nmap ICS scripts to be used "cautiously".
- OT incident response order: safety assessment first, then containment that does not disrupt the safe process, evidence by out-of-band TAP, analysis, verified restoration of PLC logic, confirmation of SIS function before restart.
- Detection ideas: alert on Modbus writes from unexpected sources, PLC RUN-to-PROG transitions outside maintenance windows, and new devices on the OT network.
- Remote-access baseline: no persistent VPN into OT, MFA, recorded and time-limited vendor sessions through a DMZ jump server.
- Errors against ATT&CK v20.1: "Loss of Protection | T0829" (MITRE: T0837 Loss of Protection, T0829 Loss of View); "12 tactics, 83+ techniques" (MITRE index: 78 top-level techniques); T0843 called "Program Download to Controller" (MITRE: Program Download).
- Internal contradictions: TRITON target given as a "Saudi Aramco facility" and later as "SABIC Yanbu"; TRITON listed among USB-delivered attacks while its own attack chain shows spear-phishing and IT/OT pivot; the 2015 Ukraine outage is 225,000 customers here and 230,000 on the sibling discipline page.
- The Stuxnet "four zero-days" table includes MS08-067, a 2008 bulletin number.

## Verbatim
- "Passive monitoring should always be the first choice. Active scanning can crash PLCs, corrupt process states, or trigger safety shutdowns."

## Relevance
- Useful as a checklist seed for protocol checks and detection validation; verify IDs, attributions and incident details before citing.
- Inference: its pymodbus examples use the `unit=` argument; check the keyword against the installed pymodbus version, since the library's API has changed over time.
- Unverified: the page credits Kaspersky with discovering COSMICENERGY and attributes the Aegis DNP3 fuzzer to Digital Bond. Neither was checked against a primary source here.
