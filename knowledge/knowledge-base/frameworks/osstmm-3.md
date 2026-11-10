---
title: "OSSTMM 3: The Open Source Security Testing Methodology Manual"
url: "https://www.isecom.org/OSSTMM.3.pdf"
type: standard
trust: primary
accessed: 2026-11-09
published: 2010-12-14
owasp_ot: [4, 9]
version: "3.02"
local_file: "sources/frameworks/OSSTMM.3.pdf"
license: "Creative Commons 3.0 Attribution-NonCommercial-NoDerivs and Open Methodology License 3.0"
---

# OSSTMM 3

## Summary

ISECOM's peer-reviewed methodology for testing operational security across five channels. It replaces risk-based scoring with the rav, a fact-based attack-surface metric computed from porosity, controls and limitations, and requires a signed Security Test Audit Report (STAR). Its 42 Rules of Engagement are the most explicit in this source set. A full-text search finds no mention of SCADA, ICS, PLC, Modbus or industrial control. Version 3.02 dates from 2010 and remains the only full edition offered by ISECOM, while OSSTMM 4 is in development.

Page references are PDF pages; the printed folio is PDF page minus 2. The local PDF is byte-identical (SHA-256 match) to the file served at the URL above on the accessed date.

## Key facts

**Version and scope**

- Current version stated as 3.02, published 2010-12-14; the original was published 2000-12-18; versions before 3.0 are obsolete (p.5).
- Tests operational security of physical locations, human interactions and all forms of communications (p.4).
- rav values from 2.x are incompatible with 3.0. Earlier metrics measured risk with degradation; 3.x measures attack surface instead (p.4).
- Use is free for testing, education, consulting and research; derivations are not allowed; methodology may not be sold within a tool or checklist without permission (p.6).

**Security and safety definitions**

- Security is the separation of an asset and a threat, and safety is the control of a threat or its effects (p.22). This is OSSTMM's own usage, not functional safety.

**Channels (p.37)**

- PHYSSEC: Human, Physical. SPECSEC: Wireless. COMSEC: Telecommunications, Data Networks.

**Six test types (p.38-39)**

| Type | Analyst knowledge | Target awareness | Also known as |
|---|---|---|---|
| Blind | none | full | Ethical Hacking |
| Double Blind | none | none | Black Box, Penetration test |
| Gray Box | limited | full | Vulnerability Test |
| Double Gray Box | limited | scope and time frame only | White Box |
| Tandem | full | full | In-House Audit, Crystal Box |
| Reversal | full | none | Red Team |

- If the precise test type is not available to a third-party reviewer, the audit should be treated as Blind, the type "with the least merit towards a thorough security test" (p.38).

**Process**

- Four Point Process: Induction, Inquest, Interaction, Intervention (p.45).
- 17 modules in four phases (Data Networks numbering, ch. 11): A Induction: Posture Review, Logistics, Active Detection Verification. B Interaction: Visibility Audit, Access Verification, Trust Verification, Controls Verification. C Inquest: Process, Configuration, Property Validation, Segregation Review, Exposure Verification, Competitive Intelligence. D Intervention: Quarantine Verification, Privileges Audit, Survivability Validation, Alert and Log Review.
- Intervention is often the final phase so disruptions do not affect less invasive tests (p.104).
- Survivability tests "must be closely monitored as the intent is to cause failure and this may be unacceptable to the target's owner" (11.16, p.185). 11.16.3 maps gatekeepers shutting down systems for evacuation or safety concerns (p.185).
- The STAR checklist includes "Applied testing safety measures", test instabilities, and downtime in scope (p.197).

**Metrics: rav (ch. 4)**

- The rav is "a scale measurement of the attack surface, the amount of uncontrolled interactions with a target", balancing operations, limitations and controls (p.65).
- 100 rav is perfect balance; below is too few controls; above suggests more controls than necessary (p.65, p.87).
- It does not measure risk but enables measuring it (p.65).
- Porosity sums visibility, access and trust (p.82). Controls and five limitation classes (Vulnerability, Weakness, Concern, Exposure, Anomaly) complete the calculation (p.30).
- Three outputs: Actual Security Delta for comparing products, True Protection, and Actual Security (p.87). There are no weights (p.81).
- Rav uses a base-10 logarithm per section 4.1 (p.65). The equations' typesetting does not survive text extraction; check PDF p.82-87 before implementing.
- A rav can only be derived from operational security testing (p.66).
- STAR requires date and duration, analysts, test type, scope, index, channel, vector, attack surface metric, tests completed or not, issues, unknowns (p.52).

**Rules of Engagement (section 2.4, p.40-42)**

- Rule 6: no testing without explicit written permission.
- Rule 7: testing obviously highly insecure and unstable systems, locations and processes is forbidden until proper security infrastructure is in place.
- Rule 9/12: liability limited to job cost unless malice is proven; signed testing permission.
- Rule 10: contract explains limits and dangers.
- Rule 13: emergency contacts in the contract.
- Rule 14: clear, specific permissions for survivability failures, DoS, process testing and social engineering.
- Rule 19: test plan may not exceed the Analyst's competence.
- Rule 20: must maintain safety, health, welfare and privacy of the public.
- Rule 22: notify only key people, to prevent temporary security raises.
- Rule 25: know tools and test them in a restricted area before client use.
- Rule 26: explicit-permission DoS only where no damage is done outside scope.
- Rule 28: limitations that may immediately endanger lives are reported immediately with a practical solution.
- Rule 30: scope may not be left in a position of less actual security.
- Rule 35: notify client before new, dangerous or high-traffic tests.
- Rule 39: only quantitative metrics in reports.

**Currency (checked 2026-11-09)**

- ISECOM's research page offers "Download OSSTMM 3" as the only full manual. It presents "OSSTMM 4: Security derived from physics" with multiple channels including PQE, AI/ML, Cloud and IoT, and early access to "Facets" for Gold members.
- ISECOM's llms.txt states: "OSSTMM 4 is in active development." No release date is given.

## Verbatim

> "The security testing of obviously highly insecure and unstable systems, locations, and processes is forbidden until the proper security infrastructure has been put in place." (Rule 7, p.40)

> "The Analyst must respect and maintain the safety, health, welfare, and privacy of the public both within and outside the scope." (Rule 20, p.41)

> "The Analysts are required to know their tools, where the tools came from, how the tools work, and have them tested in a restricted test area before using the tools on the client organization." (Rule 25, p.41)

> "The rav does not measure risk for an attack surface, rather it enables the measurement of it." (p.65)

## Relevance

Inference, not stated by the source:

- Usable for OT: RoE as a contract and conduct baseline; requirement to state what was not tested; STAR format; Trust Verification and porosity as a frame for zone-and-conduit reviews; Reversal, Tandem and Double Gray Box as clearer naming than black/white.
- Rule 7 is a real problem in OT, where fragile legacy devices are normal. A site could be read as untestable; a passive or bench-only approach is the way to reconcile it, and this should be stated in rules of engagement.
- Limited for OT: no OT protocols, no process or safety concept. "Safety" means threat control, not IEC 61508-style functional safety, so it must not be cited for the latter.
- rav weakness for OT: with no weights, one SIS-reachable path counts like any other interaction, so consequence must be assessed separately. Its comparability between scopes needs care, as counts depend on the test's scope definition.
- Age: 3.02 predates current cloud, IoT and much OT practice; license restricts embedding the methodology in commercial tools or checklists, relevant if this project productizes it.
- Informs open tasks on metrics and rules of engagement.
