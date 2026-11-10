---
title: "MITRE ATT&CK Matrix for ICS"
url: "https://attack.mitre.org/matrices/ics/"
type: standard
trust: primary
accessed: 2026-11-09
published: 2026-10-13
owasp_ot: [1,2,3,4,5,6,7,10]
version: "ATT&CK content v20.1 (website v5.2.1)"
---

## Summary
The ATT&CK for ICS matrix at content version v20.1 has 12 tactics and covers Embedded, Windows, Linux and Network Devices platforms.
It is the project's reference taxonomy for mapping test actions and findings.
`published` is the start date of v20.1 from https://attack.mitre.org/resources/versions/.
Several older technique IDs have been restructured into T16xx/T17xx parents with sub-techniques.

## Key facts
- Current version is ATT&CK v20.1, listed as "October 13, 2026 - current"; v19.2 ran April 28 to October 12, 2026; v18.1 ran October 28, 2025 to April 27, 2026; v17.1 ran April 22 to October 27, 2025.
- Tactics and top-level technique counts, in matrix order: Initial Access 12; Execution 9; Persistence 5; Privilege Escalation 2; Evasion 7; Discovery 5; Lateral Movement 6; Collection 11; Command and Control 3; Inhibit Response Function 13; Impair Process Control 4; Impact 12.
- Initial Access: T0817, T0819, T0866, T0822, T0883, T0886, T0847, T0848, T0865, T0862, T0864, T0860.
- Execution: T0895, T0858, T1701 (6 sub-techniques), T0871, T0823, T0874, T0821, T0834, T0863.
- Persistence: T1694 Insecure Credentials (2), T1693 Modify Firmware (2), T0889 Modify Program, T0873 Project File Infection (1), T0859 Valid Accounts.
- Privilege Escalation: T0890, T0874.
- Evasion: T0858, T0820, T0872, T0849, T0851, T0894, T1692 Unauthorized Message (2).
- Discovery: T0840, T0842, T0846 (3), T0888, T0887.
- Lateral Movement: T0866, T1694 (2), T0867, T0843 Program Download (3), T0886, T0859.
- Collection: T0830, T0802, T0811, T0893, T0868, T0877, T0801, T0861, T0845, T0852, T0887.
- Command and Control: T0885, T0884, T0869 (2).
- Inhibit Response Function: T0800, T0878, T1695 Block Communications (3), T1691 Block Operational Technology Message (2), T0892, T0809, T0814, T0816, T0835, T0838, T1693 (2), T0851, T0881.
- Impair Process Control: T0806, T1693 (2), T0836, T1692 (2).
- Impact: T0879, T0813, T0815, T0826, T0827, T0828, T0837, T0880, T0829, T0831, T0832, T0882.
- Techniques listed under more than one tactic include T0858, T0874, T0866, T0859, T0886, T0887, T0851, T1693, T1692, T1694.

## Verbatim
- "ATT&CK content v20.1"

## Relevance
- Record the version with every mapping, because IDs moved between versions.
- See `mitre-attack-ics-techniques.md` for names and short descriptions.
- Inference: older documents citing T0855, T0856, T0857, T0839, T0812, T0891, T0803, T0804, T0805, T0807 or T0853 (for example the ACI EUROPE guideline) need remapping, because those IDs do not appear in the v20.1 listing.
