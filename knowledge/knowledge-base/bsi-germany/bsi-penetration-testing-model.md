---
title: "Study: A Penetration Testing Model"
url: "https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/Studies/Penetration/penetration_pdf.pdf?__blob=publicationFile"
type: paper
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [4, 9]
version: "English edition, undated in text; PDF metadata created 2004-12-21, modified 2005-09-21"
local_file: "sources/bsi-germany/bsi_penetration_pdf.pdf"
---

# BSI Study: A Penetration Testing Model

## Summary

Federal Office for Information Security (BSI) study aimed at firms offering penetration tests and at those commissioning them. It defines a six-criterion test classification, German-law guidance, organizational, personnel and ethical requirements, a five-phase process, and 45 test modules (22 reconnaissance, 23 active intrusion) derived from an early OSSTMM. It is an IT-era document with no ICS or OT content, and its legal chapter predates later changes to German law. Its process, classification and contract structure remain reusable; its statutes and tool references do not.

Page references are PDF pages, which match the printed page numbers. The local PDF is byte-identical (SHA-256 match) to the file served at the URL above on the accessed date.

## Key facts

**Definition and limits**

- A penetration test is "the controlled attempt at penetrating a computer system or network from 'outside' in order to detect vulnerabilities", using the same or similar techniques as a genuine attack (p.4).
- Client goals fall into four categories: improving technical security, identifying vulnerabilities, third-party confirmation, and improving organizational and personnel security (p.11).
- A test is valid only for a point in time and cannot support assertions about future security. The more protection a system needs, the more often it should be tested (p.11, p.13).
- A penetration test does not replace other IT security tests or a security policy; authorization and backup concepts are better tested in other ways (p.13).

**Classification: six criteria (section 3.4, p.13-17)**

- Information base: black-box or white-box (p.14-15).
- Aggressiveness, four levels (p.15):
  - passive: vulnerabilities detected but not exploited;
  - cautious: exploited only if, to the tester's best knowledge, the system will not suffer (for example default passwords);
  - calculated: exploits that might cause disruption, after weighing success likelihood and consequences (for example password guessing, known buffer overflows on precisely identified targets);
  - aggressive: all potential vulnerabilities, including exploits against unclearly identified targets and DoS. The tester must expect neighboring systems or network components may also fail.
- Scope: full, limited or focused (p.15-16). A full test is advisable for a first-time test (p.15). A focused test cannot provide general information about IT security (p.15-16).
- Approach: covert or overt. Client staff may join an overt white-box test, "particularly advisable with highly critical systems" because testers can react faster to unexpected problems (p.16).
- Technique: network-based, other communications networks, physical, social engineering (p.16-17).
- Starting point: outside or inside (p.17).
- Not all combinations are useful: an aggressive test is identified quickly and fits badly with stealth (p.14).
- A multistage approach is recommended to minimize risk, for example cautious covert black-box from outside, then aggressive overt white-box from inside (p.17).

**Five phases (section 6.2, p.44-46; detail in chapter 7, p.80-85)**

1. Preparation: define goals, legal conditions, classification, risks, contingency measures; put agreements in writing (p.44-45, p.80-81). The phase ends in a detailed plan of when which components are penetrated at what intensity, plus escalation stages (p.81).
2. Reconnaissance: information gathering, described as "the passive penetration test" (p.45). Scanners supplement manual search but are no substitute (p.82).
3. Analysis of information and risks: select phase 4 targets by goals, risk and effort. Restrictions must be documented and justified because they reduce the test's informative value (p.45, p.83). A written shortlist is discussed with the client before any active attempt (p.83).
4. Active intrusion attempts: the highest-risk phase. For systems with very high availability or integrity requirements, potential effects must be weighed before critical procedures such as buffer overflow exploits (p.46).
5. Final analysis and clean-up: management summary, positive and negative findings, prioritized risks, recommendations, action plan with owner and schedule per critical vulnerability (p.84-85). The tester removes installed software and modifications and restores the prior state (p.85).

- Test objects are accessed only in phases 2 and 4 (p.48).
- Documentation is compiled during all phases, and deviations from the method are documented and justified (p.47).

**Modules**

- Reconnaissance modules I 1 to I 22 (p.49) and active intrusion modules E 1 to E 23 (p.50), each with expected results, requirements, steps and risks (p.53).
- Selection is by a negative exclusion principle: classification excludes modules, any other exclusion must be justified in writing (p.51). Example: "cautious" aggressiveness excludes E 13, the DoS test (p.52).
- E 13's stated risk is that the tested system or network components may be impaired or crash (p.73).

