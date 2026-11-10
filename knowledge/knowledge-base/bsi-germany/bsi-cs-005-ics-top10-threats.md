---
title: "Industrial Control System Security – Top 10 threats and countermeasures 2022 (BSI-CS 005)"
url: "https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Industrielle-Steuerungs-und-Automatisierungssysteme/Download/download.html"
type: standard
trust: primary
accessed: 2026-11-10
published: 2022-05-03
owasp_ot: [1, 2, 3, 4, 5, 8, 10]
version: "BSI-CS 005, Version 1.50 of 03/05/2022"
local_file: "sources/bsi-germany/BSI-CS_19_threads.pdf"
---

# BSI ICS Top 10 Threats and Countermeasures 2022

## Summary
BSI recommendation (20 pages) listing the ten most critical threats to ICS, each with problem description, threat scenarios and countermeasures, plus a risk self-check sheet for operators. The 2022 edition ranks by prevalence (order is not a ranking), merges smartphones into removable media, and adds supply-chain vulnerabilities. Read from the user's local PDF (file name `BSI-CS_19_threads.pdf`; the document's own ID is BSI-CS 005).

## Key facts
- The ten threats (p.2): malware via removable media and mobile systems; malware via Internet and intranet; human error and sabotage; compromise of extranet and cloud components; social engineering and phishing; (D)DoS attacks; Internet-connected control components; intrusion via remote maintenance access; technical failure and force majeure; soft- and hardware vulnerabilities in the supply chain.
- Distinguishes primary attacks (entry) from secondary attacks (privilege escalation, unauthorised access to other internal systems, manipulation of fieldbus communication, manipulation of network components, ransomware) (p.2-3).
- Damage categories: triggering or manipulating safety systems (harm to people/environment, physical damage), loss of availability, data leakage, manipulation of parameters reducing product quality (p.3).
- Assessment uses prevalence as the main criterion since 2022, replacing exposure/exploitability/detection used in 2014 and 2016 (p.4).
- Includes a self-check sheet for an initial evaluation of one's own security level (p.4, Fig. 2).

## Verbatim
- "Since most control components currently communicate via plain text protocols and are therefore unprotected, it is often possible to read, manipulate or import control commands without much effort." (p.3)
- "In all case compatibility with the operational business as well as applicable real-time and safety requirements must be ensured." (p.1)

## Relevance
German operator-facing threat list that maps well onto the OWASP OT Top 10 and gives entry points to model in assume-breach scenarios (remote maintenance, Internet-connected components, removable media, supply chain). Useful for the report's "threat context" section and the awareness item (#8). Edition 2022; check BSI for a newer one before citing as current.
