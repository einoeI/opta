---
title: "OWASP Testing Guide 4.0 (archive edition)"
url: "https://owasp.github.io/www-project-web-security-testing-guide/assets/archive/OWASP_Testing_Guide_v4.pdf"
type: standard
trust: primary
accessed: 2026-11-09
published: 2014-09-24
owasp_ot: [5,10]
version: "4.0 (archive); current stable WSTG is v4.2, v5.0 in development"
license: "CC BY-SA (cover states Creative Commons Attribution Share-Alike)"
superseded_by: "https://owasp.org/www-project-web-security-testing-guide/"
---

## Summary
A 224-page archived edition of the OWASP web application testing guide, led by Matteo Meucci and Andrew Muller.
It is superseded: the OWASP project page lists v4.2 as latest and v5.0 as in development.
It applies to OT only through web interfaces on HMIs, gateways, historians and PLC web servers.
`published` is the PDF CreationDate; the text itself says 2014.

## Key facts
- Current status per the OWASP project page on 2026-11-09: "v4.2 is currently available as a web-hosted release and PDF"; latest version 4.2; "We are currently developing release version 5.0".
- The v4.0 framework covers an SDLC in five phases: Before Development Begins; During Definition and Design; During Development; During Deployment; Maintenance and Operations.
- Testing is divided into a Phase 1 passive mode, which maps access points, and a Phase 2 active mode.
- Active testing is stated as 11 sub-categories with 91 controls: Information Gathering; Configuration and Deployment Management; Identity Management; Authentication; Authorization; Session Management; Input Validation; Error Handling; Cryptography; Business Logic; Client Side. A chapter sidebar on the same page says 12 subcategories.
- Test IDs use the OTG- prefix, such as OTG-AUTHN-002 Testing for default credentials and OTG-CONFIG-005 Enumerate Infrastructure and Application Admin Interfaces. Newer editions should be checked for current ID schemes.

## Verbatim
- "The set of active tests have been split into 11 sub-categories for a total of 91 controls"

## Relevance
- Inference: cite v4.2 or later for test IDs; keep this entry only as the edition the user linked.
- Inference: its passive-then-active ordering parallels OT passive-first, but it has no availability or physical-safety guidance and its active tests should not be applied to live OT web interfaces without the controls in the ACI EUROPE guideline.
