---
title: "OWASP Operational Technology (OT) Top 10, 2025 Edition"
url: https://ot.owasp.org/v/2025/
type: standard
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [1,2,3,4,5,6,7,8,9,10]
version: "2025.0.0-127-g3616452 (local PDF, built 2026-10-20); hosted PDF is 2025.0.0-131-g8deeeec (built 2026-11-03)"
local_file: "sources/owasp/OWASP-OT-Top-10-2025.pdf"
license: "CC BY-SA 4.0 per PDF p.2 and web body text; web footer says CC BY 4.0"
---

# OWASP OT Top 10 (2025)

## Summary

OWASP's list of the ten main OT security risks and missing practices, each with description, rationale, known attacks, mitigations, next steps and references.
It is the project's organizing frame. It describes risks, so test procedures have to be derived from it.
The local PDF, the hosted PDF and the web edition match in substance; differences are listed below.
Page references are PDF page numbers; printed page = PDF minus 5.

## Key facts

### Edition and comparison

- The PDF calls itself a living document, version 2025.0.0-127-g3616452, with CC BY-SA 4.0 (PDF p.2).
- Ranking: "the respective ranking was highly subjective". Items 1-4 had consensus as fundamental, items 5-9 are of similar high importance, item 10 is "not a security issue by itself" (PDF p.40).
- Method: expert opinion plus "empirical data from both offensive and defensive companies and experts"; the project started in autumn 2024 (PDF p.41). The empirical data itself is not published in the document.
- Each item has Description, Rationale, Known Attacks, Mitigation/Countermeasures (Design and Implementation, Operational), Next Actionable Steps, References (PDF pp.40-41).
- Local versus hosted PDF, compared 2026-11-09: same 98 pages; extracted text differs only in the version string on p.2 (127-g3616452 versus 131-g8deeeec); CreationDate 2026-10-20 versus 2026-11-03.
- Local PDF versus web `v/2025/` for the ten item pages and the mapping table: no web-only text was found. PDF-only text was section numbers (web headings are unnumbered) and the summary and list sections, which live on other web pages.
- Item names vary. PDF headings (pp.42-77) and the web menu use "Unknown Assets and Undocumented Services", "(Accessible) Devices with Known Vulnerabilities/Issues", "Inadequate Supply Chain Management" and "Selection of Components/Protocols With Insufficient Security Capabilities". The PDF list (p.40) and mapping table (pp.91-94) use "Unknown Assets and Unmanaged External Access", "Devices with known Vulnerabilities/Issues", "Inadequate Supplier/Supply Chain Management" and "Insufficient Security Capabilities"; p.40 also uses "Components/Protocols with Insufficient Security Capabilities".
- Licence conflict: PDF p.2 and the web body say CC BY-SA 4.0; web page footers say CC BY 4.0.
- The mapping table (PDF pp.91-95) cites "NIST SP 800-82:v3", so it maps to Rev. 3.

### On scanning and testing OT

