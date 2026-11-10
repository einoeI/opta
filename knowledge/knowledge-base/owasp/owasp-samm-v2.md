---
title: "OWASP Software Assurance Maturity Model (SAMM) v2.0"
url: "https://owaspsamm.org/model/"
type: standard
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [8, 9]
version: "V2.0 PDF; PDF metadata created 2022-08-24"
local_file: "sources/owasp/SAMM-v2-PDF.pdf"
---

# OWASP SAMM v2

## Summary

Prescriptive maturity model for software security, with 5 business functions and 15 security practices, each having two streams and three maturity levels. Each activity has an assessment question, quality criteria and a graded answer scale, which makes it usable as a scoring instrument. It targets software development, not OT or penetration-testing teams, and contains no reference to SCADA, PLC or operational technology. Education & Guidance, Strategy & Metrics, and Verification > Security Testing can be adapted to measure knowledge sharing in a testing practice.

Page references are PDF pages, which match the printed "OWASP SAMM V2.0" page numbers.

## Key facts

**Structure**

- Business functions and practices: Governance (Strategy & Metrics, Policy & Compliance, Education & Guidance); Design (Threat Assessment, Security Requirements, Secure Architecture); Implementation (Secure Build, Secure Deployment, Defect Management); Verification (Architecture Assessment, Requirements-driven Testing, Security Testing); Operations (Incident Management, Environment Management, Operational Management) (owaspsamm.org/model).
- v2 measures maturity by coverage and quality, adds quality criteria per activity, and keeps three maturity levels (owaspsamm.org/release-notes-v2).

**Verification > Security Testing (p.229-249)**

- Two streams: A Scalable Baseline favors width with automation; B Deep Understanding favors depth with manual testing of high-risk components (p.230).
- Level 1: automated tools; manual testing of high-risk components (p.231).
- Level 2: application-specific automation; manual penetration testing (p.231).
- Level 3: integrate automated testing in build and deploy; integrate security testing into the development process (p.231).
- Unlike Requirements-driven Testing, the practice uncovers weaknesses irrespective of requirements (p.229).
- Stream B L2 quality criteria: application-specific test cases; technical and logical issues; stakeholders review results under risk management; qualified personnel perform testing. Answers grade from No to most or all applications (p.246).
- Where software cannot realistically be tested outside production, techniques such as blue-green deployments or A/B testing allow "ring-fenced security testing in production" (p.244).
- L2 includes spreading knowledge of manual testing and results across the team (p.245). A central group coaches security champions on first-time execution of test cases (p.244).
- L3 activity: review results, include them in awareness training, "integrate lessons learned in overall playbooks to improve security testing" (p.248).
- L3 assessment: "Do you use the results of security testing to improve the development lifecycle?"; quality criteria include incorporating results into training and playbooks; answers range from ad-hoc to at least annually (p.249).

**Governance > Education & Guidance (p.59-80)**

- Stream A Training & Awareness; Stream B Organization & Culture (p.60).
- A L1: awareness training with auditable sign-off (p.62-63); quality criteria include updated in last 12 months and required at onboarding (p.64). A L2: role-specific training, including for testers and security auditors (p.65-66). A L3: in-house training programs facilitated by developers across teams (p.61).
- B L1: a Security Champion in each team, with set weekly hours and periodic briefings (p.72); champions review external test results before backlog entry (p.74).
- B L2: a center of excellence with a charter that publishes standards and identifies high-maturity teams to replicate their practices (p.75-77).
- B L3: communication and knowledge-sharing platforms and communities; recognize those who help the most (p.78). Criteria: a single portal across teams, used for timely information, recognized as central repository, content persistent and searchable, provides security metrics (p.80).

**Governance > Strategy & Metrics, Stream B Measure & Improve (p.20, p.29-38)**

- L1: define metrics in three categories: effort (for example training hours), result, environment (p.29). Metrics should be consistently measured, inexpensive, cardinal or percentage, and have a unit (p.30).
- L2: KPIs with thresholds and action guidance, set after enough data for realistic objectives (p.33-35).
- L3: influence strategy from metrics (p.20).

**Currency (checked 2026-11-09)**

- owaspsamm.org/model presents version 2.0 and offers the v2 PDF. Search found no SAMM v3 release.
- The GitHub repository owaspsamm/core shows v2.2.0 tagged "Latest" (date shown as 06 Jul, year not displayed) and v2.1.0 (18 Sep, year not displayed). The v2.2.0 notes only reference a merge commit, so what changed could not be determined, and the v2.1/v2.2 relationship to the published 2.0 PDF is unclear.

## Verbatim

> "Integrate lessons learned in overall playbooks to improve security testing as part of the organization development." (p.248)

> "You review test results and incorporate them into security awareness training and security testing playbooks" (p.249, quality criterion)

> "The portal is widely recognized by developers and architects as a centralized repository of the organization-specific application security information" (p.80, quality criterion)

> "Spread the knowledge of manual security testing and the results across the development team to improve security knowledge and awareness inside the organization." (p.245)

## Relevance

Inference, not stated by the source:

- SAMM does not measure pentest teams directly. Adapting it means rewording "application" and "developer" to "engagement" and "tester", which makes results an adapted self-assessment, not a SAMM score.
- Most useful instruments for knowledge sharing: Education & Guidance Stream B L3 criteria (single, searchable, persistent portal); Security Testing Stream B L3 (results fed into playbooks and training, with a time-graded scale); Strategy & Metrics L1 (effort, result, environment).
- Candidate team metrics in SAMM's terms: effort (training hours, playbook updates), result (share of findings with a reusable playbook entry), environment (number of OT protocols or vendors covered).
- Blue-green and A/B production testing do not carry over to physical processes.
- Informs open tasks on maturity measurement of a testing practice.