**Legal aspects (chapter 4, German law as of the study's date)**

- The criminal-law review covers Secs. 202a, 263a, 268, 269, 303a, 303b StGB (p.25-26). Note: p.24 mistranslates StGB as "German Civil Code"; it is the Criminal Code.
- Authorized testing is justified by client approval, so "the exact definition of the scope of action" is decisive, and a separate declaration of approval before testing is advised (p.27).
- The ZKDSG, TKG interception rules and the EU framework decision proposal are discussed (p.28-29).
- A works council has a right to be informed (Sec. 80 II BetrVG) and should be involved in planning under Sec. 87 (1) No. 6 BetrVG, since test results are objectively suited to monitoring employees. The study "strongly" recommends early involvement (p.29-30).
- Contract content: objectives, the six classification values, techniques used and excluded with reasons (p.31-32); signature by a legal representative of the client, with evidence of authority requested (p.32); subcontractors named (p.32); written form including subsidiary agreements (p.32).
- Client duties: information, notifying affected third parties, backups (p.33). Tester duties: secrecy, tool licensing, documentation, due care (p.33-34).
- Start and finish dates are fixed so later attempts can be identified as real attacks (p.34). A special right to terminate can be included (p.34-35). Liability limits apply within the AGB rules (p.35).

**Organizational requirements and production systems (section 5.1, p.36-38)**

- Outsourced systems should be excluded unless the operator approves in writing (p.36).
- "Penetration tests can impair the functionality of production systems"; attacks should occur at agreed times, avoiding crucial processing. Such scheduling is possible in white-box tests only, since black-box testers lack criticality information (p.36-37).
- The contract must at least specify who to notify and when on suspected failure. Listed disruptions: complete failure, partial failure, incorrect responses, large response-time increases, countermeasures to a covert test, third-party attacks (p.37).
- A client employee can monitor the test and halt it if necessary; extra backups and a contingency plan are advised (p.37).
- Intrusion attempts on business-critical systems may need to be made outside working hours with responsible administrators present (p.84).
- Production and test servers are tested differently, based on data classification (p.81).

**Personnel and ethics**

- Tests "should only be performed by persons with many years of experience in IT security"; required skills include OS, TCP/IP and other protocols, programming, security products, tools and applications (p.39-40).
- Testers must weigh whether exploitation is needed at all. If disruption is to be avoided as far as possible, vulnerabilities should not be actively exploited, and the result is identified vulnerabilities without proof of penetration (p.43).
- Social engineering can harm employees even in anonymized reports, and many experts reject it unless security requirements are very high (p.42-43).

## Verbatim

> "The tester has to be aware that, in addition to the systems being tested, neighboring systems or network components might also fail as a result of these tests." (p.15)

> "Penetration tests can impair the functionality of production systems. Since the aim of a test is to detect vulnerabilities, but without endangering orderly operations, the actual attacks should take place at a time agreed to by both parties." (p.36)

> "If, on the other hand, a potential disruption to operations is to be avoided as far as possible, vulnerabilities should not be actively exploited." (p.43)

> "For systems with very high availability or integrity requirements, the potential effects need to be carefully considered before performing critical test procedures, such as the utilization of buffer overflow exploits." (p.46)

## Relevance

Inference, not stated by the source:

- Transfers to OT well: six-criteria classification as the engagement-defining vocabulary; exclusion principle with justified exclusions; phase 3 shortlist reviewed with the client before active work; named observer who can halt testing; disruption categories and notification contract terms; signed authorization by a legal representative; works-council involvement.
- Needs adaptation: for live OT, "passive" and at most "cautious" look like the only defensible default levels, while "calculated" and "aggressive" fit an isolated test bench. E 13 should be excluded on production. Disruption categories need physical-process and safety outcomes added.
- Does not transfer: module content assumes TCP/IP office networks, telephone, fax and modem; nothing covers PLCs, field buses or safety systems. The "outside working hours" advice conflicts with IND.1.M17 (see `bsi-ind-1-umsetzungshinweise.md`).
- Legal chapter is historical. Current § 202c StGB criminalizes preparation by obtaining or distributing passwords, security codes or programs for §§ 202a/202b offenses, and current § 303b includes attempt, preparation and aggravation for impairing the supply of vital goods or services (read on gesetze-im-internet.de, 2026-11-09). Neither aspect appears in the study, so a current legal review is needed before reuse.
- Informs open tasks on engagement process model and rules of engagement.
