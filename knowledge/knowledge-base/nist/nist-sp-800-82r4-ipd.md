---
title: "NIST SP 800-82r4 ipd, Guide to Operational Technology (OT) Security, Initial Public Draft"
url: https://doi.org/10.6028/NIST.SP.800-82r4.ipd
type: standard
trust: primary
accessed: 2026-11-09
published: 2026-09-21
owasp_ot: [1,2,3,4,5,6,7,8,9,10]
version: "Rev. 4 Initial Public Draft (September 2026); comments through 2026-11-30"
local_file: "sources/nist/NIST.SP.800-82r4.ipd.pdf"
---

# NIST SP 800-82r4 ipd (draft)

## Summary

The Rev. 4 initial public draft, published 2026-09-21, with public comments open through 2026-11-30. It is a draft, not the current final guide, and wording may change.
It restructures the guide around CSF 2.0, widens sector coverage and adds zero trust and asset-discovery detail.
For a pentester, the CA-8 and RA-5 overlay text is effectively unchanged from Rev. 3. The real additions are a discovery-method taxonomy (Sec. 4.1.1.1) and a sentence preferring representative labs for assessment (Sec. 4.1.3.3).
Page references are "PDF p.N (printed M)"; printed = PDF minus 18 for the pages cited here. Line numbers in the draft were removed from quotes.

## Key facts

