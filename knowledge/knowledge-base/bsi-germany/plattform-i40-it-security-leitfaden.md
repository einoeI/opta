---
title: "Leitfaden IT-Security in der Industrie 4.0: Handlungsfelder für Betreiber"
url: "https://www.plattform-i40.de/IP/Redaktion/DE/Downloads/Publikation/leitfaden-it-security-i40.html"
type: other
trust: primary
accessed: 2026-11-09
published: 2016-11-15
owasp_ot: [1, 2, 3, 4, 5, 6, 7, 8, 10]
version: "Stand November 2016"
local_file: "sources/bsi-germany/leitfaden-it-security-i40.pdf"
---

# Leitfaden IT-Security in der Industrie 4.0

## Summary

German-language guide published by the Federal Ministry for Economic Affairs and Energy (BMWi) with editorial responsibility at Plattform Industrie 4.0. It gives machine and plant operators, particularly SMEs, a self-assessment and fields of action: organization, risk management, segmentation, identity management, software security, and a procurement requirements catalogue. It does not discuss penetration testing of production systems at all. Its value is the operator-side requirement set, especially the integrator catalogue in section 8.3, which can be turned into acceptance checks.

Page references are PDF pages; the printed folio is PDF page minus 2. Quotes are in the original German.

## Key facts

**Purpose and scope**

- BMWi publication, "Stand November 2016", editorial responsibility Plattform Industrie 4.0 (p.2). The publisher page gives publication date 15.11.2016.
- Aimed at the mid-sized plant operator who lacks clear fields of action, as a basis for self-assessment; the BSI IT-Grundschutz manual and IEC 62443 are named as existing but insufficient for that audience (p.6).

**Fields of action (table of contents, p.4-5)**

- Organization, processes, responsibilities (ch. 3); risk management (ch. 4); segmentation of devices, plants, networks (ch. 5); identity management (ch. 6); software security in production (ch. 7); security in procurement of machines and plants (ch. 8).

**Testing statements (all that were found)**

- The term "Penetrationstest" does not occur in the text (full-text search). Production-system testing is addressed only indirectly.
- Restoring backed-up configuration into a plant can be tested only at considerable effort, in a simulated environment or staged in individual plant segments, for example in maintenance windows (section 4.4, p.21).
- Software security testing is described for development: static and dynamic analysis, fuzzing, memory-safety testing, ideally manual code review (section 7.1, p.33).
- Post-delivery maintenance applies as far as operations and maintenance windows permit (section 7.2, p.33).
- Integrators should disclose test cases and test reports, and maintain release notes for each update (catalogue item E, p.38).

**Requirements convertible to checks**

Vulnerability and risk:

- Vulnerability analysis uses a network-communication context diagram, protocols and software components, with supplier involvement; CVSS and CCSS help, but each operator must rate criticality for its own environment (section 4.3.1, p.19).
- Operators must also consider vulnerabilities only they know of, such as additional remote access or hidden permissions active only under certain conditions (section 4.3.1, p.19).
- Example risk table with asset, threat, likelihood, damage, level and measure; damage expressed as production impact (Abbildung 9, p.20).

Segmentation:

- Zones of similar protection need must be identified and technically separated, without materially restricting production (section 5, p.22).
- Office IT and production must at least be adequately separated (section 5.1, p.22). Plant subnets are also separated horizontally to limit further compromise (section 5.2, p.22).

Remote access (section 5.5, p.23-24):

- Remote access always passes at least one dedicated zone transition.
- Strong authentication at session start, preferably at the zone-transition gateway; external communication over insecure networks is cryptographically protected.
- Session rules per zone transition (duration, function scope, maintenance intervals, IP ranges, recorded data); on violation the connection must be terminated automatically.

Field communications and monitoring:

- Field buses often lack any protection; in Industrie 4.0 contexts at least authenticity and integrity should be assured. Modbus encapsulation in OPC UA is given as an example (section 5.6, p.24).
- Anomaly detection works well at field level due to uniform traffic but requires high know-how and local knowledge (section 5.9.1, p.25).

Procurement catalogue, section 8.3 (p.37-40), requirements on the integrator:

- A: strict separation of administrative and production rights, central provisioning, strong authentication (p.37).
- C: disclosed algorithms and libraries; TLS 1.2 or higher and BSI recommendations (p.38).
- D: security by default; no default passwords or accounts at commissioning (p.38).
- F: software must not run with elevated privileges (p.38).
- G: required protocols and ports specified (p.39).
- J: remote maintenance time-limited, initiated only from inside to outside, operator administrator approval per connection (Vier-Augen-Prinzip), monitorable, restricted to the affected plant part (p.39).
- K: integrator commits to passing on new vulnerability information immediately and delivering updates promptly (p.39).
- The catalogue claims no completeness and is meant as a first inspiration (p.37).

Competences (section 3.4, p.15):

- Security knowledge is essential; role-holders must be able to demonstrate extended or expert knowledge including production specifics.
- Training should be mandatory, evidenced and documented, and improved regularly.
- SMEs may use external specialists, for example through framework agreements.

**Currency (checked 2026-11-09)**

- The publisher page still offers this guide and mentions no newer edition.
- Content reflects 2016: it references BSI-Standard 100-x and TLS 1.2. Note that a separate VDMA "Leitfaden Industrie 4.0 Security" exists and should not be conflated with this document.

## Verbatim

> "Hier kann nur unter erheblichem Aufwand eine simulierte Umgebung beziehungsweise eine gestaffelte Rückspiegelung der gesicherten Konfiguration in einzelnen Segmenten der Anlage getestet werden (etwa in Wartungsfenstern)." (section 4.4, p.21)

> "Letztlich muss der Betreiber auch solche Schwachstellen betrachten, die eventuell nur ihm bekannt sind – etwa zusätzliche Remote-Zugänge oder versteckte Berechtigungen in Systemen, die nur unter bestimmten Voraussetzungen aktiv werden." (section 4.3.1, p.19; line-end hyphenation removed)

> "Eine Initiierung der Verbindung kann nur von innen nach außen vorgenommen werden, um nicht-autorisierte Zugriffe Dritter zu erschweren." (catalogue J, p.39)

> "Bei Verstoß gegen diese vordefinierten Sitzungsregeln muss die Verbindung automatisch abgebrochen werden." (section 5.5, p.24; line-end hyphenation removed)

## Relevance

Inference, not stated by the source:

- Use section 8.3 as a factory or site acceptance checklist on new machines; items D, G and J are directly verifiable.
- Section 5.5 yields testable remote-access assertions: only via zone transition, session terminates on rule breach.
- Silence on penetration testing means this guide cannot be cited as a mandate for testing; it can be cited for requirements a test verifies.
- Age: treat crypto and standards references as dated, and note the document predates Germany's later OT regulation.
- Informs open tasks on German-market requirements and acceptance-test catalogue.
