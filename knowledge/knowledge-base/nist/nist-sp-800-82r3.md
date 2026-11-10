---
title: "NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security"
url: https://doi.org/10.6028/NIST.SP.800-82r3
type: standard
trust: primary
accessed: 2026-11-09
published: 2023-09-28
owasp_ot: [1,2,3,4,5,6,7,8,9,10]
version: "Rev. 3 (Final, September 2023)"
local_file: "sources/nist/NIST_GuideToOperationalTechnology.pdf"
license: "Not subject to copyright in the United States (PDF front matter)"
---

# NIST SP 800-82 Rev. 3

## Summary

The current final edition of NIST's OT security guide as of 2026-11-09. CSRC lists it as Final and does not mark it superseded; a Rev. 4 initial public draft is open for comment until 2026-11-30.
It carries the safe-testing rules a pentester should cite: CA-8 and RA-5 overlay discussion, the CA-2 (2) risk analysis for target selection, and Appendix E.2.2/E.2.3 on passive and active scanning.
NIST's position is conditional, not an absolute ban on active testing of live systems.
Page references are "PDF p.N (printed M)"; printed = PDF minus 17 for the pages cited here.

## Key facts

- Status: CSRC document history lists "09/28/23: SP 800-82 Rev. 3 (Final)", published September 2023, superseding Rev. 2. The page carries a 2026-09-21 planning note pointing to the Rev. 4 draft (https://csrc.nist.gov/pubs/sp/800/82/r3/final, accessed 2026-11-09).
- Audience includes "Security consultants who perform security assessments and penetration testing of OT" (PDF p.23, printed 6).
- OT cybersecurity "prioritizes safety, followed by availability, integrity, and confidentiality" (PDF p.54, printed 37).
- RMF Task P-14 note: risk assessments, "including performance/load testing and penetration testing", are done "with care to ensure that OT operations are not adversely impacted" (Table 6, PDF p.75, printed 58).
- Asset tools (Sec. 6.1.1): consider whether the collection method, for example active scanning, harms OT. Testing automated tools on offline systems or components "is recommended prior to deployment" (PDF p.108, printed 91). Fall back to manual processes if automation is not feasible.
- Data-flow tools using active scanning or in-line probes: consider using them "during planned downtime" (Sec. 6.1.1.1, PDF p.109, printed 92).
- Automated topology discovery captures only IP-based devices. Test automation "in a non-production environment", then consider using it during planned downtime; physical inspection and log analysis are alternatives (Sec. 6.1.1.2, PDF p.109, printed 92).
- Monitoring automation using active scanning "should be tested before deployment into the OT system" (Sec. 6.3.2, PDF p.145, printed 128). A passive monitor "might be able to detect vulnerable network services without having to scan the devices" (PDF p.146, printed 129).
- Vulnerability identification (Sec. 6.3.2.4, DE.CM-8): test scanning tools "in an offline environment prior to implementing them in production"; performance, load and penetration testing only "if the test will not adversely impact the production environment" (PDF p.150, printed 133).
- Patches: test on a sandbox system or test environment where possible, deploy in maintenance windows, have a recovery plan (PDF p.94, printed 77).
- Passive scanning (E.2.2): adds no traffic; identifies only actively communicating devices; cannot inspect encrypted traffic without provisioning; "will often take days to complete" (PDF pp.225-226, printed 208-209).
- Active scanning (E.2.3): owners "should exercise extreme caution"; scans may cause device instability or interfere with process state; schedule during planned outages whenever possible (PDF p.226, printed 209).
- "Safe active scanning" (E.2.3): learns equipment passively, then uses device-specific communication "without risk to OT operations" (PDF p.226, printed 209). This is NIST's description of a product class, not a tested guarantee.
- CA-2 (2) overlay: risk analysis supports choosing the assessment target, "the live system, an offline replica, or lab system" (F.7.4, PDF p.258, printed 241).
- CA-8 overlay: same logic as Rev. 2, with "replicated, virtualized, or simulated system" as example compensating controls (F.7.4, PDF p.259, printed 242).
- CA-8 is selected in the HIGH baseline only. The overlay removes CA-8 (1), independent penetration testing agent or team, from HIGH because independent OT-skilled testers may not be available (PDF pp.233, 259-260; printed 216, 242-243).
- RA-5 overlay: risk-based choice of active scanning, passive monitoring or compensating controls. Passive monitoring plus manual inspection can feed an inventory cross-referenced against CISA advisories and NVD. Automated scanning does not apply to non-routable or serial networks (F.7.15, PDF pp.295-296, printed 278-279).
- Accidental incidents retained from Rev. 2: ping sweep moving a robotic arm, ping sweep hanging a wafer fab ($50,000 of wafers), pen test locking up SCADA for four hours (C.3.4, PDF p.201, printed 184).
- Rev. 3 change log: scope expanded from ICS to OT; new OT overlay for SP 800-53 Rev. 5 (Appendix G, PDF p.316, printed 299).

## Verbatim

CA-8 (F.7.4, PDF p.259, printed 242):

> "Penetration testing is used with care on OT networks to ensure that OT functions are not adversely impacted by the testing process. In general, OT systems are highly sensitive to timing constraints and have limited resources. Example compensating controls include employing a replicated, virtualized, or simulated system to conduct penetration testing. Production OT may need to be taken offline before testing can be conducted. If OT systems are taken offline for testing, tests are scheduled to occur during planned OT outages whenever possible. If penetration testing is performed on non-OT networks, extra care is taken to ensure that tests do not propagate into the OT network."

CA-8 (1) rationale (PDF p.260, printed 243):

> "Specific expertise is necessary to conduct effective penetration testing on OT systems, and it may not be feasible to identify independent personnel with the appropriate skillset or knowledge to perform penetration testing on an OT environment."

RA-5 (F.7.15, PDF pp.295-296, printed 278-279):

> "The organization makes a risk-based determination of how to monitor or scan for vulnerabilities on their system. This may include active scanning, passive monitoring, or compensating controls, depending on the system being scanned. For example, vulnerability examination may be performed using passive monitoring and manual visual inspection to maintain an up-to-date inventory of assets. That inventory can be cross-referenced against a list of known vulnerabilities (e.g., CISA advisories, NIST NVD). Production may need to be taken offline before active scans can be conducted. Scans are scheduled to occur during planned OT outages whenever possible. If vulnerability scanning tools are used on adjacent non-OT networks, extra care is taken to ensure that they do not mistakenly scan the OT network. Automated network scanning is not applicable to non-routable communications, such as serial networks. Compensating controls include providing a replicated or simulated system for conducting scans or host-based vulnerability applications."

Active scanning (E.2.3, PDF p.226, printed 209):

> "OT network owners should exercise extreme caution when permitting active scanning on an operational network due to device sensitivity on the target network. Active scans may cause device instability or interfere with the device process state, potentially impacting safety and integrity. Active scans should be scheduled to occur during planned OT outages whenever possible."

Sec. 6.3.2.4 (PDF p.150, printed 133):

> "Performance testing, load testing, and penetration testing if the test will not adversely impact the production environment"

## Relevance

- This is the revision to cite as current. The repo's "SP 800-82 Rev. 3" citation (`research-notes.md` line 279, `handoff-prompt.md` line 167) remains correct on 2026-11-09.
- Fact versus project rule: NIST does not say live OT must be read-only or passive. It permits active scanning and pen testing with care, under a risk-based decision, ideally offline or in planned outages. The handoff's "aggressive testing only on a testbed; any live OT device is read-only/passive (NIST SP 800-82)" is stricter than the text.
- Inference: keep the stricter rule as a project policy "informed by" SP 800-82, and do not phrase it as a NIST requirement.
- Inference: the two-mode runbook maps cleanly onto CA-2 (2) (target selection), CA-8 and RA-5. A live-outage mode, with the asset owner's approval, is a case NIST allows and the project currently excludes.
- OWASP OT Top 10's mapping table cites this revision as "NIST SP 800-82:v3" (see `owasp-ot-top-10-2025.md`).
