---
title: "Umsetzungshinweise zum Baustein: IND.1 Prozessleit- und Automatisierungstechnik"
url: "https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/Umsetzungshinweise/umsetzungshinweise_node.html"
type: standard
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
version: "Listed by BSI as Edition 2022; PDF XMP creation date 2021-05-06; references last accessed 2021-04-14"
local_file: "sources/bsi-germany/Umsetzungshinweis_zum_Baustein_IND_1_Prozessleit_und_Automatisierungstechnik.pdf"
---

# BSI IT-Grundschutz IND.1 implementation notes

## Summary

German-language BSI implementation guidance for module IND.1, giving measures M1 to M24 for operational technology plus OT-specific measures for ORP.3, OPS.1.1.4 and NET.1.2. Levels are Basis (B), Standard (S), Hoch (H). It is the only source in this set that speaks directly about penetration testing of OT: M17 acknowledges it can reduce availability and sets a cadence. Most measures are concrete enough to convert into test or audit checks. M18 to M24 have no implementation notes.

Page references are PDF pages. Quotes are in the original German.

## Key facts

**OT context**

- OT is defined as hardware and software that detects or causes change through direct monitoring and control of physical devices, processes and events (p.1).
- Physical separation of OT from other networks is now applicable only in exceptional cases with elevated protection needs (p.1).
- OT differs from IT by manufacturer or legal restrictions on changes, such as updates and retrofit hardening, and by lifecycles often beyond vendor support (p.2).

**Testing of production systems: M17 Regelmäßige Sicherheitsüberprüfung (H), p.25-26**

- OT infrastructures are audited even less often than office IT, partly because of high availability requirements (p.25).
- A review process should cover manual or automated policy-conformance checks (configuration and policy reviews), with particular attention to exposed systems with external interfaces and systems with direct user access (p.25).
- Some vulnerabilities can only be found economically by practical vulnerability testing, "häufig auch als Penetrationstest bezeichnet", and this can temporarily reduce availability (p.25-26).
- Internal and external audits should always be coordinated with the responsible administrators and run during operating hours (p.26).
- Depending on protection needs, BSI recommends from one audit per system per year down to one audit before go-live, plus audits at major changes: plant extensions, new external connections, replacement installations, substantial upgrades and migrations (p.26).
- The tests need extensive skill and experience, available externally; larger institutions may build their own competence (p.26).

**Other testing statements**

- Before integration into the OT network, it is recommended to check a component's authenticity and test it for compromising behavior (M8, p.13).
- Acceptance and integration tests should verify security requirements and interoperability, focusing on backup and recovery (M11, p.19).
- Products should react robustly to invalid input; invalid network packets should not crash software (M11, p.18).
- Patch testing should be on a test environment with an identical component (M12, p.20). Alternatively, install sequentially, redundant systems first (p.21).
- Technical and organizational audits can supplement advisory-based vulnerability analysis, especially at higher protection needs or exposure (M12, p.20).
- Manual antivirus scans should run only during production standstill and be documented (M3, p.4).
- The incident response plan should be exercised at least annually (M10, p.15).
- IPS needs a very careful trial phase before activation, since uninterrupted operation has priority (M10, p.17).
- Social engineering tests must be coordinated with data protection and the works council and may not expose anyone personally (ORP.3.M6, p.27).

**Measures convertible to checks**

- M1 Security organization (p.2-3): OT-ISMS, named ICS-ISB, IT/OT cooperation.
- M3 Malware (p.3-6): infection paths include external interfaces, removable media, service stations and programming devices, new components. Signatures come only from a central DMZ distribution service, not directly from the internet (p.4). Redundant components in separate groups with staggered rollout, for example 12 hours (p.5).
- M4 Documentation (p.6-8): inventory fields including MAC, IP, firmware of each CPU and module, ports and protocols (p.6-7); physical and logical network plans plus communication relationships (p.7).
- M5 Zones (p.8-9): segments with individual protection needs, vertical and horizontal segmentation; connections established from higher to lower protection; no undocumented bypass connections (p.9).
- M6 Change management (p.9-10): time-source changes logged.
- M7 Authorization (p.10-12): two-person review of requests, time-limited external accounts, annual verification; group accounts documented; firewall rules treated as user authorizations (p.10-11). Lockouts must not make the plant inoperable (p.11).
- M8 Secure administration (p.12-14): disable unneeded interfaces (SNMP, HTTP, service ports) and default accounts; change default passwords (p.12). Remote maintenance uses encrypted protocols, hardened jump servers in a DMZ, on-demand activation, logging (p.13).
- M10 Monitoring (p.15-17): minimum event list, central log server embedded in the zone concept (p.16); HIDS/NIDS placement at external interfaces (p.17).
- M12 Vulnerability management (p.19-22): cases by patch availability and integrator approval; criticality from impact and exposure, CVSS or two-to-three-step scale (p.20); compensating measures and EOL handling (p.21).
- M13 Emergency planning (p.22): scenarios including more than one week loss of internet and remote maintenance, and compromise of critical OT IT components.
- M16 Stronger zone isolation (p.25): DMZ with application-layer gateways, protocol checks by industrial firewalls.