- A simple nmap port and service scan is "totally fine in most IT systems", but "there are many PLCs that can crash if they receive such packets" (PDF p.19).
- Nmap "can be intrusive and may disrupt operations in a production environment" (PDF p.45).
- "there is anecdotal evidence of OT components crashing during network scans" (PDF p.54).
- Cited talk "PLCs: To Scan or Not to Scan?" (20.6.2024, https://www.youtube.com/watch?v=yqhn4xPwbfQ) is described as "showing that even benign scans can cause crashes and disrupt availability" (PDF p.57). The talk itself was not reviewed.

### 1. Unknown Assets and Undocumented Services (PDF pp.42-45)

- Scope: unknown devices (legacy, unmanaged, unauthorized connections), undocumented services (remote access, cloud, third-party apps), unmanaged external access (TeamViewer, VPNs), unmanaged third-party maintenance access (pp.42-43).
- A full inventory should cover devices, established remote access, deployed privileges and other services (p.42).
- Examples: Stuxnet, Triton, WannaCry, Colonial Pipeline via a disused VPN account, Florida water plant via TeamViewer, CISA/EPA warning on Internet-exposed HMIs (p.43).
- Mitigations: document changes through change management; start with a physical walk-through inventory; asset discovery tools; regular scan and monitor for new devices; port and traffic monitoring; assume rogue devices in design (pp.43-44).
- Next steps: thorough inventory, discovery tools, change documentation process, regular inventory review (p.44).
- Tools: Nmap (with disruption warning), Shodan, Wireshark. References include NIST 1800-23 and 1800-5 (pp.44-45).

### 2. (Accessible) Devices with Known Vulnerabilities/Issues (PDF pp.46-49)

- Mitigations such as segmentation do not remove the problem: if a countermeasure has a flaw, the original vulnerability can still be exploited (p.46).
- OT constraints: safety, update windows, long lifetimes, few vendors, legacy devices, missing awareness, unknown devices; these are "not an excuse" (pp.46-47).
- Examples: APT44, Volt Typhoon, sensitive nuclear information left vulnerable partly through obsolete Windows 7 and Windows 2008 (p.47).
- Design: secure development (SAMM), pre-deployment testing (ISTG, FSTM), inform customers and provide SBOMs, avoid obscurity, memory-safe languages (p.48).
- Operational: supplier-contract vulnerability notification; asset register with versions; pre-deployment tests; vulnerability management with scanning and patching; segmentation (p.48).
- Next steps: inventory; gather SBOMs and check known vulnerabilities; "test your devices and services for known vulnerabilities if possible (pen-testing)"; risk-based treatment plan; repeat (p.48).
- Tools: shodan.io, OWASP dependency-check, dependency-track (p.49).

### 3. Inadequate Supply Chain Management (PDF pp.50-53)

- Attackers exploit trust in vendors, integrators and maintenance providers across the lifecycle: design, development and production, distribution, acquisition, deployment, maintenance, disposal (p.50).
- Examples: SolarWinds Orion, the 2024 CrowdStrike update, Dragonfly, NotPetya via M.E.Doc, Denmark's train network via a subcontractor (p.51).
- Design: security by default and by design, third-party conformity assessment before market, multi-vendor strategy (pp.51-52).
- Operational: notification procedure for severe incidents; regular supplier risk evaluation, restricting or excluding high-risk suppliers; information sharing and training; include supply chain attacks in plans and exercises (p.52).
- Next steps: regular supplier checks or required certifications (IEC 62443-4-1, 62443-4-2); preparedness or stress tests; "Create test platforms or sandbox environments for secure testing" (p.52).
- CWE: 912 Hidden Functionality; 1361 ICS Supply Chain (pp.52-53).

### 4. Loss of Availability (PDF pp.54-57)

- Includes DoS (flooding, resource exhaustion, application-layer), real-time communication disruption, integrity attacks that defeat a system's purpose, and software updates (pp.54-55).
- Out of scope: cloud-managed systems going down while the OT process continues (p.54).
- Examples: Viasat/AcidRain, Stuxnet (pp.55-56).
- Design: availability risk assessment, redundancy and failover, real-time protocols and hardware, signatures or MACs while considering overhead (p.56).
- Operational: test redundancy and failover, for example in planned maintenance windows (p.56).
- Next step: availability risk assessment (p.56). Reference: BSI ICS Top 10 (p.56).

### 5. Insufficient Access Control (PDF pp.58-61)

- Three levels: organizational (a written access matrix is required), technical, physical (often over-relied upon) (p.58).
- OT particularities: emergency stops and medical devices conflict with authentication; legacy devices often lack authentication and central identity integration (pp.58-59).
- Principles: RBAC, least privilege, separation of duties, clear trust boundaries, training, deactivating accounts (p.59).
- Implementation questions: are controls in place and well configured; is MFA enforced for remote management ("not state-of-the-art in 2025" without it); default passwords and accounts; were controls tested; are physical assumptions documented and tested; non-repudiation, which shared password lists break (pp.59-60).
- Examples: an ex-employee reusing remote login to shut down a plant; Colonial Pipeline (p.60).
- Mitigations: zero trust, trust boundaries, minimal roles (admin for configuration; read-only for measuring data), RBAC, MFA, change defaults, periodic account review, deprovisioning (p.60).
- Next steps: is sensitive information accessible via interfaces; does a role concept exist and is it implemented (p.61).

### 6. Missing Incident Detection/Reaction Capabilities (PDF pp.62-66)

- Weaknesses: auditable events not logged; unclear log messages; logs not monitored; logs only local; poor alert thresholds or escalation; "Technical security tests ... do not trigger alerts"; active attacks not detected promptly (p.62).
- A cited 2024 report: 45% of service engagements lacked visibility across OT networks (pp.62-63).
- Examples: Ukraine power attacks, Triton (found via a safety trip), LockerGoga at Norsk Hydro (p.63).
- Mitigations: boundary IPS configured not to disrupt real-time control or safety traffic; log failures with user context and retention; machine-consumable log format; safe log encoding; alerting; IR plan such as NIST 800-61 (pp.63-64).
- Next steps: detection and response exercises. Technical example: place harmless test malware on an asset and verify blocking or alarm; if blocked, encode it and retry to test host-based detection. Organizational example: tabletop exercise (p.64).
- CWE: 223, 532, 778. Tools: EICAR, Metasploit, Graylog, Wazuh, Snort, Suricata (pp.64-66).

### 7. Broken Zones and Conduits Design (PDF pp.67-69)

- Common errors: no IT/OT DMZ; overly broad IP and port ACLs; multi-homed devices; possible C2 channels such as IMAP or DNS in OT; JTAG or SWD debug interfaces left enabled; forgotten remote access acting as an unplanned conduit (pp.67-68).
- "The most common entry into OT-zones comes from IT environments"; for hardware it is debug interfaces; "in reality networks are very flat" (p.68; the PDF spells it "realty").
- The right design is not the most complex or microsegmented, but one that meets needs without being overly complex (p.67).
- Examples: Iran-linked and Russia-backed water attacks; exposed RDP and EternalBlue (p.68).
- Design: the IEC 62443-3-2 flow: identify the SuC, initial risk assessment, partition into zones and conduits, compare to tolerable risk, detailed assessment, document requirements, asset owner approval (pp.68-69).
- Operational: monitor and reassess after changes (p.69).
- Next steps: inventory including interfaces, monitor who communicates, follow the steps, consult 62443-3-2. Tools: BloodHound, nmap, traffic monitoring (p.69).

### 8. Missing Awareness (PDF pp.70-73)

- Capabilities and policies are useless if not used. Causes: security as an afterthought in tenders, IT/OT not integrated, obscurity reliance (pp.70-71).
- Examples of resulting problems: configuration errors, missing encryption even if available, JTAG/SWD left enabled, RTUs left in upload mode for convenience (p.71).
- Training must cover the grey zone between mechanical failure and cyberattack; contractors are a blind spot (p.72).
- Examples: default passwords on Internet-accessible PLCs, Colonial Pipeline, TRISIS with key switch in program mode and SIS connected to the operations network (p.72).
- Mitigations: security requirements in tenders; security tests in acceptance tests; integrate cybersecurity into HSSE; live simulation exercises; role-based training; contractor training before granting access (p.73).

### 9. Selection of Components/Protocols With Insufficient Security Capabilities (PDF pp.74-76)

- Legacy means security and cryptography capabilities that do not conform to current best practice, including systems that cannot be updated or replaced (p.74).
- Legacy protocols lack integrity protection and sufficient authentication, or have weak built-in security (p.75).
- Examples: Industroyer speaking legitimate IEC 60870-5-104, IEC 61850 and OPC DA with no vulnerability needed; INCONTROLLER/PIPEDREAM abusing Modbus, CODESYS and OPC UA (p.75).
- Design: no legacy for new deployments, updatable components, slack for future security features (p.75).
- Operational: "there are no operational countermeasures" as such; isolate, monitor, apply compensating controls (pp.75-76).
- Next steps: evaluate components and protocols, identify legacy, evaluate capabilities, replace or compensate (p.76).

### 10. Missing Hardening (PDF pp.77-80)

- Reduce attack surface (unnecessary services, unused ports, patches) and add layers; apply CIS or DISA STIG guidelines; disable default accounts and passwords (p.77).
- Rationale: empirical data "showed that missing hardening was a common part of successful exploits" (p.78).
- Examples: Stuxnet (USB), NotPetya (p.78).
- Design: disable USB, Telnet, webserver and JTAG/SWD; start from benchmarks and relax only as needed; application allow-listing; secure defaults; customer hardening guide (p.78).
- Operational: reapply hardening after maintenance; request documentation; put requirements in tenders; verify "with a Pentest or some kind of Cybersecurity Acceptance Test (during SAT/FAT)" (p.79).
- Next steps: identify applicable guidelines, implement them, disable defaults (p.79).
- Tools: Nessus/OpenVAS with compliance scanning, Microsoft Security Compliance Toolkit (p.80).

### Standards mapping (PDF pp.91-95)

| Item | NIST SP 800-82:v3 controls | Key IEC 62443 | CSF 2.0 |
|---|---|---|---|
| 1 | CM-8, AC-20, AC-17, CM-2 | FR2; 3-3 SR2.X, SR7.8 | ID.AM, PR.AA, PR.IR-01 |
| 2 | SI-2, RA-5, CM-6 | FR3, FR4; 3-3 SR3.X, SR4.X | ID.RA-01, ID.IM, PR.PS, DE.CM-09 |
| 3 | SR-2, SR-3, SR-5, SR-6 | 2-1 ORG1.6; 3-2 ZCR5.X | GV.OC-03/04/05, GV.SC, ID.RA-10 |
| 4 | CP-2, CP-7, CP-9, CP-10 | FR7; 3-3 SR7.X | GV.OC-04/05, GV.SC-07/08, PR.AA-02, PR.IR-02/03/04, DE.CM, RC.RP-01/02/04 |
| 5 | AC-2, AC-3, AC-6, AC-5 | FR1, FR2; 3-3 SR1.X, SR2.X | ID.IM-01/03, PR.AA, PR.PS-05, PR.IR-01 |
| 6 | IR-4, SI-4, AU-6, IR-6 | FR6; 2-1 ORG2.2, SPE7 | GV.SC-08, ID.IM-04, DE.CM, DE.AE, RS.X |
| 7 | SC-7, AC-4, SC-2 | FR5; 3-2 ZCR3.X | ID.IM, PR.IR-01 |
| 8 | AT-2, AT-3 | 2-1 ORG1.4; 3-3 SR7.6, SR7.7 | PR.AT |
| 9 | PM-1, CA-2, CA-7 | 3-2 ZCR5.X; 4-2 CCSC2 | ID.RA-01, ID.IM, PR.AA-02, PR.PS-01/02/03/06 |
| 10 | CM-6, CM-7, SI-3, SC-28 | 2-1 ORG1.5; 4-1 SG-3 | PR.PS |

The table also gives MITRE ATT&CK mitigations and EU NIS2 implementing-regulation clauses for most items (PDF pp.91-95). Item 9 has no ATT&CK row.

## Verbatim

PDF p.19:

> "For example, a simple port and service scan with the well-known tool nmap is a common approach to start off the enumeration in a penetration test. While this is totally fine in most IT systems, there are many PLCs that can crash if they receive such packets."

PDF p.45:

> "Nmap is the standard OSS active network scanning tool. Be aware that it can be intrusive and may disrupt operations in a production environment."

PDF p.57:

> "PLCs: To Scan or Not to Scan? (youtube, 20.6.2024): presentation analyzing the impact of active scanning as well as OT-specific targeted scanning on PLCs, showing that even benign scans can cause crashes and disrupt availability."

PDF p.79:

> "Make sure hardening is actually implemented with a Pentest or some kind of Cybersecurity Acceptance Test (during SAT/FAT)"

PDF p.40:

> "we agreed upon the items of the top 10 list while the respective ranking was highly subjective."

## Relevance

- Frame for the planned check catalog. Derived checks are in `research_notes/OT pentesting knowledge base/nist_owasp_ot.md`, labelled as inference because OWASP gives risks and mitigations, not test procedures.
- OWASP does not address live versus testbed rules directly. Its #2 pen-test step carries an "if possible", and its #10 test sits in acceptance (SAT/FAT), so combine it with SP 800-82 safe-testing rules.
- Fix the naming of items 1, 2, 3 and 9 in the tool, since the PDF has more than one form. The handoff uses the p.40/mapping-table forms.
- Pin the version string in any report; the document is living and changed build between the user's download and today.
