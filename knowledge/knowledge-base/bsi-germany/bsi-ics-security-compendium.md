---
title: "ICS Security Compendium (BSI)"
url: "https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Industrielle-Steuerungs-und-Automatisierungssysteme/Download/download.html"
type: standard
trust: primary
accessed: 2026-11-10
published: unknown
owasp_ot: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
version: "1.23 (© BSI 2013; PDF build 2016-01-28); a separate supplier/manufacturer compendium exists"
local_file: "sources/bsi-germany/ICS-Security_compendium.pdf"
---

# BSI ICS Security Compendium

## Summary
BSI's 121-page reference work on ICS security for asset owners: ICS basics and a five-level hierarchy, threats, an overview of standards (international, German, foreign), a best-practice guide for asset owners, and in chapter 6 a full "Methodology for audits of ICS installations" covering kick-off, document review, audit plan, rules of engagement, test methods (penetration tests, on-site review, interviews), assessment and reporting. It is dated (2013 text) but is the most detailed BSI description of how to test ICS. Read from the user's local PDF; canonical URL is BSI's ICS download page (direct PDF URL not confirmed).

## Key facts
- Typical audit observations (Table 1, p.8): restrictive-enough firewall rules missing, undocumented rules and modems, always-on modems, remote maintenance connected directly to field level, unhardened OS, wireless without encryption, industrial switches lacking robustness to non-standard traffic and containing hard-coded passwords.
- Audit procedure (ch. 6.2): kick-off, familiarisation, coordination workshop, audit plan, document check, on-site review, follow-up, report and final presentation; operations staff must be involved from the start (p.97).
- Required documents include the ICS security concept, network plans and communication relations, list of critical production processes, and audit reports of the last five years (p.97-98).
- A risk analysis of the planned tests, coordinated with the people in charge, is "the only way to minimise the risk of possibly critical impacts of tests on the plants" (p.98).
- Rules of engagement (6.2.3, p.99): which test methods are taboo, which systems or production areas must not be affected, who decides on unclear rules, who must be informed, who is on call, who must be present.
- Penetration tests (6.2.4.1, p.99): optional, "used with caution", most useful at FAT/SAT; components may enter an undefined state; only in the maintenance window; preferably restricted to systems not directly tied to production (e.g. engineering workstations); in some areas, dispense with them and use passive methods only.
- Vulnerability documentation table: ID, IP address, ICS component, service, description; refers to VDI 2182 Part 2 (p.100).
- Network level (6.3.3, p.105-107): sniffing via mirror port or tap is passive except for switch load; active methods (ping sweep, port scan, ARP scan) must be explicitly in the audit plan and RoE "because components may fail!"; cites the NIST cases of a ping sweep turning a 3 m robot arm 180° and a sweep halting a wafer line ($50,000 loss).
- Device level (6.3.4): vulnerability scanning, authenticated scans, and optionally exploit development to prove exploitability for the asset owner (p.107).
- ICS security test (6.3.7): functional checklist tests of authentication, logging and alarming, port security, IDS, NTP, backup/restore (p.108-109).
- Assessment scheme: measure implemented / partially / not / dispensable; deficiency "security deficiency" or "serious security deficiency" (p.101-102).

## Verbatim
- "These tests are optional and should be used with caution. They make sense especially within the scope of factory acceptance tests or site acceptance tests. The problem of penetration tests is that components may enter into an undefined state when vulnerabilities are found." (p.99)
- "Active methods in the productive areas must be documented explicitly in the audit plan and must be covered by the rules of engagement agreed upon. The possible consequences should be considered before carrying out the methods, because components may fail!" (p.106)

## Relevance
Primary German source for the scoping and rules-of-engagement step and for the passive-first rule on production, and it supports testing at FAT/SAT or on test systems, matching the project's testbed-aggressive mode. Its audit-plan and vulnerability-table structure can seed the report format. Its standards overview (ch. 4) is from 2013, so check editions before citing.