**Regulatory pointers (p.3, p.8)**

- Sector legal requirements must be known and interpreted, notably for KRITIS operators (M1, p.3).
- Energy sector: BNetzA IT-Sicherheitskatalog under § 11 (1a) EnWG requires an ISMS to DIN ISO/IEC 27001 and a network structure plan by technology category (p.8). The document says other KRITIS sectors will follow.
- Further reading cites the BSI ICS-Security-Kompendium, including "Testempfehlungen und Anforderungen für Hersteller von Komponenten" (p.30), and BSI-CS 123 on ICS training (p.31).

**Currency (checked 2026-11-09)**

- BSI's Umsetzungshinweise page lists IND.1 as Edition 2022 and says the notes are "fortlaufend angepasst und ergänzt". Newest Kompendium is Edition 2023, available since 2023-02-01, and BSI lists IND.1 in it under the same title.
- BSI states Grundschutz++ replaces the Kompendium ("Sie löst das IT-Grundschutz-Kompendium ab"). Its plan, marked "Stand Oktober 2026", has BSI-Standard 300-1 at it-sa on 2026-10-27, GS++ certifiable from 2027-01-01, and IT-Grundschutz certifiability ending 2031-11-30. Whether each milestone was met cannot be confirmed from that page, which does not mention OT or IND content.
- The Edition 2023 IND.1 module PDF was downloaded but could not be text-extracted here, so differences from these notes are unverified.

## Verbatim

> "Bei der Planung sollte zudem berücksichtigt werden, dass sich bestimmte Schwachstellen prinzipbedingt nur durch praktische Schwachstellenprüfungen (Vulnerability Assessment, häufig auch als Penetrationstest bezeichnet) wirtschaftlich aufdecken lassen. Durch eine solche Maßnahme kann grundsätzlich die Verfügbarkeit der Umgebung zeitweise vermindert werden." (M17, p.25-26)

> "Sowohl interne als auch externe Audits sollten stets in Abstimmung mit den zuständigen Administratoren während der Betriebszeiten durchgeführt werden." (M17, p.26)

> "Je nach Schutzbedarf empfiehlt sich ein Audit pro System und Jahr bis hinunter zu einem Audit vor Produktivsetzung sowie bei größeren Änderungen in der Umgebung." (M17, p.26)

> "Vor der Integration in das OT-Netz wird empfohlen, die Echtheit der Komponente zu prüfen und auf kompromittierendes Verhalten zu testen." (M8, p.13)

> "So sollten beispielsweise ungültige Netzpakete nicht zum Absturz oder zu Fehlern der Software führen, sondern von dem Protokollstack ignoriert und bei Bedarf protokolliert werden." (M11, p.18)

## Relevance

Inference, not stated by the source:

- Strongest German anchor for commissioning OT testing: M17 gives trigger events and a cadence, and supports an argument that testing is expected at the H level.
- M17's level is H, so it is formally aimed at elevated protection needs, not baseline.
- "Während der Betriebszeiten" likely reflects having staff at hand when availability is at risk; the source does not explain. It conflicts with the BSI study's off-hours advice, so rules of engagement must resolve it per site.
- M4, M5, M7, M8, M10 and M12 convert to a check catalogue: inventory reconciliation against observed traffic, undocumented cross-zone paths, connection direction, default credentials, remote-access path, log coverage, patch-exception justification.
- M11 robustness suits bench or acceptance testing, not live plant.
- Informs open tasks on German-market requirements and test catalogue.
