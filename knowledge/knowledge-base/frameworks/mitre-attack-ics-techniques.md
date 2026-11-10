---
title: "MITRE ATT&CK Techniques: ICS"
url: "https://attack.mitre.org/techniques/ics/"
type: standard
trust: primary
accessed: 2026-11-09
published: 2026-10-13
owasp_ot: [1,2,3,4,5,6,7,10]
version: "ATT&CK content v20.1"
---

## Summary
The ICS technique index at v20.1 lists 78 top-level techniques and 26 sub-techniques.
The 26 count reconciles with the per-technique sub-technique counts on the matrix page.
Descriptions below are short paraphrases from the fetched index, not MITRE's wording.
Use individual technique pages for detection and mitigation detail, which were not read here.

## Key facts
- Passive or observational: T0842 Network Sniffing; T0887 Wireless Sniffing; T0840 Network Connection Enumeration (inspects connections to infer device roles); T0846 Remote System Discovery; T0888 Remote System Information Discovery (make, model, role, configuration).
- Controller read: T0868 Detect Operating Mode; T0877 I/O Image; T0801 Monitor Process State; T0861 Point & Tag Identification; T0845 Program Upload.
- Credentials and access: T0859 Valid Accounts; T1694 Insecure Credentials (default or hardcoded); T0822 External Remote Services; T0886 Remote Services; T0883 Internet Accessible Device; T0864 Transient Cyber Asset; T0860 Wireless Compromise; T0848 Rogue Master.
- IT-adjacent execution and collection: T0819, T0866, T0890, T0867 Lateral Tool Transfer, T0811 Data from Information Repositories, T0893 Data from Local System, T0852 Screen Capture, T0802 Automated Collection, T0882 Theft of Operational Information.
- Controller write or state change: T0858 Change Operating Mode; T0843 Program Download; T0889 Modify Program; T0821 Modify Controller Tasking; T0873 Project File Infection; T1693 Modify Firmware; T0800 Activate Firmware Update Mode; T0836 Modify Parameter; T0835 Manipulate I/O Image; T0806 Brute Force I/O; T1692 Unauthorized Message; T0830 Adversary-in-the-Middle.
- Response inhibition: T0878 Alarm Suppression; T0838 Modify Alarm Settings; T1691 Block Operational Technology Message; T1695 Block Communications; T0814 Denial of Service; T0816 Device Restart/Shutdown; T0881 Service Stop; T0892 Change Credential; T0809 Data Destruction.
- Impact outcomes: T0879 Damage to Property; T0813 Denial of Control; T0815 Denial of View; T0826 Loss of Availability; T0827 Loss of Control; T0828 Loss of Productivity and Revenue; T0837 Loss of Protection; T0880 Loss of Safety; T0829 Loss of View; T0831 Manipulation of Control; T0832 Manipulation of View.
- Remaining techniques: T0817, T0820, T0823, T0834, T0847, T0849, T0851, T0862, T0863, T0865, T0869, T0871, T0872, T0874, T0884, T0885, T0894, T0895, T1701.

## Verbatim
- "ATT&CK content v20.1"

## Relevance
- Primary reference for technique names and IDs when correcting secondary sources.
- The groupings above are this entry's own arrangement; MITRE does not classify techniques by test safety. The safety tiering is in the research notes and is inference.
