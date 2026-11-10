---
title: "NIST SP 800-82 Rev. 2, Guide to Industrial Control Systems (ICS) Security"
url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r2.pdf
type: standard
trust: primary
accessed: 2026-11-09
published: 2015-06-03
owasp_ot: [1,2,3,4,5,6,7,8,9,10]
version: "Rev. 2 (May 2015), withdrawn 2023-09-28"
local_file: "sources/nist/NIST_GuideToIndustrialControlSystemspdf.pdf"
license: "Not subject to copyright in the United States (PDF front matter)"
superseded_by: nist-sp-800-82r3
---

# NIST SP 800-82 Rev. 2 (withdrawn)

## Summary

Withdrawn May 2015 edition of NIST's ICS security guide, kept for history and for comparing wording across revisions.
Its CA-8 and RA-5 ICS supplemental guidance already holds the core safe-testing position: use care, prefer a replicated, virtualized or simulated system, and take production offline during planned outages if it must be tested.
Do not cite as current. Cite SP 800-82 Rev. 3, or the Rev. 4 draft as forward-looking.
Page references give the PDF page, then the printed page label where one was checked. The local PDF carries a one-page withdrawal notice as PDF p.1.

## Key facts

- The local PDF opens with a NIST withdrawal notice: Rev. 2 was withdrawn on September 28, 2023 and is "superseded in its entirety by NIST SP 800-82r3" (PDF p.1). CSRC confirms the withdrawal and supersession (https://csrc.nist.gov/pubs/sp/800/82/r2/final, accessed 2026-11-09).
- Date stamps differ by source: the notice and CSRC "Date Published" say May 2015; the CSRC document history says 06/03/15. The frontmatter uses the history date.
- Audience explicitly includes "Security consultants who perform security assessments and penetration testing of ICS" (PDF p.16).
- ICS security objectives "typically follow the priority of availability and integrity, followed by confidentiality" (PDF p.11).
- CA-8 Penetration Testing is selected in the HIGH baseline only: the summary table shows "Not Selected / Not Selected / CA-8" (PDF p.184) and the control entry marks one selection (PDF p.205, G-25).
- CA-8 guidance: pen testing is "used with care"; replicated, virtualized or simulated systems are "example compensating controls"; production "may need to be taken off-line"; testing on non-ICS networks must not propagate into ICS (PDF p.205, G-25).
- RA-5 guidance: active scanning needs a "risk-based determination"; passive monitoring/sniffing may be a compensating control; replicated, virtualized or simulated systems are examples; host-based examination is an example compensating control (PDF p.231, G-51).
- CA-2 (2) requires risk analysis for choosing an assessment target, "e.g., the live system, an off-line replica, a simulation" (PDF p.204, G-24).
- Appendix E says traffic and exploits from active testing, combined with limited ICS resources, "have been known to cause ICS to malfunction", and describes Sandia's preferred less intrusive, passive techniques (PDF p.170, E-3, citing reference [77], SAND2005-2846P, listed at PDF p.178).
- Accidental-incident examples: a ping sweep made a 3 m robotic arm in standby swing 180 degrees; another ping sweep hung a wafer-fab controller, destroying $50,000 of wafers; an IT pen test that strayed into a network connected to SCADA locked up SCADA and stopped gas delivery for four hours (PDF p.151, C-14).
- Inventory tools should be assessed before use on ICS; evaluation "may include testing in similar, non-production control system environments" (PDF p.48, 4-7, Sec. 4.5.1).
- Security controls present during factory and site acceptance testing should be checked as still installed and working in production (PDF p.88, 6-14).

## Verbatim

CA-8 (PDF p.205, G-25):

> "Penetration testing is used with care on ICS networks to ensure that ICS functions are not adversely impacted by the testing process. In general, ICS are highly sensitive to timing constraints and have limited resources. Example compensating controls include employing a replicated, virtualized, or simulated system to conduct penetration testing. Production ICS may need to be taken off-line before testing can be conducted. If ICS are taken off-line for testing, tests are scheduled to occur during planned ICS outages whenever possible. If penetration testing is performed on non-ICS networks, extra care is taken to ensure that tests do not propagate into the ICS network."

RA-5 (PDF p.231, G-51):

> "Active vulnerability scanning, which introduces network traffic, is used with care on ICS systems to ensure that ICS functions are not adversely impacted by the scanning process. The organization makes a risk-based determination whether to employ active scanning. Passive monitoring /sniffing may be used as part of a compensating control. Example compensating controls include providing a replicated, virtualized, or simulated system to conduct scanning. Production ICS may need to be taken off-line before scanning can be conducted. If ICS are taken off-line for scanning, scans are scheduled to occur during planned ICS outages whenever possible. If vulnerability scanning tools are used on non-ICS networks, extra care is taken to ensure that they do not scan the ICS network. Network scanning is not applicable to non-addressable communications. Vulnerability examination may be performed using other mechanisms than scanning to identify the objects being examined. Host-based vulnerability examination is an example compensating control."

CA-2 (2) (PDF p.204, G-24):

> "The organization conducts risk analysis to support the selection of assessment target (e.g., the live system, an off-line replica, a simulation)."

Appendix E (PDF p.170, E-3):

> "The additional traffic and exploits used during active vulnerability and penetration testing, combined with the limited resources of many ICS, have been known to cause ICS to malfunction."

Penetration testing incident (PDF p.151, C-14):

> "The consulting organization carelessly ventured into a part of the network that was directly connected to the SCADA system. The penetration test locked up the SCADA system and the utility was not able to send gas through its pipelines for four hours."

## Relevance

- Historical baseline only, for showing that the "with care, prefer a replica" position dates back at least to 2015.
- Inference: the ping-sweep and pen-test incidents are useful rationale for scope gates, but cite Rev. 3 Appendix C.3.4 for the same incidents, because Rev. 2 is withdrawn.