- Status: CSRC lists "Initial Public Draft", dated 2026-09-21, comments due 2026-11-30, submitted to sp800-82rev4@nist.gov (https://csrc.nist.gov/pubs/sp/800/82/r4/ipd, accessed 2026-11-09; PDF p.4).
- The Publication History block in the PDF still has placeholders ("Approved by the NIST Editorial Review Board on YYYY-MM-DD [Will be added to final publication.]") (PDF p.3).
- A pre-draft call for comments was published 2026-01-22, comments due 2026-02-23, and obsoleted by this IPD on 2026-09-21 (https://csrc.nist.gov/pubs/sp/800/82/r4/iprd, accessed 2026-11-09).
- Note to Reviewers changes: expanded OT sectors (BACS, WWS, food and agriculture, freight rail, maritime, IIoT and cloud); restructure around CSF 2.0, moving risk management under Govern; alignment with enterprise risk management (NIST IR 8286r1); RMF discussion in Appendix F; expanded asset management and network monitoring guidance; guidance on protecting system management functions and on zero trust (PDF p.6, printed ii).
- Appendices C and D are to move to web-based resources; Appendix E (OT Overlay) and Appendix F (RMF) are to move to separate documents in the final publication (PDF p.6, printed ii).
- The Rev. 3 Appendix E, "OT Security Capabilities and Tools", has no counterpart here; Appendix E in this draft is the OT Overlay. The pre-draft call proposed moving the capability appendix to separate or web-based resources. As a result, the Rev. 3 "extreme caution" and "safe active scanning" wording does not appear in the IPD extracted text.
- The ping-sweep and pen-test accidental incidents from Rev. 3 C.3.4 do not appear: no "ping sweep" text exists in the IPD extract.
- Audience still includes consultants performing "security assessments and penetration testing of OT" (Sec. 1.2, PDF p.24, printed 6).
- Security objectives: "OT security objectives typically prioritize safety, followed by integrity, availability, and confidentiality" (PDF p.20, printed 2). Rev. 3 ordered availability before integrity (PDF p.54 of Rev. 3).
- Asset discovery methods (Sec. 4.1.1.1, PDF pp.79-80, printed 61-62): vendor management tools, passive network monitoring, OT-aware network scanning (native protocols), independent active network scanning, software agents.
- Independent active scanning "can also negatively impact device availability and functionality, potentially leading to unwanted operations"; scanners may be configurable to limit overload; consult vendors, scope the networks and test before production (PDF p.80, printed 62).
- Method selection by device age: older or constrained devices "may not tolerate active interrogation and are better-suited to passive monitoring"; do not apply one approach uniformly (PDF p.80, printed 62).
- Passive monitoring is limited by sensor placement: much OT traffic stays on a single switch that a sensor would not see (PDF p.79, printed 61).
- Automated tools should be tested in non-production, and offline tests are "recommended before deployment"; use planned downtime; physical inspection and log analysis remain necessary (PDF p.81, printed 63).
- Vulnerability assessment (Sec. 4.1.3.3): scanning tools and assessment methods can disrupt systems; "use caution when performing this assessment on production systems"; they "may instead want to test in representative lab environments" (PDF p.86, printed 68).
- Sec. 4.1.3.3 keeps the bullet: "Performance testing, load testing, and penetration testing if the test will not adversely impact the production environment" (PDF p.86, printed 68).
- CA-8 overlay text and CA-8 (1) removal rationale are the same as Rev. 3 (E.7.4, PDF pp.252-253, printed 234-235).
- CA-2 (2) wording: "the live system, an offline replica, lab system" (E.7.4, PDF p.251, printed 233).
- RA-5 overlay text is the same as Rev. 3 apart from minor word changes (E.7.15, PDF pp.289-290, printed 271-272).
- A regex over overlay table rows found the same 192 control IDs in Rev. 3 and this draft. A sentence-level diff of the overlay from CA-8 up to SC-1 found only editorial changes in testing and scanning sentences. These are local checks on extracted text.
- Emerging detection: AI, ML and digital twins are discussed as detection aids with limited current adoption (Sec. 4.3.2.4, PDF pp.119-120, printed 101-102).
- MITRE ATT&CK for ICS is recommended as a common language in analyst workflows (Sec. 4.3.2.3, PDF p.119, printed 101).

## Verbatim

Sec. 4.1.3.3 (PDF p.86, printed 68):

> "While organizations often execute vulnerability assessments in their environments, these can be problematic in OT environments. Specifically, both vulnerability scanning tools and vulnerability assessment methods can potentially disrupt systems. Therefore, organizations should use caution when performing this assessment on production systems. They may instead want to test in representative lab environments."

CA-8 (E.7.4, PDF pp.252-253, printed 234-235):

> "Penetration testing is used with care on OT networks to ensure that OT functions are not adversely impacted by the testing process. In general, OT systems are highly sensitive to timing constraints and have limited resources. Example compensating controls include employing a replicated, virtualized, or simulated system to conduct penetration testing. Production OT may need to be taken offline before testing can be conducted. If OT systems are taken offline for testing, tests are scheduled to occur during planned OT outages whenever possible. If penetration testing is performed on non-OT networks, extra care is taken to ensure that tests do not propagate into the OT network."

RA-5 (E.7.15, PDF p.290, printed 272):

> "The organization makes a risk-based determination about how to monitor or scan its system for vulnerabilities. This may include active scanning, passive monitoring, or compensating controls, depending on the system being scanned."

Independent active scanning (Sec. 4.1.1.1, PDF p.80, printed 62):

> "However, active scanning tools can also negatively impact device availability and functionality, potentially leading to unwanted operations. It may be possible to configure these types of scanners to limit their potential to overload the resources of OT devices."

Method selection (Sec. 4.1.1.1, PDF p.80, printed 62):

> "Older or more resource-constrained devices may not tolerate active interrogation and are better-suited to passive monitoring, which collects information without sending traffic to the device."

## Relevance

- Cite as draft only, for example "SP 800-82r4 ipd (Initial Public Draft, Sept 2026)", alongside Rev. 3, never in place of it.
- Inference: the discovery taxonomy suits the tool's device profile. Age and capability could pick among passive, OT-aware, independent active and manual discovery.
- Inference: if the final follows the Note to Reviewers, CA-8 and RA-5 citations move out of the main document into a separate overlay publication, so control-based citations should name the control ID as well as the page.
- Inference: the Sec. 4.1.3.3 lab sentence is the closest NIST text to the project's testbed-first rule, but it is draft wording and says "may".
