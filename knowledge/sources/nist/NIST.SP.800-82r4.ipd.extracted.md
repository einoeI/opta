<!-- Extracted from NIST.SP.800-82r4.ipd.pdf by extract_pdf.py (pypdf) on 2026-11-10. Working copy: check against the PDF before quoting. -->

<!-- page 1 -->

NIST Special Publication 800 
NIST SP 800-82r4 ipd
Guide to Operational Technology (OT) 
Security 
Initial Public Draft 
Keith Stouffer 
Michael Pease 
CheeYee Tang 
Adam Hahn 
Jim Gilsinn 
Daniel Rebori-Carretero 
Otis Alexander 
Michael Fialk 
Zackary Louis Silva 
This publication is available free of charge from: 
https://doi.org/10.6028/NIST.SP.800-82r4.ipd

<!-- page 2 -->

NIST Special Publication 800  
NIST SP 800-82r4 ipd 
Guide to Operational Technology (OT) 
Security 
Initial Public Draft 
 
 
 
 
 
 
 
Kei
th Stouffer 
Michael Pease 
CheeYee Tang 
Applied Cybersecurity Division 
Information Technology Laboratory 
Ad
am Hahn 
Jim Gilsinn 
Daniel Rebori-Carretero 
Otis Alexander 
Michael Fialk 
Zackary Louis Silva  
The MITRE Corporation 
This publication is available free of charge from:  
https://doi.org/10.6028/NIST.SP.800-82r4.ipd 
September 2026 
  
 
U.S. Department of Commerce  
Howard Lutnick, Secretary 
National Institute of Standards and Technology  
Arvind Raman, NIST Director and Under Secretary of Commerce for Standards and Technology

<!-- page 3 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
Certain equipment, instruments, software, or materials, commercial or non-commercial, are identified in this 
paper in order to specify the experimental procedure adequately. Such identification does not imply 
recommendation or endorsement of any product or service by NIST, nor does it imply that t he materials or 
equipment identified are necessarily the best available for the purpose .  
There may be references in this publication to other publications currently under development by NIST in 
accordance with its assigned statutory responsibilities. The information in this publication, including concepts and 
methodologies, may be used by federal agencies even before the completion of such companion publications. 
Thus, until each publication is completed, current requirements, guidelines, and procedures, where they exist, 
remain operative. For planning and transition purposes, federal agencies may wish to closely follow the 
development of these new publications by NIST.  
Organizations are encouraged to review all draft publications during public comment periods and provide feedback 
to NIST. Many NIST cybersecurity publications, other than the ones noted above, are available at 
https://csrc.nist.gov/publications. 
Authority 
T
his publication has been developed by NIST in accordance with its statutory responsibilities under the Federal 
Information Security Modernization Act (FISMA) of 2014, 44 U.S.C. § 3551 et seq., Public Law (P.L.) 113- 283. NIST is 
responsible for developing information security standards and guidelines, including minimum requirements for 
federal information systems, but such standards and guidelines shall not apply to national security systems 
without the express approval of appropriate federal officials exercising policy authority over such systems. This 
guideline is consistent with the requirements of the Office of Management and Budget (OMB) Circular A -130. 
 
No
thing in this publication should be taken to contradict the standards and guidelines made mandatory and 
binding on federal agencies by the Secretary of Commerce under statutory authority. Nor should these guidelines 
be interpreted as altering or superseding the existing authorities of the Secretary of Commerce, Director of the 
OMB, or any other federal official. This publication may be used by nongovernmental organizations on a voluntary 
basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST.  
N
IST Technical Series Policies 
C
opyright, Use, and Licensing Statements 
NIST Technical Series Publication Identifier Syntax 
Publication History 
A
pproved by the NIST Editorial Review Board on YYYY-MM-DD [Will be added to final publication.] 
Supersedes NIST Series XXX (Month Year) DOI [Will be added to final publication, if applicable.] 
H
ow to Cite this NIST Technical Series Publication 
S
touffer K, Pease M, Tang C, Hahn A, Gilsinn J, Rebori-Carretero D, Alexander O, Fialk M, Silva ZL (2026) Guide to 
Operational Technology (OT) Security. (National Institute of Standards and Technology, Gaithersburg, MD), NIST 
Special Publication (SP) NIST SP 800-82r4 ipd. https://doi.org/10.6028/NIST.SP.800-82r4.ipd  
A
uthor ORCID iDs 
K
eith Stouffer: 0000-0003-1220-5487  
Michael Pease: 0000-0002-6489-2621  
CheeYee Tang: 0009-0000-2847-1443  
Adam Hahn: 0000-0003-1214-3466 
Zackary Louis Silva: 0000-0002-0721-1420

<!-- page 4 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
Public Comment Period 
September 21, 2026 – November 30, 2026 
Submit Comments  
sp800-82rev4@nist.gov 
  
National Institute of Standards and Technology 
Attn: Applied Cybersecurity Division, Information Technology Laboratory 
100 Bureau Drive (Mail Stop 2000) Gaithersburg, MD 20899-2000 
Additional Information 
Additional information about this publication is available at https://csrc.nist.gov/pubs/sp/800/82/r4/ipd, including 
related content, potential updates, and document history.  
All comments are subject to release under the Freedom of Information Act (FOIA).

<!-- page 5 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
i 
Abstract 1 
2 T
his
 document provides guidelines on how to secure operational technology (OT) while 
addre
ssing their unique performance, reliability, and safety requirements. OT encompasses a 3 
broad range of programmable systems and devices that interact with the physical environment, 4 
such as industrial control systems, building automation and control systems (BACS), freight 5 
railroad, maritime vessels, water and wastewater systems (WWS), Industrial Internet of Things 6 
(IIoT), and cloud environments. This document provides an overview of OT and typical system 7 
topologies, identifies common threats and vulnerabilities to these systems, and offers 8 
recommended security countermeasures to mitigate the associated risks in alignment with the 9 
NIST Cybersecurity Framework (CSF) 2.0. 10 
Keywords 11 
computer security; distributed control system (DCS); industrial control system (ICS); information 12 
security; network security; operational technology (OT); programmable logic controller (PLC); 13 
risk management; security controls; supervisory control and data acquisition (SCADA); NIST 14 
Cybersecurity Framework (CSF) 2.0; zero trust. 15 
Reports on Computer Systems Technology 16 
The Information Technology Laboratory (ITL) at the National Institute of Standards and 17 
Technology (NIST) promotes the U.S. economy and public welfare by providing technical 18 
leadership for the Nation’s measurement and standards infrastructure. ITL develops tests, test 19 
methods, reference data, proof of concept implementations, and technical analyses to advance 20 
the development and productive use of information technology. ITL’s responsibilities include 21 
the development of management, administrative, technical, and physical standards and 22 
guidelines for the cost-effective security and privacy of other than national security-related 23 
information in federal information systems. The Special Publication 800-series reports on ITL’s 24 
research, guidelines, and outreach efforts in information system security, and its collaborative 25 
activities with industry, government, and academic organizations. 26 
  27

<!-- page 6 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
ii 
Note to Reviewers 28 
29 This document is the fourth revision of NIST SP 800-82. Updates in this revision include:  
• Ex
panded introduction to operational technology (OT) sectors to include Building 30 
Automation and Control Systems (BACS), Water and Wastewater Systems (WWS), food 31 
and agriculture, freight rail, maritime vessels, and Industrial Internet of Things (IIoT) and 32 
cloud convergence 33 
• Restructured around the NIST Cybersecurity Framework (CSF) 2.0, including a 34 
reorganization of the previous risk management section to focus on the CSF Govern 35 
Function 36 
• Expanded discussion of how OT risk management aligns with broader enterprise risk 37 
management, as described in NIST IR 8286r1 38 
• Discussion of the adoption of the NIST Risk Management Framework (RMF) in   39 
Appendix F 40 
• Expanded guidance on implementing OT security controls, including asset management 41 
and network monitoring and detection 42 
• Security architecture guidelines focused on protecting system management functions 43 
and applying zero trust principles 44 
• Appendix C, “Threat Sources, Vulnerabilities, and Incidents,” and Appendix D, “OT 45 
Security Organizations, Research, and Activities,” to be moved to web-based resources 46 
to support more timely content updates in the final publication 47 
• Appendix E, “OT Overlay,” and Appendix F, “Applying the Risk Management Framework 48 
to OT Systems,” to be moved to separate documents in the final publication 49 
  50

<!-- page 7 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
iii 
Call for Patent Claims 51 
52 This public review includes a call for information on essential patent claims (claims whose use 
would 
be required for compliance with the guidance or requirements in this Information 53 
Technology Laboratory (ITL) draft publication). Such guidance and/or requirements may be 54 
directly stated in this ITL Publication or by reference to another publication. This call also 55 
includes disclosure, where known, of the existence of pending U.S. or foreign patent 56 
applications relating to this ITL draft publication and of any relevant unexpired U.S. or foreign 57 
patents. 58 
ITL may require from the patent holder, or a party authorized to make assurances on its behalf, 59 
in written or electronic form, either: 60 
a) assurance in the form of a general disclaimer to the effect that such party does not hold 61 
and does not currently intend holding any essential patent claim(s); or 62 
b) assurance that a license to such essential patent claim(s) will be made available to 63 
applicants desiring to utilize the license for the purpose of complying with the guidance 64 
or requirements in this ITL draft publication either: 65 
i. under reasonable terms and conditions that are demonstrably free of any unfair 66 
discrimination; or 67 
ii. without compensation and under reasonable terms and conditions that are 68 
demonstrably free of any unfair discrimination. 69 
Such assurance shall indicate that the patent holder (or third party authorized to make 70 
assurances on its behalf) will include in any documents transferring ownership of patents 71 
subject to the assurance, provisions sufficient to ensure that the commitments in the assurance 72 
are binding on the transferee, and that the transferee will similarly include appropriate 73 
provisions in the event of future transfers with the goal of binding each successor-in-interest. 74 
The assurance shall also indicate that it is intended to be binding on successors-in-interest 75 
regardless of whether such provisions are included in the relevant transfer documents. 76 
Such statements should be addressed to: sp800-82rev4@nist.gov 77

<!-- page 8 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
iv 
Table of Contents 78 
79 Executive Summary ............................................................................................................................1  
80 
81 
82 
83 
1. Introduction ...................................................................................................................................6  84 
85 
86 
87 
2. OT Overview ..................................................................................................................................8  88 
89 
90 
91 
92 
2.4.1. OT System Design Considerations .............................................................................................. 12 93 
2.4.2. SCADA Systems ........................................................................................................................... 13 94 
2.4.3. Distributed Control Systems ....................................................................................................... 17 95 
2.4.4. Programmable Logic Controller-Based Topologies .................................................................... 19 96 
2.4.5. Safety Systems ............................................................................................................................ 20 97 
2.4.6. Cloud and IoT/IIoT Convergence ................................................................................................ 21 98 
99 
2.5.1. Building Automation and Control Systems (BACS) ..................................................................... 24 100 
2.5.1.1. Architectures and Technologies ........................................................................................... 24 101 
2.5.1.2. Key Cybersecurity Challenges and Recommendations ......................................................... 26 102 
2.5.2. Food and Agriculture .................................................................................................................. 27 103 
2.5.2.1. Architectures and Technologies ........................................................................................... 28 104 
2.5.2.2. Key Cybersecurity Challenges and Recommendations ......................................................... 29 105 
2.5.3. Transportation — Freight Rail .................................................................................................... 30 106 
2.5.3.1. Architectures and Technologies ........................................................................................... 31 107 
2.5.3.2. Key Cybersecurity Challenges and Recommendations ......................................................... 32 108 
2.5.4. Transportation – Maritime/Vessels ............................................................................................ 33 109 
2.5.4.1. Architectures and Technologies ........................................................................................... 33 110 
2.5.4.2. Key Cybersecurity Challenges and Recommendations ......................................................... 35 111 
2.5.5. Water and Wastewater Systems (WWS) .................................................................................... 36 112

<!-- page 9 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
v 
2.5.5.1. Architectures and Technologies ........................................................................................... 36 113 
114 2.5.5.2. Key Cybersecurity Challenges and Recommendations ......................................................... 37 
115 
3. OT Risk Management and Governance (CSF 2.0 – GOVERN) ........................................................... 43 116 
117 
3.1.1. Building an OT Cybersecurity Business Case .............................................................................. 45 118 
3.1.2. Presenting the OT Cybersecurity Business Case to Leadership.................................................. 46 119 
3.1.3. Aligning OT Cybersecurity With the Enterprise Mission (GV.OC) .............................................. 46 120 
3.1.3.1. Understanding Operational Consequences and Requirements ........................................... 47 121 
3.1.4. Navigating the Regulatory and Compliance Landscape (GV.OC) ............................................... 47 122 
3.1.5. Defining Shared Roles, Responsibilities, and Authorities (GV.RR) ............................................. 47 123 
124 
3.2.1. Maintaining a Risk Register ........................................................................................................ 50 125 
3.2.2. Risk Response ............................................................................................................................. 51 126 
3.2.3. OT Risk Management Life Cycle ................................................................................................. 52 127 
128 
3.3.1. Identifying and Vetting Key Suppliers and Supplies ................................................................... 54 129 
3.3.2. Defining Required Practices of Suppliers ................................................................................... 54 130 
3.3.3. Identifying and Managing Supply Chain Risk Across Product Life Cycles ................................... 55 131 
132 
3.4.1. Program Performance Measurement ........................................................................................ 56 133 
3.4.2. Organizational Oversight ............................................................................................................ 57 134 
135 
4. OT Cybersecurity Outcomes and Objectives (CSF 2.0 – ID, PR, DE, RS, RC) ...................................... 60 136 
137 
4.1.1. Asset Management (ID.AM) ....................................................................................................... 60 138 
4.1.1.1. Establishing an Asset Inventory ............................................................................................ 60 139 
4.1.1.2. Establishing Asset Criticality and Function ........................................................................... 63 140 
4.1.2. Architectures and Baselines ....................................................................................................... 63 141 
4.1.3. System-Level Risk and Vulnerability Assessment (ID.RA) .......................................................... 64 142 
4.1.3.1. Understanding OT Impacts ................................................................................................... 65 143 
4.1.3.2. Threat Characterizations....................................................................................................... 67 144 
4.1.3.3. Assessing Vulnerabilities ....................................................................................................... 67 145 
4.1.3.4. Evaluating Risk ...................................................................................................................... 68 146 
147

<!-- page 10 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
vi 
4.2.1. Identity, Authentication, and Access Control (PR.AA) ............................................................... 70 148 
149 4.2.1.1. Identity and Access Management ........................................................................................ 70 
4.2.1.2. Identity Life Cycle Management and Provisioning ............................................................... 71 150 
4.2.1.3. Separation of Duties and Dual Approval .............................................................................. 71 151 
4.2.1.4. System, Device, and Service Accounts .................................................................................. 72 152 
4.2.1.5. IT/OT Identity Convergence and Centralization ................................................................... 72 153 
4.2.1.6. Authentication Mechanisms ................................................................................................. 72 154 
4.2.1.6.1. Password Authentication ................................................................................................ 73 155 
4.2.1.6.2. Multi-Factor Authentication ........................................................................................... 73 156 
4.2.1.6.3. Token Authentication ..................................................................................................... 73 157 
4.2.1.6.4. Biometric Authentication ................................................................................................ 74 158 
4.2.1.7. Authorization and Logical Access Controls ........................................................................... 75 159 
4.2.1.7.1. Privileged Access Management ...................................................................................... 76 160 
4.2.1.8. Remote Access Controls ....................................................................................................... 76 161 
4.2.1.9. Physical Access Controls ....................................................................................................... 77 162 
4.2.2. Data Security and Cryptography (PR.DS) .................................................................................... 79 163 
4.2.2.1. Data Classification ................................................................................................................. 79 164 
4.2.2.2. Use of Cryptography ............................................................................................................. 79 165 
4.2.2.2.1. Post-Quantum Cryptography (PQC) Considerations ....................................................... 80 166 
4.2.2.3. Protecting Data at Rest ......................................................................................................... 81 167 
4.2.2.3.1. Cryptographic Protection for Data-at-Rest ..................................................................... 81 168 
4.2.2.3.2. Access Control and Enforcement .................................................................................... 81 169 
4.2.2.3.3. Media Protection ............................................................................................................ 81 170 
4.2.2.4. Protecting Data in Transit ..................................................................................................... 82 171 
4.2.2.4.1. Cryptographic Protection for Data in Transit .................................................................. 82 172 
4.2.2.4.2. Protecting Wireless Communications ............................................................................. 83 173 
4.2.2.4.3. Third-Party Communication Providers............................................................................ 84 174 
4.2.3. Platform Security and Infrastructure Resilience (PR.PS / PR.IR) ................................................ 84 175 
4.2.3.1. Platform Configuration and Maintenance ............................................................................ 84 176 
4.2.3.1.1. Developing a Maintenance Tracking Capability .............................................................. 84 177 
4.2.3.1.2. Configuration Management ............................................................................................ 85 178 
4.2.3.1.3. Software/Firmware Patch Management ........................................................................ 86 179 
4.2.3.2. Application Allowlisting ........................................................................................................ 88 180 
4.2.3.3. Hardware Management ........................................................................................................ 88 181 
4.2.3.3.1. Decommissioning Systems .............................................................................................. 88 182

<!-- page 11 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
vii 
4.2.3.3.2. System Disposal .............................................................................................................. 89 183 
184 4.2.3.4. Software Development Life Cycle ......................................................................................... 89 
4.2.3.5. Resilience of Technology Infrastructure (PR.IR) ................................................................... 90 185 
186 
4.3.1. Continuous Monitoring (DE.CM) ................................................................................................ 91 187 
4.3.1.1. System and Device Monitoring ............................................................................................. 91 188 
4.3.1.1.1. Device Logging ................................................................................................................ 91 189 
4.3.1.1.2. Service Logging ................................................................................................................ 93 190 
4.3.1.1.3. Time Synchronization ...................................................................................................... 93 191 
4.3.1.2. Malicious Code and Endpoint Monitoring ............................................................................ 94 192 
4.3.1.3. User Behavior Monitoring .................................................................................................... 95 193 
4.3.1.4. Network Monitoring ............................................................................................................. 96 194 
4.3.1.4.1. Monitoring Tools and Capabilities .................................................................................. 96 195 
4.3.1.4.2. Network Baselining ......................................................................................................... 97 196 
4.3.1.5. Physical and Environmental Monitoring ............................................................................... 98 197 
4.3.2. Anomalies and Events (DE.AE) ................................................................................................... 98 198 
4.3.2.1. Data Aggregation and Analysis ............................................................................................. 99 199 
4.3.2.2. Identifying Adverse Events and Anomalies .......................................................................... 99 200 
4.3.2.3. Integrating Cyber Threat Intelligence (CTI) ......................................................................... 101 201 
4.3.2.4. Emerging Detection Capabilities ......................................................................................... 101 202 
203 
4.4.1. Incident Response .................................................................................................................... 102 204 
4.4.2. Incident Response Planning ..................................................................................................... 103 205 
4.4.3. Incident Management (RS.MA) ................................................................................................ 106 206 
4.4.4. Incident Analysis (RS.AN) .......................................................................................................... 106 207 
4.4.5. Incident Response Reporting and Communication (RS.CO) ..................................................... 107 208 
4.4.6. Incident Mitigation (RS.MI) ...................................................................................................... 108 209 
210 
4.5.1. Recovery Planning .................................................................................................................... 109 211 
4.5.2. Incident Recovery Execution (RC.RP) ....................................................................................... 111 212 
4.5.3. Recovery Communication (RC.CO) ........................................................................................... 112 213 
5. OT Cybersecurity Architecture .................................................................................................... 113 214 
215 
216 
5.2.1. Management Network Architecture ........................................................................................ 116 217

<!-- page 12 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
viii 
5.2.2. Operational Network Architecture ........................................................................................... 119 218 
219 5.2.2.1. Distributed Control System (DCS)-Based OT Systems ........................................................ 119 
5.2.2.2. DCS- and PLC-Based OT With IIoT ....................................................................................... 122 220 
5.2.2.3. SCADA-Based OT Environments ......................................................................................... 123 221 
222 
5.3.1. OT-Specific Recommendations and Guidance ......................................................................... 125 223 
224 
5.4.1. Fault Tolerance as an Architectural Design Principle ............................................................... 126 225 
5.4.2. Redundancy Addressed as an Architecture-Level Design Principle ......................................... 126 226 
5.4.3. Analog Backups......................................................................................................................... 127 227 
5.4.4. Out-of-Band Management as an Architectural Concept .......................................................... 127 228 
References ..................................................................................................................................... 128 229 
Appendix A. List of Symbols, Abbreviations, and Acronyms ............................................................. 137 230 
Appendix B. Glossary ..................................................................................................................... 153 231 
Appendix C. Threat Sources, Vulnerabilities, and Incidents .............................................................. 165 232 
233 
234 
C.2.1. Policy and Procedure Vulnerabilities and Predisposing Conditions ......................................... 167 235 
C.2.2. System Vulnerabilities and Predisposing Conditions ............................................................... 169 236 
237 
C.3.1. Adversarial Events .................................................................................................................... 177 238 
C.3.2. Structural Events ...................................................................................................................... 182 239 
C.3.3. Environmental Events .............................................................................................................. 183 240 
C.3.4. Accidental Events ..................................................................................................................... 183 241 
Appendix D. OT Security Organizations, Research, and Activities ..................................................... 185 242 
243 
D.1.1. International Electrotechnical Commission (IEC)..................................................................... 185 244 
D.1.1.1. IEC Technical Committee 57 ............................................................................................... 185 245 
D.1.1.2. IEC Technical Committee 65 ............................................................................................... 186 246 
D.1.2. Institute of Electrical and Electronics Engineers, Inc. (IEEE) .................................................... 186 247 
D.1.2.1. IEEE Engineering in Medicine and Biology Security (EMBS) ............................................... 186 248 
D.1.2.2. IEEE Industrial Electronics Society (IES) .............................................................................. 186 249 
D.1.2.3. IEEE Power and Energy Society (PES) ................................................................................. 187 250 
D.1.2.4. IEEE Technical Committee on Power System Communications and Cybersecurity (PSCCC)251 
 187 252

<!-- page 13 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
ix 
D.1.2.5. IEEE Robotics and Automation Society (RAS) ..................................................................... 187 253 
254 D.1.2.6. IEEE Vehicular Technology Society (VTS) ........................................................................... 187 
D.1.3. International Society of Automation (ISA) ............................................................................... 188 255 
D.1.3.1. ISA95, Enterprise-Control System Integration ................................................................... 188 256 
D.1.3.2. ISA99, Industrial Automation and Control Systems Security ............................................. 188 257 
D.1.3.3. ISASecure ............................................................................................................................ 188 258 
D.1.3.4. ISAGCA ................................................................................................................................ 189 259 
D.1.3.5. ISA-TR84.00.09, Cybersecurity Related to the Functional Safety Lifecycle ........................ 189 260 
D.1.4. International Organization for Standardization (ISO) .............................................................. 189 261 
D.1.4.1. ISO 27001 ........................................................................................................................... 189 262 
D.1.4.2. ISO 27002:2022 .................................................................................................................. 189 263 
D.1.5. National Council of Information Sharing and Analysis Centers (ISACs) ................................... 190 264 
D.1.6. National Institute of Standards and Technology (NIST) ........................................................... 190 265 
D.1.6.1. NIST SP 800 Series Cybersecurity Guidelines ..................................................................... 190 266 
D.1.6.2. NIST SP 1800 Series Cybersecurity Practice Guides ........................................................... 190 267 
D.1.6.3. NIST Internal or Interagency Reports ................................................................................. 191 268 
D.1.7. NERC Critical Infrastructure Protection (CIP) Standards .......................................................... 191 269 
D.1.8. Operational Technology Cybersecurity Coalition .................................................................... 191 270 
271 
D.2.1. Clean Energy Cybersecurity Accelerator Initiative ................................................................... 191 272 
D.2.2. Cybersecurity Risk Information Sharing Program (CRISP) ....................................................... 192 273 
D.2.3. Cyber Testing for Resilient Industrial Control Systems (CyTRICS) ........................................... 192 274 
D.2.4. Homeland Security Information Network Critical Infrastructure (HSIN-CI) ............................. 192 275 
D.2.5. INL Cyber-Informed Engineering (CIE) and Consequence-Driven CIE (CCE) ............................ 193 276 
D.2.6. NIST Cyber-Physical Systems and Internet of Things Program ................................................ 193 277 
D.2.7. NIST Cybersecurity for Smart Grid Systems Project................................................................. 193 278 
D.2.8. NIST Cybersecurity for Smart Manufacturing Systems Project ............................................... 194 279 
D.2.9. NIST Reliable, High-Performance Wireless Systems for Factory Automation ......................... 194 280 
D.2.10. NIST Prognostics and Health Management for Reliable Operations in Smart Manufacturing 281 
(PHM4SM) .......................................................................................................................................... 194 282 
D.2.11. NIST Supply Chain Traceability for Agri-Food Manufacturing ............................................... 194 283 
D.2.12. NIST AI RMF Trustworthy AI in Critical Infrastructure Profile ................................................ 195 284 
D.2.13. NIST AI in Manufacturing ....................................................................................................... 195 285 
286 
D.3.1. CISA Cyber Security Evaluation Tool (CSET®) ........................................................................... 195 287

<!-- page 14 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
x 
D.3.2. CISA Cybersecurity Framework Guidance ................................................................................ 195 288 
289 D.3.3. CISA ICS Alerts, Advisories, and Reports .................................................................................. 196 
D.3.4. CISA ICS Training Courses ......................................................................................................... 196 290 
D.3.5. CISA Known Exploited Vulnerabilities (KEV) Catalog ............................................................... 196 291 
D.3.6. CISA/NCSC Secure Connectivity Principles for Operational Technology ................................. 196 292 
D.3.7. CISA Secure by Design/Secure by Default ................................................................................ 197 293 
D.3.8. MITRE ATT&CK for ICS .............................................................................................................. 197 294 
D.3.9. MITRE D3FEND for OT .............................................................................................................. 197 295 
D.3.10. MITRE EMB3D ........................................................................................................................ 197 296 
D.3.11. NIST Cybersecurity Framework 2.0 ........................................................................................ 197 297 
D.3.12. SANS ICS Security Courses ..................................................................................................... 198 298 
D.3.13. OWASP Operational Technology (OT) Top 10........................................................................ 198 299 
D.3.14. UFC 4-010-06, Cybersecurity of Facility-Related Control Systems (FRCS) ............................. 198 300 
301 
D.4.1. Chemical ................................................................................................................................... 198 302 
D.4.2. Communications ...................................................................................................................... 199 303 
D.4.3. Critical Manufacturing ............................................................................................................. 199 304 
D.4.4. Dams ........................................................................................................................................ 199 305 
D.4.5. Energy ...................................................................................................................................... 199 306 
D.4.6. Food and Agriculture ............................................................................................................... 200 307 
D.4.7. Healthcare and Public Health................................................................................................... 200 308 
D.4.8. Nuclear Reactors, Materials, and Waste ................................................................................. 200 309 
D.4.9. Transportation Systems ........................................................................................................... 200 310 
D.4.10. Water and Wastewater .......................................................................................................... 202 311 
312 
D.5.1. Digital Bond’s SCADA Security Scientific Symposium (S4) ....................................................... 202 313 
D.5.2. IFIP Working Group 11.10 on Critical Infrastructure Protection ............................................. 202 314 
D.5.3. SecurityWeek’s ICS Cyber Security Conference ....................................................................... 203 315 
Appendix E. OT Overlay .................................................................................................................. 204 316 
317 
318 
319 
320 
321 
322

<!-- page 15 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
323 
xi 
E.7.1. ACCESS CONTROL – AC ............................................................................................................. 219 324 
E.7.1.1. Tailoring Considerations for the Access Control Family ..................................................... 219 325 
E.7.2. AWARENESS AND TRAINING – AT ............................................................................................ 227 326 
E.7.3. AUDITING AND ACCOUNTABILITY – AU .................................................................................... 228 327 
E.7.3.2. Tailoring Considerations for the Audit Family .................................................................... 228 328 
E.7.4. ASSESSMENT, AUTHORIZATION, AND MONITORING – CA ...................................................... 232 329 
E.7.4.3. Tailoring Considerations for the Security Assessment and Authorization Family .............. 232 330 
E.7.5. CONFIGURATION MANAGEMENT – CM ................................................................................... 235 331 
E.7.5.4. Tailoring Considerations for the Configuration Management Family ................................ 235 332 
E.7.6. CONTINGENCY PLANNING – CP ................................................................................................ 239 333 
E.7.6.5. Tailoring Considerations for the Contingency Planning Family .......................................... 239 334 
E.7.7. IDENTIFICATION AND AUTHENTICATION – IA .......................................................................... 244 335 
E.7.7.6. Tailoring Considerations for the Identification and Authentication Family ....................... 244 336 
E.7.8. INCIDENT RESPONSE – IR .......................................................................................................... 248 337 
E.7.8.7. Tailoring Considerations for the Incident Response Family ............................................... 248 338 
E.7.9. MAINTENANCE – MA ................................................................................................................ 250 339 
E.7.9.8. Tailoring Considerations for the Maintenance Family ........................................................ 250 340 
E.7.10. MEDIA PROTECTION – MP ...................................................................................................... 253 341 
E.7.11. PHYSICAL AND ENVIRONMENTAL PROTECTION – PE ............................................................. 254 342 
E.7.11.9. Tailoring Considerations for the Physical and Environmental Protection Family ............ 254 343 
E.7.12. PLANNING – PL ....................................................................................................................... 260 344 
E.7.13. ORGANIZATION-WIDE INFORMATION SECURITY PROGRAM MANAGEMENT CONTROLS – PM345 
 262 346 
E.7.13.10. Characteristics of the Organization-Wide Information Security Program Management 347 
Control Family .................................................................................................................................. 262 348 
E.7.14. PERSONNEL SECURITY – PS .................................................................................................... 269 349 
E.7.14.11. Tailoring Considerations for the Personnel Security Family ........................................... 269 350 
E.7.15. RISK ASSESSMENT – RA .......................................................................................................... 271 351 
E.7.16. SYSTEM AND SERVICES ACQUISITION – SA ............................................................................ 273 352 
E.7.16.12. Tailoring Considerations for the System and Services Acquisition Family ..................... 273 353 
E.7.17. SYSTEM AND COMMUNICATIONS PROTECTION – SC ............................................................ 277 354 
E.7.17.13. Tailoring Considerations for the System and Communications Protection Family ........ 277 355 
E.7.18. SYSTEM AND INFORMATION INTEGRITY – SI ......................................................................... 284 356 
E.7.18.14. Tailoring Considerations for the System and Information Integrity Family ................... 284 357

<!-- page 16 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
xii 
E.7.19. SUPPLY CHAIN RISK MANAGEMENT – SR ............................................................................... 290 358 
359 Appendix F. Applying the Risk Management Framework to OT Systems .......................................... 293 
360 
361 
362 
363 
364 
365 
366 
List of Tables 367 
Table 1. OT Cyber Risks and Security Objectives ..................................................................................2  368 
Table 2: Components of an OT Defense-in-Depth Strategy ..................................................................4  369 
Table 3. Summary of typical differences between IT and OT systems ................................................. 40 370 
Table 4. Risk Register Entry Criteria .................................................................................................. 50 371 
Table 5. Categories of non-digital OT control components ................................................................. 66 372 
Table 6. Event Likelihood Evaluation ................................................................................................. 69 373 
Table 7. Example OT/ICS System Management ............................................................................... 114 374 
Table 8. Example Security Controls ................................................................................................. 115 375 
Table 9. Example Architectural Patterns ......................................................................................... 115 376 
Table 10. Threats to OT .................................................................................................................. 165 377 
Table 11. Policy and procedure vulnerabilities and predisposing conditions ..................................... 168 378 
Table 12. Architecture and design vulnerabilities and predisposing conditions ................................ 170 379 
Table 13. Configuration and maintenance vulnerabilities and predisposing conditions ..................... 172 380 
Table 14. Physical vulnerabilities and predisposing conditions ........................................................ 174 381 
Table 15. Software development vulnerabilities and predisposing conditions .................................. 175 382 
Table 16. Communication and network configuration vulnerabilities and predisposing conditions ... 175 383 
Table 17. Sensor, final element, and asset management vulnerabilities and predisposing conditions176 384 
Table 18. Control baselines ............................................................................................................ 206 385 
Table 19. Applying the RMF Prepare step to OT .............................................................................. 294 386 
Table 20. Applying the RMF Categorize step to OT .......................................................................... 297 387 
Table 21. Applying the RMF Select step to OT ................................................................................. 299 388 
Table 22. Applying the RMF Implement step to OT .......................................................................... 300 389 
Table 23. Applying the RMF Assess step to OT ................................................................................ 300 390 
Table 24. Applying the RMF Authorize step to OT ........................................................................... 301 391

<!-- page 17 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
xiii 
Table 25. Applying the RMF Monitor step to OT .............................................................................. 302 392 
393 List of Figures 
Fig. 1. Basic operation of a typical OT system .................................................................................... 11 394 
Fig. 2. A general SCADA system layout that shows control center devices, communications equipment, 395 
and field sites .................................................................................................................................. 14 396 
Fig. 3. Examples of point-to-point, series, series-star, and multi-drop SCADA communications 397 
topologies........................................................................................................................................ 15 398 
Fig. 4. An example SCADA topology that supports a large number of remote stations ........................ 16 399 
Fig. 5. A comprehensive SCADA system implementation example ..................................................... 17 400 
Fig. 6. A comprehensive DCS implementation example ..................................................................... 18 401 
Fig. 7. A PLC control system implementation example ....................................................................... 20 402 
Fig. 8. An SIS implementation example ............................................................................................. 21 403 
Fig. 9. Cloud and IIoT convergence example architecture .................................................................. 22 404 
Fig. 10. Example BACS architecture ................................................................................................... 25 405 
Fig. 11. Example freight rail architecture ........................................................................................... 31 406 
Fig. 12. Maritime cargo vessel example architecture ......................................................................... 33 407 
Fig. 13. WWS example architecture [SP1800-45] ............................................................................... 36 408 
Fig. 14. Risk management life cycle ................................................................................................... 49 409 
Fig. 15. Risk register example ........................................................................................................... 51 410 
Fig. 16. Initial identification and reporting [IR8428] ......................................................................... 105 411 
Fig. 17. Network management security architecture ....................................................................... 117 412 
Fig. 18. A security architecture example for a DCS system ............................................................... 121 413 
Fig. 19. A security architecture example for DCS system with IIoT devices ....................................... 122 414 
Fig. 20. A security architecture example for a SCADA system ........................................................... 124 415 
Fig. 21. Detailed overlay control specifications illustrated ............................................................... 218 416 
Fig. 22. Risk Management Framework steps ................................................................................... 293 417 
 418

<!-- page 18 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
xiv 
Acknowledgments for Revision 4 419  
420 The authors will acknowledge colleagues who have made significant contributions to this 
doc
ument in the final publication. 421 
A
cknowledgement for Previous Versions 422
 
The authors wish to thank their colleagues who reviewed drafts of the original version of the 423 
document and contributed to its technical content. The authors would particularly like to 424 
acknowledge Tim Grance, Ron Ross, Stu Katzke, and Freemon Johnson of NIST for their keen 425 
and insightful assistance throughout the development of the document. The authors also 426 
gratefully acknowledge and appreciate the many contributions from the public and private 427 
sectors whose thoughtful and constructive comments improved the quality and usefulness of 428 
the publication. The authors would particularly like to thank the members of ISA99, Lisa Kaiser, 429 
Department of Homeland Security, the Department of Homeland Security Industrial Control 430 
System Joint Working Group (ICSJWG), the Office of the Deputy Undersecretary of Defense for 431 
Installations and Environment, and Business Enterprise Integration Directorate staff for their 432 
exceptional contributions to this publication. The authors would also like to thank the UK 433 
National Centre for the Protection of National Infrastructure (CPNI) for allowing portions of the 434 
Good Practice Guide on Firewall Deployment for SCADA and Process Control Network to be 435 
used in the document as well as ISA for allowing portions of the ISA-62443 Standards to be used 436 
in the document. The authors would also like to thank Sallie Edwards, Blaine Jefferies, and John 437 
Hoyt, Megan Corso, Eran Salfati, Karen Scarfone, and Isabel Van Wyk. 438 
 
 
439
 
440

<!-- page 19 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
1 
Executive Summary 441 
This document provides guidelines for establishing secure operational technology (OT)1 while 442 
addressing OT’s unique performance, reliability, and safety requirements. OT encompasses a 443 
broad range of programmable systems and devices that interact with the physical environment 444 
or manage devices that do so. These systems and devices detect or cause a direct change 445 
through the monitoring and/or control of other devices, processes, and events. Examples 446 
include industrial control systems (ICS), building automation systems, transportation systems, 447 
physical access control systems, physical environment monitoring systems, and physical 448 
environment measurement systems. This document provides an overview of OT and typical 449 
system topologies, identifies common threats and vulnerabilities to these systems, and 450 
recommends security countermeasures to mitigate the associated risks. 451 
OT is vital to the operation of U.S. critical infrastructure, which is often highly interconnected 452 
and mutually dependent. While federal agencies operate much of the Nation’s critical 453 
infrastructure, a significant portion of it is privately owned and operated. Additionally, critical 454 
infrastructure is often referred to as a “system of systems” because of the interdependencies 455 
among various industrial sectors and the interconnections among business partners. 456 
Initially, OT had little resemblance to traditional information technology (IT) systems because 457 
OT systems were isolated, ran proprietary control protocols, and used specialized hardware and 458 
software. As OT systems continue to adopt IT solutions to enable connectivity to enterprise 459 
business systems and remote access, they are being designed and implemented using industry-460 
standard computers, operating systems (OSs), and network protocols, thus increasing their 461 
resemblance to IT systems. This integration supports new IT capabilities but provides 462 
significantly less isolation of OT from the outside world than predecessor systems. The 463 
increasing use of wireless networking places OT implementations at greater risk from 464 
adversaries who are in close physical proximity but lack direct physical access to the equipment. 465 
While security solutions have been designed to address these issues in typical IT systems, 466 
special precautions must be taken when introducing the same solutions into OT environments. 467 
In some cases, new security solutions that are tailored to the OT environment are needed.  468 
The Evolving Threat Landscape and Mission and Business Risk 469 
Although some characteristics are similar, OT also has features that differ from those of 470 
traditional information processing systems. Many of these differences stem from the fact that 471 
logic executing in OT directly affects the physical world. Some of these characteristics include 472 
significant risks to the health and safety of human lives, serious damage to the environment, 473 
and severe financial issues, such as production losses, negative impacts to the Nation’s 474 
economy, and the compromise of proprietary information. OT has unique performance and 475 
reliability requirements and often uses OSs and applications that may be considered 476 
 
1 See https://csrc.nist.gov/Projects/operational-technology-security.

<!-- page 20 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
2 
unconventional to typical IT personnel. Furthermore, the goals of safety and efficiency 477 
478 sometimes conflict with security in the design and operation of OT systems. 
OT cyb
ersecurity programs should always be part of broader OT safety and reliability programs 479 
at both industrial sites and enterprise cybersecurity programs because cybersecurity is essential 480 
to the safe and reliable operation of modern industrial processes. Threats to OT systems can 481 
come from numerous sources, including hostile governments, terrorist groups, disgruntled 482 
employees, malicious intruders, system complexities, natural disasters, malicious insider 483 
actions, and unintentional actions (e.g., human error, failure to follow established policies and 484 
procedures). OT security objectives typically prioritize safety, followed by integrity, availability, 485 
and confidentiality.  486 
To mitigate the unique threats facing operational environments, organizations must align their 487 
defensive strategies with potential operational consequences. Table 1 outlines possible OT 488 
incidents alongside their corresponding security objectives. 489 
Table 1. OT cyber risks and security objectives 490 
Strategic Focus Potential OT Incident / 
Consequence 
Key Security Objective 
Access & Architecture 
(Protect) 
- Unauthorized changes to 
instructions, commands, or alarm 
thresholds that could damage 
equipment or endanger life 
- Modified software or 
configurations, including malware 
infections 
- Restrict Logical Access: Employ 
multi-layer network topologies, 
DMZs, and unidirectional gateways, 
and separate IT/OT credentials.  
- Restrict Physical Access: Use 
physical controls (e.g., locks, card 
readers, guards) to protect 
components.  
- Protect Components: Deploy 
tested patches, disable unused ports, 
and restrict user privileges. 
System & Data Integrity 
(Protect & Detect) 
- Inaccurate information sent to 
operators to disguise malicious 
actions or prompt inappropriate 
responses 
- Interference with the operation of 
equipment protection or safety 
systems 
- Restrict Data Modification: Protect 
data from unauthorized modification 
in all states (i.e., at rest, in transit, in 
use) and across network boundaries. 
- Detect Events: Deploy continuous 
monitoring to detect failed 
components, exhausted resources, 
and anomalies to break the attack 
chain early. 
Resilience & Continuity 
(Respond & Recover) 
- Blocked or delayed flow of 
information through OT networks, 
causing a critical loss of view or loss 
of control for operators 
- Maintain Functionality: Design 
redundant systems that are capable 
of graceful degradation (moving 
from automated to manual 
operations) during adverse 
conditions.  
- Restore and Recover: Develop and 
rigorously test incident response

<!-- page 21 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
3 
Strategic Focus Potential OT Incident / 
Consequence 
Key Security Objective 
plans to ensure rapid system 
recovery. 
Strategic Governance and Risk Management 491 
492 Because cyber incidents can directly cause safety and reliability failures, OT cybersecurity 
p
rograms must be seamlessly integrated into broader enterprise risk management (ERM) and 493 
facility safety programs. Effective OT governance requires organizations to focus on the 494 
following strategic imperatives:   495 
• Shared governance and accountability: Securing OT requires a shared governance 496 
structure that brings together senior leadership, OT, IT, safety, legal, operations, and 497 
other relevant stakeholders to establish the program’s scope, assign responsibilities, 498 
and coordinate day-to-day cybersecurity activities. Ultimate accountability for OT 499 
cybersecurity and any resulting physical impacts resides with executive leadership, 500 
including the Chief Executive Officer (CEO), Chief Operating Officer (COO), and Chief 501 
Information Officer (CIO) or Chief Security Officer (CSO).  502 
• OT risk management strategy: Organizations must establish how OT cybersecurity risks 503 
are prioritized, evaluated, tracked, reported, and addressed in a manner consistent with 504 
the organization’s mission, operational requirements, and risk tolerance. This includes 505 
maintaining risk registers and documenting risk responses (e.g., mitigate, transfer, 506 
accept, avoid).  507 
• Supply chain risk management: Organizations should manage cybersecurity supply 508 
chain risks that arise from the products, services, suppliers, and third parties that 509 
support OT environments. Because OT systems often depend on specialized equipment 510 
and remote vendor maintenance, organizations must vet suppliers to ascertain the 511 
adequacy of their internal security practices and continuously manage supplier risk 512 
across the product lifecycle.  513 
Core OT Cybersecurity Capabilities: A Defense-in-Depth Strategy 514 
Organizations should not rely on “security by obscurity.” Securing OT requires a consequence-515 
driven defense-in-depth strategy that not only layers security mechanisms to minimize the 516 
impact of a failure in any single control but also aligns with the core functions of the NIST 517 
Cybersecurity Framework (CSF) 2.0:   518 
• Identify: Organizations must establish an accurate inventory of hardware, software, and 519 
network baselines to fully understand asset criticality. Risk assessments must evaluate 520 
both logical dependencies and potential physical consequences.  521 
• Protect: Safeguards must be implemented without compromising continuous physical 522 
processes. This includes using multi-layer network topologies, restricting logical and 523

<!-- page 22 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
4 
physical access through role-based privileges and demilitarized zones (DMZs), and 524 
525 securing data at rest and in transit with appropriate cryptography. 
• Det
ect: Organizations must deploy continuous monitoring across networks, devices, and 526 
physical environments to identify anomalies, unauthorized changes, and cyber threats 527 
before they escalate into high-impact incidents. 528 
• Respond and Recover: Incidents are inevitable, making robust incident response plans 529 
essential. Systems must be designed for graceful degradation, moving from full 530 
automation to manual operations if necessary, and recovery procedures must ensure 531 
the safe, timely restoration of physical processes. 532 
Unlike traditional IT environments, security controls in OT must never compromise continuous 533 
physical processes. Therefore, the defense-in-depth implementation strategies outlined in 534 
Table 2 should be applied when safe, technically feasible and thoroughly tested to ensure that 535 
they do not adversely affect OT operations or human safety. 536 
Table 2. Components of an OT defense-in-depth strategy 537 
Strategic Domain (Focus) Implementation Strategies 
Governance & Life Cycle 
(Policy & Program Management) 
- Develop OT-specific security policies, procedures, training, and 
educational material.  
- Align security postures with the National Terrorism Advisory System 
(NTAS).  
- Address security throughout the entire system life cycle, from 
architecture design and procurement to operations and 
decommissioning. 
Architecture & Boundaries 
(Network Isolation & Topologies) 
- Implement multi-layer network topologies that keep critical 
communications in the most secure layers.  
- Provide logical and physical separation between enterprise and OT 
networks using DMZs, stateful firewalls, and unidirectional gateways.  
- Employ reliable and secure network protocols.  
Access Control 
(Identity & Privilege Management) 
- Restrict physical access to OT networks and devices.  
- Enforce the principle of least privilege using role-based access control 
(RBAC).  
- Require multi-factor authentication (MFA) for remote access, and use 
modern technologies (e.g., smart cards).  
- Maintain separate authentication mechanisms and credentials for IT 
and OT networks.  
System Protection & Detection 
(Asset Hardening & Monitoring) 
- Expeditiously deploy security patches after testing them under field 
conditions.  
- Disable unused ports and services.  
- Apply encryption and/or cryptographic hashes to protect data.

<!-- page 23 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
5 
Strategic Domain (Focus) Implementation Strategies 
- Implement malware protection, intrusion detection, and file integrity 
checking.  
- Track and monitor audit trails in critical areas.  
System Resilience 
(Fault Tolerance) 
- Ensure that critical components and networks are redundant.  
- Design critical systems for graceful degradation to prevent catastrophic 
cascading events.  
OT Cybersecurity Architecture and the SP 800-53r5 Overlay 538 
539 In cooperation with the public and private-sector OT community, NIST has developed specific 
guidelines (
see Appendix E) for applying the security controls in NIST Special Publication (SP) 540 
800-53r5 (Revision 5), Security and Privacy Controls for Information Systems and Organizations 541 
[SP800-53r5], to OT. While many of the controls in SP 800-53r5 are applicable to OT as written, 542 
some controls require OT-specific interpretation and/or augmentation by adding one or more 543 
of the following: 544 
• OT Discussion provides organizations with additional information on the application of 545 
security controls and control enhancements to OT and the environments in which these 546 
specialized systems operate. This also explains why a particular security control or 547 
control enhancement may not be applicable in some OT environments or may be a 548 
candidate for tailoring (i.e., the application of scoping guidance and/or compensating 549 
controls). OT Discussion does not replace the original Supplemental Guidance in SP 800-550 
53r5. 551 
• Control Enhancements (one or more) provide augmentations to the original control that 552 
may be required for some OT systems. 553 
 554 
  555 
The most successful method for securing OT systems is to gather industry-recommended 
practices and engage in a proactive, collaborative effort between management, OT 
engineers and operators, the IT organization, and a trusted OT advisor. This team should 
draw upon the wealth of information available from the Federal Government, industry 
groups, vendors, and standards activities.

<!-- page 24 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
6 
1. Introduction 556 
1.1. Purpose and Scope 557 
The purpose of this document is to provide guidelines for establishing secure OT2 while 558 
addressing its unique performance, reliability, and safety requirements. This document 559 
provides an overview of OT systems and typical system topologies, identifies common threats 560 
and vulnerabilities, and recommends security countermeasures to mitigate associated risks. 561 
The recommendations are aligned with the NIST Cybersecurity Framework (CSF) 2.0. 562 
Additionally, it presents an OT-tailored security control overlay based on NIST Special 563 
Publication (SP) 800-53r5 (Revision 5) [SP800-53r5] that customizes controls for the unique 564 
characteristics of the OT domain. The body of the document provides context for the overlay, 565 
but the overlay is intended to stand alone.  566 
Because there are many types of OT with varying levels of potential risk and impact, this 567 
document provides a list of many methods and techniques for securing OT systems. It should 568 
not be used as a checklist to secure a specific system. Readers are encouraged to conduct a 569 
risk-based assessment of their systems and tailor the recommended guidelines and solutions to 570 
their specific security, business, and operational requirements. The range of applicability of the 571 
basic concepts for securing OT systems presented in this document will continue to expand. 572 
1.2. Audience 573 
This document covers details that are specific to OT systems. Readers of this document should 574 
be familiar with general computer security concepts and communication protocols, including 575 
those used in networking. The document is technical in nature but provides the necessary 576 
background to understand the topics that are discussed. 577 
The intended audience is varied and includes the following: 578 
• Control engineers, integrators, and architects who design or implement OT systems 579 
• System administrators, engineers, and other information technology (IT) professionals 580 
who administer, patch, or secure OT systems 581 
• Security consultants who perform security assessments and penetration testing of OT 582 
systems 583 
• Managers who are responsible for OT systems 584 
• Senior management who needs to better understand the risks to OT systems as they 585 
justify and apply an OT cybersecurity program 586 
• Researchers and analysts who are trying to understand the unique security needs of OT 587 
systems 588 
 
2 The acronym “OT” can stand for either “operational technology” or “operational technologies.” The context around the acronym, especially 
the use of singular or plural words, will indicate which meaning is intended.

<!-- page 25 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
7 
• Vendors who are developing products that will be deployed as part of an OT system 589 
1.3. Document Structure 590 
The remainder of this document is divided into the following major sections: 591 
• Section 2 gives an overview of OT compared with IT systems. It provides a more in-592 
depth review of various OT sectors, including building automation, maritime, freight 593 
railroad, water, and agriculture. It also discusses the growing convergence of OT 594 
with IIoT and cloud environments. 595 
• Section 3 discusses implementation of the Govern CSF function to address risk 596 
management and governance in an OT environment, including organizational context 597 
and shared governance, OT risk management strategy, cybersecurity supply chain risk 598 
management (C-SCRM), and OT security policy and oversight. 599 
• Section 4 provides OT-specific guidelines for implementing the CSF’s Identify, Protect, 600 
Detect, Respond, and Recover functions. 601 
• Section 5 provides recommendations for integrating security into network architectures 602 
that are typically found in OT systems with an emphasis on network segmentation and 603 
separation practices. 604 
• The References section provides a list of citations used in the development of this 605 
document. 606 
This guide also contains several appendices with supporting material:  607 
• Appendix A lists the acronyms and abbreviations used in this document. 608 
• Appendix B contains a glossary of the terms used in this document. 609 
While included in this draft for public review, the following appendices will be transitioned to 610 
online supplemental resources or separate documents for the final publication: 611 
• Appendix C discusses OT threat sources, vulnerabilities, predisposing conditions, threat 612 
events, and incidents. 613 
• Appendix D presents lists and descriptions of OT security organizations, research, and 614 
activities. 615 
• Appendix E defines the SP 800-53r5 OT overlay and lists security controls, 616 
enhancements, and supplemental guidance that apply specifically to OT systems. 617 
• Appendix F includes guidelines for implementing the NIST Risk Management Framework 618 
(RMF) on OT systems.  619 
  620

<!-- page 26 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
8 
2. OT Overview 621 
OT3 encompasses a broad range of programmable systems and devices that interact with the 622 
physical environment or manage devices that do so. These systems and devices detect or cause 623 
a direct change through the monitoring and/or control of devices, processes, and events. 624 
Examples include industrial control systems, building automation systems, transportation 625 
systems, physical access control systems, physical environment monitoring systems, and 626 
physical environment measurement systems.  627 
OT systems consist of combinations of control components (e.g., electrical, mechanical, 628 
hydraulic, pneumatic) that act together to achieve an objective (e.g., manufacturing, 629 
transportation of matter or energy). The part of the system primarily concerned with producing 630 
an output is referred to as the process. The part of the system primarily concerned with 631 
maintaining conformance with specifications is referred to as the controller (or control). The 632 
control components of the system include the specification of the desired output or 633 
performance. The system can be configured in one of three ways:  634 
• Open loop: The output is controlled by established settings.  635 
• Closed loop: The output affects the input in such a way as to maintain the desired 636 
control objective.  637 
• Manual mode: The system is completely controlled by humans.  638 
This section provides an overview of several types of common OT systems, including 639 
supervisory control and data acquisition (SCADA), distributed control systems (DCS), 640 
programmable logic controllers (PLCs), building automation systems (BASs), physical access 641 
control systems (PACSs), and the Industrial Internet of Things (IIoT). Diagrams depict the 642 
network topology, connections, components, and protocols that are typically used for each 643 
system type. These examples only attempt to identify notional concepts in topology. Actual 644 
implementations of these types of control systems may be hybrids that blur the lines between 645 
them. The diagrams in this section do not focus on securing OT. Security architecture and 646 
security controls are discussed in Sec. 5 and Appendix E of this document, respectively.  647 
2.1. Evolution of OT 648 
Much of today’s OT evolved from the insertion of IT capabilities into existing physical systems, 649 
often replacing or supplementing physical control mechanisms. For example, embedded digital 650 
controls replaced analog mechanical controls in rotating machines and engines. Improvements 651 
in cost and performance have driven this evolution and led to many of today’s “smart” 652 
technologies, such as the smart electric grid, smart transportation, smart buildings, smart 653 
manufacturing, and IoT. While this increases the connectivity and criticality of these systems, it 654 
also creates a greater need for their adaptability, resilience, safety, and security. Engineering 655 
OT continues to provide new capabilities while maintaining the typical longevity of these 656 
systems. The introduction of IT capabilities into physical systems presents emergent behavior 657 
 
3 See https://csrc.nist.gov/Projects/operational-technology-security.

<!-- page 27 -->

NIST SP 800-82r4 ipd (Initial Public Draft) Guide to OT Security 
September 2026 
9 
with security implications. Engineering models and analyses are evolving to address these 658 
emergent properties, including interdependence across safety, security, privacy, and 659 
environmental impact. 660 
2.2. OT-Based Systems and Their Interdependencies 661 
OT is used in many industries and infrastructures, including those identified by the 662 
Cybersecurity and Infrastructure Security Agency (CISA) as critical infrastructure sectors listed 663 
below. OT can be found across all critical infrastructures and is more prevalent in the sectors 664 
highlighted in bold and marked with an asterisk (*): 665
 
666
 
667
 
668
 
669
 
670
 
671
 
672
 
673
 
674
 
675
 
676
 
677
 
678
 
679
 
680
 
• Chemical Sector*
• Commercial Facilities Sector*
• Communications Sector
• Critical Manufacturing Sector*
• Dams Sector*
• Defense Industrial Base Sector*
• Emergency Services Sector*
• Energy Sector*
• Financial Services Sector
• Food and Agriculture Sector*
• Government Facilities Sector*
• Healthcare and Public Health Sector*
• Information Technology Sector
• Nuclear Reactors, Materials, and Waste Sector*
• Transportation Systems Sector*
• Water and Wastewater Systems Sector*681
 
OT is vital to the operation of U.S. critical infrastructure, which is often highly interconnected 682 
and mutually dependent, both physically and through a host of information and 683 
communications technologies. While federal agencies operate many of the critical 684 
infrastructures mentioned above, many others are privately owned and operated. Additionally, 685 
critical infrastructure is often referred to as a “system of systems” because of 686 
interdependencies among industrial sectors and interconnections among business partners 687 
[Peerenboom][Rinaldi]. An incident in one infrastructure can directly and indirectly affect other 688 
infrastructures through cascading and escalating failures. For example, both the electrical 689 
power transmission and distribution grid industries use geographically distributed SCADA 690 
control technology to operate highly interconnected, dynamic systems comprising thousands of 691

<!-- page 28 -->

NIST SP 800-82r4 ipd (Initial Public Draft) Guide to OT Security 
September 2026 
10 
public and private utilities and rural cooperatives that supply electricity to end users. Some 692 
SCADA systems monitor and control electricity distribution by collecting data from and issuing 693 
commands to geographically remote field control stations from a centralized location. SCADA 694 
systems are also used to monitor and control the distribution of water, oil, and natural gas, as 695 
well as pipelines, ships, trucks, rail systems, and wastewater collection systems. 696 
SCADA systems and DCS are often networked together. This is the case for electric power 697 
control centers and generation facilities. Although the operation of an electric power 698 
generation facility is typically controlled by a DCS, the DCS must communicate with the SCADA 699 
system to coordinate production output with transmission and distribution demands. Electric 700 
power is often considered one of the most prevalent sources of disruptions to interdependent 701 
critical infrastructures. For example, a cascading failure can be initiated by a disruption of the 702 
microwave communications network used for an electric power transmission SCADA system. 703 
The lack of monitoring and control capabilities could cause a large generating unit to be taken 704 
offline, leading to a power outage at a transmission substation. This loss could cause a major 705 
imbalance, triggering a cascading failure across the power grid and resulting in large-area 706 
blackouts that potentially affect oil and natural gas production, refinery operations, water 707 
treatment systems, wastewater collection systems, and pipeline transport systems that rely on 708 
the grid for electric power. 709 
2.3. Strategic Defense Mindsets 710 
Defense-in-depth (DiD) should be treated as more than layered cybersecurity tooling. It is a 711 
deliberate strategy to create diverse and independent barriers across people, processes, 712 
technology, and the physical system so that no single failure, person, control, or knowledge gap 713 
can lead directly to an unacceptable consequence. While administrative and technical controls 714 
(e.g., procedures, access control, network segmentation, monitoring, backups, detection, 715 
response plans, recovery capabilities) reduce risk, the primary objective in OT is to prevent or 716 
limit unsafe, unreliable, or destructive physical outcomes. 717 
A mature OT defense mindset is consequence-driven. Cyber controls should be evaluated 718 
alongside engineering countermeasures that can remove or reduce the impact of a successful 719 
attack. For example, if manipulation of a control system could cause a tank to over-pressurize, 720 
the risk may be reduced not only through monitoring and access control but also through 721 
pressure relief valves, hardwired interlocks, safety instrumented functions, fail-safe design, or 722 
manual operating procedures. When selecting countermeasures, organizations should 723 
incorporate engineering-based methods (e.g., Cyber-Informed Engineering4)[CIE] so that risk 724 
reduction includes both cyber resilience and physical process resilience. 725 
4 Wright, Virginia L., Jakob P. Meng, Robert S. Anderson, et al. Cyber-Informed Engineering Implementation Guide. INL/RPT-23-74072-Rev000. 
Idaho National Laboratory (INL), Idaho Falls, ID (United States), 2023. https://www.osti.gov/biblio/1995796.

<!-- page 29 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
11 
2.4. OT System Operation, Architectures, and Components 726 
A typical OT system includes numerous control loops, human-machine interfaces, and remote 727 
diagnostics and maintenance tools, as shown in Fig. 1.  728 
 729 
 730 
Fig. 1. Basic operation of a typical OT system 731 
The system is built using an array of network protocols on layered network architectures. Some 732 
critical processes may also include safety systems.  733 
A control loop utilizes sensors, actuators, and controllers to manipulate some controlled 734 
processes. A sensor is a device that measures a physical property and then sends that 735 
information as a controlled variable to the controller. The controller interprets the 736 
measurements, generates the corresponding manipulated variables based on a control 737 
algorithm and target set points, and transmits them to the actuators. Actuators (e.g., control 738 
valves, breakers, switches, motors) are used to directly manipulate the controlled process in 739 
response to commands from the controller.  740 
In a monitoring system, there are typically no direct connections between sensors and 741 
actuators. Sensor values are transmitted to a monitoring station for human analysis. However, 742 
these types of systems can still be considered OT systems (albeit with a human in the loop) 743 
because the objective of the monitoring system is likely to identify and ultimately mitigate an 744 
event or condition (e.g., a door alerting that it has been forced open, resulting in security 745 
personnel being sent to investigate; an environmental sensor that detects high temperatures in 746 
a server room, resulting in control center personnel activating an auxiliary air conditioning unit). 747

<!-- page 30 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
12 
Operators and engineers use human-machine interfaces (HMIs) to monitor and configure 748 
setpoints, control algorithms, and controller parameters. The HMI also displays process status 749 
information and historical information. Diagnostics and maintenance utilities are used to 750 
prevent, identify, and recover from abnormal operations or failures.  751 
Sometimes, control loops are nested and/or cascaded, meaning that the set point for one loop 752 
is based on the process variable determined by another loop. Supervisory-level loops and 753 
lower-level loops operate continuously throughout a process with cycle times ranging from 754 
milliseconds to minutes. 755 
2.4.1. OT System Design Considerations 756 
The design of an OT system depends on many factors, including whether a SCADA, DCS, or PLC-757 
based topology is used. This section identifies key factors that drive design decisions regarding 758 
the control, communication, reliability, and redundancy properties of the OT system. Because 759 
these factors heavily influence the design of the OT system, they also help determine the 760 
system’s security needs.  761 
• Safety. Systems must be able to detect unsafe conditions and trigger actions to reduce 762 
unsafe conditions to safe ones. In most safety-critical operations, human oversight and 763 
control of a potentially dangerous process are essential.  764 
• Control timing requirements. System processes have a wide range of time-related 765 
requirements, including very high speed, consistency, regularity, and synchronization. 766 
Humans may be unable to reliably and consistently meet these requirements, so 767 
automated controllers may be necessary. Some systems may require computation to be 768 
performed as close to sensors and actuators as possible to reduce communication 769 
latency and perform necessary control actions on time.  770 
• Geographic distribution. Systems have varying degrees of distribution, ranging from 771 
small systems (e.g., local PLC-controlled processes) to large, distributed systems (e.g., oil 772 
pipelines, electric power grids). Greater distribution typically implies a need for wide 773 
area networking (e.g., leased lines, circuit switching, packet switching) and mobile 774 
communication. 775 
• Hierarchy. Supervisory control provides a central location that aggregates data from 776 
multiple locations to support control decisions based on the current state of the system. 777 
A hierarchical or centralized control is often used to provide human operators with a 778 
comprehensive view of the entire system.  779 
• Control complexity. Simple controllers and preset algorithms can often perform control 780 
functions. However, more complex systems (e.g., air traffic control) require human 781 
operators to ensure that all control actions are appropriate for meeting the larger 782 
objectives of the system.  783

<!-- page 31 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
13 
• Availability. Systems with stringent availability and uptime requirements may require 784 
greater redundancy or alternative implementations across all communications and 785 
controls. 786 
• Impact of failures. The failure of a control function could cause substantially different 787 
impacts across domains. Systems with greater impacts often require the ability to 788 
continue operations through redundant controls or to operate in a degraded state. 789 
2.4.2. SCADA Systems 790 
SCADA systems are used to control dispersed assets for which centralized data acquisition is as 791 
important as control [Bailey][Boyer]. These systems are used in distribution systems, such as 792 
water distribution and wastewater collection systems, oil and natural gas pipelines, and 793 
electrical utility transmission and distribution systems. SCADA systems integrate data 794 
acquisition systems with data transmission systems and HMI software to provide a centralized 795 
monitoring and control system for numerous process inputs and outputs. SCADA systems are 796 
designed to collect field information, transfer it to a control center, and display the information 797 
to the operator graphically or textually, thereby allowing the operator to monitor or control an 798 
entire system from a central location in near real-time. Based on the sophistication and setup 799 
of the individual system, control of any individual system, operation, or task can be automatic, 800 
or it can be performed by operator commands.  801 
Typical hardware includes a control server placed at a control center, communications 802 
equipment (e.g., radio, telephone line, cable, satellite), and one or more geographically 803 
distributed field sites consisting of remote terminal units (RTUs) and/or PLCs that control 804 
actuators and/or monitor sensors. The control server stores and processes the information 805 
from RTU inputs and outputs, while the RTU or PLC controls the local process. The 806 
communications hardware allows for the transfer of information and data between the control 807 
server and the RTUs or PLCs. The software is programmed to tell the system what to monitor, 808 
what parameter ranges are acceptable, and what response to initiate when a process variable 809 
changes outside of acceptable values. An intelligent electronic device (IED), such as a protective 810 
relay, may communicate directly to the control server, or a local RTU may poll the IEDs to 811 
collect the data and pass it to the control server. IEDs provide a direct interface for controlling 812 
and monitoring equipment and sensors. IEDs may be directly polled and controlled by the 813 
control server and, in most cases, have local programming that allows for the IED to act without 814 
direct instructions from the control center. SCADA systems are usually designed to be fault-815 
tolerant with significant redundancy built in, although redundancy may not be a sufficient 816 
countermeasure against a malicious attack.  817 
Figure 2 shows the components and general configuration of a SCADA system.  818

<!-- page 32 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
14 
 819 
Fig. 2. A general SCADA system layout that shows control center devices, communications equipment, and field 820 
sites 821 
The control center at the top of the diagram houses the control server and communications 822 
routers. Other control center components include the HMI, engineering workstations, and the 823 
data historian, which are all connected by a local area network (LAN). The control center 824 
collects and logs information gathered by the field sites, displays it to the HMI, and may trigger 825 
actions based on detected events. The control center is also responsible for centralized 826 
alarming, trend analyses, and reporting.  827 
The field sites at the bottom of Fig. 2 locally control actuators and monitor sensors. Field sites 828 
are often equipped with remote access capabilities to allow operators to perform diagnostics 829 
and repairs, usually via a separate dial-up modem or a wide-area network (WAN) connection. 830 
Standard and proprietary communication protocols that run over serial and network 831

<!-- page 33 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
15 
communications are used to transport information between the control center and field sites 832 
using telemetry techniques, such as telephone lines, cables, fibers, and radio frequencies (e.g., 833 
broadcast, microwave, satellite). 834 
SCADA communication topologies vary among implementations. The various topologies used 835 
are shown in Fig. 3, including point-to-point, series, series-star, and multi-drop [AGA12].  836 
 837 
 838 
Fig. 3. Examples of point-to-point, series, series-star, and multi-drop SCADA communications topologies 839 
Point-to-point is functionally the simplest type, though it can be expensive due to the individual 840 
channels required for each connection. In a series configuration, the number of channels used 841 
is reduced, but channel-sharing impacts the efficiency and complexity of SCADA operations. 842

<!-- page 34 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
16 
Similarly, the series-star and multi-drop configurations’ use of one channel per device results in 843 
decreased efficiency and increased system complexity. 844 
The four basic SCADA topologies shown in Fig. 3 can be further augmented by using dedicated 845 
devices to manage communication exchanges and perform message switching and buffering.  846 
Large SCADA systems that contain hundreds of RTUs often employ a sub-control server to 847 
alleviate the burden on the primary server. This type of topology is shown in Fig. 4. 848 
 849 
 850 
Fig. 4. An example SCADA topology that supports a large number of remote stations  851

<!-- page 35 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
17 
Figure 5 shows an example SCADA system implementation that consists of a primary control 852 
center and three field sites.  853 
 854 
 855 
Fig. 5. A comprehensive SCADA system implementation example 856 
A second backup control center provides redundancy in the event of a primary control center 857 
malfunction. Point-to-point connections are used for all communications between the control 858 
center and the field site, and two of those connections use radio telemetry. The third field site 859 
is local to the control center and uses the WAN for communications. A regional control center 860 
resides above the primary control center for a higher level of supervisory control. The 861 
enterprise network has access to all control centers via the WAN, and field sites can be 862 
accessed remotely for troubleshooting and maintenance operations. The primary control center 863 
polls field devices for data at defined intervals (e.g., 5 seconds, 60 seconds) and can send new 864 
set points to field devices as required. In addition to polling and issuing high-level commands, 865 
the control server also monitors priority interrupts from field-site alarm systems.  866 
2.4.3. Distributed Control Systems 867 
A DCS is used to control production systems within the same geographic location for various 868 
industries, such as oil refineries, water and wastewater treatment, electric power generation, 869 
chemical manufacturing, automotive production, and pharmaceutical processing. These 870 
systems are usually process control or discrete part control systems. 871

<!-- page 36 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
18 
A DCS is integrated as a control architecture that contains a supervisory level of control to 872 
oversee multiple integrated sub-systems that are responsible for controlling the details of a 873 
localized process. A DCS uses a centralized supervisory control loop to mediate a group of 874 
localized controllers that share the overall tasks of carrying out an entire production process 875 
[Erickson]. Product and process control are usually achieved by deploying feedback or 876 
feedforward control loops, which automatically maintain key product and/or process conditions 877 
around a desired set point. Specific process controllers or more capable PLCs are employed in 878 
the field and tuned to provide the desired tolerance and the rate of self-correction during 879 
process upsets. By modularizing the production system, a DCS reduces the impact of a single 880 
fault on the overall system. In many modern systems, the DCS is interfaced with the enterprise 881 
network to give business operations a view of production.  882 
Figure 6 shows an example implementation of the components and general configuration of a 883 
DCS.  884 
 885 
Fig. 6. A comprehensive DCS implementation example 886 
This DCS encompasses an entire facility, from the bottom-level production processes up to the 887 
enterprise layer. In this example, a supervisory controller (control server) communicates to its 888 
subordinates via a control network. The supervisor sends set points to and requests data from 889 
the distributed field controllers. The distributed controllers control their process actuators 890 
based on control server commands and sensor feedback from process sensors.  891 
Figure 6 also provides examples of low-level controllers found on a DCS system. The field 892 
control devices shown include a machine controller, a PLC, and a process controller. The 893 
machine controller interfaces with sensors and actuators via point-to-point wiring, while the 894

<!-- page 37 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
19 
other three field devices use fieldbus networks to connect to process sensors and actuators. 895 
Fieldbus networks eliminate the need for point-to-point wiring between a controller and 896 
individual field sensors and actuators. Additionally, a fieldbus allows for greater functionality 897 
beyond control, including field device diagnostics, and can accomplish control algorithms within 898 
the fieldbus, thereby avoiding signal routing back to the PLC for every control operation. 899 
Standard industrial communication protocols designed by industry groups (e.g., Modbus and 900 
Fieldbus [Berge]) are often used on control networks and fieldbus networks. 901 
In addition to the supervisory-level and field-level control loops, intermediate levels of control 902 
may also exist. For example, in the case of a DCS controlling a discrete part manufacturing 903 
facility, there could be an intermediate-level supervisor for each cell in the plant. This 904 
supervisor encompasses a manufacturing cell containing a machine controller that processes a 905 
part and a robot controller that handles raw stock and final products. There could be several of 906 
these cells that manage field-level controllers under the main DCS supervisory control loop. 907 
2.4.4. Programmable Logic Controller-Based Topologies 908 
PLCs are used in both SCADA and DCS systems as the control components of an overall 909 
hierarchical system to locally manage processes through feedback control, as described in the 910 
previous sections. In the case of SCADA systems, they may provide similar functionality to RTUs. 911 
When used in DCS systems, PLCs are implemented as local controllers within a supervisory 912 
control scheme.  913 
PLCs can also be implemented as the primary controller in smaller OT system configurations to 914 
provide operational control of discrete processes (e.g., automobile assembly lines, process 915 
controllers). These topologies differ from SCADA and DCS in that they generally lack a central 916 
control server or HMI and, therefore, primarily provide closed-loop control with minimal 917 
human involvement. PLCs have a user-programmable memory for storing instructions for the 918 
purpose of implementing specific functions, such as I/O control, logic, timing, counting, three 919 
mode proportional-integral-derivative (PID) control, communications, arithmetic, and data and 920 
file processing.  921 
Figure 7 shows a PLC over a fieldbus network performing the control of a manufacturing 922 
process. The PLC is accessible via a programming interface located on an engineering 923 
workstation, and data is stored in a data historian, all of which are connected on a LAN.  924

<!-- page 38 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
20 
 925 
Fig. 7. A PLC control system implementation example 926 
2.4.5. Safety Systems 927 
Many of the physical processes that OT systems control have the potential to create hazardous 928 
situations to human life and safety, property, and the environment. Safety systems are 929 
designed to reduce the likelihood and/or consequences of these potentially hazardous 930 
situations by bringing the system to a safe state. There are several types of safety systems 931 
related to OT environments, including emergency shutdown (ESD), process safety shutdown 932 
(PSS), and fire and gas systems (FGS).  933 
One of the more well-known types of safety system is the safety instrumented system (SIS), 934 
which is composed of one or more safety instrumented functions (SIFs). An SIF is an engineered 935 
system that is typically comprised of sensors, logic solvers, and final control elements (e.g., 936 
actuators) whose purpose is to bring a system to a safe state when predetermined thresholds 937 
are violated. An SIS is implemented as part of an overall risk reduction strategy to reduce the 938 
likelihood and/or potential consequences of a previously identified event so that it is within the 939 
organization’s risk tolerance. Although numerous other terms are associated with safety 940 
systems, the SIS is specifically designed in accordance with [IEC61511]. An SIS is typically found 941 
in chemical, refinery, and nuclear processes.  942

<!-- page 39 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
21 
An SIS is often independent from all other control systems in such a manner that a failure of the 943 
basic process control system (BPCS) will not negatively affect SIS functionality. Historically, an 944 
SIS was designed to be stand-alone, physically and logically separated, and air-gapped from the 945 
rest of the control system. In the configuration shown in Fig. 8, the SIS and BPCS operate 946 
completely independently of each other with no direct communication between the systems.  947 
 948 
 949 
Fig. 8. An SIS implementation example 950 
However, some modern SISs have been designed to allow communication with the control 951 
system. These types of SISs are called Integrated Control and Safety Systems (ICSSs). An ICSS 952 
solution may be an all-in-one device from a single vendor or incorporate multiple devices from 953 
multiple vendors. While an ICSS combines the functionality of both control and safety systems, 954 
the SIS must still comply with the requirements outlined in [IEC61511]. One of the advantages 955 
of this ICSS methodology is the ability to communicate information from the SIS to the BPCS.  956 
While this guide contains recommendations that are applicable and could be used as a 957 
reference to protect safety systems against cybersecurity threats, readers are encouraged to 958 
perform a risk-based assessment on their systems and tailor the recommended guidelines and 959 
solutions to meet their specific security, business, and operational requirements.  960 
2.4.6. Cloud and IoT/IIoT Convergence 961 
OT environments are increasingly connected to cloud services, IoT, and IIoT platforms. Cloud 962 
environments are shared pools of configurable computing resources that are typically operated 963 
by external service providers. While IoT refers to both consumer and industrial devices 964 
connected to the internet, the Industrial IoT Consortium (IIC) defines IIoT as “subset of IoT and 965

<!-- page 40 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
22 
focuses specifically on industrial applications such as transportation, manufacturing, healthcare, 966 
energy and agriculture” [IIC1]. 967 
These technologies can support data collection, monitoring, analytics, remote access, 968 
enterprise integration, predictive maintenance, managed services, and security operations. 969 
Common examples include advanced metering infrastructure (AMI), environmental and asset 970 
condition monitoring, enterprise resource planning (ERP), manufacturing execution systems 971 
(MES), security information and event management (SIEM), vulnerability management, threat 972 
detection, remote engineering access, and zero trust network access (ZTNA). These capabilities 973 
can reduce the need to operate some local infrastructure and offer provider-managed 974 
scalability, analytics, maintenance, and security capabilities. That said, these integrations can 975 
also expand the OT attack surface by introducing externally operated services, remotely 976 
managed devices, shared infrastructure, and new communication paths into or near OT 977 
networks. 978 
Figure 9 illustrates an example architecture with IIoT and cloud connectivity.  979 
 980 
Fig. 9. Cloud and IIoT convergence example architecture 981 
IIoT architectures commonly include sensors, instruments, machines, edge gateways, wireless 982 
or wired access networks, and backend platforms hosted on premises, in the cloud, or with a 983

<!-- page 41 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
23 
vendor. Cloud, IoT, and IIoT integrations can be implemented using several common 984 
architectural patterns, such as:  985 
• Telemetry-to-cloud architecture. Sensors, monitoring devices, or gateways send 986 
selected operational data to a cloud platform for dashboards, analytics, reporting, or 987 
predictive maintenance. Control functions typically remain local.  988 
• Edge gateway architecture. OT devices communicate with an industrial gateway or edge 989 
platform that normalizes protocols, filters data, enforces policy, and forwards selected 990 
data to cloud, vendor, or enterprise systems. 991 
• Remote access/ZTNA architecture. Cloud-hosted identity, broker, or zero trust access 992 
services mediate remote engineering, vendor support, or administrative access into the 993 
OT environment. 994 
Cloud and IIoT integrations can introduce dependencies on external services, vendor-managed 995 
devices, telecommunications providers, SaaS platforms, and cloud infrastructure. These 996 
dependencies can complicate many security functions and require additional planning, 997 
coordination, and controls, especially when used to expand existing OT systems. Examples of 998 
key considerations include:  999 
• Shared responsibility. Organizations should define responsibility for identity and access 1000 
management, patching, configuration, monitoring, logging, incident response, backup, 1001 
vulnerability handling, and recovery. These responsibilities may be shared among OT, IT, 1002 
cloud providers, SaaS providers, telecommunications providers, system integrators, and 1003 
equipment vendors. 1004 
• Availability and resilience. Organizations should determine which OT functions can 1005 
tolerate loss of cloud, vendor, or communications services. Safety, protection, and time-1006 
critical control functions should generally remain capable of local operation with 1007 
documented fallback, fail-safe behavior, and tested recovery procedures. 1008 
• Data governance and terms of use. Organizations should review what data is collected, 1009 
transmitted, stored, analyzed, retained, or shared by cloud and IIoT devices. This 1010 
includes operational data, asset information, logs, metadata, user activity, and 1011 
maintenance data. Terms of use, contracts, and service agreements should define data 1012 
ownership, access rights, storage location, third-party sharing, retention, deletion, and 1013 
security protections. 1014 
• Network boundaries and communications. Connections between OT systems, IIoT 1015 
devices, edge gateways, cloud services, and vendor environments should use defined 1016 
and monitored boundaries, strong authentication, encrypted communications, least-1017 
privilege access, and logging. Cellular modems and vendor-managed connections can 1018 
bypass enterprise and OT network security controls. Organizations should inventory and 1019 
approve these connections, restrict what they can reach, monitor their use where 1020 
possible, and prevent them from creating unmanaged paths into OT networks.  1021 
• Device life cycle management. IIoT devices should be inventoried, uniquely identified, 1022 
securely configured, patched or otherwise mitigated, and monitored throughout their 1023

<!-- page 42 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
24 
life cycle. Organizations should evaluate default credentials, firmware update 1024  
mec
hanisms, secure boot, vulnerability disclosure practices, vendor remote access, and 1025 
end-of-s
upport risks before deployment. 1026 
O
rganizations (e.g., Industry IoT Consortium) provide additional guidance on IIoT architectures 1027 
and operations [IICSMM]. Further guidance on IoT security is defined in the following 1028 
documents:   1029 
• SP 800-213, IoT Device Cybersecurity Guidance for the Federal Government: Establishing 1030 
IoT Device Cybersecurity Requirements 1031 
• SP 1800-36, Trusted Internet of Things (IoT) Device Network-Layer Onboarding and 1032 
Lifecycle Management: Enhancing Internet Protocol-Based IoT Device and Network 1033 
Security  1034 
• IR 8228, Considerations for Managing Internet of Things (IoT) Cybersecurity and Privacy 1035 
Risks 1036 
2.5. Sector Specific Architecture and Security Challenges 1037 
Some sectors rely on specialized architectures and technologies that introduce distinct 1038 
cybersecurity challenges. This section examines sector-specific architectures associated 1039 
operational requirements and related cybersecurity considerations. 1040 
2.5.1. B
uilding Automation and Control Systems (BACS) 1041 
A building automation and control system (BACS) is a type of OT system used to manage critical 1042 
building infrastructure and optimize facility operations. These systems oversee heating, 1043 
ventilation, and air conditioning (HVAC), fire safety, electrical and lighting systems, physical 1044 
security and access controls, and energy management. While most modern buildings are 1045 
constructed with BACS integration, older facilities often require retrofitting to achieve this level 1046 
of centralized control and the associated operational benefits.  1047 
2.5.1.1. Architectures and Technologies 1048 
BACS may include supervisory-level systems that collect, analyze, and report data across many 1049 
subsystems. The automation layer will have controllers for dedicated subsystems that may be 1050 
connected to the supervisory layer, depending on system functions. The BACS may have 1051 
multiple different subsystems, including: 1052 
• Fire and life safety systems. Fire and life safety systems are typically built around 1053 
centralized fire alarm control panels connected to distributed detection, notification, 1054 
and suppression field devices. These systems are often among the most critical BACS 1055 
assets and should operate in an isolated or heavily segmented network with fail-safe 1056 
architectures.  1057

<!-- page 43 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
25 
• Electronic Security Sy stems (ESS). ESS include systems used to monitor and control 1058 
ac
cess to the facility. Physical access control systems (PACS) use access control panels to 1059 
manag
e readers, credentials, locks, and door position sensors. PACS systems may 1060 
be inte
grated with enterprise systems, especially identity management and monitoring. 1061 
Th
ey may also include CCTV and motion sensors to monitor for unauthorized access.  1062 
•
 HVAC systems. HVAC systems use direct digital control (DDC) controllers to manage 1063 
sensors, valves, dampers, and air handlers and may need integration with enterprise IT 1064 
systems. HVAC systems can be critical because failures may create unsafe conditions or 1065 
damage equipment if climate requirements cannot be maintained. 1066 
• Lighting management systems. Lighting systems use controllers to manage zones and 1067 
respond to occupancy sensors. Lighting can be important for safety in certain locations.  1068 
• Energy management systems. Meters may be used to collect and monitor energy usage 1069 
within the building.  1070 
An example of a BACS is shown in Fig. 10.  1071 
 1072 
Fig. 10. Example BACS architecture 1073 
Key properties of BACS architectures include:   1074 
• BACS environment variability. BACS architectures can differ depending on the scale of 1075 
the facility (e.g., a single building versus a campus environment). BACS subsystems can 1076 
range from isolated analog systems to digital networked control systems that integrate 1077 
multiple BACS subsystems through a single-pane-of-glass dashboard. Security 1078 
needs for a BACS environment depend heavily on the extent to which the system uses 1079 
digital technology, interconnects multiple subsystems, and requires connectivity with 1080 
remote sites or external systems.  1081

<!-- page 44 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
26 
• U nique  criticality and risk across subsystems. Different BACS subsystems have different 1082  
c
riticality and cybersecurity risks. Some subsystems perform safety-critical functions 1083
 
(
e.g., fire suppression, sprinkler activation,  elevator safety) but may be isolated from 1084
 
o
ther systems. Other subsystems are networked and integrated with 1085
 
s
upervisory control layers, which can increase their exposure to threats. 1086
 
• Commercial versus government/military operation. Common architectures, 1087 
technologies, and security requirements often vary significantly between commercial 1088 
buildings and those used in government and defense environments. Therefore, 1089 
organizations should explore guidance that is tailored to their specific 1090 
operating environment.   1091 
• Shared network infrastructure. A BACS often leverages a building’s existing 1092 
telecommunications infrastructure because it is a highly efficient way to connect devices 1093 
distributed across a large physical footprint. However, utilizing this shared medium can 1094 
create unintended connection points and security vulnerabilities between the OT 1095 
environment and the organization’s enterprise IT network.    1096 
• Use of wireless. Wireless communications offer deployment flexibility, which is 1097 
particularly beneficial when retrofitting older facilities where installing new cabling is 1098 
impractical. However, wireless BACS deployments face specific physical and security 1099 
challenges. Operationally, signals are prone to degradation and dead zones caused by 1100 
structural building materials (e.g., concrete walls, steel, treated glass). From a security 1101 
standpoint, because these signals are broadcast through spaces shared by a wide variety 1102 
of occupants and visitors, they are inherently more exposed to eavesdropping, jamming, 1103 
and unauthorized access.  1104 
2.5.1.2. Key Cybersecurity Challenges and Recommendations  1105 
Cybersecurity challenges and recommendations include: 1106 
• Poorly defined security responsibility. BACS security is often overlooked, primarily due 1107 
to ambiguous governance responsibilities among facilities management, OT, and IT 1108 
cybersecurity groups. This can be further complicated in buildings with landlord/tenant 1109 
relationships, especially in multi-tenant commercial buildings. Unresolved items often 1110 
include ownership of the BACS network, responsibility for security management, and 1111 
accountability for BACS data. BACS security requires a shared responsibility model with 1112 
clearly defined roles, including the owner of BACS security risk, the entity responsible 1113 
for secure design, vulnerability management, and dedicated roles for security 1114 
monitoring and operations.    1115 
• Prioritize investments by criticality. Due to the variety of BACS systems within a 1116 
building, organizations may have to prioritize efforts and investments based on 1117 
s
ubsystem criticality rather than apply uniform controls across all BACS subsystems. 1118 
Particular emphasis should be placed on safety-critical functions and systems that are 1119

<!-- page 45 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
27 
subject to regulatory requirements. Criticality should be validated with appropriate 1120 
g
roups, including operations and technical teams.  1121
 
• Cybersecurity insufficiently defined during integration and commissioning. BACS also 1122 
commonly exhibits security challenges during the construction of new buildings, 1123 
especially large commercial projects that can have many subcontractors with access to 1124 
the OT network and devices. Common issues include default credentials, improperly 1125 
managed laptops, and unauthorized remote access systems. Often, the commissioning 1126 
process does not adequately address security, meaning default credentials or keys are 1127 
never changed before the system transitions to production. Security responsibilities 1128 
should be clearly defined for contractors who support building integration efforts. These 1129 
responsibilities should specify who is accountable for securely configuring 1130 
infrastructure, changing critical credentials and cryptographic keys during 1131 
commissioning, and validating that these changes have been completed.  1132 
• Insufficient incident response and recovery planning. BACS systems and facilities 1133 
personnel may not have performed adequate incident response and recovery planning 1134 
or have not incorporated it into broader incident response and recovery plans within 1135 
the organization. This means that BACS environments and personnel may not be 1136 
adequately prepared to respond to an incident. Organizations should ensure that BACS 1137 
environments are incorporated into their incident response plans along with supporting 1138 
groups and external organizations (e.g., vendors, service providers). These activities 1139 
need to be commensurate with the criticality of the subsystems and avoid 1140 
overburdening key operational staff. The BACS environment should also include 1141 
dedicated playbooks that address key threats, such as ransomware, unauthorized 1142 
remote access, and integrity loss in critical systems. Tabletop exercises (TTXs) should be 1143 
held periodically and should include BACS-specific scenarios. Recovery procedures 1144 
should be documented and tested on representative devices and environments.  1145 
• Cloud and AI adoption. For new commercial installations, cloud-connected BACS is 1146 
becoming the standard approach and may be required for full support and features. AI 1147 
is also increasingly common for many BACS functions, including occupancy sensing, 1148 
smart HVAC controls, appliance management, renewable energy balancing, and 1149 
malfunction detection.  1150 
• Regulatory requirements for safety and data collection. BACS environments often have 1151 
regulatory requirements that dictate the operation of safety-critical systems, such as 1152 
elevators and fire suppression systems. Regulations may also require the reporting of 1153 
data from buildings, such as for energy or environmental purposes. Organizations 1154 
should understand relevant regulations and ensure that cybersecurity decisions and 1155 
architectures broadly align with the associated requirements.   1156 
2.5.2. Food and Agriculture 1157 
Food and agriculture OT spans the full production chain: primary production (e.g., crop and 1158 
animal agriculture), processing and manufacturing, storage and refrigeration, and distribution. 1159

<!-- page 46 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
28 
The majority of the segments in this chain overlap with OT sectors that have already been 1160 
addressed in these guidelines. For example, processing corresponds to existing manufacturing 1161 
guidance; storage and refrigeration correspond to building automation and cold-chain 1162 
monitoring; and distribution corresponds to transportation OT. Because architectures, 1163 
technologies, and security requirements vary significantly across these segments, organizations 1164 
should apply guidance tailored to the specific segment of the food and agriculture chain in 1165 
which they operate. This guidance accordingly focuses on the on-farm and first-handler 1166 
environment and encompasses technologies such as guided and automated field equipment, 1167 
irrigation control, livestock environmental control, and grain handling and storage. 1168 
2.5.2.1. Architectures and Technologies 1169 
Five system types cover most of the on-farm and first-handler footprint: 1170 
1. Guided and automated field equipment. Tractors, combines, planters, and sprayers use 1171 
Global Navigation Satellite System (GNSS) guidance to support autosteer functions, 1172 
while late-model machines report continuously to a manufacturer’s cloud platform. 1173 
2. Irrigation control. Automated valves, center-pivot controllers, and soil-moisture sensor 1174 
networks are often adjusted remotely over cellular links through small SCADA systems 1175 
or vendor portals. 1176 
3. Livestock environmental control and automated milking. Ventilation and climate 1177 
controllers are typically used in poultry and swine housing, robotic milking systems, RFID 1178 
animal tracking, herd-management software (e.g., invisible fencing), and milk cooling 1179 
tanks. These technologies are often closely interconnected, and a single compromised 1180 
controller can disable an entire working operation. 1181 
4. Grain handling and storage. Dryers, aeration fans, and silo temperature and level 1182 
sensors are frequently integrated with elevator automation at cooperatives. 1183 
5. Farm-management and cooperative software platforms. A cloud layer aggregates field 1184 
data and returns prescriptions to equipment. 1185 
Key properties of food and agriculture control environments include: 1186 
• Unique criticality across system types. Different food and agriculture system types 1187 
carry different criticality and risk profiles. Some directly affect animal life and welfare if 1188 
compromised, such as livestock environmental control and milking systems. For 1189 
example, a ventilation shutoff or emergency-stop function should sit on a circuit or 1190 
controller that is independent of the monitoring and data systems so that a compromise 1191 
of the monitoring layer cannot cascade into a safety failure. Others primarily affect 1192 
operational continuity and economic outcomes, such as grain handling and farm-1193 
management platforms. Security priorities and controls should be calibrated to the 1194 
specific consequences of each system type rather than applied uniformly. 1195 
• Biological and environmental operating constraints. Many food and agriculture control 1196 
processes are governed by biological or environmental cycles rather than a schedule set 1197

<!-- page 47 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
29 
by operators. For example, animal welfare, growth cycles, and seasonal windows dictate 1198 
whe
n systems must run continuously and when they cannot be interrupted. These 1199
 
s
ystems often have no downtime window, and a missed operating cycle cannot always 1200
 
b
e recovered afterward. 1201
 
• Prevalence of small, under-resourced operations. Unlike many OT sectors dominated 1202 
by large enterprises, food and agriculture is composed overwhelmingly of small 1203 
operations. Most American farms lack dedicated compliance staff, security budgets, or 1204 
reliable broadband; typically operate with limited resources; and often rely on manual 1205 
processes, paper-based recordkeeping, and legacy analog or mechanical equipment. As 1206 
a result, a baseline level of digital maturity or security posture cannot be assumed 1207 
across the sector, and guidance intended for well-resourced enterprises will not reach 1208 
most of the organizations that make up this space. 1209 
• Reliance on public and shared networks. Connectivity at the farm edge relies on 1210 
whatever reaches a remote site, including cellular service across 3G, 4G, and 5G; 1211 
commercial satellite; low-power wide-area networks, such as LoRaWAN; and Wi-Fi. That 1212 
reliance extends to the operator’s own device. Personal smartphones running vendor 1213 
equipment apps and weather tools have become an operational interface of their own. 1214 
These phones typically carry no security management and mix personal and farm use 1215 
freely. On a small operation, the phone is often the only way to reach either function.  1216 
• Equipment and fixed-installation protocols. On equipment, the ISOBUS standard (ISO 1217 
11783) running over a Controller Area Network (CAN) bus handles communication 1218 
between a tractor and its implements and governs interoperability rather than security. 1219 
In fixed installations (e.g., irrigation, grain handling), Modbus and similar industrial 1220 
protocols are common, and few carry authentication or encryption. 1221 
2.5.2.2. Key Cybersecurity Challenges and Recommendations 1222 
Cybersecurity challenges and recommendations include: 1223 
• Guided and autonomous equipment vulnerable to signal disruption. Guided and 1224 
autonomous field equipment relies on GNSS signals and correction services, so spoofing, 1225 
jamming, or natural disruption can halt or misdirect machinery across a wide area. 1226 
Organizations should evaluate the availability of correction-service redundancy and 1227 
manual fallback procedures for planting and harvest operations. They should confirm 1228 
that equipment vendors disclose remote-access and remote-disable capabilities since a 1229 
field operation needs to be completable if that connectivity is lost. 1230 
• Platform dependence. Farm operations and cooperatives frequently depend on a single 1231 
cloud or software platform to conduct essential functions. When this platform is 1232 
disrupted, the resulting impact is not confined to a single operation. Given the degree to 1233 
which operations rely on a common underlying system, it may extend across an entire 1234 
region or industry segment. Organizations should assess their dependence on individual 1235 
platforms, maintain degraded-mode or offline-capable fallback procedures, and ensure 1236

<!-- page 48 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
30 
data portability so that no single platform constitutes an unrecoverable point of failure. 1237 
Fo
r example, irrigation controllers should be segmented from the business network with 1238
 
i
nbound internet access removed, and grain-handling operations should maintain 1239
 
man
ual, offline procedures for receiving and movement so that a platform outage does 1240
 
no
t halt physical operations on its own. 1241
 
• Cyber incidents can surface as food-safety incidents. Pasteurization, clean-in-place 1242 
sanitation, and allergen dosing are governed by OT, so a manipulated setpoint or a lost 1243 
monitoring record becomes a food-safety problem with the same consequences as 1244 
contamination. Security controls in these environments should be evaluated jointly with 1245 
food-safety teams, and cyber-incident scenarios should be built into food-safety hazard 1246 
analyses. 1247 
• Small operators lack security resources. Most American farms are small operations 1248 
without dedicated compliance staff or security budgets. For the large population of 1249 
small operations, the critical security controls are multi-factor authentication, regular 1250 
offline backups, sound password practices, and security awareness training, which 1251 
together help deter the opportunistic automated scanning responsible for most attacks 1252 
against this segment. 1253 
• Cloud and AI adoption. Cloud computing is already pervasive because manufacturer 1254 
telematics platforms are cloud-based by default, and the associated risk is both 1255 
operational dependence and an expanded network attack surface. AI adoption is 1256 
growing in computer vision for weed and pest detection, yield prediction, and 1257 
autonomy, raising concerns about the manipulation of sensor and vision inputs, the 1258 
poisoning of training data, and the additional connectivity that these systems require. 1259 
2.5.3. Transportation — Freight Rail 1260 
Freight railroad environments rely on control systems to support the safe and reliable 1261 
movement of trains across mainlines, yards, and terminals. These environments are highly 1262 
distributed and often depend on a combination of fixed infrastructure, mobile assets, remote 1263 
field equipment, and enterprise systems. Freight railroad OT environments can include train 1264 
control systems, dispatch and traffic management systems, signal and interlocking systems, 1265 
wayside monitoring systems, grade crossing warning systems, yard and terminal automation, 1266 
locomotive onboard systems, and supporting telecommunications infrastructure.  1267

<!-- page 49 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
31 
 1268 
Fig. 11. Example freight rail architecture 1269 
2.5.3.1. Architectures and Technologies  1270 
An example of a freight railroad architecture is shown in Fig. 11. Railroad control 1271 
systems depend on multiple components, including:   1272 
• Wayside and switching/signaling systems. Wayside environments include 1273 
infrastructure that monitors track state, controls signals and switches, and 1274 
communicates with locomotives, dispatch, and back-office systems. This can include 1275 
wayside interface units (WIUs), signal bungalows, switch machines, grade crossing 1276 
equipment, vital signal controllers (VSCs), and train management computers (TMC).  1277 
• Dispatch and traffic management systems. Dispatch systems provide centralized 1278 
visibility and control over train movements, track occupancy, work authorities, and 1279 
operational restrictions. These systems often integrate with IT-based planning, crew, 1280 
maintenance, and monitoring systems, making them a critical IT/OT boundary.  1281

<!-- page 50 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
32 
• Locomotives. Locomotives include onboard control systems, event recorders, PTC 1282 
controllers, end-of-train (EOT) devices, telemetry systems, and remote diagnostics. EOT 1283 
devices transmit train-line and rear-of-train statuses to head-end equipment and may 1284 
support braking functions. Locomotives increasingly maintain connectivity with 1285 
manufacturers or fleet systems for health monitoring and real-time telemetry.  1286 
• Positive Train Control (PTC) systems. PTC uses locomotive-mounted units (LMUs), 1287 
wayside interface units (WIUs), wireless communications, positioning data, and back-1288 
office systems to enforce train movement limits and reduce the risk of collisions, 1289 
overspeed derailments, incursions into work zones, and movement through misaligned 1290 
switches.  1291 
• Yard and terminal systems. Railyards and terminals may include yard management 1292 
systems, scales, inspection portals, gate systems, and local communications networks.  1293 
Key properties of freight railroad architectures include:   1294 
• Geographically distributed and remote sites. Freight railroads include numerous 1295 
geographically distributed endpoints, such as locomotives, wayside devices, signal 1296 
bungalows, grade crossings, and communications shelters. This distribution creates 1297 
dependencies on diverse communications services, including private networks, 1298 
commercial carriers, and wireless modalities. 1299 
• Use of wireless. Freight rail devices depend heavily on wireless communications 1300 
because assets are mobile, transient, and geographically dispersed. Communications to 1301 
wayside assets and locomotives may rely on cellular, radio, microwave, or other wireless 1302 
services. PTC also uses 220 MHz radio systems to support interoperable 1303 
communications among locomotives, wayside devices, and back-office systems.  1304 
• Interconnection with IT and external systems. Rail OT often exchanges data with 1305 
enterprise systems for dispatch support, train planning, crew management, 1306 
maintenance, asset management, customer visibility, cybersecurity monitoring, and 1307 
regulatory reporting. These integrations create operational value but also introduce 1308 
IT/OT dependencies that should be segmented, monitored, and governed. 1309 
2.5.3.2. Key Cybersecurity Challenges and Recommendations 1310 
Cybersecurity challenges and recommendations include: 1311 
• Safety-related and regulated systems. Many rail systems are safety-critical, including 1312 
switching, signaling, highway-rail grade crossings, dispatch authority, and PTC. 1313 
Cybersecurity teams should coordinate relevant decisions with operations, signal, 1314 
communications, safety, legal, and regulatory personnel. 1315 
• IT/OT interdependencies in dispatch and operations. Many systems (e.g., dispatch, 1316 
traffic management, planning, maintenance applications) are critical to rail operations 1317 
but often depend on enterprise systems and data. Organizations should identify these 1318

<!-- page 51 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
33 
dependencies, understand how enterprise disruptions could affect rail operations, and 1319 
e
stablish response plans that support sustained operations.  1320
 
• Dependencies on commercial communications. Railroads are often highly dependent 1321 
on external communications services to connect remote sites and assets. Organizations 1322 
should ensure communications redundancy where needed and develop operating 1323 
procedures for telecom outages, degraded wireless coverage, or the loss of remote 1324 
connectivity.  1325 
• Interoperability and shared operational responsibility. Freight rail operations often 1326 
involve multiple railroads, shared corridors, tenant operations, and terminal partners. 1327 
Cybersecurity roles and responsibilities should be documented for shared systems, 1328 
shared data, incident reporting, and recovery coordination.  1329 
2.5.4. Transportation – Maritime/Vessels 1330 
Vessels depend on control systems to support safe, environmentally sound, and reliable 1331 
operations, including navigation, propulsion, steering, and communication needs. A 1332 
compromise or malfunction of these systems can result in service disruption, casualties (i.e., 1333 
loss of life), or harm to the marine environment. These systems are typically deployed across 1334 
the shipboard control network, bridge systems, and various control rooms. Vessels often have a 1335 
shared cybersecurity responsibility model. Shipyards, OEMs, classification societies, vessel 1336 
owners, and rotating crews each contribute to the implementation of a cybersecurity program. 1337 
2.5.4.1. Architectures and Technologies 1338 
An example of a vessel architecture is shown in Fig. 12.  1339 
 1340 
Fig. 12. Maritime cargo vessel example architecture 1341

<!-- page 52 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
34 
Vessel control systems have multiple components that are grouped by function into zones, 1342 
including:  1343 
• Bridge/navigation. Vessels use a variety of systems to support navigation and avoid 1344 
collisions. The Automatic Identification System (AIS) is a transponder-based system that 1345 
displays a vessel’s location on Electronic Chart Display and Information Systems (ECDIS). 1346 
Navigation also relies heavily on GPS/GNSS, radar, and weather data. Vessels must often 1347 
maintain voyage rata recorders as well. 1348 
• Propulsion and machinery. Control systems support engine control, cooling, fuel 1349 
management, boiler control, thruster operations, and power management. These 1350 
systems are important to maneuverability, safe operation, and the continuity of vessel 1351 
services.  1352 
• Safety and security. This includes fire and gas detection systems, watertight door 1353 
controllers, CCTV, PACS, and alarm systems, including the public address/general alarm 1354 
(PA/GA). These systems are often critical to the safe operation of the vessel.  1355 
• Cargo, ballast, and power management. Control systems support cargo handling and 1356 
monitoring (e.g., loading computers, tank level gauging), ballast water management, 1357 
and electrical power generation and distribution. These systems directly affect vessel 1358 
stability, stress limits, and the continuity of electrical services. 1359 
• Engine control room. This includes systems that are necessary for supervisory control of 1360 
key OT systems, including automation servers, historians, HMIs, and workstations.  1361 
• Shipboard business network. Vessels also have networks that support administrative 1362 
workstations, maintenance systems, passenger support systems, and crew welfare 1363 
systems.  1364 
• Ship-to-shore communication. Most vessels require a Global Maritime Distress and 1365 
Safety System (GMDSS) for ship-to-shore communication, safety, operational 1366 
requirements, and passenger convenience. 1367 
Key characteristics of maritime vessel architectures include:  1368 
• Safety-related systems. Bridge/navigation, propulsion and machinery, cargo/ballast, 1369 
power, and safety/security systems directly affect safe operations. 1370 
• Mobile and intermittent connectivity. Vessels rely on satellite communications while at 1371 
sea and may use cellular or Wi-Fi when close to shore or in port. Depending on its 1372 
operational phase (e.g., at sea, dry dock, in port), the vessel can present a different 1373 
network topology and attack surface. 1374 
• Integr
ated and shared infrastructure. Vessels include components from many OEMs or 1375 
vendors that share access to vessel OT networks. These organizations often need vessel 1376 
access to perform management roles for these components.  1377

<!-- page 53 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
35 
• Diverse wireless communications. Ships are heavily dependent on satellite 1378 
communicatio
ns; HF, VHF, and UHF Radio to provide communication when at sea; and 1379 
cellu
lar or Wi
-Fi when close to shore.   1380 
• N
avigation and specific communications. Ships depend on multiple communication 1381 
systems to support navigation functions, including AIS, ECDIS, and GPS/GNSS. 1382 
• Emergency communications. Ships require emergency communications to be 1383 
operational in times of distress to provide swift response to maritime incidents, 1384 
including GMDSS, Distress Radio Beacons, and NAVTEX alerts. 1385 
• Shipboard OT protocols. Navigation  and automation systems commonly communicate 1386 
using maritime-specific protocols (e.g., NMEA 0183/2000 and IEC 61162-450 Ethernet 1387 
networks) alongside industrial protocols (e.g., Modbus, CAN bus) in machinery systems, 1388 
many of which lack native authentication or encryption. 1389 
2.5.4.2. Key Cybersecurity Challenges and Recommendations 1390 
• Mixed criticality systems using shared infrastructure. Vessels have multiple control 1391 
systems and network segments that perform separate functions with varying criticality 1392 
but share core communication architectures. Therefore, less critical systems (e.g., crew 1393 
welfare and passenger systems) should be strongly segmented from more critical 1394 
systems (e.g., engine control, safety, security). 1395 
• Interfacing with untrusted systems and devices. Vessels must often communicate with 1396 
untrusted devices (e.g., ship-to-shore communication systems used at overseas ports). 1397 
Systems and networks that must interact with untrusted systems should be strongly 1398 
segmented from critical control systems. 1399 
• Dependency on remote access. Vessels are often physically inaccessible to maintenance 1400 
staff since they are primarily at sea. Therefore, vessels require remote access for 1401 
authorized staff to perform maintenance. OEMs and vendors often require exclusive or 1402 
privileged remote access to equipment for maintenance purposes, especially during a 1403 
voyage. 1404 
• Insider threat. Vessels often have requirements for unfamiliar but high-privilege 1405 
individuals onboard (e.g., harbor pilots, port captains, superintendents, riding crew, 1406 
vendor technicians). Vessels may also house diverse populations, especially for cruise 1407 
and passenger vessels. Therefore, vessels should consider insider threats and develop 1408 
adequate plans and controls to manage risks, including physical security measures and 1409 
limited use of removable media (e.g., USB devices). 1410 
• Crew rotation. Vessel crews rotate on fixed cycles, so personnel responsible for 1411 
operating and interacting with OT systems change regularly. Rotations introduce 1412 
credential management challenges. Accounts need to be provisioned/deprovisioned in 1413 
environments that may lack centralized identity management and use shared accounts. 1414 
Security awareness and training levels will vary across crews, which can affect 1415

<!-- page 54 -->

NIST SP 800-82r4 ipd (Initial Public Draft) Guide to OT Security 
September 2026 
36 
knowledge transfer between rotations. Vessels can enforce role-based access controls 1416  
that are aligned to shipboard positions and require cybersecurity turnover briefings as 1417 
part of standard crew change procedures.  1418 
• F
ragmented governance. OEMs often maintain their own systems on board, requiring1419 
access from multiple organizations. Additionally, many vessels must operate1420 
internationally, but flag states often have their own set of requirements, and vessels1421 
must comply with standards across multiple ports, states, or nations. This can result in1422 
redundant or conflicting requirements.1423 
2.5.5. Water and Wastewater Systems (WWS) 1424 
Water and Wastewater Systems (WWS) use a combination of DCS, SCADA, and PLCs 1425 
to monitor and control water treatment, distribution networks, wastewater collection, and 1426 
wastewater treatment operations. These environments are often geographically distributed 1427 
and include both centralized control facilities and remote stations. 1428 
2.5.5.1. Architectures and Technologies 1429 
An example of a WWS architecture is shown in Fig. 13. 1430 
1431 
Fig. 13. WWS example architecture [SP1800-45] 1432

<!-- page 55 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
37 
WWSs have multiple components, including:    1433 
• Primary control station. A centralized control station operates water or wastewater 1434 
treatment plants with remote access to other control stations, remote stations, and 1435 
business information systems. 1436 
• Regional control station. Larger utilities may have secondary control stations for 1437 
monitoring and controlling multiple treatment plants in a service area. OT network 1438 
infrastructure located in a service area or at localized treatment centers can include 1439 
servers, SCADA systems, human-machine interfaces (HMIs), and programmable logic 1440 
controllers (PLCs) with process control data and sensor readings. 1441 
• Remote stations. Wireless or wired telemetry is used to monitor remote infrastructure 1442 
(e.g., pump stations, water distribution networks) that feed data back to SCADA servers 1443 
and operators.  1444 
• Various locations/stations. PLCs and controls are distributed among the network and 1445 
pump stations with sensors to enable the logging of metrics, such as pressure, 1446 
temperature, and physical-chemical characteristics [SP1800-45]. 1447 
Key properties of WWS architectures include: 1448 
• Safety-related systems. Many WWS have safety-related systems, especially water 1449 
treatment systems that perform filtration (e.g., reverse osmosis), chemical feeds (e.g., 1450 
sodium hypochlorite), or UV purification. Other safety-critical functions include those 1451 
necessary for testing and reporting on water quality. Cybersecurity teams should 1452 
coordinate relevant decisions with operations, signal, communications, safety, legal, and 1453 
regulatory personnel.  1454 
• Geographically remote sites. Water distribution systems often depend on remote 1455 
stations, including pump systems, pressure sensors, and telemetry equipment. This 1456 
creates dependencies on communications infrastructure, such as microwave radio links, 1457 
leased lines, or cellular modems.  1458 
2.5.5.2. Key Cybersecurity Challenges and Recommendations  1459 
• Regulatory requirements for safety and data collection. WWSs include systems that are 1460 
critical to water safety and must often report testing results to state agencies. 1461 
Organizations should understand applicable regulations and ensure that cybersecurity 1462 
decisions, system architectures, and operational procedures align with those 1463 
requirements.    1464 
• MSPs for OT management. Many small organizations depend on managed service 1465 
providers (MSPs) to manage OT infrastructure. Cybersecurity responsibilities and 1466 
functions are often not adequately specified in service contracts and, therefore, may not 1467 
be performed by the utility or the provider. WWS operators should ensure that 1468 
contracts clearly define the cybersecurity responsibilities, access controls, incident-1469 
reporting expectations, and maintenance practices that MSPs must follow.   1470

<!-- page 56 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
38 
• Internet exposure and remote access. Because WWSs often rely on geographically 1471 
remote sites and remote access from external MSPs or vendors to manage OT assets, 1472 
they may require internet-exposed systems or remote-access services. These services 1473 
can introduce risks if they lack adequate security controls, such as multi-factor 1474 
authentication, strong credential management, secure configuration, monitoring, 1475 
and timely patching.   1476 
2.6. Comparing OT and IT System Security 1477 
OT systems have many characteristics that differ from traditional IT systems, including distinct 1478 
risks and priorities. Some of these include significant risks to human health and safety, serious 1479 
environmental damage, and financial issues (e.g., production loss). OT has different 1480 
performance and reliability requirements and uses OSs and applications that may be 1481 
considered unconventional in a typical IT network environment. Security protections must be 1482 
implemented in a way that maintains system integrity during normal operations as well as 1483 
during cyber attacks [Knapp].  1484 
Initially, OT systems had little resemblance to IT systems because they were isolated and ran 1485 
proprietary control protocols using specialized hardware and software. Widely available, low-1486 
cost Ethernet, Internet Protocol (IP), and wireless devices are now replacing older proprietary 1487 
technologies, increasing the likelihood of cybersecurity vulnerabilities and incidents. OT 1488 
systems are increasingly resembling IT systems as they adopt IT technologies to promote 1489 
enterprise connectivity and remote access capabilities (e.g., using industry-standard computers, 1490 
OSs, network protocols). This integration supports new IT capabilities but provides significantly 1491 
less isolation for OT from the outside world than predecessor systems. While security solutions 1492 
have been designed to deal with these issues in typical IT systems, special precautions must be 1493 
taken when introducing these same solutions to OT environments. In some cases, new security 1494 
solutions tailored to the OT environment are needed.  1495 
Some special considerations when securing OT include: 1496 
• Timeliness and performance requirements. OT systems are generally time-critical, and 1497 
individual installations determine acceptable levels of delay and jitter. Some systems 1498 
require reliable, deterministic responses. High throughput is typically not essential to 1499 
OT. In contrast, IT systems typically require high throughput and can withstand some 1500 
level of delay and jitter. For some OT, automated response times or system responses to 1501 
human interaction are critical. Many OT systems use real-time operating systems 1502 
(RTOSs), which refer to timeliness requirements. The units of real time are highly 1503 
application-dependent and must be explicitly stated.  1504 
• Availability requirements. Many OT processes are continuous in nature. Unexpected 1505 
outages of systems that control industrial processes are unacceptable. Outages must 1506 
often be planned and scheduled days or weeks in advance. Exhaustive pre-deployment 1507 
testing is essential to ensuring high availability (i.e., reliability). OT systems often cannot 1508 
be stopped and started without affecting production. In some cases, the products 1509 
produced or equipment being used are more important than the information being 1510

<!-- page 57 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
39 
relayed. Therefore, typical IT strategies (e.g., rebooting a component) are usually not 1511 
ac
ceptable for OT due to adverse impacts on the requirements for high availability, 1512
 
re
liability, and maintainability. Some OT employ redundant components that often run 1513
 
in
 parallel to provide continuity when primary components are unavailable.  1514
 
• Risk management requirements. For OT, primary concerns include safety, fault 1515 
tolerance to prevent the loss of life or the endangerment of public health or confidence, 1516 
regulatory compliance, the loss of equipment, the loss of intellectual property, and lost 1517 
or damaged products. The personnel responsible for operating, securing, and 1518 
maintaining OT must understand the important link between safety and security. Any 1519 
security measure that impairs safety is unacceptable.  1520 
• Physical effects. Field devices (e.g., PLCs, operator stations, DCS controllers) are directly 1521 
responsible for controlling physical processes. OT can have complex interactions with 1522 
physical processes, and consequences in the OT domain can manifest in physical events. 1523 
Understanding these potential physical effects often requires communication between 1524 
OT experts and experts in the relevant physical domain.  1525 
• System operation. OT OSs and control networks often require different skill sets, 1526 
experience, and levels of expertise than their IT counterparts. Control networks are 1527 
typically managed by control engineers rather than IT personnel. Assuming that 1528 
differences are insignificant can have disastrous consequences on system operations.  1529 
• Resource constraints. OT systems and their RTOSs are often resource-constrained and 1530 
lack typical contemporary IT security capabilities. Legacy systems often lack the 1531 
resources common to modern IT systems. Many systems may also lack desired features, 1532 
including encryption capabilities, error logging, and password protection. The 1533 
indiscriminate use of IT security practices in OT may cause disruptions to availability and 1534 
timing. There may not be computing resources available on OT components to retrofit 1535 
these systems with current security capabilities. Adding resources or features may not 1536 
be possible. 1537 
• Communications. Communication protocols and media used by OT environments for 1538 
field device control and intra-processor communication are typically different from IT 1539 
environments and may be proprietary.  1540 
• Change management. Change management is paramount to maintaining the integrity 1541 
of both IT and OT systems. Unpatched software represents one of the greatest 1542 
vulnerabilities to a system. Software updates to IT systems, including security patches, 1543 
are typically applied in a timely manner in accordance with appropriate security policies 1544 
and procedures. In addition, these procedures are often automated using server-based 1545 
tools. Software updates on OT cannot always be implemented on a timely basis. These 1546 
updates need to be thoroughly tested by both the vendor and the end user of the 1547 
industrial control application before being implemented. Additionally, the OT owner 1548 
must plan and schedule OT outages days or weeks in advance. The OT may also require 1549 
revalidation as part of the update process. Another issue is that many OT systems utilize 1550 
older versions of OSs that are no longer supported by the vendor through patches. 1551

<!-- page 58 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
40 
Change management is also applicable to hardware and firmware. The change 1552 
man
agement process requires careful assessment by OT experts (e.g., control 1553
 
e
ngineers) working in conjunction with security and IT personnel.  1554
 
• Managed support. Typical IT systems support diverse support styles that span disparate 1555 
but interconnected technology architectures. For OT, service support is sometimes only 1556 
available from a single vendor. In some instances, third-party security solutions are not 1557 
allowed due to OT vendor licensing and service agreements, and service support can be 1558 
lost if third-party applications are installed without vendor acknowledgment or 1559 
approval.  1560 
• Component lifetime. Typical IT components have a lifespan of three to five years due to 1561 
rapid technological evolution. For OT, where technology has often been developed for 1562 
specific uses and implementations, the lifetime of the deployed technology may be in 1563 
the order of 10 to 15 years and sometimes longer.  1564 
• Component location. Most IT components and some OT components are located in 1565 
business and commercial facilities that are physically accessible by local transportation. 1566 
Remote locations may be utilized for backup facilities. Distributed OT components may 1567 
be isolated, remote, and require extensive transportation effort to reach. The 1568 
component location must also account for the necessary physical and environmental 1569 
security measures.  1570 
Table 3. Summary of typical differences between IT and OT systems 1571 
Category Information Technology Operational Technology 
Performance 
Requirements 
• Non-real time. 
• Response must be consistent. 
• High throughput is demanded. 
• High delay and jitter may be 
acceptable. 
• Emergency interaction is less critical. 
• Tightly restricted access control can 
be implemented to the degree 
necessary for security. 
• Real time. 
• Response is time-critical. 
• Modest throughput is acceptable. 
• High delay and/or jitter is 
unacceptable. 
• Response to human and other 
emergency interaction is critical. 
• Access to OT should be strictly 
controlled but should not hamper or 
interfere with human-machine 
interaction. 
Availability 
(Reliability) 
Requirements 
• Responses (e.g., rebooting) are 
acceptable. 
• Availability deficiencies can often be 
tolerated, depending on the system’s 
operational requirements. 
• Responses (e.g., rebooting) may not 
be acceptable because of process 
availability requirements. 
• Availability requirements may 
necessitate redundant systems. 
• Outages must be planned and 
scheduled days or weeks in advance. 
• High availability requires exhaustive 
pre-deployment testing. 
Risk Management 
Requirements 
• Manage data. 
• Data confidentiality and integrity is 
paramount. 
• Control the physical world. 
• Human safety is paramount, 
followed by protection of the 
process.

<!-- page 59 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
41 
Category Information Technology Operational Technology 
• Fault tolerance is less important; 
momentary downtime is not a major 
risk. 
• The major risk impact is a delay of 
business operations. 
• Fault tolerance is essential; even 
momentary downtime may be 
unacceptable. 
• The major risk impacts are 
regulatory non-compliance, 
environmental impacts, and the loss 
of life, equipment, or production. 
System Operation • Systems are designed for use with 
typical OSs. 
• Upgrades are straightforward with 
the availability of automated 
deployment tools. 
• Systems often use different and 
possibly proprietary OSs, sometimes 
without security capabilities built in. 
• Software changes must be carefully 
made, usually by software vendors, 
because of the specialized control 
algorithms and potentially modified 
hardware and software involved. 
Resource Constraints • Systems are specified with enough 
resources to support the addition of 
third-party applications, such as 
security solutions. 
• Systems are designed to support the 
intended industrial process and may 
not have enough memory or 
computing resources to support the 
addition of security capabilities. 
Communications • Standard IT communications 
protocols are used. 
• Primarily wired networks with some 
localized wireless capabilities. 
• Typical IT networking practices are 
employed. 
• Many proprietary and standard 
communication protocols are used. 
• Several types of communications 
media are used, including dedicated 
wired and wireless (e.g., radio, 
satellite). 
• Complex networks exist that 
sometimes require the expertise of 
control engineers. 
Change Management • Software changes are applied in a 
timely fashion in the presence of 
good security policies and 
procedures, and the procedures are 
often automated. 
• Software changes must be 
thoroughly tested and deployed 
incrementally throughout a system 
to ensure that the integrity of the OT 
system is maintained. 
• OT outages must often be planned 
and scheduled days or weeks in 
advance.  
• OT may use OSs that are no longer 
supported. 
• OT systems often have custom 
applications. 
Managed Support • Allow for diversified support styles. • Service support is usually provided 
through a single vendor. 
Component Lifetime • Lifetime on the order of three to five 
years. 
• Lifetime on the order of 10 to 15 
years 
Components 
Location 
• Components are usually local and 
easy to access. 
• Components can be isolated, 
remote, and require extensive 
physical effort to gain access to 
them.

<!-- page 60 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
42 
In summary, the operational and risk differences between IT and OT systems require greater 1572 
sophistication in applying cybersecurity and operational strategies. A cross-functional team of 1573 
control engineers, control system operators, and IT security professionals must work closely to 1574 
understand the potential implications of installing, operating, and maintaining security 1575 
solutions alongside control system operations. IT professionals working with OT need to 1576 
understand the reliability impacts of information security technologies before deployment. 1577 
Moreover, some OSs and applications running on OT may not operate correctly with 1578 
commercial-off-the-shelf (COTS) IT cybersecurity solutions due to their unique requirements. 1579 
 1580

<!-- page 61 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
43 
3. OT Risk Management and Governance (CSF 2.0 – GOVERN) 1581 
This section describes the development and outcomes of an OT cybersecurity program and 1582 
governance structure for new and deployed OT systems as well as OT-specific considerations. 1583 
The organization should apply its own organizational processes to develop workflows for 1584 
establishing, implementing, and reviewing programs.  1585 
To establish an effective OT cybersecurity governance capability, develop a process and assign 1586 
responsibilities and accountability to appropriate roles in the enterprise risk management 1587 
function. A cybersecurity governance process should include the following: 1588 
• Ensure that the OT cybersecurity policy is established and communicated. 1589 
• Ensure that OT cybersecurity roles and responsibilities are coordinated and aligned with 1590 
internal roles and external partners. 1591 
• Ensure that legal and regulatory requirements regarding OT cybersecurity, including 1592 
privacy, are understood and managed. 1593 
• Ensure that cybersecurity risks are integrated into enterprise risk management 1594 
processes. 1595 
At a high level, OT governance should include the policies, procedures, and processes for 1596 
managing the organization’s regulatory, legal, risk, environmental, and operational 1597 
requirements. Governance should ensure that the policies, procedures, and processes are well-1598 
understood by staff and inform the management of OT cybersecurity risk. 1599 
Organizations come in various sizes, structures, geographical spreads, and levels of complexity. 1600 
These factors, along with strategies related to resource and budget constraints, may drive 1601 
organizations to hire OT cybersecurity resources as employees or contractors or to outsource 1602 
the OT security operations function as a managed security service. Regardless of the security 1603 
operation and resource model used, the responsibility for OT cybersecurity management 1604 
should be integrated with IT cybersecurity and the enterprise risk management function. In 1605 
addition, although the following sections are described separately, they often occur in an 1606 
iterative process or in different sequences, depending on the organizational approach. 1607 
Additional information and specific examples for establishing a cybersecurity governance 1608 
capability are also provided in NIST Interagency Report (NIST IR) 8183A, Cybersecurity 1609 
Framework Manufacturing Profile Low Impact Level Example Implementations Guide [IR8183A]. 1610 
3.1. Organizational Context and Shared Governance (GV.OC and GV.RR) 1611 
The following describes how organizations should align OT cybersecurity risk management with 1612 
enterprise risk management (ERM) and define the collaborative roles needed to govern risk 1613 
effectively and support the broader mission. Because OT cybersecurity events can affect safety, 1614 
operations, regulatory compliance, the environment, and business performance, OT risk should 1615 
not be managed as a stand-alone technical issue but as part of the organization’s broader risk 1616 
management processes.  1617

<!-- page 62 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
44 
Achieving this requires a shared governance structure that brings together senior leadership, 1618 
OT, IT, safety, legal, operations, and other relevant stakeholders to establish program scope, 1619 
assign responsibilities and decision-making authority, and coordinate day-to-day cybersecurity 1620 
activities. Through this organizational context and shared governance model, organizations can 1621 
ensure that OT cybersecurity decisions are informed by both enterprise priorities, risk 1622 
tolerances and operational realities. 1623 
To mitigate cybersecurity risks to their OT systems, organizations should develop and deploy an 1624 
OT cybersecurity program. It should be integrated with existing IT cybersecurity programs and 1625 
practices but also account for the specific requirements and characteristics of OT systems and 1626 
environments. Organizations should regularly review and update their OT cybersecurity plans 1627 
and programs to reflect changes in technologies, operations, standards, regulations, and the 1628 
security needs of specific facilities. 1629 
The effective integration of cybersecurity into OT operations requires defining and executing a 1630 
comprehensive program that addresses all aspects of cybersecurity. This includes defining the 1631 
objectives and scope of the program; establishing a cross-functional team that understands OT 1632 
and cybersecurity; establishing policies and procedures; identifying cyber risk management 1633 
capabilities that include people, processes, and technologies; and identifying day-to-day 1634 
operations (including event monitoring and auditing for compliance and improvement).  1635 
Senior management must demonstrate a clear commitment to cybersecurity and communicate 1636 
its importance throughout the organization. Cybersecurity is a shared responsibility across all 1637 
members of the organization, especially by its leaders and IT and OT teams. Commitment to 1638 
cybersecurity can be demonstrated by establishing a charter for a cybersecurity program with 1639 
adequate funding, visibility, governance, and support from senior leaders. 1640 
A charter for a cybersecurity program is a plain-language high-level description that establishes 1641 
clear ownership and accountability, including for protecting OT resources and provides a 1642 
mandate for the most senior person responsible to establish and maintain the cybersecurity 1643 
program (e.g., the CISO).  1644 
A cybersecurity program charter should include program objectives, scope, and responsibilities. 1645 
Senior management establishes the OT cybersecurity program charter and identifies an OT 1646 
cybersecurity manager with the appropriate authority to lead the program. The OT 1647 
cybersecurity manager should define the roles and responsibilities of system owners, mission 1648 
and business process managers, and users. The OT cybersecurity manager should also 1649 
document the objectives and scope of the OT security program, including the affected business 1650 
organizations, the systems and networks involved, the budget and resources required, and the 1651 
division of responsibilities. 1652 
The organization may already have an information security program in place or have developed 1653 
one for its IT systems. The OT cybersecurity manager should identify which existing practices to 1654 
leverage and which are specific to the OT system. Ultimately, it will be more effective for the 1655 
team to share resources with others in the organization that have similar objectives. 1656

<!-- page 63 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
45 
3.1.1. Building an OT Cybersecurity Business Case  1657 
A strong OT cybersecurity program is fundamental to sustainable mission objectives and 1658 
business operations and can enhance system reliability and availability. This includes minimizing 1659 
unintentional OT system information security impacts from inappropriate testing, policies, and 1660 
misconfigured systems. Cyber attacks can also have other significant impacts, such as: 1661 
• Physical impacts. Physical impacts encompass the set of direct consequences of OT 1662 
failure, particularly personal and public health and safety. Other effects include the loss 1663 
of property (including data) and potential damage to the environment. 1664 
• Economic impacts. Economic impacts are a second-order effect of the physical impacts 1665 
that ensue from an OT incident, which in turn cause greater economic losses to the 1666 
facility, organization, or others who depend on the OT systems. The unavailability of 1667 
critical infrastructure (e.g., electrical power, transportation) can have economic impacts 1668 
far beyond the systems that sustain direct and physical damage. These effects could 1669 
negatively impact the local, regional, national, or possibly global economy. 1670 
• Social impacts. Another second-order effect is the loss of national or public confidence 1671 
in an organization. 1672 
The potential consequences of an OT incident also include the following intersecting examples:  1673 
• Impact on national security (e.g., facilitate an act of terrorism) 1674 
• Reduction or loss of production at one site or multiple sites simultaneously 1675 
• Injury or death of employees 1676 
• Injury or death of persons in the community 1677 
• Damage to equipment 1678 
• Release, diversion, or theft of hazardous materials 1679 
• Environmental damage 1680 
• Violation of regulatory requirements 1681 
• Product contamination 1682 
• Criminal or civil legal liabilities 1683 
• Loss of proprietary or confidential information 1684 
• Loss of brand image or customer confidence 1685 
Safety and security incidents can have negative impacts that last longer than other types of 1686 
incidents on all stakeholders, including employees, shareholders, customers, and the 1687 
communities in which an organization operates. Senior management should identify and 1688 
evaluate the highest priority items to estimate the annual business impact (e.g., in financial 1689 
terms). 1690

<!-- page 64 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
46 
A well-defined business case for an OT cybersecurity program is essential for management buy-1691 
in, the organization’s long-term commitment, and the allocation of resources needed for the 1692 
program’s development, implementation, and maintenance. The first step in developing an OT 1693 
security program is to identify the organization’s business objectives and missions, as well as 1694 
how the cybersecurity program can reduce risk and protect the organization’s ability to perform 1695 
those objectives and missions. The business case should capture senior management’s 1696 
concerns and provide the business impact and financial justification for creating an integrated 1697 
organizational cybersecurity program. It should include detailed information about the 1698 
following: 1699 
• Potential costs and failure scenarios if an OT cybersecurity program is not implemented 1700 
• High-level overview of the process, costs, and resources required to implement, 1701 
operate, monitor, review, maintain, and improve the information security program 1702 
• Opportunities to improve efficiencies by coordinating and aligning with existing 1703 
governance structures and security programs (e.g., enterprise, IT) 1704 
The economic benefits of the cybersecurity program may be evaluated in the same way as 1705 
worker health and safety programs. However, an attack on the OT system could have significant 1706 
consequences that far exceed monetary costs. 1707 
3.1.2. Presenting the OT Cybersecurity Business Case to Leadership 1708 
Organization-level management in both IT and OT operations has the perspective to 1709 
understand risks and the authority to assume responsibility for them. Senior management will 1710 
be responsible for approving and driving information security policies, assigning security roles 1711 
and responsibilities, and implementing the information security program across the 1712 
organization. Funding for the entire program can usually be done in phases. While some 1713 
funding may be required to start the program, additional funding can be obtained later as the 1714 
program’s security vulnerabilities and needs are better understood and additional strategies 1715 
are developed. 1716 
Often, a good approach to obtaining management buy-in is to build the business case on a 1717 
successful example of how another organization solved a similar problem. This often prompts 1718 
management to ask how that solution might apply to their organization. 1719 
3.1.3. Aligning OT Cybersecurity With the Enterprise Mission (GV.OC) 1720 
OT cybersecurity should be guided by the organization’s mission, business objectives, and 1721 
broader ERM strategy. OT risk management should not be treated as an isolated technical 1722 
activity. Rather, it should support the organization’s ability to safely and reliably carry out its 1723 
core functions, such as producing goods, generating energy, or delivering essential services. 1724 
Establishing this organizational context helps define the scope of the OT cybersecurity program, 1725 
identify relevant internal and external stakeholders, clarify dependencies, and ensure that OT 1726 
cybersecurity decisions are aligned with operational, regulatory, mission, and business 1727 
priorities. 1728

<!-- page 65 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
47 
The organizational context should define the scope of the OT security programs, especially the 1729 
alignment of responsibilities and coordination with closely related programs, including IT, 1730 
physical security, legal, safety, operations, and procurement. The context must also clearly 1731 
define the external stakeholders, including regulators, suppliers, contractors, and service 1732 
providers. It should have a clearly defined mission, involve all relevant stakeholders, maintain 1733 
awareness of requirements (e.g., regulatory, contractual), define and achieve objectives, and 1734 
address organizational dependencies.  1735 
3.1.3.1. Understanding Operational Consequences and Requirements 1736 
Organizations must understand the possible negative consequences that an OT cybersecurity 1737 
event could cause and what organizational requirements could be impacted. OT organizations 1738 
are often required to perform a hazard analysis to demonstrate that associated risks are 1739 
adequately managed. These processes should account for the possibility that OT security 1740 
incidents could influence or contribute to these harms. The organization should ensure that the 1741 
cybersecurity decisions are informed by the analysis. Relevant approaches include Cyber-1742 
Informed Engineering [CIE] and Cyber PHAs.  1743 
3.1.4. Navigating the Regulatory and Compliance Landscape (GV.OC) 1744 
The legal, regulatory, and compliance landscape shapes the governance of OT cybersecurity 1745 
risk. In addition to managing technical and operational risk, organizations should understand 1746 
and account for the administrative, reporting, safety, health, environmental, and sector-specific 1747 
obligations that apply to their OT environments. These requirements should be incorporated 1748 
into the organizational context, risk management processes, and cybersecurity program so that 1749 
OT cybersecurity decisions support not only safe and reliable operations but also compliance 1750 
with applicable laws, regulations, and contractual obligations. Appendix D provides examples of 1751 
cybersecurity regulations and directives applicable to critical infrastructure sectors.  1752 
The programs should ensure that they align with all necessary requirements across the 1753 
regulatory, safety, health, and environmental landscape. Regulated industries must consider 1754 
cyber-related regulatory requirements when designing their cybersecurity architecture. 1755 
Organizations should also ensure that their compliance program helps prevent business 1756 
decisions and system operations from unduly generating environmental hazards (e.g., waste). 1757 
Substantial hazards may lead to non-compliance, fines, or injury. 1758 
3.1.5. Defining Shared Roles, Responsibilities, and Authorities (GV.RR) 1759 
This section addresses the human and organizational aspects of OT cybersecurity by defining 1760 
shared roles, responsibilities, and decision-making authorities across IT, OT, and business 1761 
leadership. It should clarify who owns OT cybersecurity risk, who has the authority to approve 1762 
changes to operational systems, and how cross-functional teams coordinate enterprise 1763 
cybersecurity priorities with operational requirements. Governance should also address 1764 
boundary technologies (e.g., firewalls, data diodes) so that ownership, administration, and 1765

<!-- page 66 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
48 
monitoring responsibilities are clearly assigned, and the use of these devices does not create 1766 
unmanaged “shadow OT” functions or communication gaps between IT and OT teams. This 1767 
governance should not only account for operational data that crosses IT/OT boundaries, but 1768 
also for cybersecurity telemetry, alerts, and logs generated by devices and monitoring systems 1769 
within the OT environment. 1770 
It is essential for a cross-functional cybersecurity team to share their varied domain knowledge 1771 
and experience to evaluate and manage risk in OT. The OT cybersecurity team should consist of 1772 
representatives from the following departments: IT staff, control engineer, safety experts, 1773 
control system operator, security subject-matter expert, and enterprise risk management. For 1774 
completeness, the information security team should also include any cybersecurity service 1775 
providers. 1776 
While control engineers will play a large role in securing OT, they cannot do so without 1777 
collaboration and support from both the IT department and management. IT often has years of 1778 
cybersecurity experience, much of which is applicable to OT. As the cultures of control 1779 
engineering and IT are often significantly different, their integration will be essential for the 1780 
development of a collaborative security design and operation. 1781 
The responsibilities and authorities of each member of the cybersecurity team and peer groups 1782 
must also be defined. Examples of key authorities that must be clearly defined include: 1783 
• Ownership of systems and networks, including areas of shared responsibility (e.g., 1784 
between IT and OT) and boundary devices (e.g., firewalls, data diodes) 1785 
• The avoidance, acceptance, transfer, and mitigation of identified risks within the OT 1786 
environment 1787 
• The approval of change management issues, including decisions to patch an OT system 1788 
• Access management changes, including the approval of access by both the organization 1789 
and third parties.  1790 
• Support during incident response, including the changes in OT operational mode, 1791 
recovery changes, and third-party communication and engagement 1792 
• Responsibilities for investing in the cybersecurity program and making decisions 1793 
regarding additional investments  1794 
• The responsibilities for third-party providers, which can include service providers, 1795 
contractors, and other organizations that provide OT system development and services 1796 
and security operation and management 1797 
Supplemental guidance for establishing a cross-functional team can be found in the following 1798 
documents IR 8183A, Cybersecurity Framework Manufacturing Profile Low Impact Level 1799 
Example Implementations Guide. 1800

<!-- page 67 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
49 
3.2. Defining the OT Risk Management Strategy (GV.RM) 1801 
This section describes how organizations should define an OT risk management strategy that 1802 
aligns with enterprise risk management while reflecting the unique characteristics and 1803 
constraints of OT environments. This strategy should establish how OT cybersecurity risks are 1804 
prioritized, evaluated, tracked, reported, and addressed in a manner consistent with the 1805 
organization’s mission, operational requirements, and risk tolerance. Because OT risk decisions 1806 
can affect safety, system availability, production, and the environment, the risk management 1807 
approach should be tailored to the organization’s operating context and integrated with the 1808 
broader governance processes established in Sec. 3.1 and the risk assessment activities 1809 
described in Sec. 4.1.3. 1810 
Organizations should tailor a risk management approach that performs best based on their 1811 
operating context. A general approach for ERM is defined in IR 8286 and shown in Fig. 14.  1812 
  1813 
 1814 
Fig. 14. Risk management life cycle 1815 
OT organizations should tailor this process to align with their existing processes for managing 1816 
both business and operational risks. Additional guidance on how OT environments can align 1817 
with the RMF are included in Appendix F. 1818 
There are multiple factors to consider when applying risk management to OT systems, 1819 
including:  1820 
• Safety. It is the organization’s greatest responsibility to ensure that each risk response is 1821 
ultimately a decision that makes the workplace safer. Risks to safety are generally 1822 
unacceptable and must be treated accordingly. 1823 
• Operational impact. Risk response options that require a mission-critical system to be 1824 
taken offline may not be feasible. The organization should consider the criticality of 1825

<!-- page 68 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
50 
production assets and their continued operation before approving any action that would 1826  
re
quire downtime and potential cascading impact to other organizations.  1827 
T
he risk management process must align with other elements of cybersecurity programs, 1828 
including key steps in governance, especially the defined Organizational Context (GV.OC), and 1829 
the process of performing a risk assessment to identify risks and assess their severity and 1830 
likelihood (ID.RA). Risk management should focus on how these risks are prioritized and 1831 
reported, the decisions made to address them, and how they will be tracked and monitored. 1832 
3.2.1. Maintaining a Risk Register 1833 
Once risks are enumerated, they must be recorded and reported. Organizations should 1834 
maintain a risk register with sufficient information to both make informed risk management 1835 
decisions and inform stakeholders and interested parties. Criteria to include for each risk is 1836 
included in Table 4. 1837 
Table 4. Risk register entry criteria 1838 
Register Criteria  Description  
Priority   An ordinal or scaled indicator of the risk criticality relative to others (e.g., low, 
moderate, high, critical).   
Risk Description  A summary of the risk scenario.    
Risk Category  The high-level classification of the risk (e.g., Operational, Strategic, Compliance, 
Financial).    
Estimated Likelihood  A qualitative measure (e.g., low, moderate, imminent) of the likelihood of 
occurrence.  
Estimated Impact  A qualitative measure (e.g., low, moderate, high, critical) of how grave the associated 
consequences would be if the risk manifested.  
Impact Categories  A list of potential business functions impacted by the risk (e.g., financial, health, 
safety, and environmental [HSE]; mission) and a description of how the impact would 
manifest.  
Combined Exposure Rating  A measure (e.g., low, moderate, high, critical) of the total associated risk based on 
likelihood and impact in accordance with the matrix in use.    
Chosen Risk Response  A concise narrative of the selected response strategy (e.g., mitigate, transfer, accept, 
avoid).  
Risk Owner  The person or team responsible for managing and monitoring the risk and chosen risk 
response. This risk owner is also responsible for communicating the implications of 
their risk(s) to the ERM team.    
Status  The current condition of the risk (e.g., Open, In-Progress, Closed) and information on 
next steps.  
Figure 15 shows an example of the structure of a risk register using a risk associated with a 1839 
SCADA vulnerability.  1840

<!-- page 69 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
51 
 1841 
Fig. 15. Risk register example 1842 
In this example, the team receives an alert from the vendor indicating a vulnerability in the 1843 
SCADA server software. They have created a patch to fix the vulnerability, but it requires a 1844 
reboot. Since this server has no redundancy and cannot fail over, it cannot be rebooted while 1845 
the plant is at peak operation, as a forced outage is unacceptable. 1846 
3.2.2. Risk Response 1847 
Once a risk has been identified and incorporated into the register, the organization must decide 1848 
how to respond to it. Risk responses can be performed in many ways, including: 1849 
• Mitigate. The organization may choose to deploy a security control to mitigate that risk 1850 
or make a change to the system (e.g., a patch). For risks where the organization decides 1851 
mitigation is the best response, controls must be selected and subsequently 1852 
implemented. For more information on the selection and implementation of security 1853 
controls and other mechanisms, see Sec. 4.  1854 
• Transfer. The risk can be transferred to another business unit or organization. This can 1855 
include purchasing cybersecurity insurance or establishing contractual clauses with third 1856 
parties to define their liability for this risk.  1857 
• Accept. In many cases, OT organizations are constrained in their ability to either 1858 
mitigate or transfer risks. This is often due to the inability to modify operational systems 1859 
or to address vulnerabilities in critical components. In these cases, the organization may 1860 
decide that the risk and associated consequences are within acceptable tolerances. Risk 1861 
acceptance must be formally approved by the designated risk owner or governance 1862 
team and documented accordingly.  1863 
• Avoid. Apply responses to ensure that the risk does not occur. Avoiding a risk may be 1864 
the best option if there is not a cost-effective method for reducing the cybersecurity risk 1865 
to an acceptable level. The cost of the lost opportunity associated with such a decision 1866 
should be considered as well. 1867 
After risk response, the organization must estimate the residual risk to continually inform its 1868 
overall risk environment. A key consideration, among others, is how to keep residual risk within 1869 
the organization’s defined risk appetite and risk tolerance. 1870 
Supplemental guidance for Risk Management can be found in IR 8286. 1871

<!-- page 70 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
52 
3.2.3. OT Risk Management Life Cycle 1872 
OT risk management should be implemented as a continuous life cycle rather than as a one-1873 
time assessment or compliance exercise. In OT environments, risk decisions should account for 1874 
safety, reliability, environmental, regulatory, and mission impacts and should be revisited as 1875 
systems, threats, and operating conditions change. Building on the strategy described in Sec. 1876 
3.2, this life cycle connects the organizational context and risk management approach 1877 
established in Sec. 3.1 with the practical activities of framing risk, categorizing systems, 1878 
selecting and tracking risk responses, applying compensating controls when necessary, planning 1879 
transitions to more durable solutions, and continuously monitoring whether residual risk 1880 
remains within defined tolerances. 1881 
The OT risk management life cycle should function as an iterative process that reflects OT-1882 
specific operational consequences. It links risk framing, system categorization, risk response, 1883 
transition planning, compensating controls, and continuous monitoring in a manner that 1884 
supports safe and reliable operations. Compensating controls should be treated as temporary 1885 
measures rather than permanent substitutes for remediation. Organizations should maintain 1886 
clear visibility into these temporary conditions and tie them to funded upgrade or remediation 1887 
plans since adversaries may exploit such gaps when targeting the environment. 1888 
Risk management should be guided by the organizational context, roles, responsibilities, and 1889 
risk tolerances established in Sec. 3.1 and 3.2. These elements define the assumptions, 1890 
constraints, priorities, and risk tolerance that shape OT cybersecurity decisions. System 1891 
categorization then translates those priorities into an understanding of system criticality, 1892 
operational dependencies, and potential consequences.  1893 
Once risks are framed and systems are categorized, the organization selects an appropriate risk 1894 
response consistent with Sec. 3.2.2. Where feasible, risks should be mitigated through 1895 
engineering changes (e.g., architecture improvements, segmentation, secure configuration, 1896 
access control, monitoring, patching, replacement of vulnerable components). However, OT 1897 
environments often include legacy systems, unsupported components, proprietary protocols, 1898 
fragile integrations, and limited maintenance windows that prevent immediate remediation. In 1899 
these cases, compensating controls may be used to reduce exposure while maintaining safe and 1900 
reliable operations. 1901 
Compensating controls may not always fully address the associated risk and may need to be 1902 
treated as temporary mitigations rather than permanent substitutes for correcting the 1903 
underlying weakness. Examples include additional segmentation, restricted remote access, 1904 
enhanced logging, manual verification steps, additional jump host controls and monitoring, 1905 
application allowlisting, increased operator awareness, vendor access supervision, and out-of-1906 
band monitoring. Each compensating control should be tied to a specific risk, a residual risk 1907 
rating, an accountable owner, a review date, and a retirement condition. The risk register 1908 
described in Sec. 3.2.1 should capture this information.  1909 
Transition planning is the mechanism that prevents compensating controls from becoming risk 1910 
acceptance by default. When the preferred mitigation is not immediately feasible, the 1911 
organization should establish a funded path to a durable solution. The transition plan should 1912

<!-- page 71 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
53 
identify the target-state control or architecture, required budget, procurement dependencies, 1913 
maintenance-window requirements, engineering design work, vendor support, testing and 1914 
validation activities, implementation milestones, and accountable owner. This ties temporary 1915 
mitigation decisions to capital planning, outage planning, procurement, and life cycle 1916 
management. 1917 
The OT risk management life cycle operates as a continuous loop: frame risk in terms of mission 1918 
and operational consequences; categorize systems by criticality and physical impact; select risk 1919 
responses appropriate to OT constraints; apply compensating controls only when necessary; 1920 
establish funded transition plans to durable risk reduction; and continuously monitor whether 1921 
residual risk remains within tolerance. 1922 
3.3. Cybersecurity Supply Chain Risk Management (GV.SC) 1923 
Organizations should manage cybersecurity supply chain risks arising from products, services, 1924 
suppliers, and third parties that support OT environments. Because OT systems often depend 1925 
on specialized equipment, limited supplier options, vendor-maintained services, and remote 1926 
access by external parties, supply chain risks can directly affect the availability, integrity, and 1927 
confidentiality of OT systems and data with possible consequences ranging from operational 1928 
disruption to safety impacts. To address these risks, organizations should incorporate C-SCRM 1929 
into their broader governance, procurement, and life cycle management practices, including 1930 
identifying critical suppliers, defining required supplier security practices, and managing 1931 
supplier and product risk throughout the system life cycle. 1932 
Supply chain risks can include the insertion of counterfeits, unauthorized production, malicious 1933 
insiders, tampering, theft, the insertion of malicious software and hardware, and poor 1934 
manufacturing and development practices across the products or services acquired to support 1935 
OT needs. Whether they are malicious, natural, or unintentional, these risks have the potential 1936 
to compromise the availability and integrity of critical OT systems and components as well as 1937 
the availability, integrity, and confidentiality of the data utilized by the OT, thereby causing 1938 
harms that range from minor disruptions to impacts on life and safety. OT organizations have 1939 
key challenges with managing supply chain risks, including:  1940 
• Organizations often have sector-specific equipment requirements and depend on a 1941 
smaller number of key suppliers. Therefore, organizations may be required to decide 1942 
whether to accept or manage the risk posed by suppliers that do not meet 1943 
organizational requirements. 1944 
• Many suppliers may require remote access to the OT environment, including MSPs that 1945 
need remote access to OT networks or vendors that require access to data from their 1946 
equipment within the OT network. 1947 
• OT environments must often integrate new equipment or systems that consist of many 1948 
diverse digital devices (e.g., cranes, electric transformers, water treatment systems). 1949 
The organization must track and validate the supply chain risk of that equipment and all 1950 
associated digital components.  1951

<!-- page 72 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
54 
Identifying, assessing, and effectively responding to cybersecurity risks in supply chains is best 1952 
accomplished by incorporating C-SCRM considerations into organizational policies, plans, and 1953 
practices.  1954 
3.3.1. Identifying and Vetting Key Suppliers and Supplies 1955 
The organization must develop and maintain a process to prioritize suppliers according to their 1956 
criticality to the mission, operations, and security of its systems. This means evaluating which 1957 
suppliers, service providers, and components are most essential to maintaining safe and 1958 
reliable operations. This should include embedded components, ICS firmware, and 1959 
maintenance services.  1960 
The organization should first clearly define criteria for criticality. This may include the third 1961 
party’s role in sustaining normal operations (e.g., the extent to which they drive business 1962 
outcomes), their role in safety functions, their level of access to organizational OT networks, 1963 
and their influence on the confidentiality, integrity, or availability of systems. 1964 
Organizations should also consider whether OT is purchased directly from the original 1965 
equipment manufacturer (OEM) or an authorized third-party distributor or reseller. Suppliers 1966 
should be assessed or reviewed to ensure that they continue to follow best practices. 1967 
3.3.2. Defining Required Practices of Suppliers 1968 
Organizations should define the required processes, technical mitigations, and evidence 1969 
expected from a supplier of any OT component. This can include:  1970 
1. Criteria for secure software development and life cycle management 1971 
2. Service level agreements (SLAs) that document the supplier’s approach to the 1972 
notification and resolution of vulnerabilities 1973 
3. Defined maintenance and support agreements to determine acceptable methods for 1974 
vendor remote access (if necessary), SLAs for issue resolution and incident response (if 1975 
applicable), and obligate the third party to comply with the organization’s access control 1976 
procedures when on-site 1977 
4. Technical mechanisms regarding the hardware and software components within the 1978 
products, such as through HBOMs and SBOMs 1979 
5. Digital artifacts to validate the authenticity of vendor-provided OT hardware, software, 1980 
and firmware, such as digital signatures 1981 
6. Clear incentive structures in supplier contracts to encourage and reward strong security 1982 
practices 1983

<!-- page 73 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
55 
3.3.3. Identifying and Managing Supply Chain Risk Across Product Life Cycles 1984 
Organizations must manage supply chain risks across the product life cycle. This should include 1985 
documented processes to validate the authenticity and integrity of products, control supplier 1986 
access, and assess supplier and product risks. Using these processes, organizations should vet 1987 
suppliers and service providers to ascertain their capabilities, trustworthiness, the adequacy of 1988 
their internal security practices, the effectiveness of their safeguards, their supply chain 1989 
relationships, and any risks that may be associated with those relationships and dependencies.  1990 
Examples of key checks that the organization should validate include:  1991 
• Whether the products include any unauthorized components, software, suppliers, or 1992 
regions for all acquisitions 1993 
• Remote access and on-site management requirements and mechanisms to audit and 1994 
control access 1995 
• The existence of unauthorized communication devices (e.g., cellular modems) 1996 
Additionally, special consideration should be given to how difficult it may be to obtain original 1997 
replacement parts or updates over the life of the product and how diverse the sources of 1998 
supply are and may be in the future. 1999 
Supplemental guidance for supply chain risk management can be found in the following 2000 
documents: 2001 
• SP 800-161r1, Cybersecurity Supply Chain Risk Management Practices for Systems and 2002 
Organizations 2003 
• IR 8276, Key Practices in Cyber Supply Chain Risk Management: Observations from 2004 
Industry 2005 
• CISA Software Acquisition Guide Fact Sheet 2006 
• CISA Software Bill of Materials (SBOM) 2007 
• CISA A Hardware Bill of Materials Framework for Supply Chain Risk Management Fact 2008 
Sheet 2009 
3.4. OT Security Policy and Oversight (GV.PO) 2010 
Organizational leadership should develop and disseminate policies that establish security 2011 
requirements for their environments. These policies may include the identification and 2012 
assignment of roles, responsibilities, management commitment, and compliance. The policies 2013 
may also reflect coordination among the organizational entities responsible for the different 2014 
aspects of security (e.g., technical, physical, personnel, cyber-physical, access control, media 2015 
protection, vulnerability management, maintenance, monitoring). 2016 
Where possible, OT-specific security policies and procedures should be compatible and 2017 
coordinated with other groups and existing policies and procedures throughout the 2018 
organization. This includes coordination with IT management, human resources, and 2019

<!-- page 74 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
56 
organizational governance teams. Examples of where policy coordination is necessary across 2020 
groups include:  2021 
• IT: When IT infrastructure is used to provide user access to OT infrastructure or protect 2022 
OT data along with processes to investigate and respond to security incidents that 2023 
potentially span both OT and IT networks 2024 
• Human resources: The investigation or remediation of security issues regarding 2025 
organizational personnel 2026 
• Organization governance: The incorporation of necessary regulatory requirements, 2027 
decision authorities, and reporting to facilitate awareness 2028 
The development of cybersecurity policies should be based on a risk assessment that will set 2029 
the security priorities and goals for the organization. Procedures that support the policies 2030 
should be developed so that the policies are implemented fully and properly for OT. 2031 
Cybersecurity procedures should also be documented, tested, and updated periodically in 2032 
response to changes in policy, technology, and threats. 2033 
Supplemental guidance for cybersecurity policy can be found in the following documents: 2034 
• SP 800-39, Managing Information Security Risk: Organization, Mission, and Information 2035 
System View 2036 
• SP 800-37r2, Risk Management Framework for Information Systems and Organizations: 2037 
A System Life Cycle Approach for Security and Privacy 2038 
• SP 800-100, Information Security Handbook: A Guide for Managers 2039 
• IR 8286r1, Integrating Cybersecurity and Enterprise Risk Management (ERM) 2040 
• IR 8183Av2, Cybersecurity Framework Manufacturing Profile Low Impact Level Example 2041 
Implementations Guide 2042 
3.4.1. Program Performance Measurement 2043 
The OT cybersecurity program should be continually observed to determine its overall 2044 
effectiveness. This may include evaluating the current charter and related policies to determine 2045 
whether they remain the most appropriate components.  2046 
The organization should define both key performance indicators (KPIs) and key risk indicators 2047 
(KRIs), analyzing them over time to gauge the program’s performance and the organization’s 2048 
risk posture. While KPIs are quantitative measures of the program’s operational efficiency, KRIs 2049 
may result from shortcomings in the governance program. 2050 
Examples of KPIs include: 2051 
• Percentage of OT assets with applied system hardening 2052 
• Mean time to detect incidents (MTTD) 2053 
• Mean time to respond to incidents (MTTR) 2054

<!-- page 75 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
57 
• Percentage of security policies reviewed and reapproved in the past 12 months 2055 
• Personnel security awareness training completion rate 2056 
• Percentage of personnel who reported phishing simulations 2057 
Examples of KRIs include: 2058 
• Percentage of production assets deemed end-of-service (EOS) or end-of-life (EOL) by 2059 
vendors 2060 
• Percentage of personnel who have not completed security awareness training 2061 
• Percentage of personnel who failed phishing simulations 2062 
• Number of open, critical vulnerabilities yet to be remediated 2063 
The organization should define KPI targets and KRI thresholds to better manage the program 2064 
throughout its life cycle. While a KPI target is a numerical value that the organization hopes to 2065 
meet or exceed (e.g., 90 % of OT assets are hardened), a KRI threshold is an expression of the 2066 
maximum numerical value before risk is deemed unacceptable (e.g., no more than 5 % of staff 2067 
should have missed or failed their security awareness training). 2068 
3.4.2. Organizational Oversight 2069 
Organizations must establish oversight capabilities and teams to monitor risk management 2070 
activities and make necessary decisions, investments, and strategies. These teams should help 2071 
review key artifacts and indicators from the risk management process, including incidents, 2072 
vulnerabilities, audit findings, and assessments to track the status of the security program.  2073 
An organization-wide risk management strategy is foundational to developing an OT 2074 
cybersecurity strategy.5 The OT cybersecurity strategy leverages the organization-wide risk 2075 
management strategy — including organization-defined risk tolerance, threats, assumptions, 2076 
constraints, priorities, and trade-offs — to further tailor the strategy to apply to the OT 2077 
cybersecurity program. By consciously choosing to develop and implement a cybersecurity 2078 
strategy, an organization establishes a disciplined approach that considers all aspects of the 2079 
system life cycle, from procurement to decommissioning, with cybersecurity in mind. As a 2080 
result, the organization can ensure that cybersecurity goals are realized in its systems. The 2081 
adoption of a cybersecurity strategy can result in a more systematic implementation of risk 2082 
decisions into system development and operation. Decisions on cybersecurity strategy should 2083 
flow from a high-level understanding of the organization’s operations, objectives, and 2084 
cybersecurity goals. A comprehensive and accepted cybersecurity strategy can assist an 2085 
organization with consistently maintaining acceptable risk management throughout the life 2086 
cycle of an OT system. 2087 
The OT cybersecurity strategy should: 2088 
 
5 For additional information on developing an organization-wide risk management strategy, refer to [SP800-37r2], Prepare Step, Task P-2, Risk 
Management Strategy. Section 3 provides additional information on organization-level and system-level tasks to prepare for implementing the 
NIST RMF.

<!-- page 76 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
58 
• Refine the OT operation’s organizational risk tolerance, which drives the OT 2089 
cybersecurity operation’s priorities 2090 
• Refine and supplement guidance from the organization-wide risk management strategy 2091 
to address OT-specific constraints and requirements 2092 
• Identify the OT cybersecurity team and personnel and the associated OT-specific 2093 
cybersecurity training and awareness necessary 2094 
• Address the OT cybersecurity operation model (e.g., insource, outsource, use managed 2095 
security services) 2096 
• Outline the appropriate cybersecurity architecture for the various OT sites within the OT 2097 
program. 2098 
• Address both IT and OT concerns and requirements; while IT may prioritize data loss or 2099 
system availability, OT may prioritize system safety, production efficiency, and 2100 
environmental protection 2101 
• Incorporate critical infrastructure standards and regulatory requirements, which are 2102 
typically designed to protect critical cyber assets to support reliability and may carry 2103 
additional legal obligations for the organization 2104 
• State the need for sound cybersecurity practices, such as patching or monitoring 2105 
The strategy should provide guidance on how the organization will make key cybersecurity 2106 
decisions, including: 2107 
• Architectural decisions informed by a cybersecurity to increase the likelihood that high-2108 
level cybersecurity goals will be reflected in the cybersecurity of individual systems, 2109 
including the approach to securing integration with other networks and systems (e.g., 2110 
business networks, cloud, IIoT technologies)  2111 
• The management of OT systems across the life cycle, including the approach to 2112 
addressing products that pass end-of-life status or have identified cybersecurity or 2113 
supply chain concerns 2114 
• The required approval, evaluation, or restrictions necessary to inform the adoption and 2115 
use of new technologies (e.g., crypto agility, artificial intelligence [AI], and machine 2116 
learning [ML] technologies, digital twins)  2117 
• Data governance issues, especially those associated with data hosted on IT 2118 
environments, and any third parties (e.g., contractors, integrators)  2119 
Supplemental guidance for establishing an OT cybersecurity strategy can be found in IR 8183A, 2120 
Cybersecurity Framework Manufacturing Profile Low Impact Level Example Implementations 2121 
Guide. 2122 
  2123

<!-- page 77 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
59 
3.5. OT Cybersecurity Awareness and Training (PR.AT) 2124 
This section addresses governance and workforce considerations for OT cybersecurity 2125 
awareness and training with a particular focus on preparing personnel to carry out their 2126 
security-related responsibilities in OT environments. Because human actions can directly affect 2127 
the safety, reliability, and security of OT systems, organizations should incorporate 2128 
cybersecurity into personnel security practices, access management processes, and role-based 2129 
training programs. This includes coordinating with human resources, IT, physical security, and 2130 
OT leadership to ensure that personnel in critical roles are appropriately screened, trained, and 2131 
authorized and that they maintain the knowledge needed to recognize and respond to 2132 
cybersecurity issues relevant to their job functions.  2133 
A general personnel security program should address policy, position risk designations, 2134 
personnel screening, terminations, transfers, access agreements, and third-party roles and 2135 
responsibilities. OT personnel should communicate with human resources, IT, and physical 2136 
security to ensure that personnel security requirements are being met. Cybersecurity should 2137 
also be included in human resources practices to reduce the risk of human error, theft, fraud, or 2138 
other intentional or unintentional misuse of information systems. 2139 
Organizations should consider establishing an access agreement and request form to manage 2140 
physical and/or logical access to OT equipment. Organizations should also screen the personnel 2141 
assigned to critical positions who control and maintain the OT. Additionally, each employee 2142 
should receive training that is relevant to and necessary for their job functions. Organizations 2143 
should require personnel to demonstrate competence in their job functions to retain physical 2144 
and logical access to OT. Organizations should consider adopting a framework, such as the 2145 
National Initiative for Cybersecurity Education (NICE) Framework, for training their OT 2146 
personnel. 2147 
Supplemental guidance on personnel security controls can be found in the following 2148 
documents: 2149 
• SP 800-35, Guide to Information Technology Security Services 2150 
• SP 800-73-4, Interfaces for Personal Identity Verification 2151 
• SP 800-76-2, Biometric Specifications for Personal Identity Verification 2152 
• SP 800-100, Information Security Handbook: A Guide for Managers 2153 
 2154

<!-- page 78 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
60 
4. OT Cybersecurity Outcomes and Objectives (CSF 2.0 – ID, PR, DE, RS, RC) 2155 
4.1. Identify (ID) 2156 
This section discusses the unique opportunities and challenges of identifying assets and risks 2157 
within an OT environment. It will first explore the asset management category, which is critical 2158 
to ensuring that an organization broadly understands its assets and their functions. It will then 2159 
discuss the risk assessment process to understand the resulting risks in the OT environment. 2160 
4.1.1. Asset Management (ID.AM) 2161 
Asset management depends on understanding individual assets, their architecture, data flows, 2162 
and associated operational functions. Accurate inventory information supports multiple risk 2163 
management objectives, including risk assessment, vulnerability management, and 2164 
obsolescence tracking. Asset inventories are also critical to supporting other security functions, 2165 
including detection and response/recovery.  2166 
This section will explore key challenges and recommendations for establishing an asset 2167 
inventory. While asset management also encompasses the security configuration and 2168 
maintenance associated with assets, the discussion of these topics is included in Sec. 4.2.3. 2169 
4.1.1.1. Establishing an Asset Inventory 2170 
An accurate asset inventory is the foundation of an asset management program. Organizations 2171 
need to maintain a process to identify all of their assets and understand key information and 2172 
configurations for those assets, their communication needs, functions, and their criticality to 2173 
the overall process. Organizations should consider including the following to support their asset 2174 
management capability:  2175 
• Unique identifiers to differentiate and track assets.  2176 
• Hardware inventory management to track computing and network devices within the 2177 
environment, including device details and location. Device details may include vendor, 2178 
model, serial number, purchase information, and manufacturing/build information (e.g., 2179 
provenance information).  2180 
• Software and firmware inventory management to track the software and firmware 2181 
installed with the OT components, including version numbers, location information, and 2182 
software bill of materials (SBOM).  2183 
• Vendor information to establish a repository of vendor information, points of contact, 2184 
warranty information, locations of recall, end-of-life dates, and update information. 2185 
• Documented roles and responsibilities to identify specific individuals, teams, or 2186 
organizational groups who represent the asset owner and those with operational, 2187 
maintenance, and cybersecurity roles and responsibilities. 2188

<!-- page 79 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
61 
Additionally, updating inventory information when components are added, removed, or 2189 
changed (e.g., patched, new firmware installed, component swapped during maintenance) 2190 
helps organizations accurately manage their overall environmental risks. Establishing an asset 2191 
inventory typically depends on a combination of automated tools that continually discover 2192 
changes in the environment along with manual processes to validate the completeness and 2193 
accuracy of the collected data. Various tools are available to support automated discovery and 2194 
the collection of asset data. While automated tools provide many benefits for maintaining an 2195 
updated inventory, organizations should consider how the tool collects information and 2196 
whether the collection method (e.g., active scanning) may negatively impact their OT systems.  2197 
While each approach has some benefits, there are also challenges associated with each, such 2198 
as:  2199 
• Vendor management tools. Many vendors provide engineering tools to discover devices 2200 
and manage configurations. These often use vendor-provided dedicated network 2201 
services and are usually designed primarily for operational functionality rather than 2202 
security. Vendor management tools may have access to very detailed information about 2203 
devices (e.g., configurations, model and serial numbers, firmware versions), which feed 2204 
directly into an asset inventory. One drawback is that these tools typically work with a 2205 
single vendor’s product line and cannot read information from other vendors’ products. 2206 
The asset owner must then maintain multiple vendor tools if they want to incorporate 2207 
all of the information into an inventory, and there is no guarantee that each tool will 2208 
consistently provide that information. 2209 
• Passive network monitoring. Passive network monitoring tools are often designed to 2210 
monitor networks for cybersecurity threats. As part of this process, they also provide 2211 
the ability to identify assets based on passively monitoring and analyzing network traffic 2212 
to discern identifying information about devices. As these tools listen to more network 2213 
traffic, they build a broader and more extensive database of assets and network data 2214 
flows. These tools can be valuable for identifying all devices communicating on the 2215 
network, not just the ones that are known. However, the tools are highly dependent on 2216 
the placement of the listening sensors. Unlike typical IT designs, it is not uncommon for 2217 
large amounts of communication in an OT network to be isolated to a single switch 2218 
buried within the architecture, where a listening sensor would not detect them. Asset 2219 
owners need to evaluate their network architecture to determine the optimal 2220 
placement of listening sensors to avoid gaps. 2221 
• OT-aware network scanning. Some network scanning tools, whether specifically 2222 
designed for asset management or security monitoring, can interrogate devices for 2223 
identifying information using native OT protocols. These tools act in similar ways to 2224 
vendor management tools by using the native capabilities of the OT devices to report 2225 
configuration information, model and serial numbers, or firmware versions. These tools 2226 
may be able to gather information from multi-vendor, multi-protocol environments, 2227 
potentially reducing the number of tools that an asset owner needs to manage. Asset 2228 
owners may want to consult with their vendors and should perform testing before 2229 
implementing them in the production environment. 2230

<!-- page 80 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
62 
• Inde pendent active network scanning . These tools establish network connections to 2231  
v
arious services on network devices to identify device profiles without using the native 2232
 
O
T protocols. They perform more independent, extensive scans of devices to 2233
 
in
terrogate all available resources, sometimes requiring credentials to fully collect the 2234
 
in
formation. These types of tools may be designed more for compliance or vulnerability 2235
 
man
agement rather than just asset management. These independent active-scanning 2236
 
to
ols can often provide a more comprehensive view of devices by revealing both 2237
 
publ
ished and unpublished information. However, active scanning tools can also 2238
 
n
egatively impact device availability and functionality, potentially leading to unwanted 2239
 
o
perations. It may be possible to configure these types of scanners to limit their 2240
 
po
tential to overload the resources of OT devices. Asset owners may want to consult 2241
 
w
ith their vendors, assess the scope of networks and systems in which these tools are 2242
 
us
ed, and test them before implementing them in the production environment. 2243
 
• Software agents. Many asset management tools that are common in the IT 2244 
environment operate using software agents installed on devices. While these can 2245 
provide broad visibility into a device’s software and configuration, they are not typically 2246 
deployed across the OT environment for various reasons. First, many devices in the OT 2247 
environment (e.g., PLCs, sensors, other embedded devices) do not run common OSs 2248 
that are capable of supporting these software agents. Next, if devices do run common 2249 
OSs, there may be contractual or warranty-related reasons for why vendors may not 2250 
permit these agents from being installed (e.g., incompatibilities, operational impacts). 2251 
When considering a software agent to collect asset information, asset owners should 2252 
consult with the appropriate vendors prior to installation and test their implementation 2253 
to understand the potential risks. 2254 
The appropriate discovery method for a given asset is often determined by the equipment’s age 2255 
and capabilities. Modern devices with sufficient processing resources, and network connectivity 2256 
can generally tolerate more active forms of discovery. Older or more resource-constrained 2257 
devices may not tolerate active interrogation and are better-suited to passive monitoring, 2258 
which collects information without sending traffic to the device. Legacy or isolated devices that 2259 
lack network connectivity or cannot be reached by automated tools require manual processes 2260 
(e.g., physical inspection, direct console access) to capture accurate inventory information. 2261 
Organizations should evaluate the age and capabilities of their assets when selecting discovery 2262 
methods and should not apply a single approach uniformly across environments with a mix of 2263 
modern and legacy equipment. 2264 
The deployment of asset management infrastructure must also incorporate network 2265 
architecture challenges. Tools that perform active network scanning must have routable 2266 
connections to all deployed devices. Passive monitoring tools must have access to switch SPAN 2267 
or TAP ports that provide access. Software agents must deal with the configuration 2268  
management of deployed agents across the devices in which they are installed. Further, asset 2269 
management tools typically require server infrastructure to aggregate data from various 2270 
remote monitoring tools and agents.  2271

<!-- page 81 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
63 
Organizations may face multiple challenges in establishing an asset inventory, especially when 2272 
adopting and integrating automated tools. For example:   2273 
• Many OT environments contain isolated systems, components, or systems that are 2274 
connected on non-IP networks and cannot be remotely accessed to support the 2275 
discovery or management of assets.  2276 
• The use of incompatible or untested automated asset discovery and management tools 2277 
can negatively impact OT operations.  2278 
Asset owners may also want to consider how automated scanning activities could impact the 2279 
OT system by testing automation tools in a non-production environment. Based on testing 2280 
results, asset owners should consider utilizing automated OT network architecture 2281 
documentation tools during planned downtime. Performing tests using automated asset 2282 
management tools on offline systems or components is recommended before deployment into 2283 
the OT production environment. When automated tools are not feasible due to network 2284 
architecture or other OT environment issues, the organization should consider manual 2285 
processes to maintain a current inventory. 2286 
While automated tools are useful for building inventory, they may not be able to discover or 2287 
collect relevant data from all assets. Therefore, organizations should consider physically 2288 
inspecting OT network connections or analyzing network logs to document the OT network 2289 
architecture.  2290 
Supplemental guidance for ID.AM can be found in the following documents:  2291 
• SP 1800-5, IT Asset Management  2292 
• SP 800-53r5, Security and Privacy Controls for Information Systems and Organizations  2293 
4.1.1.2. Establishing Asset Criticality and Function 2294 
Asset inventories should also include information on the organization or individual responsible 2295 
for managing the device, the device’s operational criticality, and any regulatory oversight of 2296 
that asset. This information is critical to ensuring that the asset is adequately protected and 2297 
that any decisions associated with it involve the correct groups and are documented 2298 
appropriately. Information about the device’s criticality can include the key safety functions 2299 
supported as well as its role in maintaining key operations. This information can be obtained 2300 
from the results of risk assessment processes (ID.RA) and broader decisions on the governance 2301 
context (GV.OC). 2302 
4.1.2. Architectures and Baselines 2303 
A comprehensive understanding and baseline of the data flows associated with the assets is 2304 
critical for the successful deployment of cybersecurity controls. This information is also 2305 
important for other security functions, including network monitoring and incident response. 2306

<!-- page 82 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
64 
To establish a baseline, organizations should begin by understanding which devices a specific 2307 
asset communicates with; which addresses, ports, and protocols it uses; and the functional 2308 
purpose of the communication. This information should be documented within a broad 2309 
network diagram to ensure that it can be broadly shared and communicated with individuals 2310 
across the organization. While establishing baselines for all devices across an organization may 2311 
not be feasible, organizations should prioritize focusing on critical assets, network segments, 2312 
and areas in which communications cross key boundaries, such as connectivity with the DMZ, 2313 
internet, and external parties.  2314 
Numerous tools can support the development of an architecture document, including tools to 2315 
perform asset discovery and management (Sec. 4.1.1) and network detection tools (Sec. 2316 
4.3.1.4). These tools can help an organization identify, document, and diagram the 2317 
interconnections between devices, enterprise networks, and other external connections.  2318 
Organizations should pay particular attention to cloud conduits when documenting their 2319 
architecture. Cloud conduits are connections between OT systems and cloud-based services or 2320 
platforms that may bypass traditional network boundaries and introduce exposure that is not 2321 
immediately visible in standard network diagrams. These connections should be explicitly 2322 
identified, documented, and assessed as part of the baseline process. 2323 
Organizations should also treat the discovery of unknown assets and undocumented 2324 
connections as a core objective of the architecture and baseline process. Unauthorized or 2325 
undocumented devices and connections, sometimes referred to as Shadow IT/OT, can 2326 
introduce unmanaged risks into the OT environment. Any device or connection that cannot be 2327 
attributed to a known, authorized function should be investigated and either formally 2328 
documented or removed. 2329 
4.1.3. System-Level Risk and Vulnerability Assessment (ID.RA) 2330 
Cybersecurity risk assessments are performed to identify risks and estimate the magnitude of 2331 
harm to operations, assets, or individuals that might result from cyber incidents, such as 2332 
unauthorized access, use, disclosure, disruption, modification, or destruction of an information 2333 
system or data. Risk assessments require understanding the impacts (i.e., consequences) and 2334 
methods (e.g., threats and vulnerabilities) that cause them. Risk assessments leverage the risk 2335 
management strategy (e.g., acceptable risk assessment methodologies, risk tolerance) and 2336 
facilitate efforts to identify, estimate, and prioritize risks to operations, assets, individuals, and 2337 
other organizations.  2338 
Risk assessments help organizations understand how cybersecurity events could affect safety, 2339 
reliability, and operations so that resources (e.g., people, money, technology) can be applied in 2340 
a manner that reduces the most significant risks. Results from a risk assessment can be used to 2341 
generate scenarios that inform decisions around controls, system design, maintenance, incident 2342 
response, tabletop exercises, vendor management, and data collection management strategies. 2343 
It also helps in identifying critical assets, functions, dependencies, and cascading impacts.  2344 
The objective of a risk assessment is to determine how a cybersecurity event could affect the 2345 
organization’s ability to accomplish its mission safely and reliably. This includes the loss of view 2346

<!-- page 83 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
65 
and/or control, which can lead to an inability to produce products, a degradation of product 2347 
quality, damage to equipment, environmental damage, or a health and safety incident. 2348 
Organizations may need to evaluate the potential physical impacts across all parts of an OT 2349 
system. Organizations may also need to determine how OT systems interact with or depend on 2350 
IT to support risk decisions. These processes may require organizations to identify a common 2351 
framework for evaluating impacts that incorporates OT considerations. One approach is based 2352 
on NIST Federal Information Processing Standards (FIPS) publication 199 [FIPS199], which 2353 
specifies that systems are categorized as low impact, moderate impact, or high impact for the 2354 
security objectives of confidentiality, integrity, and availability. Another approach based on ISA 2355 
62443-3-2 [ISA62443] provides example definitions for determining system categorization 2356 
based on OT impacts. 2357 
Risk assessments are typically point-in-time reports. As a result, organizations should ensure 2358 
that they are up to date and that their security levels remain adequate.  2359 
Supplemental guidance for risk assessments can be found in the following documents:  2360 
• SP 800-30r1, Guide for Conducting Risk Assessments  2361 
• SP 800-37r2, Risk Management Framework for Information Systems and Organizations: 2362 
A System Life Cycle Approach for Security and Privacy 2363 
• SP 800-39, Managing Information Security Risk: Organization, Mission, and Information 2364 
System View  2365 
• CISA Risk Assessments Resources  2366 
• ISA/IEC 62443-3-2, Security for industrial automation and control systems, Part 3-2: 2367 
Security risk assessment for design 2368 
• ISA Global Cybersecurity Alliance, Leveraging ISA 62443-3-2 For IACS Risk Assessment 2369 
and Risk Related Strategies 2370 
4.1.3.1. Understanding OT Impacts 2371 
In OT environments, impacts may relate to safety, health, and the environment as well as 2372 
business and financial impacts. Organizations should use existing analyses (e.g., PHA, FMEA) or 2373 
past events (e.g., power outages, control failures, upstream feed disruptions, downstream 2374 
capacity issues, major equipment failures) to understand the potential impacts of a cyber 2375 
incident. 2376 
One major concern for OT system operators is the availability of services provided by the OT 2377 
system. The OT system may be part of critical infrastructure (e.g., water or power systems), 2378 
where continuous, reliable operations are essential. As a result, OT systems may have strict 2379 
requirements for availability or recovery. Organizations should understand and plan for the 2380 
levels of redundancy required to achieve the desired resilience for their operating 2381 
e
nvironments and incorporate these requirements into their risk framing. This will help 2382 
organizations make risk decisions that avoid unintended consequences for those who depend 2383

<!-- page 84 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
66 
on their services. More specifically, organizations should consider identifying interdependent 2384 
OT systems that pose cybersecurity risks that threaten system availability.  2385 
OT systems often rely on supporting services that reside in the enterprise network (e.g., billing, 2386 
maintenance), remote access solutions (internal and third-party), identity infrastructure, time 2387 
synchronization, and backup infrastructure or cloud-based services, which may introduce risk. 2388 
Organizations should identify both logical and physical dependencies and evaluate failures and 2389 
the impacts they can have across those relationships.  2390 
The impact of a cyber incident in an OT environment may include both physical and digital 2391 
effects that risk assessments need to incorporate, including:  2392 
• Impacts on safety and the use of safety assessments 2393 
• Physical impacts of a cyber incident on an OT, including the larger physical environment 2394 
and the effect on the process being controlled 2395 
• The consequences for risk assessments of non-digital control components within an OT 2396 
Risk assessments also require reviewing the digital and non-digital mechanisms that are 2397 
implemented to minimize adverse event impacts. OT systems often incorporate non-digital 2398 
mechanisms to provide fault tolerance and prevent OT systems from operating outside 2399 
acceptable parameters. These non-digital mechanisms may help mitigate the negative impacts 2400 
of a digital incident in the OT and should be incorporated into the risk assessment process. For 2401 
example, OT often has non-digital control mechanisms that can prevent it from operating 2402 
outside of a safe boundary and thereby limit the impact of an attack (e.g., a mechanical relief 2403 
pressure valve). Analog mechanisms (e.g., meters, alarms) can also be used to observe the 2404 
physical system state and provide operators with reliable data if digital readings are unavailable 2405 
or corrupted. Table 5 categorizes non-digital control mechanisms that could reduce the impact 2406 
of an OT incident. 2407 
Table 5. Categories of non-digital OT control components 2408 
Control Type Description 
Analog 
displays 
or alarms 
 
Non-digital mechanisms measure and display the state of the physical system (e.g.,  
temperature, pressure, voltage, current) and can provide the operator with accurate  
information when digital displays are unavailable or corrupted. The information may be  
provided to the operator on some non-digital display (e.g., thermometers, pressure gauges) 
and through audible alarms. 
Manual 
control 
mechanisms 
 
Manual control mechanisms (e.g., manual valve controls, physical breaker switches) allow  
operators to manually control an actuator without relying on the digital OT system. This  
ensures that an actuator can be controlled even if the OT system is unavailable or  
compromised. 
Analog 
control 
systems 
 
Analog control systems use non-digital sensors and actuators to monitor and control a physical 
process. These may prevent the physical process from entering an undesired state  when the 
digital OT system is unavailable or corrupted. Analog controls include devices , such as 
regulators, governors, and electromechanical relays. An example is a device that is  designed to 
open during emergency or abnormal conditions to prevent the rise of internal  fluid pressure in 
excess of a specified value, thus bringing the process to a safer state. The device may also be 
designed to prevent an excessive internal vacuum, such as a pressure  relief valve, a non-
reclosing pressure relief device (e.g., rupture disc), or a vacuum relief valve.

<!-- page 85 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
67 
Additionally, organizations should consider how an incident could propagate to connected 2409 
systems and their components. An OT system may be interconnected with other systems so 2410 
that failures in one system or process can easily cascade to other systems, both within and 2411 
outside the organization. Impact propagation could occur due to both physical and logical 2412 
dependencies. Properly communicating the results of risk assessments to the operators of 2413 
connected or interdependent systems and processes is one way to manage such impacts.  2414 
4.1.3.2. Threat Characterizations 2415 
There are three factors for a threat to be applicable: capability, intent, and vulnerability. 2416 
Capability and intent information can be obtained from OSINT and external intelligence-sharing 2417 
sources (e.g., Information Sharing and Analysis Centers [ISACs], threat feeds). Organizations 2418 
should consider participating in cyber threat information sharing [SP800-150]. Threats can be 2419 
external (e.g., APTs) or internal (i.e., insiders). 2420 
Organizations may want to consider incorporating resources (e.g., the MITRE ATT&CK for 2421 
Industrial Control Systems [ICS] framework [ATTACK-ICS]) into their processes for assessing risks 2422 
to the mission and OT systems. ATT&CK for ICS categorizes adversarial tactics, techniques, and 2423 
procedures (TTPs) that have been used to target ICS environments across real-world threat 2424 
events. It provides a strong understanding of how threat actors are currently targeting OT 2425 
environments, which is critical to ensuring that the organization’s risk management processes 2426 
adequately incorporate realistic threat behavior. 2427 
Supplemental guidance for threat characterization can be found in the following documents:  2428 
• MITRE ATT&CK for ICS 2429 
• National Council of ISACs 2430 
4.1.3.3. Assessing Vulnerabilities 2431 
A key part of risk assessment is the identification of vulnerabilities and associated predisposing 2432 
conditions within the OT environment. A list of common vulnerabilities and predisposing 2433 
conditions is defined in Appendix C. While vulnerabilities are often associated with the products 2434 
and services used by the organization, others depend on the device’s unique architecture or 2435 
implementation details.  2436 
Understanding vulnerabilities associated with vendor products and services depends on an 2437 
accurate inventory of IT and OT assets within the operating environment, including the vendor, 2438 
model numbers, firmware, OSs, and software versions installed on the assets. This inventory 2439 
facilitates the identification, tracking, and remediation of vulnerabilities. OT-specific 2440 
vulnerability information is available through multiple methods, including:  2441 
• Using OT-specific tools to automate asset inventory creation, cross-correlation of the 2442 
inventory with known vulnerabilities and threats, and regular updates 2443 
• Monitoring security groups, associations, and vendors for security alerts and advisories  2444

<!-- page 86 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
68 
• Reviewing the NIST National Vulnerability Database (NVD) and CISA Known Exploited 2445 
Vulnerabilities (KEV) Catalog for detailed information on known vulnerabilities for 2446 
hardware and software assets 2447 
In addition to understanding the vulnerabilities across products and services, organizations 2448 
must also examine their architectures, deployed security controls, configurations, and any 2449 
custom infrastructure that may introduce additional vulnerabilities. While organizations often 2450 
execute vulnerability assessments in their environments, these can be problematic in OT 2451 
environments. Specifically, both vulnerability scanning tools and vulnerability assessment 2452 
methods can potentially disrupt systems. Therefore, organizations should use caution when 2453 
performing this assessment on production systems. They may instead want to test in 2454 
representative lab environments. 2455 
Vulnerabilities can be identified through a combination of automated and manual techniques. 2456 
These vulnerability scans should be performed on an ongoing basis to capture newly discovered 2457 
vulnerabilities. Some common ways to achieve vulnerability identification in the OT 2458 
environment are:  2459 
• Continuous monitoring using passive or active scanning capabilities. Organizations 2460 
should consider how vulnerability scanning tools may affect OT components and 2461 
communications by testing them in an offline environment before implementing them 2462 
in production. 2463 
o Passive scanning tools typically use network traffic analyzers to detect assets and 2464 
identify potential vulnerabilities affecting them.  2465 
o Active scanning tools typically use an agent to connect to networked assets and 2466 
perform detailed queries and analyses of components to identify possible 2467 
vulnerabilities affecting the assets.  2468 
• Performance testing, load testing, and penetration testing if the test will not adversely 2469 
impact the production environment.  2470 
• Regular audits, assessments, and peer reviews to identify gaps in security.  2471 
4.1.3.4. Evaluating Risk 2472 
As discussed in Sec. 3, the organization needs to define risk tolerances and add findings to the 2473 
risk register. For risks that exceed the organization’s tolerance, implemented remediations or 2474 
mitigations should align with Sec. 4.2 Protect (PR), Sec. 4.3 Detect (DE), Sec. 4.4 Respond (RS), 2475 
and Sec. 4.5 Recover (RC). 2476 
To support the risk assessment process, organizations should also define how the likelihood of 2477 
occurrence for cybersecurity events will be determined to maintain consistency when assessing 2478 
risks. [SP800-30r1] provides guidelines on developing likelihood-weighted risk factors. 2479 
Organizations should consider weighting risk factors based on an analysis of the probability that 2480 
a given threat is capable of exploiting a given vulnerability (or set of vulnerabilities), that the 2481 
threat event will be initiated, and that the threat event will result in adverse impacts. 2482

<!-- page 87 -->

NIST SP 800-82r4 ipd (Initial Public Draft) Guide to OT Security 
September 2026 
69 
For adversarial threats, the likelihood of occurrence is typically assessed based on the 2483 
adversary’s intent, capability, and targeting. For other-than-adversarial threat events, the 2484 
likelihood of occurrence is estimated using historical evidence, empirical data, and other 2485 
factors. If organizations find that their historical data is minimal, they may want to extend their 2486 
analysis to include industry-specific data on cybersecurity events reported by similar 2487 
organizations. 2488 
The likelihood of threat occurrence can also be based on the state of the organization (e.g., its 2489 
core mission and business processes, enterprise architecture, information security architecture, 2490 
information systems, the environments in which those systems operate) and consider 2491 
predisposing conditions and the presence and effectiveness of deployed security controls to 2492 
protect against unauthorized or undesirable behavior, detect and limit damage, and/or other 2493 
resiliency factors for the OT capabilities. 2494 
Organizations that establish definitions for event likelihood may want to review Appendix G of 2495 
SP 800-30r1 for more detailed guidance and suggestions. Based on this guidance, organizations 2496 
should consider defining five levels of likelihood, from Very Low to Very High, for both 2497 
adversarial (i.e., intentional threat actors) and non-adversarial (e.g., errors, accidents, acts of 2498 
nature) events. Additionally, organizations may want to establish definitions for the likelihood 2499 
that an event may result in an adverse impact. Using these two factors, organizations can 2500 
establish a heat map like the one shown in Table 6 to determine the likelihood of supporting 2501 
the risk analysis. 2502 
Table 6. Event likelihood evaluation 2503 
Likelihood of 
Threat Event 
Initiation or 
Occurrence 
Likelihood That Threat Events Result in Adverse Impacts 
Very Low Low Moderate High Very High 
Very High Low Moderate High Very High Very High 
High Low Moderate Moderate High Very High 
Moderate Low Low Moderate Moderate High 
Low Very Low Low Low Moderate Moderate 
Very Low Very Low Very Low Low Low Low 
4.2. Protect (PR) 2504 
Within OT environments, the primary objective of the CSF 2.0 PROTECT (PR) function is to 2505 
develop, implement, and sustain appropriate safeguards to manage the organization’s 2506 
cybersecurity risk without compromising the safety, reliability, or availability of continuous 2507 
physical processes. Achieving this requires organizations to carefully tailor and apply four core 2508 
control families: identity, authentication, and access control (PR.AA); data security (PR.DS); 2509 
platform security (PR.PS); and technology infrastructure resilience (PR.IR). This section provides 2510 
specific guidelines on implementing these control objectives and addressing the unique 2511

<!-- page 88 -->

NIST SP 800-82r4 ipd (Initial Public Draft) Guide to OT Security 
September 2026 
70 
operational constraints, legacy system limitations, and safety imperatives inherent to OT 2512 
environments.6 2513 
4.2.1. Identity, Authentication, and Access Control (PR.AA) 2514 
The CSF 2.0 Identity Management, Authentication, and Access Control (PR.AA) controls ensure 2515 
that access to physical and logical assets is strictly limited to authorized users, services, and 2516 
hardware and is managed commensurate with the assessed risk of unauthorized access. 2517 
Establishing a robust access control architecture in an operational environment is a multi-step 2518 
process that encompasses the full life cycle of an identity. It begins with foundational identity 2519 
and access management (IAM) to administer accounts and assign permissions, followed by the 2520 
deployment of appropriate authentication mechanisms to reliably verify those identities. Once 2521 
verified, authorization and logical access controls ensure that local and remote users are 2522 
granted only the minimum privileges necessary to perform their duties. Furthermore, because 2523 
gaining physical access to an OT control room or component often implies gaining logical access 2524 
to the system, these digital safeguards must be seamlessly integrated with comprehensive 2525 
physical access controls. 2526 
While enterprise IT environments typically rely on stringent, ubiquitous access controls, 2527 
implementing these capabilities in OT environments requires careful tailoring to avoid 2528 
adversely impacting continuous physical processes. Organizations must balance the need to 2529 
secure systems against the imperative for immediate operator access during emergency 2530 
situations. In critical situations, the time required to enter a user’s credentials may impede 2531 
rapid response or intervention, resulting in negative consequences for safety, health, or the 2532 
environment. When legacy OT equipment cannot natively support modern IAM capabilities, or 2533 
when strict access controls introduce unacceptable latency or safety risks, organizations should 2534 
select compensating countermeasures to provide an equivalent level of protection for the OT 2535 
environment. 2536 
To navigate these complexities, the following subsections outline key considerations and 2537 
recommendations for evaluating IAM processes, selecting appropriate authentication 2538 
mechanisms, and adapting logical, remote, and physical access controls to fit the operational 2539 
realities of their OT environments. 2540 
4.2.1.1. Identity and Access Management 2541 
Identity and access management (IAM) addresses the administration of accounts, the 2542 
deployment of authentication, and the assignment of access rights or permissions for both 2543 
users and systems. 2544 
When OT equipment cannot support IAM or the organization determines that it is not advisable 2545 
due to adverse impacts on performance, safety, or reliability, the organization should select 2546 
6 Awareness and training (PR.AT) is discussed in Sec. 3.5 due to the importance that training has with the broader roles and responsibilities 
within the organization.

<!-- page 89 -->

NIST SP 800-82r4 ipd (Initial Public Draft) Guide to OT Security 
September 2026 
71 
compensating countermeasures to provide an equivalent security capability or level of 2547 
protection for the OT. 2548 
An example of a unique challenge in OT is the need for immediate access to systems and 2549 
interfaces during emergencies. The time required to enter a user’s credentials may impede the 2550 
operator’s response or intervention, resulting in negative consequences for safety, health, or 2551 
the environment. 2552 
Supplemental guidance for implementing identity management and access control outcomes 2553 
can be found in the following documents: 2554 
• SP 800-63-3, Digital Identity Guidelines2555 
• SP 800-73-4, Interfaces for Personal Identity Verification2556 
• SP 800-76-2, Biometric Specifications for Personal Identity Verification2557 
• SP 800-100, Information Security Handbook: A Guide for Managers2558 
The following sections describe some areas in which protections may need to be augmented to 2559 
support identity and access management in the OT environment. 2560 
4.2.1.2. Identity Life Cycle Management and Provisioning 2561 
Coordinating the organization’s processes for authenticating and authorizing users to access 2562 
the OT environment can be difficult when systems are not connected. Having a process to 2563 
remove a user’s access to physical locations and the computer systems they use may require 2564 
multiple steps and involve both automated and manual processes. It can also be complicated 2565 
when OT systems are disconnected or have local accounts. 2566 
Written processes and checklists can help organizations ensure that, as personnel join, change 2567 
job roles, or leave the organization, their associated user accounts are properly modified to 2568 
reflect their appropriate access needs. These written processes will help ensure that linkages 2569 
between departments within the organization are not overlooked. 2570 
4.2.1.3. Separation of Duties and Dual Approval 2571 
The ability to create, modify, or delete user accounts needs to be managed within an 2572 
organization. Separating the approver of these changes from the implementor provides an 2573 
additional layer of protection, ensuring that no single person can compromise the system. 2574 
Multiple approvers may be required for accounts with higher levels of privilege. For example, 2575 
creating a normal user account may only require their manager’s approval, but creating a 2576 
system administrator may require their direct manager and a security officer to confirm that 2577 
additional background checks have been performed. 2578

<!-- page 90 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
72 
4.2.1.4. System, Device, and Service Accounts 2579 
In OT environments, many systems communicate automatically without the need for a human 2580 
user. These may be controllers talking to HMI, data aggregators talking to historians, or 2581 
software talking to a license server. In many cases, these use some form of user account as one 2582 
layer of protection for the information being communicated. While these user accounts are not 2583 
inherently different from human user accounts, they may have some different requirements 2584 
since they are often not changed once established. If the devices are capable, these accounts 2585 
should use the most complex credentials possible. These accounts are usually tied to 2586 
automated processes. Modifying the credentials for these accounts can cause operational 2587 
downtime if the change is made in one location but not the other. Therefore, procedures to 2588 
change credentials should be developed and validated to ensure credentials can be changed if 2589 
necessary. 2590 
4.2.1.5. IT/OT Identity Convergence and Centralization 2591 
As organizations modernize their industrial environments, they may find opportunities to 2592 
streamline account administration by centralizing user, device, and process identification and 2593 
authentication. Utilizing common network technologies, such as Active Directory or Lightweight 2594 
Directory Access Protocol (LDAP), can support centralizing identity management across both IT 2595 
and OT environments. This centralization enables the convergence of physical and logical access 2596 
controls. For example, standardizing on federal PIV smart cards allows an organization to use 2597 
the same credential mechanism for both physical entry into a facility and logical authentication 2598 
into OT assets, adjusting the required authentication factors (e.g., Card-Only vs. Card+PIN) 2599 
based on the risk level of the protected resource. However, while unified credentialing 2600 
improves monitoring capabilities and reduces administrative overhead, organizations must 2601 
carefully weigh the operational benefits of centralized accounts against the increased 2602 
cybersecurity risks of allowing authenticated accounts from the IT environment to access the 2603 
OT environment. 2604 
4.2.1.6. Authentication Mechanisms 2605 
There are several possible factors for determining the authenticity of a person, device, or 2606 
system, including something you know (e.g., PIN, password), something you have (e.g., key, 2607 
dongle, smart card), something you are (i.e., a biological characteristic, such as a fingerprint or 2608 
retinal signature), and where you are (e.g., geofencing).  2609 
OT organizations must manage user accounts and authentication mechanisms across diverse 2610 
environments, and many device manufacturers and legacy devices lack support for modern 2611 
authentication mechanisms. Therefore, organizations are often forced to share user accounts, 2612 
which limits both the accountability of user access and the ability to have individual user 2613 
credentials. Organizations must also often provide accounts and credentials for manufacturers, 2614 
integrators, or contractors that require remote or on-site access.  2615

<!-- page 91 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
73 
4.2.1.6.1. Password Authentication  2616  
While password authentication schemes are extremely common, they present challenges in OT 2617 
environments. Device protocols may transmit passwords in plaintext, and complex passwords 2618 
could pose safety issues if operators are locked out during critical events. 2619 
Organizations should consider the following password recommendations: 2620 
• Change default passwords. Always change default passwords on OT equipment to 2621 
prevent trivial exploitation. 2622 
• Balance complexity and safety. Enforce appropriate password length and complexity, 2623 
balancing security requirements with the operational necessity for rapid access during 2624 
safety-critical functions. 2625 
• Protect privileged accounts. Administrative accounts require stronger complexity, more 2626 
frequent rotation, and additional physical safeguards. 2627 
• Secure transmission and storage. Passwords should never be transmitted over the 2628 
network unless protected by FIPS-approved encryption. Organizations should also 2629 
consider using a secure, centralized password management tool. 2630 
• Life cycle management. Implement procedures to rotate passwords periodically, when 2631 
a compromise is suspected, or when an individual leaves the organization 2632 
4.2.
1.6.2. Multi-Factor Authentication 2633
 
Organizations need to consider whether multi-factor authentication (MFA) is required to 2634 
protect OT environments in whole or in part. MFA is an accepted best practice for remote 2635 
access to OT applications. When determining the placement and use of MFA within an OT 2636 
environment, organizations may need to consider different authentication scenarios, as some 2637 
OT components support only a single factor or no authentication. Organizations may consider 2638 
adjusting credential requirements based on the type of access or other mitigating factors for 2639 
the environment. For example, remote access to the OT environment may require MFA, while 2640 
local access may only require a user ID and password due to other mitigating factors (e.g., 2641 
physical access controls) before gaining physical access to the area in which the user ID and 2642 
password may be used.  2643 
4.2.
1.6.3. Token Authentication  2644
 
Traditional passwords can become lost or stolen without notice, leaving credentials more 2645 
vulnerable to exploitation. Token authentication primarily addresses this issue by requiring 2646 
physical possession of the token. If a security token is lost or stolen, the token owner is typically 2647 
aware of its absence and can notify security personnel to disable access.  2648

<!-- page 92 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
74 
Physical token authentication is more secure when combined with a second form of 2649 
authentication, such as a memorized PIN used alongside the token. Common forms of physical 2650 
token authentication include:  2651 
• Security cards (e.g., magnetic, smart chip, optical coding)  2652 
• Radio frequency devices in the form of cards, key fobs, or mounted tags  2653 
• Dongles with secure encryption keys that attach to the USB, serial, or parallel ports of 2654 
computers  2655 
• One-time authentication code generators (e.g., key fobs)  2656 
When token authentication uses cryptographic verification, the access control system should 2657 
conform to the requirements of NIST SP 800-78-5.  2658 
Additionally, if smart cards are implemented in an OT setting, organizations should consider 2659 
provisions for managing lost or damaged cards, the costs of incorporating and sustaining the 2660 
respective access control system, and a management process for card distribution and retrieval. 2661 
These procedures should consider the ability to grant temporary access to OT personnel to 2662 
prevent operational or safety disruptions.  2663 
4.2.1.6.4. Biometric Authentication 2664 
Biometric authentication enhances software-only solutions (e.g., password-based 2665 
authentication) by providing an additional authentication factor and eliminating the need for 2666 
people to memorize complex secrets. In addition, because biometric characteristics are unique 2667 
to a given individual, biometric authentication addresses the issues of lost or stolen physical 2668 
tokens and smart cards. Biometric devices provide a useful secondary check versus other forms 2669 
of authentication that can become lost or borrowed. Using biometric authentication in 2670 
combination with token-based access control or badge-operated employee time clocks 2671 
increases security.  2672 
While biometrics can provide a valuable authentication mechanism, organizations may need to 2673 
carefully assess the technology for use with industrial applications, including:   2674 
• Handling environmental factors (e.g., temperature, humidity) to which some biometric 2675 
devices are sensitive. 2676 
• Addressing industrial applications for which employees may have to wear safety glasses 2677 
and/or gloves and industrial chemicals are present 2678 
• Denying needed access to the OT system because of a temporary inability of the sensing 2679 
device to acknowledge a legitimate user 2680 
When token-based access control employs biometric verification, the access control system 2681 
should conform to the requirements of [SP800-76-2].  2682

<!-- page 93 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
75 
4.2.1.7. Authorization and Logical Access Controls 2683 
Logical access controls restrict access to an organization’s systems, data, and networks. Access 2684 
control lists (ACLs) are sometimes used to support logical access controls. An ACL is a list of one 2685 
or more rules that determine whether an access request should be granted or denied, and it 2686 
supports the principle of least functionality and controls access to restricted areas. ACLs are 2687 
commonly used with isolation technologies (e.g., firewalls), where an ACL might specify the 2688 
source, destination, and protocol allowed through the isolation device to or from the protected 2689 
network segment. ACLs may also be used to control physical or logical access to areas or 2690 
information, such as network file shares, databases, and other data repositories and 2691 
applications.  2692 
Role-based access control (RBAC) also supports logical access controls. RBAC is a technology 2693 
that has the potential to reduce the complexity and cost of security administration in networks 2694 
with large numbers of intelligent devices. RBAC is built on the principle that employees change 2695 
roles and responsibilities more frequently than the duties within those roles and 2696 
responsibilities. Under RBAC, security administration is simplified using roles, hierarchies, and 2697 
constraints to organize user access levels.  2698 
Additionally, attribute-based access control (ABAC) is an access control approach in which 2699 
access is determined based on the attributes associated with subjects (requesters) and the 2700 
objects being accessed. Each object and subject has a set of associated attributes, such as 2701 
location, time of creation, and access rights. Access to an object is authorized or denied 2702 
depending on whether the required (e.g., policy-defined) correlation can be made between the 2703 
attributes of that object and the requesting subject.  2704 
For federal employees and contractors, Personal Identity Verification (PIV) in accordance with 2705 
FIPS 201 may be required for access control. Organizations may also consider one or more of 2706 
these techniques when determining how to support local access controls within their 2707 
environments.  2708 
Some logical access controls (e.g., RBAC) support the principle of least privilege and the 2709 
separation of duties by providing a uniform means to manage access to OT devices while 2710 
reducing the cost of maintaining individual device access levels and minimizing errors. These 2711 
logical access controls can also restrict OT user privileges to only those required to perform 2712 
each person’s job (i.e., configuring each role based on the principle of least privilege). The level 2713 
of access can take several forms, including viewing, using, and altering specific OT data or 2714 
device functions.  2715 
Solutions that provide credential management, authentication, authorization, and system use 2716 
monitoring can help manage risks associated with OT devices and protocols by offering a secure 2717 
platform for authorized personnel to access OT devices. 2718 
Access control systems should verify the identity of individuals, processes, or devices before 2719 
granting access while minimizing latency and delays in processing OT system access or 2720 
commands. 2721

<!-- page 94 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
76 
Systems should also be highly reliable and not interfere with OT personnel’s routine or 2722 
emergency duties. Solutions should be designed to reduce the impact of identity and 2723 
authorization checks on OT operations and safety. 2724 
Supplemental guidance for access controls can be found in the following documents:  2725 
• SP 800-63-3, Digital Identity Guidelines  2726 
• SP 800-73-4, Interfaces for Personal Identity Verification  2727 
• SP 800-76-2, Biometric Specifications for Personal Identity Verification  2728 
• SP 800-78-5, Cryptographic Algorithms and Key Sizes for Personal Identity Verification  2729 
• SP 800-96, PIV Card to Reader Interoperability Guidelines  2730 
• SP 800-97, Establishing Wireless Robust Security Networks: A Guide to IEEE 802.11i  2731 
• SP 800-162, Guide to Attribute Based Access Control (ABAC) Definition and 2732 
Considerations  2733 
To support access controls, an organization is not limited to a single access control approach. In 2734 
some cases, applying different access control techniques to different zones based on criticality, 2735 
safety, and operational requirements is more efficient and effective. For example, ACLs on 2736 
network zone firewalls, RBAC on engineering workstations and servers, and ABAC integrated 2737 
into physical security for sensitive areas may meet an organization’s risk-based access control 2738 
requirements.  2739 
4.2.
1.7.1. Privileged Access Management 2740
 
Privileged access management (PAM) is a set of technologies and processes used to control, 2741 
secure, and monitor accounts with elevated permissions (e.g., administrator, engineer, and 2742 
service accounts) so that critical systems can only be accessed by authorized users for approved 2743 
purposes. One feature often found in PAM solutions is to rotate shared or embedded 2744 
credentials, which are commonly found in OT. Additionally, PAM solutions can provide audited 2745 
session recording for remote vendor and maintenance access, creating clear accountability for 2746 
privileged actions.  2747 
4.2.1.8. Remote Access Controls 2748 
OT environments often require access from remote users or devices, including those external to 2749 
the company. Access requirements and accounts for remote access should be maintained for all 2750 
external access. A process should be developed and communicated to the organization for 2751 
requesting and enabling remote access. This should include the business justification for the 2752 
access and document the expected security controls and the responsibilities of the external 2753 
organization and device. Further, ensure mechanisms exist to revoke access rights and accounts 2754 
associated with external users along with mechanisms to audit their access.  2755

<!-- page 95 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
77 
Deploying secure remote access technologies requires the deployment of various technologies 2756 
and devices to authenticate and secure access sessions. Remote access often requires the use 2757 
of the following devices:  2758 
• TLS/SSL VPNs. VPN appliances are often used to establish secure tunnels to a VPN 2759 
appliance within an OT DMZ. The use of VPNs should be complemented with additional 2760 
tools to help manage access to OT devices.  2761 
• Access management tools. Access management solutions (including privileged access 2762 
management) manage credentials and sessions across heterogeneous OT devices. They 2763 
can enforce strong authentication (including MFA), enable least-privilege access, and 2764 
improve auditing of OT access.  2765 
• Jump hosts. Jump hosts or servers can also be used to broker user access to remote OT 2766 
devices, including to control and monitor access.  2767 
• Authentication servers. OT environments often require dedicated and segmented 2768 
authentication services (e.g., LDAP, Active Directory) to keep OT credential stores and 2769 
authentication workflows separate from those used in IT networks.  2770 
Remote access methods include remote agents, jump hosts, site-to-site direct connections, 2771 
and, most commonly, VPNs. These technologies must be carefully managed to minimize the 2772 
organization’s attack surface. For example, persistent VPN tunnels with poor authentication 2773 
factors may be exploited by attackers to gain network access using trivial techniques. 2774 
4.2.1.9. Physical Access Controls 2775 
Defense in depth is a multifaceted strategy that integrates people, technology, and operational 2776 
capabilities to establish variable barriers across multiple layers and dimensions of the 2777 
organization. Physical security should be included in a comprehensive defense-in-depth 2778 
strategy. Physical security measures are designed to reduce the risk of accidental or deliberate 2779 
loss or damage to assets and the surrounding environment. Limiting physical access to assets 2780 
helps prevent undesirable effects, including unauthorized physical access to sensitive locations; 2781 
the unauthorized introduction of new systems, infrastructure, communications interfaces, or 2782 
removable media; and the unauthorized disruption of the physical process. Physical access 2783 
controls include controls for managing and monitoring physical access, maintaining logs, and 2784 
handling visitors.  2785 
Safeguarded assets may include control systems, tools, equipment, the environment, the 2786 
surrounding community, and intellectual property, including proprietary data (e.g., process 2787 
settings and customer information). Organizations may also need to consider additional 2788 
environmental, safety, regulatory, legal, and other requirements when implementing physical 2789 
security. 2790 
The deployment of physical security controls is often subject to specific environmental, safety, 2791 
regulatory, legal, and other requirements that must be identified and addressed for a given 2792 
environment. Physical security controls may be broadly applied or specific to certain assets.  2793

<!-- page 96 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
78 
The initial layers of physical access control are often determined based on the risk of access to 2794 
the overall facility, not just OT components. Some regulations may also determine the strength 2795 
and quantity of barriers used for the physical protection of a facility, such as the North 2796 
American Electric Reliability Corporation (NERC), Critical Infrastructure Protection (CIP), or 2797 
those from the Nuclear Regulatory Commission (NRC). 2798 
A defense-in-depth solution to physical security should consider the following attributes:  2799 
• Protection of physical locations. Classic physical security considerations typically 2800 
include a layered architecture of security measures that create multiple physical barriers 2801 
around buildings, facilities, rooms, equipment, and other information assets. Physical 2802 
security controls should be implemented to protect physical locations and may include 2803 
fences, anti-vehicle ditches, earthen mounds, walls, reinforced barricades, gates, door 2804 
and cabinet locks, guards, or other measures.  2805 
• Physical access control. Equipment cabinets should be locked when not required for 2806 
operation or safety, and wiring should be neat and contained within cabinets or under 2807 
floors. Additionally, consider keeping all computing and networking equipment in 2808 
secured areas.  2809 
Organizations should consider whether the physical security of remote assets is implemented at 2810 
differing levels and whether those differences could create cyber risks. For example, one 2811 
remote location may utilize only a padlock with minimal electronic surveillance to secure access 2812 
to network equipment that, if bypassed, could allow a malicious actor to gain access to an OT 2813 
network segment from the remote location.  2814 
Organizations should also consider whether secondary services require additional redundancy, 2815 
isolation, protection, and monitoring, such as communications and power supporting physical 2816 
security devices (e.g., cameras, sensors). 2817 
The physical protection of OT cyber components and associated data must be addressed as part 2818 
of the overall security of OT environments. Physical security at many OT facilities is closely tied 2819 
to operational safety, keeping personnel out of hazardous situations without preventing them 2820 
from doing their jobs or carrying out emergency procedures.  2821 
Physical access controls are often applied to the OT environment as compensating controls 2822 
when legacy systems do not support modern IT logical access controls (e.g., an asset could be 2823 
locked in a cabinet when the USB port or power button cannot be logically disabled). When 2824 
implementing these mitigations, organizations should consider whether the OT component 2825 
being protected can be compromised using a wireless or network connection that might bypass 2826 
the physical security controls.  2827 
Providing physical security for control centers and control rooms can reduce the potential of 2828 
many threats, including unauthorized access. Access to these areas should be limited to 2829 
authorized personnel due to the increased probability of finding sensitive servers, network 2830 
components, control systems, and consoles that support continuous monitoring and rapid 2831 
response. Gaining physical access to a control room or OT system components often implies 2832 
gaining logical access to the system or system components. In extreme cases, organizations 2833

<!-- page 97 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
79 
may need to consider designing control centers to be blast-proof or provide an off-site 2834 
emergency control center to maintain control if the primary control center becomes 2835 
uninhabitable.  2836 
Supplemental guidance for access controls can be found in the following documents:  2837 
• CISA, Cybersecurity and Physical Security Convergence Action Guide 2838 
• UFC 4-020-01, Security Engineering Facilities Planning Manual 2839 
4.2.2. Data Security and Cryptography (PR.DS) 2840 
Data security includes protecting the confidentiality, integrity, and availability of data at rest 2841 
and data in transit, protecting assets after removal, and preventing data leaks. The protection 2842 
of data should also extend to backup images and data stores to ensure they remain available 2843 
and free from tampering. This section will explore the key technologies needed to protect data, 2844 
including the deployment of cryptography in OT environments. 2845 
4.2.2.1. Data Classification   2846 
Different types of OT system data can be found in the OT network, such as control data (e.g., 2847 
setpoints, recipes, interlocks, alarm settings), process data (e.g., sensor readings, batch records, 2848 
quality measurements), and identity and access data (e.g., accounts, roles, remote access logs). 2849 
Additionally, information related to the OT system data can be found on the IT network, such as 2850 
engineering data (e.g., Piping and Instrument Drawings [P&IDs], electrical diagrams, robot 2851 
programs, operating manuals, Programmable Logic Controller [PLC]/Distributed Control System 2852 
[DCS] code, firmware, network diagrams), asset data (e.g., inventories, firmware versions, 2853 
vulnerability/patch status), environmental data (e.g., emission records, compliance evidence), 2854 
and maintenance data (e.g., work orders, service reports).  2855 
OT data needs to be classified based on its impact on the organization due to loss or 2856 
modification. Some of the criteria to be considered include the safety/operational impact if the 2857 
data is altered or lost, how difficult recovery would be, who currently has access to the data, 2858 
whether the data is exported and to whom, and whether an adversary reviewing the data 2859 
would gain an understanding of the organization’s system or be able to use it to help plan a 2860 
campaign. Data control considerations can include data access, handling rules (e.g., storage, 2861 
transmission, access, retention), sharing with vendors/third parties, and compliance 2862 
requirements. These considerations apply to data at rest and in transit.  2863 
4.2.2.2. Use of Cryptography  2864 
Cryptography can support data security requirements. Encryption, digital signatures, hashing, 2865 
and other cryptographic functions are available to prevent unauthorized access or the 2866 
modification of data at rest and in transit. Encrypting data that flows over networks (i.e., in 2867 
transit) or data stored in memory and local storage (i.e., at rest) can also be used in defending 2868 
OT. Encryption prevents an attacker from viewing or modifying cleartext data streams.  2869

<!-- page 98 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
80 
OT applications often focus on data availability. Before deploying cryptography in OT, ensure 2870 
that confidentiality or integrity is the goal of applying the security. Understanding the 2871 
advantages and disadvantages of cryptography can help organizations make an informed 2872 
decision about where to incorporate it into the defense-in-depth strategy. 2873 
Organizations should deliberately scope where encryption is applied across their OT 2874 
environment rather than treating it as uniformly deployable. Not all OT systems can support 2875 
encryption since legacy devices may lack native cryptographic capabilities, sufficient processing 2876 
capacity, or the ability to tolerate the latency introduced by encryption. The concept of 2877 
encryption exposure radius refers to organizations identifying which systems, data flows, and 2878 
storage locations carry the highest risk if exposed and prioritizing encryption there while 2879 
documenting where encryption is not feasible and implementing compensating controls 2880 
accordingly. 2881 
Organizations should also consider that cryptography may introduce key management issues. 2882 
Sound security policies require key management processes that can become more difficult as 2883 
the geographic size of the OT increases. Because site visits to change or manage keys can be 2884 
costly and time-consuming, organizations should consider whether cryptographic protection 2885 
with remote key management may be beneficial, such as when the protected units become so 2886 
numerous or geographically dispersed that managing keys is difficult or expensive.  2887 
When cryptography is selected, organizations should use a certified cryptographic system. 2888 
Additionally, cryptographic hardware should be protected from physical tampering and 2889 
uncontrolled electronic connections. 2890 
For OT, encryption can be deployed as part of a comprehensive, enforced security policy. A 2891 
cryptographic key should be long enough so that guessing it or determining it through analysis 2892 
takes more effort, time, and cost than the value of the protected asset.  2893 
4.2.2.2.1. Post-Quantum Cryptography (PQC) Considerations 2894 
The emergence of quantum computing presents a long-term threat to current public-key 2895 
cryptographic algorithms (e.g., RSA, elliptic-curve cryptography), which could be rendered 2896 
vulnerable by a sufficiently capable quantum computer. OT environments face a particular 2897 
challenge in transitioning to post-quantum cryptographic standards since many OT devices have 2898 
life cycles measured in decades and cannot be easily patched or replaced. Organizations should 2899 
begin assessing their cryptographic inventory now, which involves identifying the systems that 2900 
rely on public-key cryptography, understanding the vendor’s roadmap for PQC support, and 2901 
prioritizing migration planning for the highest-risk systems. 2902 
Supplemental guidance for data security can be found in the following documents:  2903 
• SP 800-47r1, Managing the Security of Information Exchanges  2904 
• SP 800-111, Guide to Storage Encryption Technologies for End User Devices  2905 
• SP 800-209, Security Guidelines for Storage Infrastructure  2906

<!-- page 99 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
81 
4.2.2.3. Protecting Data at Rest 2907 
Identify critical physical and electronic file types and data to protect while at rest. This may 2908 
include personally identifiable information and sensitive, proprietary, or trade secret 2909 
information. Organizations should consider centralizing critical data within secure storage 2910 
locations. When OT data is stored in the cloud or on vendor servers, organizations should 2911 
consider conducting a risk analysis to assess how the service provider protects the data and 2912 
whether additional countermeasures are needed to manage risk to an acceptable level.  2913 
4.2.2.3.1. Cryptographic Protection for Data-at-Rest 2914 
Encryption can also be used on hard local storage to protect information at rest. Full disk 2915 
encryption is recommended for portable laptops, devices, and removable media. Organizations 2916 
may also want to consider encrypting folders that contain sensitive files. When using disk or file 2917 
encryption, organizations should ensure that appropriate backup keys are maintained and 2918 
securely stored to support recovery if the primary encryption key is lost or forgotten.  2919 
4.2.2.3.2. Access Control and Enforcement 2920 
Access to data should be restricted to authorized users and services through the 2921 
implementation of access enforcement to critical data. Organizations should ensure that logical 2922 
access controls are deployed to restrict access based on the defined authorization policy. If 2923 
devices or software do not support modern access control mechanisms, compensating controls 2924 
may be necessary, such as restricting access to a secure workstation or placing the system 2925 
behind a protected network boundary. 2926 
4.2.2.3.3. Media Protection  2927 
Processes and procedures for handling media assets should be developed and followed. This 2928 
includes labeling media for distribution and handling requirements, storage, transport, 2929 
sanitization, destruction, and disposal. Media assets include removable media and devices, such 2930 
as floppy disks, Compact Disks (CDs), Digital Video Disks (DVDs), Secure Digital (SD) cards, 2931 
Universal Serial Bus (USB) memory sticks, and printed reports and documents. Physical security 2932 
controls should address specific requirements for the safe and secure maintenance of these 2933 
assets and provide guidance for transporting, handling, erasing, or destroying these assets. 2934 
Security requirements could include safe storage from loss, fire, theft, unintentional 2935 
distribution, or environmental damage.  2936 
OT devices should be protected against the misuse of media. The use of any unauthorized 2937 
removable media or device on any node that is part of or connected to the OT should not be 2938 
permitted. Solutions could be either procedural or technical to prevent the introduction of 2939 
malware or the inadvertent loss or theft of data. Organizations should apply a verification 2940 
process that includes, at a minimum, scanning devices (e.g., laptops, USB storage devices) for 2941 
malicious code prior to allowing them to connect to OT devices or networks.  2942

<!-- page 100 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
82 
Physically protecting media or encrypting the data on media is critical to protecting the OT 2943 
environment. Access to media containing OT data could provide a malicious actor with valuable 2944 
information to launch an attack. 2945 
Supplemental guidance can be found in the following documents:  2946 
• SP 800-88r1, Guidelines for Media Sanitization  2947 
• SP 800-100, Information Security Handbook: A Guide for Managers  2948 
• SP 800-209, Security Guidelines for Storage Infrastructure  2949 
4.2.2.4. Protecting Data in Transit 2950 
Critical OT data should be protected while in transit, especially over third-party network 2951 
segments and other untrusted or vulnerable network paths (e.g., cellular, wireless, internet, 2952 
WAN).  2953 
4.2.2.4.1. Cryptographic Protection for Data in Transit 2954 
Organizations should consider using encryption and authentication to support secure 2955 
connections or conduits for OT environments when connections must pass over non-OT 2956 
network segments (e.g., enterprise networks, the internet, wireless).  2957 
Many modern automation protocols incorporate cryptographic protections and can be used to 2958 
establish secure communication to OT devices, including OPC-UA and DNP3-SAv6. However, 2959 
many devices utilize either unencrypted automation protocols (e.g., DNP3, Modbus) or 2960 
unprotected management protocols (e.g., Telnet, HTTP). If OT devices lack cryptographic 2961 
support, it may be necessary to encapsulate communication using other protocols to protect 2962 
communications between network segments, such as a virtual private network (VPN). For 2963 
example, a remote site might have a boundary protection device on-site that uses a VPN to 2964 
establish a secure tunnel over an untrusted network (e.g., the internet) to a VPN-enabled 2965 
device in the main control center at a different location.  2966 
Deploying cryptography on OT presents numerous challenges, including: 2967 
• The use of cryptography could introduce communications latency. Therefore, solutions 2968 
should be tested to determine whether latency is acceptable for the application.  2969 
• Various cryptographic protocols depend on pre-shared keys or certificates across 2970 
devices. However, certificates need to be signed by a common authority, or devices 2971 
need to be configured to only accept authorized certificates (i.e., pinning). Certificates 2972 
also have a limited validity period and may expire well before the OT environment 2973 
reaches the end of its operational life. Organizations should ensure that they consider 2974 
these challenges and validate that deployed technologies adequately address these 2975 
challenges. 2976

<!-- page 101 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
83 
VPN devices used to protect OT systems should be thoroughly tested to verify that the VPN 2977 
technology is compatible with the application and that their implementation does not 2978 
negatively affect network traffic characteristics. 2979 
Supplemental guidance for access controls can be found in the following documents:  2980 
• SP 800-52r2, Guidelines for the Selection, Configuration, and Use of Transport Layer 2981 
Security (TLS) Implementations  2982 
• SP 800-63B, Digital Identity Guidelines: Authentication and Lifecycle Management  2983 
• SP 800-77r1, Guide to IPsec VPNs  2984 
• SP 800-113, Guide to SSL VPNs  2985 
• Cybersecurity and Infrastructure Security Agency (CISA) Barriers to Secure OT 2986 
Communication: Why Johnny Can’t Authenticate 2987 
4.2.2.4.2. Protecting Wireless Communications  2988 
Wireless communication can be used for local-area communication (e.g., wireless LANs, field 2989 
networks) and wide-area communication using cellular, microwave, or satellite-based systems. 2990 
While radio frequency (RF)-based communications provide enhanced flexibility over traditional 2991 
physical (i.e., wired) communication capabilities, they are also more susceptible to interference, 2992 
unauthorized access, eavesdropping, and reliability issues (e.g., signal jamming, distance 2993 
limitations, line-of-sight requirements). Prior to installation, a wireless survey should be 2994 
performed to identify antenna locations and signal strength for adequate coverage and to 2995 
minimize the exposure of the wireless network to interference from OT environmental factors 2996 
and eavesdropping.  2997 
When implementing a wireless field or local area network, the following security features 2998 
should be considered:  2999 
• A wireless mesh network to improve resiliency or to eliminate areas with poor signal 3000 
strength. Mesh networks can provide fault tolerance through alternate route selection 3001 
and preemptive failover of the network. Organizations should also consider the 3002 
performance and security implications of using mesh networks. For example, when 3003 
roaming between access points, devices may experience temporary communication 3004 
loss. Roaming may also require different security controls to reduce the transition time. 3005 
Organizations will need to find the appropriate balance between functional capabilities 3006 
and cybersecurity to achieve the risk tolerance. 3007 
• Selecting a standard, non-proprietary protocol (e.g., IEEE 802.15.x).  3008 
• Allowlisting devices in the wireless device manager to prevent rogue devices from 3009 
connecting. 3010 
• Implementing appropriately complex passwords and join keys.  3011

<!-- page 102 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
84 
• Consider implementing network access control mechanisms to strengthen 3012 
authentication. 3013 
While encrypting and securing the data transmitted over wireless networks is critical, these 3014 
data-level protections must be paired with network boundary defenses. For specific guidance 3015 
on safely segmenting, isolating, and integrating wireless technologies within the broader OT 3016 
environment, refer to Sec. 4.2.2.4. 3017 
Supplemental guidance for wireless communications security can be found in the following 3018 
documents:  3019 
• SP 800-97, Establishing Wireless Robust Security Networks: A Guide to IEEE 802.11  3020 
• SP 800-121r2, Guide to Bluetooth Security  3021 
• SP 800-153, Guidelines for Securing Wireless Local Area Networks (WLANs)  3022 
• SP 800-187, Guide to LTE Security  3023 
4.2.2.4.3. Third-Party Communication Providers  3024 
OT environments often depend on third-party communication providers for connectivity to 3025 
geographically remote sites and with external partners. These providers may lack adequate 3026 
network protection, leaving them vulnerable to threats that degrade their availability and 3027 
integrity. Therefore, organizations should deploy technical redundancies and contingency plans 3028 
to support operations if these providers are compromised and unavailable, including 3029 
establishing backup and contingency communications capabilities (e.g., PACE plans) or 3030 
establishing procedures to operate in an isolated or manual mode if these communications are 3031 
unavailable. 3032 
4.2.3. Platform Security and Infrastructure Resilience (PR.PS / PR.IR) 3033 
Platform security is a broad topic that encompasses many aspects of deploying, operating, 3034 
maintaining, and decommissioning systems and devices in an asset owner’s facility. Even the 3035 
most secure device can be configured and/or maintained in such a way that renders its security 3036 
ineffective.  3037 
4.2.3.1. Platform Configuration and Maintenance 3038 
4.2.3.1.1. Developing a Maintenance Tracking Capability 3039 
Establish processes and implement tools to ensure that routine and preventative maintenance 3040 
and repairs (both local and remote) of OT assets are performed consistently with OT 3041 
organizational policies and procedures. 3042 
Ensure that the processes and tools allow for scheduling, authorizing, tracking, monitoring, and 3043 
auditing maintenance and repair activities for OT assets. Documenting these events provides an 3044

<!-- page 103 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
85 
audit trail that can aid in cybersecurity-related troubleshooting, response, and recovery 3045 
activities. Maintenance tracking can also provide visibility into scheduled maintenance for OT 3046 
devices and help inform end-of-life decisions.  3047 
Any maintenance performed on an OT device can inadvertently modify its configuration and 3048 
result in an increased attack surface. The OT device should remain in a hardened state, 3049 
regardless of the maintenance performed. Device configuration should be verified after 3050 
maintenance and software patching as some features may have inadvertently been reenabled 3051 
or new features installed. Best practices and other supporting documents should be obtained 3052 
from the device vendor to guide and inform maintenance activities.  3053 
Maintenance tracking tools enable an organization to schedule, track, authorize, monitor, and 3054 
audit maintenance and repair activities to OT and ensure that maintenance logs or changes are 3055 
properly documented. The software used for OT maintenance activities should be approved 3056 
and controlled by the organization. Approved software should be obtained directly from 3057 
vendors and its authenticity verified (e.g., validate certificates, compare the hashes of 3058 
installers). If the ability for remote maintenance is required, ensure that the remote access tool 3059 
supports the authentication of maintenance personnel, connection establishment at the 3060 
beginning of maintenance activities, and immediate teardown once the maintenance activities 3061 
are complete. Additionally, ensure that the tool can log the remote maintenance activities that 3062 
are performed. 3063 
Maintenance devices that remain secure within the OT environment reduce their exposure. 3064 
Using maintenance devices outside of the OT environment or connecting the devices to non-OT 3065 
networks should be restricted or minimized. Devices may contain wireless radios and other 3066 
communications devices that may be vulnerable to side-channel attacks or may allow 3067 
simultaneous connections between networks (i.e., dual-homed). Any devices that are 3068 
connected to the OT system should be disconnected after the maintenance activities are 3069 
completed, and any temporary connections should be removed. Vendor documentation should 3070 
be thoroughly reviewed to understand these capabilities.  3071 
4.2.3.1.2. Configuration Management  3072 
Applying configuration management practices (e.g., setting access controls, enabling 3073 
encryption) that support secure configurations and application hardening is important to meet 3074 
organizational and regulatory security requirements. Application hardening procedures may 3075 
also include disabling or blocking specific network communication ports, application features, 3076 
or unnecessary services that run on the system.  3077 
Configuration management helps ensure that systems are deployed and maintained in a secure, 3078 
consistent state and reduces the risk of outages by improving visibility and the tracking of 3079 
system changes. In addition, configuration management can detect improper configurations 3080 
before they negatively impact performance, safety, or security. Organizations should document 3081 
the approved baseline configuration for their OT devices and establish the system development 3082 
life cycle (SDLC) approach to document, test, and approve changes before deploying them to 3083 
the OT environment. Organizations should also verify that default configurations align with the 3084

<!-- page 104 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
86 
predetermined safe states defined for each system to ensure that a device restored to its 3085 
baseline configuration does not inadvertently place the physical process in an unsafe operating 3086 
condition. 3087 
Some organizations may maintain logbooks or other similar methods to document changes to 3088 
OT components. Organizations should consider centralizing the tracking and documentation of 3089 
changes to the OT environment to improve visibility and ensure proper testing and approvals 3090 
for system changes. Such a process may help organizations prevent accidental reconfiguration 3091 
or identify the intentional reconfiguration of components to unapproved or untested versions.  3092 
Configuration management tools enable an asset owner to establish and maintain the integrity 3093 
of system hardware and software components by controlling the processes for initializing, 3094 
changing, monitoring, and auditing the configurations of the components throughout the 3095 
system life cycle. If the use of automated configuration management tools is deemed to be 3096 
appropriate, processes should be in place to validate configurations prior to deployment. Many 3097 
OT changes can be made only during scheduled maintenance downtime to minimize impact. 3098 
When considering automated configuration management tools, organizations should also 3099 
consider potential impacts on the OT system. In some cases, these tools transfer numerous 3100 
types of data, potentially in large amounts, over the manufacturing system network. 3101 
Additionally, some tools may also have the potential to impact OT system operations by 3102 
attempting to change device configurations or manipulating active files. Keys for OT assets (e.g., 3103 
PLCs, safety systems) should be in the “Run” position at all times unless they are actively being 3104 
programmed.  3105 
Supplemental guidance for configuration management can be found in the following 3106 
documents:  3107 
• SP 800-128, Guide for Security-Focused Configuration Management of Information 3108 
Systems  3109 
• SP 1800-5, IT Asset Management  3110 
• IR 8183A, Cybersecurity Framework Manufacturing Profile Low Impact Level Example 3111 
Implementations Guide 3112 
4.2.3.1.3. Software/Firmware Patch Management 3113 
Organizations should implement an OT patch management process that defines how it will 3114 
monitor for patches, when to apply them, how to test them (e.g., with vendors, on offline 3115 
systems), and how to select compensating controls to limit exposure of the vulnerable system 3116 
when patching is delayed. The process should be designed to not only reduce cybersecurity 3117 
risks but also account for OT reliability, availability, and safety needs. 3118 
Organizations are responsible for staying informed and determining when patches should be 3119 
applied as part of their documented patch management process. Many OT vulnerabilities are 3120 
published to CISA as advisories or CVEs. However, not all vendors report known vulnerabilities 3121 
to CISA or CVE. Organizations can often stay informed by subscribing to vendor-specific 3122 
notifications in addition to CISA alerts and advisories. Private cybersecurity companies also 3123

<!-- page 105 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
87 
offer services to help organizations stay informed about known vulnerabilities in their OT 3124 
environments.  3125 
OT environments present numerous challenges that constrain the deployment of patches. 3126 
Patch management decisions should account for the following considerations: 3127 
• Many OT environments must run nearly continuously for extended periods or have 3128 
small maintenance windows to apply approved updates. This limits the frequency with 3129 
which patches can be applied. 3130 
• A patch may remove a vulnerability, but it can also introduce greater reliability or safety 3131 
risks. Patching the vulnerability may also change the way the OS or application behaves, 3132 
potentially resulting in some loss of functionality. 3133 
• Legacy devices and software often lack vendor support and may no longer receive 3134 
patches for identified flaws and vulnerabilities. 3135 
OT patching decisions should factor in operational requirements and potential adverse effects 3136 
of installing the patch and be determined by knowledgeable OT personnel. Many organizations 3137 
define decision frameworks (e.g., Now/Next/Never, Now/Next/Later) to triage and inform 3138 
patching decisions: 3139 
• Now. Patches that pose immediate risks and can be installed without impacting 3140 
operations may be applied immediately. These may include patches for components 3141 
within DMZ environments, network segments that are more exposed, or vulnerabilities 3142 
that allow unauthorized remote access to the OT environment.  3143 
• Next. Vulnerabilities that pose a significant risk to operations but cannot be feasibly 3144 
patched may need to be scheduled during the next scheduled maintenance period.  3145 
• Later (or Never). Other vulnerabilities that present reduced or minimal risk may be 3146 
scheduled for a future time. Additional information about this approach is defined here.  3147 
An organization’s patch management process should also define processes to prevent or 3148 
recover from any unintended consequences of deployed patches. For example:  3149 
• Consider separating the automated OT patch management process from the automated 3150 
non-OT application process. 3151 
• Patches should be adequately tested (e.g., offline system testing) to assess the 3152 
acceptability of any performance impacts before being deployed into a production 3153 
system.  3154 
• Have a recovery plan for the OT component or system being patched in case the patch 3155 
causes an unexpected issue. 3156 
If patches cannot be deployed, the organization should explore appropriate compensating 3157 
controls. Security tools (e.g., web application firewalls, IDSs) could be configured to provide 3158 
additional protection to detect or prevent attacks exploiting unpatched vulnerabilities while the 3159 
organization waits for an opportunity to apply the updates. Other tools (e.g., bump-in-the-wire 3160

<!-- page 106 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
88 
security devices) can be installed in line with devices that cannot be updated or are using 3161 
obsolete operating systems. 3162 
Organizations may be required to follow industry-specific patch management guidance. 3163 
Otherwise, they may develop patch management procedures based on existing standards. 3164 
Supplemental guidance for flaw remediation and patch management can be found in the 3165 
following documents:  3166 
• SP 800-40r4, Guide to Enterprise Patch Management Planning: Preventive Maintenance 3167 
for Technology 3168 
• ISA 62443-2-3, Patch Management in the IACS Environment 3169 
4.2.3.2. Application Allowlisting 3170 
Application allowlisting technologies provide an additional protection mechanism on hosts by 3171 
restricting which applications are allowed to execute. When properly configured, non-3172 
authorized applications will not execute on the host environment.  3173 
The relatively static nature of OT environments presents an opportunity for organizations to 3174 
include application allowlisting as part of their defense-in-depth strategy, and DHS 3175 
recommends it as a best practice. When considering application allowlisting within an OT 3176 
environment, organizations should coordinate with their vendors and review available 3177 
implementation guidance, such as SP 800-167, Guide to Application Whitelisting, or relevant 3178 
guidance for their industry. The configurations and policies should be thoroughly tested before 3179 
being deployed to ensure that the rules and settings properly support organizational security 3180 
objectives.  3181 
4.2.3.3. Hardware Management 3182 
Hardware must also be managed securely throughout its life cycle, especially during 3183 
decommissioning and disposal. 3184 
4.2.3.3.1. Decommissioning Systems 3185 
Managing OT hardware throughout the system life cycle is essential to ensuring operational 3186 
efficiency and reducing the organization’s attack surface. When OT devices are 3187 
decommissioned, associated risks may manifest as many devices participate in tightly coupled 3188 
control and safety functions. These devices may also have dependencies that are unknown to 3189 
the maintenance staff (e.g., time synchronization, OPC links, software licensing).  3190 
When the decision is made to decommission a system, a thorough review must be conducted 3191 
to ensure that the asset’s removal from production has no negative or otherwise adverse 3192 
effects on normal operations (e.g., no impact on system functionality, overall monitoring, or 3193 
operator visibility). If the review yields no findings of note, staff may proceed and remove the 3194 
system from production. It is recommended that operators revoke devices’ certificates or other 3195

<!-- page 107 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
89 
keys, disable device-related and service accounts, remove firewall and ACL entries, and ensure 3196 
that the device is no longer reachable via the network or other logical means upon removal. 3197 
4.2.3.3.2. System Disposal 3198 
Upon the completion of system decommissioning, secure disposal is necessary. OT devices may 3199 
contain proprietary information (e.g., PLC logic, product recipes, product batch records, 3200 
calibration information, other artifacts) that could enable process replication, thereby 3201 
compromising an organization’s competitive advantage.  3202 
To establish a paper trail during the disposal process, organizations should leverage a chain of 3203 
custody from removal through storage and transportation to the decommissioned device’s final 3204 
disposition. Additionally, the organization should note whether the equipment is being 3205 
destroyed, returned to its vendor, or retained as a spare. Retained in-scope assets should be 3206 
inventoried, securely stored, and — if applicable — reintroduced in a secure manner in keeping 3207 
with defined policy. 3208 
Some OT devices may be environmentally hazardous or subject to e-waste statutes, depending 3209 
on jurisdiction, and must be handled accordingly. Should the organization handle destruction, 3210 
careful steps must be taken to purge all media and leave no trace of its past production state 3211 
unless data retention is required by policy or law. Proprietary process data or secrets may 3212 
persist on devices even after decommissioning, so performing and validating a factory reset is 3213 
imperative. 3214 
If devices are to be destroyed by a third party, the organization must require that party to 3215 
follow its expected media sanitization procedures and obtain proof of completion. 3216 
4.2.3.4. Software Development Life Cycle 3217 
Organizations that develop in-house systems and components should incorporate policies and 3218 
procedures that support and validate secure code development practices into the cybersecurity 3219 
program. The software development life cycle (SDLC) should consider security during each 3220 
phase, including security reviews and coding techniques for each of the following processes:  3221 
• Using or developing tools to audit and automate secure code techniques  3222 
• Testing and reviewing code to comply with secure coding practices  3223 
• Testing the software for security errors in programming  3224 
For organizations that procure components or services from third parties, these same practices 3225 
should be reviewed prior to executing contracts with vendors. Organizations can help industries 3226 
move toward more secure products by incorporating security requirements into their 3227 
procurement decisions and vendor agreements. This approach is known as secure-by-design 3228 
procurement and shifts the burden of security from the asset owner back to the manufacturer, 3229 
where it can be addressed most efficiently and at scale. Prior to procurement, organizations 3230 
should evaluate prospective OT products against key security criteria, including secure-by-3231

<!-- page 108 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
90 
default configurations, strong authentication, baseline logging, commitment to vulnerability 3232 
management, and support for open standards.  3233 
The SDLC is especially critical for programmable automation devices (e.g., PLCs) because 3234 
unauthorized or untested changes to device logic can cause operational disruptions or safety 3235 
incidents. Organizations should follow applicable industry guidance for secure coding practices 3236 
for automation logic, including PLC programming. 3237 
Supplemental guidance for secure-by-design procurement and secure coding practices for 3238 
automation logic can be found in the following documents:  3239 
• Secure by Demand: Priority Considerations for Operational Technology Owners and 3240 
Operators when Selecting Digital Products, U.S. Cybersecurity and Infrastructure 3241 
Security Agency, Jan. 2025. 3242 
• Top 20 Secure PLC Coding Practices, PLC Security, admeritia GmbH. 2026 3243 
4.2.3.5. Resilience of Technology Infrastructure (PR.IR) 3244 
Managing the physical operating environment includes emergency protection controls, such as 3245 
emergency shutdown of the system, backup power and lighting, temperature and humidity 3246 
controls, and protection against fire and water damage. Organizations should develop policies 3247 
and procedures to ensure that environmental operating requirements for assets are achieved. 3248 
To this end, organizations should consider the following factors when identifying potential 3249 
countermeasures to protect the operating environment:  3250 
• Environmental factors. Environmental factors can be important. For example, if a site is 3251 
dusty, systems should be placed in a filtered environment, especially if the dust is likely 3252 
to be conductive or magnetic, as in the case of sites that process coal or iron. If vibration 3253 
is likely to be a problem, systems should be mounted on rubber bushings to prevent disk 3254 
crashes and wiring connection problems.  3255 
• Environmental control systems. HVAC systems for control rooms must support OT 3256 
personnel during normal operation and emergency situations, which could include the 3257 
release of toxic substances. Risk assessments should consider the risks of operating 3258 
HVAC systems (e.g., air intakes) in an occupied shelter during a toxic release as well as 3259 
the risks of continued operation during a power outage (e.g., using an uninterruptible 3260 
power supply in critical environments). Additionally, fire systems must be carefully 3261 
designed to avoid causing more harm than good (e.g., avoid mixing water with 3262 
incompatible products). HVAC and fire systems play significant roles arising from the 3263 
interdependence of process control and security. For example, fire prevention and 3264 
HVAC systems that support industrial control computers need to be protected against 3265 
cyber incidents. In addition, environments that contain systems and media (e.g., backup 3266 
tapes, floppy disks) should maintain stable temperature and humidity. An alarm should 3267 
be generated in the OT system when environmental specifications (e.g., temperature, 3268 
humidity) are exceeded.  3269

<!-- page 109 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
91 
• B ackup p ower. Reliable power for OT is essential so backup power should be provided 3270  
fo
r critical systems. Depending on the site’s needs, this can be something that lasts for 3271
 
s
econds to minutes (e.g., UPS) or for hours to days (e.g., generator). The backup power 3272
 
s
hould be sized to support operational needs, which can range from just long enough 3273
 
f
or a safe shutdown to supporting continued operations for an extended period.  3274
 
• Cabling. While unshielded twisted-pair communications cables may be acceptable in an 3275 
office environment, they may not be suitable for some OT environments due to their 3276 
susceptibility to interference from magnetic fields, radio waves, temperature extremes, 3277 
moisture, dust, and vibration. Organizations should consider using alternative cabling or 3278 
shielding that provides suitable protection against environmental threats. Additionally, 3279 
organizations should consider color-coded cables, connectors, conduits, and labeling to 3280 
clearly delineate OT and IT network segments and reduce the risk of potential cross-3281 
connections. Organizations should also consider running spare cables during the initial 3282 
commissioning.  3283 
4.3. Detect (DE) 3284 
Situational awareness of the OT system is imperative for understanding its current state, 3285 
validating that it is operating as intended, and ensuring that no policy violations or cyber 3286 
incidents have hindered its operation. To detect security incidents across the OT environment, 3287 
the organization should deploy infrastructure to monitor and collect data from networks, hosts, 3288 
users, and physical access systems. In addition to collecting this data, the organization should 3289 
ensure that it is properly collected, stored, and reviewed by security analysts to help identify 3290 
and investigate potential intrusions. 3291 
4.3.1. Continuous Monitoring (DE.CM) 3292 
The goal of continuous monitoring is to observe systems and user activities to detect 3293 
anomalies, indicators of compromise, and other potentially adverse events. Monitoring 3294 
includes collecting and analyzing digital artifacts from devices, network traffic, and user 3295 
interactions, such as physical access and system use.  3296 
4.3.1.1. System and Device Monitoring 3297 
OT environments contain a diverse set of services, endpoints, and devices that should be 3298 
monitored for potential malicious activity. This includes identifying and collecting logs, 3299 
detecting the presence of malware across endpoints and servers, and aggregating and 3300 
correlating user access records across the environment. 3301 
4.3.1.1.1. Device Logging 3302 
Network and computing devices (e.g., routers, gateways, switches, firewalls, servers, 3303 
workstations) should be configured to log events to support monitoring, alerting, and incident 3304

<!-- page 110 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
92 
response analysis. Logging capabilities are typically available for recording events in 3305 
applications, OSs, and network communications. Logging should also be configured and 3306 
collected from any external computing platforms used by the organization, such as cloud 3307 
services. 3308 
Capturing log events is critical to maintaining situational awareness of the OT system. 3309 
Organizations should review their available logging capabilities and configure them to record 3310 
the operational and cybersecurity events that are appropriate for their environment. Typical 3311 
events include maintenance functions (e.g., access control, configuration changes, backup, 3312 
restore), OS functions, and application (i.e., process) events. The specific types of events 3313 
available for logging will vary between OT devices and should be chosen based on the device’s 3314 
capabilities and the desired events to capture. In general, each log entry should also include 3315 
where the event occurred, the type of event, when it occurred, the source of the event, the 3316 
identities of any users or system accounts involved, and the outcome of the event.  3317 
To support log correlation, each log entry should identify the device that generated the event, 3318 
the timestamp of the event, and the user or system account that generated the event. 3319 
Correlating events across multiple OT devices can be difficult if the event timestamps generated 3320 
by the devices were not informed by a shared time source. Each device’s internal clock should 3321 
be synchronized with a primary clock to support event correlation across devices. Log entries 3322 
should also use a consistent timestamp format (e.g., time zone format, string format, daylight 3323 
saving). Organizations should verify timestamp consistency after log collection since device 3324 
clock drift or loss of time synchronization can introduce discrepancies that affect the accuracy 3325 
of event correlation and incident reconstruction. 3326 
Organizations should establish how long event logs should be retained and ensure that 3327 
adequate storage is available to support log retention requirements. Many sector-specific 3328 
regulations require data retention for a specific length of time. Depending on the frequency of 3329 
events being logged, the log size may grow quickly and result in increasing space utilization. 3330 
Disk space and memory are limited on most OT devices, so adequate storage should be 3331 
provided locally or remotely to reduce the likelihood of exceeding device capacity, which could 3332 
ultimately result in the loss of logging capability. Transferring logs from OT devices to alternate 3333 
storage should be considered to free up device storage and ensure logs remain available for 3334 
monitoring, analysis, and incident response. 3335 
Many OT devices either lack mechanisms to store logs or do not provide a network service that 3336 
supports remote log collection (e.g., syslog). If device-level logs are unavailable, organizations 3337 
should identify compensating data sources that can partially reconstruct activity on those 3338 
devices. In this scenario, the engineering workstation or other programming terminal used to 3339 
interact with the device is often the most valuable log source, as it may record engineering 3340 
sessions, project file access, and maintenance activity even when the device itself cannot. 3341 
Network infrastructure devices (e.g., switches, routers, firewalls) that sit adjacent to OT devices 3342 
may also provide partial visibility through their own logs and capture connection activity and 3343 
traffic patterns associated with those devices. Organizations should document which devices in 3344 
their environment are incapable of generating or exporting logs and define compensating 3345 
monitoring strategies for those device classes. 3346

<!-- page 111 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
93 
Organizations that use unidirectional gateways, data diodes, or similar devices to enforce highly 3347 
segregated boundaries between OT and IT networks must explicitly design a security telemetry 3348 
export path to ensure that security logs generated within the OT environment can still reach 3349 
the IT SOC. These devices enforce one-way data flow by design, which can create a detection 3350 
blind spot if this export path is not deliberately accounted for. 3351 
Supplemental guidance can be found in SP 800-92, Guide to Computer Security Log 3352 
Management. 3353 
4.3.1.1.2. Service Logging 3354 
If cloud-based or hosted services (e.g., remote access platforms, cloud-based historians, vendor 3355 
remote monitoring services) are present in the OT architecture, the log sources they generate 3356 
should be included in the organization’s host-based logging inventory. Unlike device-level logs, 3357 
which originate from hardware within the OT environment, service logs are generated and may 3358 
be retained by an external platform. This introduces considerations around log accessibility, 3359 
retention controls, and data sovereignty that organizations should account for when defining 3360 
their overall logging requirements. 3361 
4.3.1.1.3. Time Synchronization  3362 
Time synchronization solutions enable an organization to synchronize time across many 3363 
devices. This is important for a variety of functions, including event and log correlation, 3364 
authentication mechanisms, access control, and quality of service. Synchronizing the internal 3365 
clocks of OT systems and devices is critical for cyber event correlation and other OT functions 3366 
(e.g., motion control). If a device or system clock is inaccurate, the timestamps generated by 3367 
the clock for event and log entries will also be inaccurate, as will any other functions that use 3368 
the clock.  3369 
A common time should be used across all OT devices. Utilizing multiple time sources can reduce 3370 
clock error and compensate if the primary time source is lost or its time quality degrades. 3371 
Authenticated Network Time Protocol (NTP) and secure Precision Time Protocol (PTP) (i.e., PTP 3372 
with an authentication TLV [type, length, value]) can be used if there is a risk of malicious 3373 
modification to the network time (e.g., RF jamming, packet spoofing, denial of service). Non-3374 
authenticated NTP is susceptible to spoofing and should be located behind the firewall.  3375 
Time sources located in the OT environment should be included in the system and network 3376 
monitoring programs. If available, logs from each time source (e.g., syslog) should be forwarded 3377 
to a log collection system. 3378 
Supplemental guidance can be found in the following documents:  3379 
• SP 800-92, Guide to Computer Security Log Management  3380 
• IR 8323, Foundational PNT Profile: Applying the Cybersecurity Framework for the 3381 
Responsible Use of Positioning, Navigation, and Timing (PNT) Services 3382

<!-- page 112 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
94 
4.3.1.2. Malicious Code and Endpoint Monitoring 3383 
Tools should be used to monitor for malicious code and cyber threats across the organization, 3384 
including file transfer tools and endpoint devices for potential threat actor behavior. OT 3385 
organizations should be especially cautious about the use of tools on OT endpoints, as they 3386 
could potentially introduce reliability or performance concerns. 3387 
There are multiple approaches and tools to detect unauthorized behavior on endpoints. 3388 
Traditional antivirus software, which relies on a combination of heuristic algorithms and known 3389 
malware signatures to detect and block potentially malicious code, can often be ineffective 3390 
against novel malware or more modern threat actor tactics. More recent endpoint detection 3391 
and response (EDR) tools focus on endpoint behavior analysis and telemetry collection, which 3392 
can improve the ability to detect these threats.  3393 
The use of malicious code and endpoint monitoring within OT may require adopting special 3394 
practices, including compatibility checks, change management, and performance impact 3395 
metrics. These tools may consume significant CPU usage when running manual scans and 3396 
signature updates, which could have negative impacts on OT computers and servers. Some OT 3397 
vendors recommend and even support the use of vendor-specific malicious code and endpoint 3398 
monitoring tools. In some cases, OT system vendors may have performed regression testing 3399 
across their product line to support a particular malicious code or endpoint monitoring tool and 3400 
provide associated installation and configuration documentation.  3401 
The decision to deploy these tools to an endpoint should be determined by both its functional 3402 
role and the associated software it deploys. Generally:  3403 
• General-purpose Windows, Unix, and Linux systems used as engineering workstations, 3404 
data historians, maintenance laptops, and backup servers can be secured like 3405 
commercial IT equipment by installing push- or auto-updated malicious code and 3406 
endpoint monitoring software with updates distributed via an update server located 3407 
within the process control network. Follow organization-developed procedures for 3408 
transferring the latest updates from known vendor sites to the OT platform servers and 3409 
other OT computers and servers.  3410 
• Follow vendor recommendations on all other servers and computers (e.g., DCS, PLC, 3411 
instruments) that have time-dependent code, modified or extended OSs, or any other 3412 
change that makes them different from a standard PC. Test the malicious code and 3413 
endpoint monitoring software and updates on an offline system, if possible (e.g., install 3414 
on a backup HMI and validate that performance is not degraded before applying to the 3415 
primary HMI).  3416 
Before deploying malicious code and endpoint monitoring, software organizations should 3417 
validate that they are compatible with the target platform and do not introduce any reliability 3418 
or performance issues. Key checks include:  3419 
• The configuration of the antivirus software should be tested on an offline system, if 3420 
possible.  3421

<!-- page 113 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
95 
• Manual scanning and signature updates should be performed while the system is not 3422 
c
ritical for operations.  3423
 
• Redundancy should be considered for critical systems that require ongoing tool updates 3424 
such that signature updates can be performed without impacting operations (e.g., 3425 
consoles, HMIs).  3426 
• When configuring file exclusion lists, determine which control application files should 3427 
not be scanned during production to avoid potential OT system malfunctions or 3428 
performance degradation.  3429 
Malicious code protection tools only function effectively when they are installed, configured, 3430 
run full-time, and properly maintained in light of known attack methods and payloads.  3431 
CISA provides a recommended practice for updating antivirus software in OT environments. 3432 
Supplemental guidance for anti-malware practices can be found in the following documents:  3433 
• SP 800-83r1, Guide to Malware Incident Prevention and Handling for Desktops and 3434 
Laptops  3435 
• SP 1058, Using Host-Based Anti-Virus Software on Industrial Control Systems: Integration 3436 
Guidance and a Test Methodology for Assessing Performance Impacts 3437 
• IR-18-214 - Recommended Practice: Updating Antivirus in an Industrial Control Systems.  3438 
U.S. Department of Homeland Security. 2018 3439 
4.3.1.3. User Behavior Monitoring 3440 
User behavior monitoring focuses on observing and analyzing the actions performed by 3441 
operators, engineers, administrators, and third-party personnel within the OT environment. 3442 
Monitoring user activity requires collecting and correlating events from host devices, 3443 
engineering software, and authentication servers to build a complete picture of personnel 3444 
actions across the OT environment. Organizations should establish baselines of expected 3445 
behavior for individual users or user groups, including normal working hours, expected 3446 
privilege/access levels, typical systems accessed, expected software usage, and routine 3447 
operational tasks. This will provide a reference point against which deviations can be identified. 3448 
Anomalous activity (e.g., access outside of normal hours, privilege escalation, use of 3449 
unauthorized accounts, configuration changes outside of approved maintenance windows) may 3450 
indicate policy violations or potential security incidents.  3451 
User attribution in OT environments can be difficult for several reasons, including the use of 3452 
shared accounts, limited device-level logging capabilities, legacy systems that do not support 3453 
authentication, local access to devices that may bypass authentication and logging entirely, and 3454 
automated processes that operate under generic service accounts. If individual attribution is 3455 
not directly available, compensating controls (e.g., work orders, physical access logs, network 3456 
infrastructure logs, session recording, personnel sign-in procedures) should be used to attribute 3457 
actions to specific individuals. Network monitoring data and packet captures may also contain 3458

<!-- page 114 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
96 
user identity information if protocols transmit usernames or session context in clear text, 3459 
providing an additional source for user attribution.  3460 
Third-party and vendor access warrants particular attention, as these users operate outside of 3461 
the organization’s normal oversight structures while often having elevated access to OT devices 3462 
for maintenance and support purposes. Third-party sessions should be monitored against 3463 
approved work orders and maintenance schedules, and activities should be logged and 3464 
reviewed for any actions outside of the approved scope. 3465 
4.3.1.4. Network Monitoring 3466 
Network monitoring can greatly enhance the ability to detect attacks that are entering or 3467 
leaving OT networks. It can also improve network efficiency by detecting non-essential traffic. 3468 
OT cybersecurity personnel must be part of the diagnostic process for interpreting alerts from 3469 
network monitoring tools. Careful monitoring and an understanding of the OT network’s 3470 
normal state can help distinguish transient conditions from legitimate attacks and provide 3471 
insight into events outside of the normal state.  3472 
Network monitoring involves the continuous observation and analysis of traffic that traverses 3473 
OT network segments to detect anomalous activity, identify potential cybersecurity incidents, 3474 
and maintain situational awareness of the OT environment. Unlike host-based monitoring, 3475 
which focuses on activities that occur on individual devices, network monitoring provides 3476 
visibility into communications between devices across the OT architecture. 3477 
OT system traffic is typically more deterministic (i.e., repeatable, predictable, and designed) 3478 
than IT network traffic, which can be leveraged to support network monitoring for anomaly and 3479 
error detection. Organizations should refer to Sec. 5 for guidelines on OT network architecture, 3480 
including network segmentation and zone design, which can directly inform sensor placement 3481 
and monitoring strategy. 3482 
All sensors should undergo extensive testing and be implemented in a test environment before 3483 
deployment to the OT network. Configuring the sensor to test or learning mode after it is 3484 
installed on the network provides an opportunity to tune the device using real OT network 3485 
traffic. Tuning can help reduce false-positive alerts, reduce alert “noise” from typical network 3486 
traffic, and help identify implementation and configuration problems.  3487 
4.3.1.4.1. Monitoring Tools and Capabilities 3488 
Tools and capabilities that support behavior anomaly detection (BAD), SIEM, intrusion 3489 
detection systems (IDS), and intrusion prevention systems (IPS) can assist organizations in 3490 
monitoring network traffic and generating alarms when anomalous or suspicious traffic is 3491 
detected.  3492 
Effective network monitoring in OT requires tools that can parse and interpret OT-specific 3493 
industrial protocols. Organizations should ensure that their monitoring tools support the 3494 
specific protocols in use within their environment, which may include Modbus, DNP3, IEC 3495 
61850, Ethernet/IP, PROFINET, OPC-DA/UA, and other vendor- or industry-specific protocols. 3496

<!-- page 115 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
97 
Some IDS and IPS vendors have incorporated attack signatures for common OT protocols to 3497 
detect known attack patterns that target those protocols. 3498 
Organizations should carefully consider the impacts of automated response capabilities 3499 
associated with IPS deployment in OT environments. Automated actions that are appropriate in 3500 
IT environments may disrupt time-critical control processes or safety functions in OT. 3501 
Organizations may consider limiting automated response capabilities to higher network levels 3502 
(e.g., DMZ interfaces) if the risk of disrupting OT operations is lower while relying on alerts and 3503 
manual responses at lower network levels that are closer to field devices. 3504 
Organizations should also consider the effects of encrypted network communications on their 3505 
network monitoring capabilities and deployment strategies. For example, a BAD system or IDS 3506 
may be unable to determine whether encrypted network communication is malicious and could 3507 
generate false-positive or false-negative alerts for the traffic. Changing the data collection point 3508 
to capture network traffic before or after encryption (e.g., using host-based network 3509 
monitoring tools) could help improve monitoring capabilities when encrypted communication is 3510 
expected.  3511 
4.3.1.4.2. Network Baselining 3512 
Careful monitoring and an understanding of the OT network’s normal state can help distinguish 3513 
transient conditions from legitimate attacks and provide insight into events outside of the 3514 
normal state. A well-defined baseline differentiates between expected operational traffic and 3515 
anomalous activity that may indicate a cybersecurity incident, misconfiguration, or equipment 3516 
issue. 3517 
Building a network baseline involves observing and documenting the normal state of the OT 3518 
network across several dimensions, including expected communication pairs, the protocols and 3519 
port numbers in use, typical polling intervals and data volumes, and the function codes or 3520 
command types used within OT protocols. Implementing network monitoring tools in a passive 3521 
(e.g., listen or learning) mode and analyzing the information to differentiate between known 3522 
and unknown communication may be a necessary first step in implementing network security 3523 
monitoring. Organizations should also document expected communication flows between 3524 
network zones, including traffic that crosses the OT/IT boundary or traverses the DMZ. 3525 
Once established, baseline information can be used as a reference point to identify deviations 3526 
in network traffic. Not all deviations are malicious; for instance, equipment changes, software 3527 
updates, and process modifications can all alter normal traffic patterns. Because of this, 3528 
baseline maintenance should account for authorized changes to the environment. Baselines 3529 
should also be reviewed and updated when significant changes are made to the OT 3530 
environment, such as the addition of new devices, network reconfigurations, or changes to 3531 
operational processes.  3532 
Supplemental guidance can be found in the following documents:  3533 
• SP 800-94, Guide to Intrusion Detection and Prevention Systems (IDPS)  3534

<!-- page 116 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
98 
• IR 8219, Securing Manufacturing Industrial Control Systems: Behavioral Anomaly 3535 
De
tection  3536
 
4.3.1.5. Physical and Environmental Monitoring 3537 
Physical access monitoring provides log sources for tracking personnel movement and detecting 3538 
unauthorized access to sensitive areas. Monitoring the physical environment contributes to 3539 
broader situational awareness and supports both safety and incident response activities across 3540 
physical and cyber domains. 3541 
Organizations should also deploy systems to track and monitor physical access and activities 3542 
across key sites and facilities. Examples of this include:  3543 
• Access monitoring systems. Access monitoring systems include electronic surveillance 3544 
capabilities, such as still and video cameras, sensors, and identification systems (e.g., 3545 
badge readers, biometric scanners, electronic keypads). Such devices typically do not 3546 
prevent access to a particular location. Rather, they store and record either the physical 3547 
presence or the lack of physical presence of individuals, vehicles, animals, or other 3548 
physical entities. Adequate lighting should be provided based on the type of access 3549 
monitoring device deployed. These systems can also sometimes alert or initiate action 3550 
upon detecting unauthorized access.  3551 
• People and asset tracking. Locating people and vehicles within a facility can be 3552 
important for both safety and security. Asset location technologies can be used to track 3553 
the movements of people and vehicles to ensure that they remain in authorized areas, 3554 
identify personnel who may need assistance, and support emergency response.  3555 
While these systems are critical to preventing unauthorized physical access to OT facilities, they 3556 
also provide a key data source to support the investigation of cybersecurity incidents. Systems 3557 
such as badge readers, biometric scanners, and electronic door controllers can generate 3558 
timestamped access event logs that record who accessed a given area, when, and whether 3559 
access was granted or denied. These logs are valuable not only for physical security purposes 3560 
but also as a data source that can be correlated with cyber activity to detect threats that span 3561 
both domains. 3562 
4.3.2. Anomalies and Events (DE.AE) 3563 
To effectively detect cyber threats, organizations must be able to collect and analyze diverse 3564 
data from logs, devices, hosts, users, and network monitoring tools. This includes centralized 3565 
data collection and storage, the ability to correlate and analyze information across multiple 3566 
sources, the ability to assess activity against known adversary behaviors identified in current 3567 
cyber threat intelligence (CTI), and properly staffed analysts who can investigate alerts and 3568 
anomalies. 3569

<!-- page 117 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
99 
4.3.2.1. Data Aggregation and Analysis 3570 
Organizations should define how security events are integrated into their security operations 3571 
center (SOC) or network operations center (NOC) functions. In some organizations, OT 3572 
monitoring is handled by a dedicated OT security team, while in others it is integrated into an 3573 
existing IT SOC or NOC. Regardless of the model, the roles and responsibilities for monitoring, 3574 
triaging, and escalating OT network alerts should be clearly defined and documented. 3575 
Organizations should develop a plan to identify their available log sources and establish a 3576 
centralized collection and aggregation capability that consolidates them into a unified platform 3577 
for analysis, correlation, and retention. A SIEM platform can accomplish this by providing 3578 
organizations with a single location to aggregate logs, apply correlation rules, and maintain a 3579 
searchable record of security-relevant activities across the OT environment. 3580 
A significant challenge in SOC/NOC integration is the context gap between security analysts and 3581 
OT operations personnel. Security analysts may have limited familiarity with OT protocols, 3582 
equipment, and operational processes, which can make it difficult to accurately assess the 3583 
significance of an alert without an operations context. Conversely, OT operations personnel 3584 
may not have the security expertise to recognize threat patterns or assess the implications of 3585 
anomalous network activity. Effective SOC/NOC integration requires close collaboration 3586 
between security and operations teams, and organizations should establish clear escalation 3587 
paths that involve operations personnel in the triage and assessment of OT network alerts 3588 
before containment or response actions are taken. 3589 
Physical access, network, and host logs should be forwarded to the SIEM to enable this type of 3590 
time-based correlation. Defining alert logic around physical-cyber event sequences adds a 3591 
detection layer that is difficult for an adversary to avoid without simultaneously defeating 3592 
physical access controls and operating within expected cyber behavioral patterns. 3593 
Organizations should work with both physical security and OT operations teams to define what 3594 
normal physical-cyber activity sequences look like so that anomalies can be identified with 3595 
appropriate context. 3596 
4.3.2.2. Identifying Adverse Events and Anomalies 3597 
Organizations should understand various events and anomalies as well as their potential 3598 
impacts on systems and the environment to establish an effective detection capability. Within 3599 
any environment, numerous non-malicious and potentially malicious events and anomalies 3600 
occur almost continuously. Some examples of common events include:  3601 
• Information events  3602 
o Multiple failed logon attempts  3603 
o Locked-out accounts  3604 
o Unauthorized creation of new accounts  3605

<!-- page 118 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
100 
o Unexpected remote logons (e.g., logons of individuals who are on vacation, 3606 
remote logon when the individual is expected to be local, remote logon for 3607 
maintenance support when no support was requested)  3608 
o Cleared event logs  3609 
o Unexpectedly full event logs  3610 
o Antivirus or IDS alerts 3611 
o Disabled antivirus or other security controls  3612 
o Requests for information about the system or architecture (e.g., social 3613 
engineering or phishing attempts)  3614 
• Operational events  3615 
o Unauthorized configuration changes  3616 
o Unauthorized patching of systems  3617 
o Unplanned shutdowns  3618 
• Physical access events  3619 
o Physical intrusions  3620 
• Networking events  3621 
o Unexpected communication, including new ports or protocols being used 3622 
without appropriate change management  3623 
o Unusually heavy network traffic  3624 
o Unauthorized devices connecting to the network  3625 
o Unauthorized communication to external IPs  3626 
Organizations should consider that not all events and anomalies are malicious or require 3627 
investigation. Organizations should define incident alerting thresholds and response 3628 
requirements for the events and anomalies that affect their systems and environment to 3629 
establish an efficient incident detection capability. To reduce false positive and nuisance 3630 
alarms, organizations should establish their OT alerting thresholds based on baselines of normal 3631 
network traffic, data flows, and human and OT process behavior.  3632 
Additionally, OT components are often physically remote and not continually staffed. Alerting 3633 
thresholds may need to account for the alert response time as well as the speed of the physical 3634 
process itself. Some OT processes can transition to an unsafe or damaging state within seconds 3635 
of a malicious or anomalous command being executed. Alert prioritization and escalation paths 3636 
should reflect these physical process response times to ensure that the most time-critical alerts 3637 
are immediately routed to personnel with the authority and ability to take action. 3638 
Organizations should consider collecting and correlating event data from multiple sources and 3639 
sensors using automated mechanisms to improve detecting and alerting capabilities. For 3640 
example, a centralized intrusion detection system could accept data feeds and logs from 3641

<!-- page 119 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
101 
multiple devices and network segments to identify organization- or environment-specific events 3642 
and sound an alarm. Detection tools should also be integrated with asset management tools. 3643 
This integration can provide additional context to an event (e.g., system location, firmware 3644 
version, system criticality) to help an organization determine the event’s impact.  3645 
Supplemental guidance can be found in the following documents:  3646 
• SP 800-92, Guide to Computer Security Log Management  3647 
• SP 800-94, Guide to Intrusion Detection and Prevention Systems  3648 
• SP 1800-7, Situational Awareness for Electric Utilities  3649 
4.3.2.3. Integrating Cyber Threat Intelligence (CTI) 3650 
CTI provides analysts with external context about recent adversary behaviors, tactics, 3651 
techniques, and procedures (TTPs) that can be used to enrich alert triage and improve 3652 
detection capabilities. Organizations should identify and integrate CTI sources to ensure that 3653 
they monitor for known threat actor behavior and indicators of compromise (IoCs). 3654 
Organizations should identify and establish access to CTI sources relevant to their industry 3655 
sector and the specific technologies deployed in their environment, including vendor feeds, 3656 
sector-specific information-sharing and analysis centers (ISACs), and government advisories. 3657 
Organizations should develop a process for evaluating incoming CTI for relevance and 3658 
actionability, recognizing that not all intelligence will be immediately usable and that some may 3659 
only inform longer-term detection improvements or patch planning. 3660 
The MITRE ATT&CK for ICS framework provides a structured knowledge base of adversary 3661 
tactics and techniques observed in attacks against industrial control systems. Incorporating 3662 
ATT&CK for ICS into analyst workflows provides a common language for describing and 3663 
categorizing observed activity, enables analysts to map alerts and events to known adversary 3664 
behavior patterns, and supports the identification of detection gaps where monitoring 3665 
coverage is limited.  3666 
An event that appears benign in isolation may take on considerably more significance when 3667 
mapped to known adversary techniques and considered alongside CTI relevant to the 3668 
organization’s sector and environment. Organizations should establish processes for routinely 3669 
cross-referencing active alerts and observed anomalies against current CTI and relevant 3670 
ATT&CK for ICS techniques so that individual events can be evaluated independently and with 3671 
the broader threat context relevant to their environment. For example, an individual alert for a 3672 
stop in controller operation may appear routine, but when observed in sequence with a 3673 
program download followed by a transition back to run mode, this sequence can be associated 3674 
with adversary efforts to impair process control. 3675 
4.3.2.4. Emerging Detection Capabilities 3676 
Technologies (e.g., AI, ML, digital twins) offer advanced detection capabilities that could 3677 
complement traditional signature-based and threshold-based detection approaches in OT 3678

<!-- page 120 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
102 
environments. While adopting these technologies for OT anomaly detection remains limited in 3679 
current industry practice, organizations should understand both their potential benefits and the 3680 
security considerations associated with their implementation. 3681 
ML-based anomaly detection models could be trained on historical data from the OT 3682 
environment to establish a baseline of normal behavior and help identify subtle deviations that 3683 
conventional threshold-based alerts may miss. Digital twins, which maintain a synchronized 3684 
virtual representation of physical OT assets or processes, could also be used to compare 3685 
expected behavior with observed conditions and flag potentially anomalous activity. 3686 
Organizations should weigh several considerations before evaluating and implementing these 3687 
technologies. Training and operating AI/ML models requires access to extensive historical and 3688 
live process data, which expands data collection and retention needs beyond conventional 3689 
monitoring. The integrity of the training data is also critical, as a model trained on an 3690 
unrepresentative or compromised baseline may produce unreliable results. These models can 3691 
also behave non-deterministically and produce different outputs across runs or model versions 3692 
in ways that may complicate validation and consistency expectations.  3693 
Beyond AI/ML models specifically, digital twins carry their own distinct considerations. Their 3694 
bidirectional connectivity to physical systems for synchronization creates a new attack surface 3695 
that warrants additional boundary protections in the OT environment. If the twin’s underlying 3696 
model drifts out of sync with the physical asset’s actual state, it may also fail to flag genuine 3697 
anomalies or generate false positives. A compromised twin could further serve as a deception 3698 
vector, allowing an adversary to manipulate its model or inputs to mask anomalies in the 3699 
physical system it is meant to monitor. 3700 
4.4. Respond (RS) 3701 
The Respond Function supports activities for containing a cybersecurity incident when it occurs. 3702 
4.4.1. Incident Response 3703 
Organizations should establish an OT cybersecurity incident response (IR) function that includes 3704 
planning, detection, analysis, containment, and reporting activities in the event of a 3705 
cybersecurity incident. The IR function requires establishing several cybersecurity capabilities, 3706 
including incident management, forensic analysis, vulnerability management, and response 3707 
communication. Stakeholders should also review and approve the plan.  3708 
NIST IR 8428, Digital Forensics and Incident Response (DFIR) Framework for Operational 3709 
Technology (OT), provides a more tailored discussion of OT IR challenges and associated 3710 
guidance. This includes guidance on the composition and roles of incident response teams, 3711 
tools and resources needed to support IR activities, training requirements, and an overall 3712 
framework for managing cybersecurity incidents. This resource can support and inform the 3713 
development of IR capabilities within an organization.   3714

<!-- page 121 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
103 
Supplemental guidance for implementing incident response can be found in the following 3715 
documents:  3716 
• IR 8428, Digital Forensics and Incident Response (DFIR) Framework for Operational 3717 
Technology (OT) 3718 
• SP 800-61r2, Computer Security Incident Handling Guide  3719 
• SP 800-83r1, Guide to Malware Incident Prevention and Handling for Desktops and 3720 
Laptops  3721 
• SP 800-100, Information Security Handbook: A Guide for Managers  3722 
• CISA, Handling Destructive Malware  3723 
• Federal Emergency Management Agency (FEMA) National Incident Management System 3724 
(NIMS)  3725 
• FEMA National Preparedness Goal 3726 
• SANS ICS Cybersecurity Field Manuals, Volume 3 3727 
• Patrick Kral. Incident Handler's Handbook. December 2011, SANS Institute 3728 
• ICS4ICS Incident Command System for Industrial Control Systems 3729 
(https://www.ics4ics.org) 3730 
4.4.2. Incident Response Planning 3731 
As part of building the IR function, the OT cybersecurity department should create an incident 3732 
response plan that applies to all OT personnel, networks, systems, and data. The purpose of the 3733 
incident response capability is to determine the scope and risk of cybersecurity incidents, 3734 
respond appropriately to them, communicate the incidents to all stakeholders, and reduce their 3735 
future impacts. Response plans should be measured against the service being provided, not just 3736 
the compromised system. Organizations should consider a systematic approach to response 3737 
planning, such as the process described in CISA’s Cybersecurity Incident and Vulnerability 3738 
Response Playbooks [CISA-CIVR]. 3739 
During the preparation of the incident response plan, input should be obtained from various 3740 
stakeholders, including operations, engineering, IT, system support vendors, management, 3741 
organized labor, legal, and safety. Common IR planning steps include preparation, detection 3742 
and analysis, containment, recovery, post-incident activity, communication, and coordination. . 3743 
Personnel should be trained on where to find the response plan and the actions to take as part 3744 
of an incident response. Organizations should also regularly review and update their response 3745 
plans. Response plans should be documented on paper or on an offline system (e.g., air-3746 
gapped) that cannot be compromised during a cyber attack. 3747 
Response plans include personnel roles and responsibilities as well as: 3748 
• Identification and classification of incidents. Various types of OT incidents should be 3749 
identified and classified based on their potential impact so that a proper response can 3750

<!-- page 122 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
104 
be formulated for each. This classification may inform who needs to be notified and 3751 
wha
t response and recovery actions should be taken. Additionally, many sectors have 3752
 
re
gulatory requirements regarding what constitutes a cybersecurity event and the 3753
 
ne
cessary reporting that must be done when one occurs. Organizations should ensure 3754
 
t
hat the classification procedures adequately address possible regulatory requirements.  3755
 
• Response actions. Incident response can range from doing nothing to performing a full 3756 
system shutdown, which could result in a shutdown of the physical process. The 3757 
response taken will depend on the type of incident and its effect on the OT system and 3758 
the physical process being controlled. A written plan documenting the response to each 3759 
incident type should be prepared. This will provide guidance if confusion or stress arise 3760 
due to the incident. This plan should include step-by-step actions to be taken by various 3761 
stakeholders. 3762 
• Reporting requirements should be documented along with contact information and the 3763 
reporting format to reduce confusion.  3764 
• Response actions should also include steps for detection, analysis, containment, 3765 
eradication, recovery, and post-incident activity. Some considerations for OT may 3766 
include:  3767 
o Determining a priority, such as returning to normal operations as quickly as 3768 
possible, or performing an investigation and preserving forensic data 3769 
o Communicating with the incident response team 3770 
o Disconnecting infected systems from the network  3771 
o Physically isolating operationally independent networks (e.g., enterprise from 3772 
control, control from safety)  3773 
o Transitioning to manual operations  3774 
o Resourcing for additional operations support to manually validate data  3775 
o Notifying management, public relations, and/or outside companies and agencies 3776 
as required  3777 
o Defining appropriate approaches, procedures, and tools to eradicate threat 3778 
actors from OT environments and devices  3779 
o Identifying the necessary capabilities to collect evidence for OT devices, including 3780 
what tools and systems would be used and what evidence would be collected 3781 
• Requirements for engaging external incident response teams to support the response 3782 
efforts should be defined, and the plan should clarify who has the authority to bring in 3783 
the external team and establish rules and procedures for providing access to 3784 
organizational resources.  3785 
Even when preventive maintenance is performed, equipment malfunctions and failures remain 3786 
common in industrial and OT environments. Because many systems were designed and 3787 
deployed before current cybersecurity threats were widely considered, abnormal behavior or 3788

<!-- page 123 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
105 
equipment failure may initially be attributed to routine mechanical, electrical, software, or 3789 
process-related causes rather than to potential malicious activity. In addition, OT incidents 3790 
often lack clear initial cyber indicators (e.g., ransomware messages, malware IOCs), especially in 3791 
organizations without strong OT monitoring and detection capabilities. When outages or 3792 
disruptions occur with unknown root causes, organizations may suspect a cyber intrusion and 3793 
begin initial incident analysis steps before a cyber incident has been clearly confirmed. 3794 
As a result, organizations may prioritize the rapid restoration, replacement, or rebuilding of 3795 
affected components, inadvertently destroying or altering valuable forensic data. Operations, 3796 
maintenance, engineering, and cybersecurity personnel should coordinate to establish practical 3797 
procedures for identifying failures that may warrant additional cyber-related review, preserving 3798 
relevant data where feasible, and supporting incident response while minimizing operational 3799 
burden and unnecessary false positives. Historical failure data can serve as a useful starting 3800 
point for establishing a baseline or normal failure threshold for critical devices. NIST IR 8428 3801 
provides additional guidance on event identification, particularly the need for situational 3802 
awareness among both cybersecurity analysts and OT engineers when alerts or anomalies are 3803 
detected. Figure 16 illustrates a workflow that demonstrates how incidents may originate from 3804 
an SOC analyst or operational staff (referred to as the Facility Control Room in the figure), 3805 
thereby requiring coordination between both groups to ensure that incidents are properly 3806 
identified.  3807 
 3808 
Fig. 16. Initial identification and reporting [IR8428] 3809 
The plan should also indicate requirements for the timely replacement of components in the 3810 
case of an emergency. If possible, replacements for hard-to-obtain critical components should 3811 
be kept in inventory. 3812 
In addition to developing incident response plans, organizations may want to develop 3813 
predefined playbooks for common OT scenarios, such as ransomware, insider threats, and 3814 
malware on critical OT devices. Playbooks can provide more detailed, step-by-step guidance on 3815

<!-- page 124 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
106 
how to respond to specific scenarios, including processes for forensic analysis and threat 3816 
eviction, which can improve response actions and minimize operational impacts. 3817 
IR plans are only effective if personnel know about them and receive periodic training. Tabletop 3818 
exercises are important to ensure that staff understand the plan and to determine whether the 3819 
plan effectively covers and informs key decisions and processes through a scenario. Periodic 3820 
exercises should be performed across different hypothetical scenarios to evaluate the 3821 
effectiveness of the IR plan and identify where the plan should be improved. 3822 
Additional information with specific examples for OT incident response is also provided in NIST 3823 
IR 8183A, Cybersecurity Framework Manufacturing Profile Low Impact Level Example 3824 
Implementations Guide [IR8183A], Sec. 6.2.4.5. 3825 
4.4.3. Incident Management (RS.MA) 3826 
If an incident is discovered, organizations should assess the risk to the OT environment to 3827 
evaluate the attack’s effects and available response options. For example, one possible 3828 
response option is to physically isolate the system under attack. However, this may negatively 3829 
affect the OT and may not be possible without compromising operational performance or 3830 
safety. It may also affect the organization’s ability to conduct incident response activities if the 3831 
system is remote or if remote personnel are assisting. 3832 
When responding to events, organizations should attempt to capture the details required to 3833 
execute the documented response plans. This may help organizations identify gaps or potential 3834 
opportunities for improvement in the response plan during the post-incident review process. 3835 
Due to the time sensitivity of response efforts, organizations may want to consider other 3836 
techniques (e.g., reviewing logs, reviewing video footage captured during the response 3837 
activities, interviewing response personnel) if capturing execution details impacts safety or 3838 
increases the time to complete the response plan.  3839 
Organizational response activities are improved by incorporating lessons learned from current 3840 
and previous detection and response activities. Organizations should designate one or more 3841 
individuals to be responsible for documenting and communicating response actions to the 3842 
incident response team, which can later be reviewed for lessons learned. 3843 
4.4.4. Incident Analysis (RS.AN) 3844 
Cybersecurity incidents are analyzed to ensure effective response and recovery activities that 3845 
are consistent with the detection process and the response plan. Analysis includes reviewing 3846 
notifications, determining whether an investigation is required, understanding potential 3847 
impacts, performing forensics, categorizing the incident consistent with the response plan, and 3848 
analyzing disclosed vulnerabilities.  3849 
When determining the overall impact of a cybersecurity incident, consider the dependencies of 3850 
OT and its resulting impact on operations. For example, an OT system may depend on IT for 3851 
business applications, so an incident on the IT network can result in an OT disconnect or 3852 
shutdown. 3853

<!-- page 125 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
107 
Traditional IT forensic tools may not work on OT systems and devices. Organizations should 3854 
therefore establish and test procedures for performing necessary forensic activities in OT 3855 
environments, including the collection of configuration data and the extraction and validation 3856 
of programs. If an organization does not have adequate resources or capabilities to conduct OT 3857 
forensics, consider engaging external organizations to perform forensic analysis.  3858 
Organizations should identify and classify cyber and non-cyber incidents that affect the OT 3859 
environment in accordance with the incident response plan. When developing the OT incident 3860 
response plan, potential classes of incidents could include accidental actions taken by 3861 
authorized personnel, targeted malicious attacks, and untargeted malicious attacks.  3862 
Supplemental guidance for the response analysis controls can be found in the following 3863 
documents:  3864 
• SP 800-86, Guide to Integrating Forensic Techniques into Incident Response 3865 
• IR 8428, Digital Forensics and Incident Response (DFIR) Framework for Operational 3866 
Technology (OT) 3867 
4.4.5. Incident Response Reporting and Communication (RS.CO) 3868 
Responding to a cybersecurity incident includes coordinating with internal and external 3869 
stakeholders. An incident response team should be assembled. Depending on the complexity 3870 
and impact of the incident, the incident response team could consist of one or many individuals 3871 
who have been trained on incident response.  3872 
Prior to an incident, organizations should consider how to communicate with response 3873 
personnel and external entities, including:  3874 
• Developing an email distribution list for incident response  3875 
• Leveraging an emergency notification system  3876 
• Establishing backup communication plans for radio, phone, or email if primary 3877 
communication systems fail  3878 
• Designating a spokesperson for external communications  3879 
• Designating a scribe for internal incident communications 3880 
The response plan should include a detailed list of organizations and personnel that should be 3881 
contacted for incident response and reporting under various circumstances. Each individual 3882 
should be assigned roles that are required for incident response, which could include incident 3883 
commander; operations, planning, logistics, or finance/administration section chief or member; 3884 
and public information, safety, or liaison officer. The personnel responsible for responding to an 3885 
incident should be informed of and trained on their responsibilities. 3886 
To support a response in an OT environment, an organization should consider including the 3887 
following personnel in the response plan:  3888 
• Internal Resources  3889

<!-- page 126 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
108 
o Designated Incident Commander  3890 
o Operations leadership  3891 
o Safety personnel  3892 
o On-call OT systems personnel  3893 
o On-call IT personnel  3894 
o Physical security personnel  3895 
o Administrative personnel  3896 
o Procurement personnel  3897 
o Public relations personnel  3898 
o Legal personnel  3899 
o Human resources 3900 
• External Industry Partners  3901 
o OT technical support (e.g., vendors, integrators)  3902 
o Operational supply chain (e.g., suppliers, customers, distributors, business 3903 
partners)  3904 
o External incident response team  3905 
o Surge support  3906 
o Impacted community (e.g., facility neighbors)  3907 
o Regulatory organizations 3908 
Organizations should establish procedures to identify and satisfy all applicable incident 3909 
reporting requirements, including those necessary to support federal statutes, executive policy, 3910 
agency directives, sector-specific regulations, contractual requirements, and other legal 3911 
authorities. For organizations that support critical infrastructure, reporting procedures should 3912 
align with the roles and responsibilities established under National Security Memorandum 22 3913 
(NSM-22) and applicable guidance from CISA and the appropriate Sector Risk Management 3914 
Agency (SRMA). 3915 
Legal departments can often assist with developing non-disclosure agreements or other 3916 
contracts if an organization plans to utilize external resources for incident response. It may be 3917 
beneficial to develop these contracts before an incident occurs. Private companies can be held 3918 
on retainer in case of an OT incident. 3919 
4.4.6. Incident Mitigation (RS.MI) 3920 
Mitigation activities are meant to prevent the expansion of an incident, alleviate its effects, and 3921 
resolve the incident, and they should be consistent with the response plan. OT components are 3922 
often physically remote and not continually staffed. For these cases, consider how the 3923

<!-- page 127 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
109 
organization would respond during an incident and the additional time required to coordinate 3924 
the response. The system may need to be designed to minimize impacts until personnel arrive 3925 
on-site (e.g., remote shutdowns, disconnects).  3926 
Cyber incident mitigation and eradication may involve process shutdowns, communication 3927 
disconnects, or emergency isolation of affected systems that may impact operations and 3928 
therefore require approval from senior leaders. The organization should explore these possible 3929 
mitigation and eradication procedures, ensure that their broader impacts on operations are 3930 
understood, and ensure that the processes and approvals required to authorize these decisions 3931 
are well-defined. Human safety must take precedence over system preservation when 3932 
implementing these mitigations, particularly during incidents that pressure system operators to 3933 
isolate systems quickly (e.g., ransomware), increasing the risk of abrupt decisions that do not 3934 
account for the physical process state. When implementing these mitigations, organizations 3935 
should consider not only the core OT devices but also the devices and platforms used to 3936 
manage the OT environment. 3937 
4.5. Recover (RC) 3938 
Timely recovery to normal operations after a cybersecurity incident is critical. The Recover 3939 
Function addresses developing and implementing activities to maintain system resilience and 3940 
ensure the timely restoration of capabilities and services affected by a cybersecurity incident. 3941 
4.5.1. Recovery Planning  3942 
The organization should establish the capability to recover from cybersecurity incidents and to 3943 
restore the assets and services that were impaired by the cybersecurity incident to a pre-cyber-3944 
incident state. This capability typically includes the following tasks:  3945 
• Define recovery objectives when recovering from disruptions. For example, the recovery 3946 
capability should prioritize human and environmental safety before restarting the OT 3947 
operation impaired by the cybersecurity event.  3948 
• Develop a site disaster recovery plan (DRP) and business continuity plan (BCP) to 3949 
prepare the OT organization to respond appropriately to significant disruptions in their 3950 
operations due to the cybersecurity incident.  3951 
• Maintain an inventory of necessary spare devices to restore operations, including on-3952 
site spares and supplier contracts for expedited delivery.  3953 
• Establish processes for restoring relevant OT systems’ state, data, configuration files, 3954 
and programs from backups in a timely manner. 3955 
• Establish recovery processes and procedures that will be executed to restore the OT 3956 
assets and services affected by cybersecurity incidents.  3957 
• Establish communication plans to coordinate restoration activities with internal and 3958 
external stakeholders and the executive management team.  3959

<!-- page 128 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
110 
• Establish communication plans to manage public relations.  3960 
• Establish a lessons-learned task as part of the recovery process to continuously improve 3961 
cybersecurity capabilities (e.g., vulnerability management, cybersecurity operations, 3962 
incident response, recovery).  3963 
• Test these plans at reasonable intervals that are appropriate for the organization. 3964 
Business continuity planning addresses the overall issue of maintaining or reestablishing 3965 
production in the case of an interruption. Recovery time can vary widely depending on the 3966 
cause. For example, a natural disaster may take days, weeks, or months to recover from, while 3967 
a malware infection or a mechanical or electrical failure may take only minutes or hours. BCPs 3968 
are often written to cover many types of incidents that involve several different disciplines. The 3969 
BCP for cybersecurity incidents should broadly cover long-term outages (e.g., disaster recovery) 3970 
and short-term outages that require operational recovery. It is important to work with physical 3971 
security to develop the BCP for cybersecurity incidents. This collaboration with physical security 3972 
should include identifying critical equipment and the associated countermeasures in place to 3973 
prevent incidents. Before creating a BCP to address potential outages, it is important to specify 3974 
the recovery objectives for the various systems and subsystems involved based on typical 3975 
business needs.  3976 
There are two distinct types of objectives: system recovery and data recovery. System recovery 3977 
involves restoring communication links and processing capabilities and is usually specified in 3978 
terms of a recovery time objective (RTO). Management should define the acceptable RTO, and 3979 
technical personnel should work to achieve that target. Data recovery involves recovering data 3980 
that describes past production or product conditions and is usually specified in terms of a 3981 
recovery point objective (RPO). This is defined as the time for which an absence of data can be 3982 
tolerated. The RTO and RPO may justify investment in spare inventory if recovery objectives 3983 
cannot be met by other means. Once the recovery objectives are defined, a list of potential 3984 
interruptions should be created, and the recovery procedure should be developed and 3985 
described. A contingency plan is then created for the variety of potential interruptions. The 3986 
contingency plan should be reviewed with managers to ensure that the cost of meeting the 3987 
contingency plan is approved. For many smaller-scale interruptions, a critical spares inventory 3988 
will likely prove adequate to meet the recovery objectives. For larger-scale recovery, vendor 3989 
relationships will likely be leveraged. For all types of recovery, backups are critical.  3990 
A disaster recovery plan (DRP) is a documented process or set of procedures that comprises a 3991 
comprehensive statement of recovery actions to be taken before, during, and after a disaster. 3992 
The DRP is ordinarily documented in both electronic and paper form to ensure that it is readily 3993 
available during any type of disaster (e.g., natural, environmental, caused by humans). 3994 
Organizations should develop, maintain, and validate disaster recovery plans for their 3995 
environments to help minimize the impact of an event by reducing the time required to restore 3996 
capabilities. Organizations may already have some emergency response plans in place and 3997 
should consider leveraging existing plans when developing a response plan for cybersecurity 3998 
events.  3999

<!-- page 129 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
111 
The organization should have a means for prioritizing recovery activities. This prioritization may 4000 
leverage existing documentation, such as risk assessments or startup procedures. For example, 4001 
the focus may be on recovering the systems that support critical utilities before those that 4002 
support manufacturing, based on the order of start-up activities.  4003 
Testing recovery plan procedures for OT components may be difficult due to operational and 4004 
safety requirements. Organizations may need to determine whether “bench tests” or other 4005 
offline testing is feasible to confirm recovery procedures for OT components. At a minimum, 4006 
organizations should verify the integrity of the backups if a full recovery test cannot be 4007 
performed. 4008 
Supplemental guidance for recovery planning can be found in the following documents:  4009 
• SP 800-184, Guide for Cybersecurity Event Recovery  4010 
• SP 800-209, Security Guidelines for Storage Infrastructure 4011 
• IR 8183A, Cybersecurity Framework Manufacturing Profile Low Impact Level Example 4012 
Implementations Guide  4013 
• SP 800-34r1, Contingency Planning Guide for Federal Information Systems  4014 
4.5.2. Incident Recovery Execution (RC.RP) 4015 
When recovering from events, organizations should attempt to capture details associated with 4016 
the execution of the documented recovery plans. Capturing execution details may help 4017 
organizations during the post-incident review process to determine whether any gaps or 4018 
potential opportunities for improvement in the recovery plan should be considered. Due to the 4019 
time sensitivity of recovery efforts, organizations may want to consider other techniques (e.g., 4020 
reviewing logs, reviewing video footage captured during the recovery activities, interviewing 4021 
recovery personnel) if capturing execution details compromises safety or delays completion of 4022 
the recovery plan.  4023 
OT systems often have strict sequencing and timing requirements for restart that must be 4024 
followed to avoid unsafe conditions. Recovery plans should document these dependencies, 4025 
including restart order and required validation checks. These plans should be developed in 4026 
coordination with control engineers who understand the consequences of restoring systems 4027 
out of sequence. 4028 
Organizations should also protect OT backups from tampering (e.g., encryption) or deletion by 4029 
storing them in a production environment using immutable mechanisms that cannot be altered 4030 
or destroyed by malware. Recovery plans should specify how backup integrity is validated 4031 
before restoration begins to ensure that clean backups are not inadvertently replaced with 4032 
compromised data during the recovery process.  4033

<!-- page 130 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
112 
4.5.3. Recovery Communication (RC.CO) 4034 
Restoration activities are coordinated with internal and external parties. In addition to 4035 
operational recovery, an organization may need to manage public relations and repair its 4036 
reputation.  4037 
A list of internal and external resources for recovery activities should be developed as part of 4038 
the recovery planning effort. During an event, this list should be used to get all necessary 4039 
personnel on-site, as required, to recover within the RTO and RPO.  4040 
• Internal Communications  4041 
o OT personnel  4042 
o IT personnel  4043 
o Procurement  4044 
o Management with appropriate authority to approve the cost of recovery  4045 
o Storage or warehouse personnel  4046 
• External Communications  4047 
o OT vendors  4048 
o Security companies that may be held on retainer for response and recovery 4049 
efforts  4050 
o Storage or warehouse personnel  4051 
o Internet service providers  4052 
o Owners of the attacking systems and potential victims  4053 
During or after a cyber incident, the primary communication infrastructure may be unavailable 4054 
or compromised. Organizations should develop and maintain a backup communication plan to 4055 
ensure that coordination can continue through alternative means. A PACE plan (Primary, 4056 
Alternate, Contingency, and Emergency) provides a structured framework for defining 4057 
communication methods at each level of degradation. Organizations should pair this with pre-4058 
established point-of-contact trees to ensure that personnel know who to reach and what 4059 
mechanism to use when primary channels become unavailable. Supply chain partners and 4060 
critical vendors should also be included in out-of-band communication planning, as their 4061 
support may be essential to recovery and their primary communication channels may be 4062 
similarly affected. 4063 
Supplemental guidance for recovery communications can be found in SP 800-184, Guide for 4064 
Cybersecurity Event Recovery. 4065

<!-- page 131 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
113 
5. OT Cybersecurity Architecture 4066 
When designing a security architecture for an OT environment, it is generally recommended to 4067 
separate the OT network from the enterprise network. The nature of network traffic on these 4068 
two network types differs significantly. Internet access, email, and remote access are typically 4069 
permitted on the enterprise network but not allowed on OT networks. There may also be 4070 
differences in the degree of rigor associated with enterprise and OT environment change 4071 
control procedures. Additionally, using the enterprise network for OT communication protocols 4072 
could expose OT components to cyber attacks, such as the denial of service, adversary-in-the-4073 
middle, or other network-based attacks. Utilizing separate networks allows for greater flexibility 4074 
to address the security and performance requirements of each environment independently. 4075 
This separation should extend beyond the boundary between enterprise and OT networks. 4076 
Within the OT environment itself, networks that serve different functions and purposes warrant 4077 
their own segmentation. Operational networks (i.e., those that carry process control traffic 4078 
between supervisory systems and field devices) have fundamentally different traffic 4079 
characteristics, availability requirements, and security properties than networks dedicated to 4080 
management functions, such as configuration, patching, and access control. Combining these 4081 
on a shared network infrastructure may introduce risk to operational traffic from management 4082 
activity, limit the ability to apply independent security policies to each function, and create 4083 
conditions in which a security event that affects one network type can propagate to the other. 4084 
Additionally, external parties (e.g., vendors, other third parties) should have access paths that 4085 
are architecturally separate from both operational and internal management traffic with their 4086 
own credential stores, entry points, and enforcement boundaries so that the trust level 4087 
extended to external access does not inadvertently reach internal functions through shared 4088 
infrastructure. 4089 
Practical considerations (e.g., digital transformation, the cost of OT installation, maintaining a 4090 
homogenous network infrastructure) often mean that connections are required between OT 4091 
networks and other IT networks. These connections represent additional risk, and organizations 4092 
should seek to minimize them and implement additional security controls where they exist. This 4093 
section identifies a representative set of functions, security controls, and architecture patterns 4094 
for organizations to consider when engineering their OT environments to support the 4095 
cybersecurity objectives described in Sec. 4. 4096 
5.1. Summary of Cybersecurity Capabilities 4097 
This section presents the functions and architectural patterns that support a defensible OT 4098 
cybersecurity architecture, organized into three categories. 4099 
OT/ICS system management (Table 7) and security controls (Table 8) are functions: discrete 4100 
operational capabilities that produce a specific security-relevant outcome. System management 4101 
functions establish and maintain visibility into managed assets and govern the introduction of 4102 
change. Security controls enforce protection at points where access, transfer, or observation 4103 
occurs. Architecture patterns (Table 9) are distinct from these functions. Rather than 4104 
performing an operation, an architecture pattern defines the structural context in which 4105

<!-- page 132 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
114 
functions are deployed and enforced, determining where a given function applies and what it is 4106 
permitted to reach. 4107 
Each function and pattern addresses one or more outcomes defined in the OT Cybersecurity 4108 
Outcomes and Objectives framework referenced throughout this document and was selected 4109 
for its role in mitigating risk characteristics of OT environments, including insufficient asset 4110 
visibility, uncontrolled configuration drift, ungoverned content ingress, propagation of 4111 
credential compromise across trust domains, and the absence of independent, tamper-resistant 4112 
monitoring. 4113 
No individual function or pattern is sufficient in isolation. System management and security 4114 
controls are interdependent: system management provides the visibility and governance 4115 
records that security controls act on. Architecture patterns establish the structural conditions 4116 
that require clearly defined boundaries, controlled and auditable access paths, and assurance 4117 
that compromise of one component does not silently defeat protections implemented 4118 
elsewhere. 4119 
Table 7 through Table 9 identify each function and architecture pattern, together with a 4120 
description and reference to related guidance presented elsewhere in this document. Section 4121 
5.2 presents representative example architectures demonstrating how these may be 4122 
composed, sequenced, and enforced in combination. 4123 
Not every item identified in Table 7 through Table 9 will be applicable to every environment. 4124 
Asset owners and operators should evaluate applicability against the criticality of the assets 4125 
being protected, the operational constraints of the environment, and organizational risk 4126 
tolerance, consistent with the risk-informed approach described throughout this document. 4127 
Table 7. Example OT/ICS system management 4128 
Function Description 
Asset Management Building on the asset inventory concepts addressed in Sec. 4.1.1.1, 
the asset management function maintains a continuously updated 
record of every managed device: its identity, firmware, configuration, 
and security state. 
Industrial Code 
Management 
Changes to industrial code should move through a defined workflow 
that includes authoring or receipt, review, approval, and controlled 
deployment, extending the secure coding and change-control 
practices discussed in Sec. 4.2.3.4. 
Configuration 
Management 
Database 
The CMDB is the governance record for the asset inventory, 
reflecting the configuration management concepts addressed in Sec. 
4.2.3.1. 
Work Order 
Integration 
The work order function integrates with asset management, code 
management, and access management to create a complete audit 
record for every authorized touch to a managed asset, consistent 
with the maintenance tracking capability described in Sec. 4.2.3.1. 
Update Services 
and Vendor Patch 
Delivery 
Many vendors offer software update services (i.e., platforms that 
maintain a connection to a vendor server to retrieve approved 
firmware, software updates, and security patches on demand or on a 
schedule) following the patch management approach outlined in Sec. 
4.2.3.1.

<!-- page 133 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
115 
Table 8. Example security controls 4129 
Function Description 
File Transfer — General 
Content Ingestion 
Content should undergo antivirus scanning, file type validation, 
and integrity checking before it is permitted to proceed, 
mirroring the endpoint monitoring guidance in Sec. 4.3.1.2. 
Bidirectional Transfer — 
Outbound Content and 
Vendor Data Access 
Outbound content should be routed through the same 
controlled infrastructure used for inbound content in line with 
the remote access control principles introduced in Sec. 4.2.1.8. 
Removable Media and 
Portable Devices — USB 
Kiosk Workflow 
A USB scanning kiosk should serve as the mandatory entry point 
for removable media before it is permitted to connect to any 
field device, engineering workstation, or other asset, building 
on the media protection concepts addressed in Sec. 4.2.2.3. 
Credential Separation Credentials should be maintained separately across trust 
domains, as discussed in the identity convergence and 
centralization guidance in Sec. 4.2.1.5. 
Privileged Access 
Management 
Privileged access should be mediated through an access 
manager that enforces least-privilege entitlements, time-
bounded session authorization, and session recording with live 
termination capability, as addressed in Sec. 4.2.1.7. 
Passive Network 
Monitoring 
Passive network monitoring sensors deployed via span ports or 
network taps extend the passive monitoring concepts 
introduced in Sec. 4.1.1.1. 
Log Collection and 
Telemetry 
Telemetry should flow one-way outbound to a central 
collection point, mirroring the device logging guidance 
discussed in Sec. 4.3.1.1. 
Table 9. Example architectural patterns 4130 
Architecture 
Pattern 
Description 
Access 
Architecture 
The design and operation of a full access management architecture 
build on the remote access control principles introduced in Sec. 
4.2.1.8. 
DMZ and the Two-
Firewall 
Architecture 
A two-firewall DMZ architecture separates trusted infrastructure 
from untrusted external connections with traffic routed through it 
rather than crossing directly between planes, consistent with the 
boundary protection principles discussed in Sec. 4.2.1.8. Without this 
separation, a single set of firewall rules must accommodate both 
trust levels and is, therefore, necessarily broader than either requires. 
VPN Gateways and 
Remote Site 
Connectivity 
Remote sites and remote users should reach protected infrastructure 
through VPN gateways terminating in a DMZ rather than connecting 
directly, thus building on the data-in-transit protections described in 
Sec. 4.2.2.4. Persistent VPN tunnels with poor authentication can be 
exploited by attackers to gain network access using otherwise-
blocked paths. 
Intra-Site 
Segmentation and 
Field-Facing 
Gateways 
Segmentation should separate distinct network zones from one 
another, each governed by its own access control list and firewall 
policy, to reflect the authorization and logical access control practices 
addressed in Sec. 4.2.1.7. Without this internal segmentation, a

<!-- page 134 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
116 
Architecture 
Pattern 
Description 
foothold gained anywhere on the site-level network has unrestricted 
reach across every zone. 
5.2. Cybersecurity Architecture Models 4131 
Building on the concepts and guidance from Sec. 4, the following subsections expand on the 4132 
management network described in Sec. 5.1 as well as the operational networks described in 4133 
Sec. 2. They provide examples for how these environments might be adapted to incorporate 4134 
the functions, security controls, and architecture patterns identified above. 4135 
5.2.1. Management Network Architecture 4136 
Separating OT from the enterprise network is a baseline architectural practice. The two 4137 
networks carry fundamentally different traffic, tolerate different levels of risk, and are subject 4138 
to different change control rigor. Combining them exposes OT components to network-based 4139 
attacks that enterprise traffic would otherwise absorb. This same logic extends inside the OT 4140 
environment itself. Operational traffic (i.e., supervisory-to-field-device communication) has 4141 
different availability requirements and traffic characteristics than management traffic, such as 4142 
configuration changes, patching, and access control sessions. Running both on shared 4143 
infrastructure lets management activity introduce risk to operational traffic, prevents an 4144 
independent security policy per function, and allows a security event on one to propagate to 4145 
the other. 4146 
The management network exists to give these functions the isolation that separation requires. 4147 
It provides the connectivity, credential domain, and audit posture that asset management, code 4148 
management, and monitoring need without exposing that access on the operational network, 4149 
where broad device connectivity would otherwise sit unguarded on infrastructure designed 4150 
only for deterministic process traffic. An attacker seeking a physical impact must establish 4151 
separate footholds in networks that each require their own credentials and have their own 4152 
enforced boundary, which materially raises the cost and detectability of an attack. Vendor and 4153 
third-party access follows the same principle: external connections use their own credential 4154 
stores and entry points that are architecturally separate from internal management traffic so 4155 
that the trust extended externally cannot reach internal functions through shared 4156 
infrastructure. 4157 
Figure 17 illustrates the management network architecture relative to the operational network, 4158 
the enterprise network, and external vendor connections, including asset and code 4159 
management, configuration governance, patch and update management, identity and access 4160 
management, and security monitoring. 4161

<!-- page 135 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
117 
 4162 
Fig. 17. Network management security architecture 4163

<!-- page 136 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
118 
Where connections between OT and enterprise or other IT networks are operationally 4164 
necessary, they represent additional risk and should be minimized and controlled rather than 4165 
treated as routine. For network security, the organization should consider incorporating the 4166 
following capabilities into the security architecture: 4167 
• The management network is separated into zones based on function. Asset 4168 
management, industrial code management, and the configuration management 4169 
database occupy one zone; patch staging and file transfer occupy a second; identity and 4170 
access management infrastructure occupies a third; and security monitoring occupies an 4171 
isolated zone with no staff access path. 4172 
• Asset management and code management connectivity is restricted to the management 4173 
network. Both functions require active, write-adjacent connectivity to read and validate 4174 
device state or running logic. The asset management platform holds a complete 4175 
inventory and vulnerability picture, and the code repository holds every authorized 4176 
version of device logic, making both high-value targets that are not reachable from the 4177 
operational network directly. Access to field devices for these functions routes through 4178 
the engineering network and a field-facing gateway rather than a direct path. 4179 
• Boundary devices (e.g., firewalls) control and monitor communications between zones. 4180 
Rules define authorized traffic per function rather than a shared rule set across the 4181 
management network. 4182 
• A two-firewall DMZ architecture separates the management network from both the 4183 
enterprise network and untrusted external connections. Vendor update services are 4184 
staged in the DMZ rather than run directly in the management network. If DMZ staging 4185 
is not available, the update client is restricted to a tightly scoped outbound rule that 4186 
permits only the specific vendor endpoint, documented as a risk acceptance. 4187 
• All file transfers route through a DMZ-hosted file transfer server as the exclusive 4188 
sanctioned ingestion path. Content is scanned for malicious code, validated by file type, 4189 
and integrity-checked before reaching the management network. Content that fails 4190 
validation is quarantined within the DMZ. Outbound content (e.g., logs, diagnostics, 4191 
configuration exports) routes through the same DMZ infrastructure rather than a 4192 
separate path. 4193 
• A USB scanning kiosk serves as the mandatory entry point for removable media and 4194 
engineer laptops before either is permitted to connect to any field device, engineering 4195 
workstation, or other management-network asset. Media that passes scanning may be 4196 
loaded with content from the mirrored file transfer server so that files placed on it are 4197 
the same files that passed DMZ validation, rather than files sourced externally. 4198 
• A dedicated OT authentication server resides within the management network, distinct 4199 
from enterprise directory services, so that a compromised enterprise credential cannot 4200 
grant access to the management infrastructure. 4201 
• All privileged access is mediated through an Access Manager who enforces least-4202 
privilege entitlements, time-bounded session authorization, and session recording with 4203

<!-- page 137 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
119 
live termination capability for every privileged session against a managed asset. Staff 4204 
and
 vendor access paths are architecturally distinct (e.g., separate entry points, 4205 
cre
dential stores, firewall policy lanes, and entitlement profiles) with just-in-time 4206 
appr
oval required for vendor and third-party access before any session is established. 4207 
Stan
ding, always-on vendor access is avoided. If it cannot be eliminated, it is formally 4208 
risk-a
ccepted and continuously monitored. Because a compromise of this infrastructure 4209 
aff
ects the authorization layer for every managed device rather than any single one, it is 4210 
tre
ated as a high-value target in its own right. 4211 
•
 Security monitoring infrastructure resides in its own isolated zone that is reachable only 4212 
via one-way telemetry feeds from the other management zones so that monitoring data 4213 
and infrastructure are not accessible through the same paths used for management 4214 
operations. 4215 
5.2.2.  Operational Network Architecture 4216 
The operational network carries process control traffic (i.e., traffic that is deterministic, latency-4217 
sensitive, and essential to safe and reliable operation of the physical process) between 4218 
supervisory systems, distributed field controllers, and the sensors and actuators they 4219 
command. This traffic differs fundamentally from enterprise network traffic (e.g., internet 4220 
access, email, remote access) and from management network traffic (e.g., configuration 4221 
changes, patch delivery, administrative access). Running any of this alongside operational traffic 4222 
exposes OT components to network-based attacks (e.g., denial of service, adversary-in-the-4223 
middle) that the operational network was never designed to withstand. 4224 
Isolating the operational network preserves the narrow, predictable traffic envelope that makes 4225 
it a high-signal environment for anomaly detection. Deviations from expected process 4226 
communication are easier to identify precisely because nothing else is competing for that 4227 
bandwidth or introducing variable traffic patterns. It also directly limits the attacker’s 4228 
capabilities. Supervisory and field-level functions operate within a defined operating envelope 4229 
(e.g., control logic, setpoints, process limits), and an adversary confined to the operational 4230 
network is constrained by that same envelope. Changing the envelope itself requires reaching 4231 
the management network, so an attacker seeking consequential physical impact must establish 4232 
and maintain separate footholds in each, defeating a separately enforced boundary for each 4233 
one. 4234 
The specific architecture of the operational network varies with the type of control system 4235 
deployed. The following sections address these considerations as they apply to Distributed 4236 
Control System (DCS)-Based OT Systems and SCADA-Based OT Environments. 4237 
5.2.2.1. Distributed Control System (DCS)-Based OT Systems 4238 
A distributed control system (DCS) is used to control production systems within the same 4239 
geographic location by organizing the network into separate functional areas, such as: 4240 
• A field level with devices typically associated with Purdue Levels 0, 1, and 2 4241

<!-- page 138 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
120 
• An operations management level with devices used to monitor and manage field 4242 
devices and Purdue Level 3 components 4243 
• A DMZ with devices that support communication between the operations management 4244 
level and enterprise systems 4245 
Additional network segments may also be used for systems, such as: 4246 
• Physical monitoring and access controls 4247 
• Doors 4248 
• Gates 4249 
• Cameras 4250 
• Voice over Internet Protocol (VoIP) 4251 
• Access card readers 4252 
Boundary devices (e.g., firewalls) can be placed between these areas to control and monitor 4253 
communications. Industrial-class firewalls may be used between field devices and operations 4254 
management systems to support OT-specific protocols or to operate in harsh environments. 4255 
Inbound and outbound rules should be defined so that only authorized communication passes 4256 
between adjacent areas. 4257 
A DMZ can be used to separate the OT environment from the enterprise network. 4258 
Communications between enterprise systems and operations management systems should 4259 
pass through services located in the DMZ rather than directly between the two environments. 4260 
Because the DMZ connects to outside environments, the services within it should be monitored 4261 
and protected to reduce the chance that a compromise in the DMZ could be used to reach the 4262 
OT environment. 4263 
Some architectures may use separate authentication services for enterprise and OT users, such 4264 
as: 4265 
• An IT authentication server in the enterprise network 4266 
• An OT authentication server in the operations management network 4267 
Devices in the field level, operations management level, and DMZ should be configured to only 4268 
use the capabilities required for their purpose. Non-essential software, services, and ports 4269 
should be identified and disabled. For example, if a PLC or HMI contains a web server or SSH 4270 
server that is not needed, that service and its associated TCP/UDP ports should be disabled.  4271

<!-- page 139 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
121 
Figure 18 shows a security architecture example for a DCS system.  4272 
 4273 
Fig. 18. A security architecture example for a DCS system 4274

<!-- page 140 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
122 
5.2.2.2. DCS- and PLC-Based OT With IIoT 4275 
When DCS- and PLC-based OT environments include IIoT devices, the architecture may be 4276 
expanded to support the additional communication and processing needs of those devices. For 4277 
example, IIoT devices may be connected to a local IIoT platform that provides computing 4278 
capabilities. Because IIoT introduces different communication and architectural components, 4279 
separate network segments may be used for those components. 4280 
Communication from the IIoT platform tier can be routed through a DMZ border firewall. This 4281 
allows organizations to support data transmission to: 4282 
• Servers in the DMZ or 4283 
• The enterprise or internet, as needed for IIoT operational requirements. 4284 
This also allows cybersecurity services located in the DMZ to monitor the IIoT platform tier. 4285 
Figure 19 shows a simplified example security architecture implementation for the DCS system 4286 
with additional IIoT devices configured to utilize a local IIoT platform for providing computing 4287 
capabilities. 4288 
 4289 
 4290 
Fig. 19. A security architecture example for DCS system with IIoT devices 4291

<!-- page 141 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
123 
5.2.2.3. SCADA-Based OT Environments   4292 
A SCADA environment often includes primary and backup control centers, regional control 4293 
centers, and remote stations in different geographic locations. Because these components are 4294 
distributed, communication between locations often passes over external or WAN connections 4295 
using wired or wireless media. The network can be divided into different zones or regions. 4296 
Additional separation may also be used for systems, such as: 4297 
• Physical monitoring and access controls 4298 
• Doors 4299 
• Gates 4300 
• Cameras 4301 
• VoIP 4302 
• Access card readers 4303 
Boundary devices (e.g., firewalls) can be placed between regions to control and monitor 4304 
communications between network segments. Industrial-class stateful firewalls may provide 4305 
better support for OT-specific protocols and may enhance protection for OT devices, such as 4306 
PLCs and controllers. Inbound and outbound rules should be defined so that only authorized 4307 
communication passes between regions. 4308 
Secure connections should be used between network segments, such as: 4309 
• VPN tunnels 4310 
• Encrypted channels 4311 
• Point-to-point connections 4312 
These secure connections may be used: 4313 
• Between a regional center and primary control centers 4314 
• Between remote stations and control centers 4315 
For geographically distant locations, these secure connections may traverse the internet or a 4316 
wide area network. Devices in each network segment should only connect to other segments 4317 
through the secure connection, and direct internet access should be restricted. 4318 
A DMZ can also be used to separate control centers from the enterprise network. 4319 
Communications between the enterprise network and control centers should pass through 4320 
services within the DMZ. Those services should be monitored and protected to prevent them 4321 
from becoming a path into the OT environment. 4322 
Remote station components, control center components, and DMZ devices should be 4323 
configured to support only necessary functions. Non-essential software, services, and ports 4324 
should be identified and disabled. For example, if a newer PLC or HMI includes a web server or 4325 
SSH server that is not required, it should be disabled along with the associated TCP/UDP ports. 4326

<!-- page 142 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
124 
Fig. 20 shows an example implementation of the components and general configuration of a 4327 
SCADA system. 4328 
 4329 
Fig. 20. A security architecture example for a SCADA system 4330 
5.3. Integrating Zero Trust Principles in OT  4331 
A zero trust architecture (ZTA) is a cybersecurity paradigm that focuses on protecting resources 4332 
(e.g., information services, data) by authorizing access decisions closer to the resource being 4333 
requested and continuously evaluating them rather than implicitly granting access. 4334 
Conventional network security focuses on segmentation and perimeter defenses. Once inside 4335 
the network perimeter, users are typically considered “trusted” and often given broad access to 4336 
accessible resources. As a result, boundary protection devices between zones do not mitigate 4337 
lateral movement risks within a zone. Additionally, with the growing prevalence of distributed 4338 
computing, wireless and cellular communications, and cloud and hybrid cloud environments, 4339 
traditional network perimeters and boundaries are becoming less defined. For these situations, 4340 
organizations might consider incorporating the principles of zero trust into their security 4341 
architecture. 4342

<!-- page 143 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
125 
Several of the functions and controls described throughout this document already embody core 4343 
zero trust principles and can serve as an organization’s practical starting point for a broader ZTA 4344 
implementation rather than requiring a separate initiative: 4345 
• Continuous, per-session authorization rather than implicit trust. Privileged access 4346 
management (see Sec. 4.2.1.7) is the clearest expression of zero trust. The Access 4347 
Manager evaluates and authorizes each privileged session individually to enforce least-4348 
privilege entitlements, time-bounded authorization, and live session termination rather 4349 
than granting standing trust once a user reaches the network. Extending this same 4350 
continuous-evaluation model to non-privileged access is a natural next step in a ZTA 4351 
implementation. 4352 
• Strong, verifiable identity as the basis for authorization decisions. Credential separation 4353 
(see Sec. 4.2.1.5) ensures that identity verification for OT network access does not 4354 
inherit trust from the enterprise identity domain. A dedicated OT authentication server 4355 
gives a ZTA policy engine an identity source that it can evaluate independently rather 4356 
than one in which a compromised enterprise credential could satisfy an OT 4357 
authorization check. 4358 
• Content-level verification rather than perimeter trust. File transfer controls (see Sec. 4359 
4.3.1.2) and removable media controls (see Sec. 4.2.2.3) apply zero trust logic to content 4360 
rather than users. Nothing is trusted by virtue of having reached the DMZ or passing the 4361 
USB kiosk once. Each artifact is scanned, validated, and quarantined on failure before it 4362 
is trusted for use. 4363 
• Continuous monitoring as the enforcement feedback loop. Security monitoring (see Sec. 4364 
4.3.2.1) supplies the continuous observation that a ZTA model depends on to revoke or 4365 
adjust trust in near real-time rather than relying on a one-time authorization decision 4366 
made at the start of the session. 4367 
Some challenges to implementing a ZTA include: 4368 
• Organizations may not find a suitable single solution for a ZTA and may instead need to 4369 
integrate several technologies with varying maturity levels to support their 4370 
environment. 4371 
• Implementing zero trust principles into an existing environment may require a greater 4372 
investment in time, resources, and technical expertise. 4373 
5.3.1. OT-Specific Recommendations and Guidance 4374 
Many OT components (e.g., PLCs, controllers, HMIs) do not support the technologies or 4375 
protocols required to fully integrate with a ZTA implementation. Therefore, organizations 4376 
should consider applying a ZTA to compatible devices, such as those typically found at the 4377 
functionally higher levels of the OT architecture (e.g., Purdue model Levels 3, 4, 5; OT DMZ). 4378 
This corresponds closely with the functions addressed in Sec. 4.2.1.7, 4.2.1.5, 4.3.1.2, 4.2.2.3, 4379 
and 4.3.2.1, where the controls already provide much of the necessary foundation. 4380

<!-- page 144 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
126 
Organizations may also want to consider whether any adverse impacts might occur, such as if 4381 
the ZTA solution increases the latency to respond to resource requests or if one or more ZTA 4382 
components become unavailable. Based on this analysis, organizations should consider 4383 
adjusting the ZTA implementations to minimize latency and ensure adequate redundancy to 4384 
minimize risks to OT and safety operations. 4385 
Another important aspect of ZTA implementations is the identity of person and non-person 4386 
entities accessing resources. Within OT environments, shared credentials may be utilized, which 4387 
could impact the ability to fully implement a ZTA solution. This reinforces the importance of 4388 
credential separation control (see Sec. 4.2.1.5) and privileged access management control (see 4389 
Sec. 4.2.1.7) as preconditions for meaningful ZTA adoption. 4390 
5.4. Designing for Security, Safety, and Resilience 4391 
The functions, security controls, and architectural patterns described in this section reduce the 4392 
likelihood that a given threat will succeed. They do not, on their own, ensure that operations 4393 
continue when a component fails or a control is defeated. The following design principles 4394 
address that separate concern: ensuring that the OT environment degrades gracefully, recovers 4395 
predictably, and remains manageable even when primary systems or paths are unavailable. 4396 
5.4.1. Fault Tolerance as an Architectural Design Principle 4397 
Fault tolerance is the property of a system to continue operating when a component fails rather 4398 
than failing outright, potentially at a reduced level. In OT environments, fault tolerance is a 4399 
design principle: a failed component should fail in a manner that does not generate 4400 
unnecessary traffic, cascade to other systems, or leave the process in an unsafe state. This 4401 
differs meaningfully from IT environments, in which momentary downtime is typically an 4402 
acceptable and recoverable event. In OT, momentary downtime may be unacceptable because 4403 
it could directly affect a physical process. Architectures should support graceful degradation 4404 
(i.e., moving from full automation to increasingly manual modes of operation) so that a fault 4405 
reduces functionality rather than availability entirely. 4406 
Guidelines on engineering resilient systems, including fault-tolerant design, are provided in SP 4407 
800-160v2r1, Developing Cyber-Resilient Systems: A Systems Security Engineering Approach, 4408 
which defines resilience techniques and design principles applicable to OT and other cyber-4409 
physical systems. 4410 
5.4.2. Redundancy Addressed as an Architecture-Level Design Principle 4411 
Redundancy supports fault tolerance by ensuring that no single point of failure can interrupt a 4412 
critical function. Redundancy should be addressed at the architecture level rather than the 4413 
component level. Critical components should have a redundant counterpart on a redundant 4414 
network path, and any redundant communication path should be protected to the same 4415 
security level as the primary path it backs up. Architecture-level redundancy also extends to 4416 
identity and access infrastructure and monitoring infrastructure. A redundant authentication 4417

<!-- page 145 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
127 
server or monitoring collector that shares the same failure domain as its primary provides 4418 
limited additional resilience. 4419 
Redundancy requirements should be scoped to the criticality of the asset or function being 4420 
protected, consistent with an organization’s risk tolerance, rather than applied uniformly across 4421 
the environment. The architectural treatment of resilience and redundancy is addressed in SP 4422 
800-160v2r1. 4423 
5.4.3. Analog Backups 4424 
If a process can be safely operated using non-digital instrumentation and controls, maintaining 4425 
an analog backup (e.g., hardwired instrumentation, physical gauges, manual control stations 4426 
that do not depend on the digital control system) provides a recovery path that is unaffected by 4427 
a cyber incident against the digital environment. Analog backups are most relevant for safety-4428 
critical or highly critical processes for which the consequences of extended digital system 4429 
unavailability are unacceptable. They should be evaluated as a complement rather than a 4430 
replacement for digital backup and restoration processes. 4431 
Digital backup and restoration practices (e.g., layered, time-sequenced “backup-in-depth” 4432 
approach with local, facility, and disaster-recovery backups) are addressed at a general level in 4433 
SP 800-82r3, Sec. 5.3.2.1. Broader contingency planning guidelines, including backup strategy 4434 
selection and testing, is provided in SP 800-34r1, Contingency Planning Guide for Federal 4435 
Information Systems. 4436 
5.4.4. Out-of-Band Management as an Architectural Concept 4437 
Out-of-band management provides an administrative access path that is physically or logically 4438 
separate from the primary data path used for normal operations. Where implemented, 4439 
management traffic (e.g., access to boundary devices, the Access Manager, and monitoring 4440 
infrastructure) does not traverse the same network segments as operational or enterprise 4441 
traffic, so a compromise of the in-band path does not also compromise the ability to administer 4442 
or recover the environment. This separation is particularly relevant to the management 4443 
network architecture since an out-of-band path preserves the ability to manage boundary 4444 
devices and recover monitoring infrastructure even if the in-band management network is 4445 
degraded or unavailable.  4446

<!-- page 146 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
128 
References 4447 
[AGA12] American Gas Association (2006) Cryptographic Protection of SCADA 4448 
Communications, Part 1: Background, Policies and Test Plan. AGA Report No. 4449 
12. 4450 
[ANSI-ISA-5-1] International Society of Automation (2009) Instrumentation Symbols and 4451 
Identification, ANSI/ISA-5.1-2009. Available at 4452 
https://webstore.ansi.org/Standards/ISA/ANSIISA2009  4453 
[ANSI-ISA-51-1] International Society of Automation (1993) Process Instrumentation 4454 
Terminology, ANSI/ISA-51.1-1979 (R1993). Available at 4455 
https://www.isa.org/products/isa-51-1-1979-r1993-process-instrumentation-4456 
termin  4457 
[ANSI-ISA-84] Instrumentation, Systems, and Automation Society (2004) Functional Safety: 4458 
Safety Instrumented Systems for the Process Industry Sector – Part 1: 4459 
Framework, Definitions, System, Hardware, and Software Requirements. 4460 
ANSI/ISA-84.00.01-2004 Part 1. Available at 4461 
https://webstore.ansi.org/standards/isa/ansiisa8400012004part  4462 
[ATTACK-ICS] The MITRE Corporation (2022) ATT&CK® for Industrial Control Systems. 4463 
Available at https://attack.mitre.org/techniques/ics/ 4464 
[Bailey] Bailey D, Wright E (2003) Practical SCADA for Industry. (IDC Technologies, 4465 
Vancouver, Canada). 4466 
[Berge] Berge J (2002) Fieldbuses for Process Control: Engineering, Operation, and 4467 
Maintenance. (International Society of Automation, Research Triangle Park, 4468 
North Carolina). 4469 
[Boyer] Boyer S (2010) SCADA: Supervisory Control and Data Acquisition. 4th ed. 4470 
(International Society of Automation, Research Triangle Park, North 4471 
Carolina). 4472 
[CIE] Cyber-Informed Engineering (CIE). U.S. Department of Energy (DOE). 4473 
Available at: https://www.energy.gov/ceser/cyber-informed-engineering 4474 
[CISA-CIVR] Cybersecurity and Infrastructure Security Agency (2021) Cybersecurity 4475 
Incident & Vulnerability Response Playbooks: Operational Procedures for 4476 
Planning and Conducting Cybersecurity Incident and Vulnerability Response 4477 
Activities in FCEB Information Systems. Available at 4478 
https://www.cisa.gov/sites/default/files/publications/Federal_Government_4479 
Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf 4480 
[CISA-PACE] Cybersecurity and Infrastructure Security Agency (CISA), National Council of 4481 
Statewide Interoperability Coordinators (NCSWIC) Planning, Training, and 4482 
Exercise Committee (2024) Leveraging the PACE Plan into the Emergency 4483 
Communications Ecosystem. Available at: 4484 
https://www.cisa.gov/sites/default/files/2024-4485

<!-- page 147 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
129 
10/2024_NCSWICPTE_Leveraging_PACE_Plan_Emergency_Comms_Ecosyste4486 
ms.pdf 4487 
[CNSS1253] Committee on National Security Systems (2014) Security Categorization and 4488 
Control Selection for National Security Systems. CNSS Instruction (CNSSI) No. 4489 
1253. Available at https://www.cnss.gov/CNSS/issuances/Instructions.cfm  4490 
[CNSS4009] Committee on National Security Systems (2022) Committee on National 4491 
Security Systems (CNSS) Glossary. CNSS Instruction (CNSSI) No. 4009. 4492 
Available at https://www.cnss.gov/CNSS/issuances/Instructions.cfm  4493 
[CSF] National Institute of Standards and Technology (2024) The NIST 4494 
Cybersecurity Framework (CSF), Version 2.0. (National Institute of Standards 4495 
and Technology, Gaithersburg, MD). https://doi.org/10.6028/NIST.CSWP.29 4496 
[CSRC-PQC] National Institute of Standards and Technology. Post-Quantum 4497 
Cryptography. Available at: https://csrc.nist.gov/topics/security-and-4498 
privacy/cryptography/post-quantum-cryptography 4499 
[DOE-AMI] U.S. Department of Energy, Office of Electricity Delivery and Energy 4500 
Reliability (2016) Advanced Metering Infrastructure and Customer Systems: 4501 
Results from the Smart Grid Investment Grant Program. Available at: 4502 
https://www.energy.gov/sites/prod/files/2016/12/f34/AMI%20Summary%24503 
0Report_09-26-16.pdf 4504 
[EO13636] Executive Order 13636 (2013) Improving Critical Infrastructure Cybersecurity. 4505 
(The White House, Washington, DC), DCPD-201300091, February 12, 2013. 4506 
https://www.govinfo.gov/app/details/DCPD-201300091 4507 
[Erickson] Erickson K, Hedrick J (1999) Plantwide Process Control. (John Wiley & Sons, 4508 
Inc., New York, NY). 4509 
[FIPS140-2] National Institute of Standards and Technology (2001) Security Requirements 4510 
for Cryptographic Modules. (U.S. Department of Commerce, Washington, 4511 
DC), Federal Information Processing Standards Publication (FIPS) NIST FIPS 4512 
140-2, Change Notice 2 December 03, 2002. 4513 
https://doi.org/10.6028/NIST.FIPS.140-2    4514 
[FIPS140-3] National Institute of Standards and Technology (2019) Security Requirements 4515 
for Cryptographic Modules. (U.S. Department of Commerce, Washington, 4516 
DC), Federal Information Processing Standards Publication (FIPS) NIST FIPS 4517 
140-3. https://doi.org/10.6028/NIST.FIPS.140-3  4518 
[FIPS180] National Institute of Standards and Technology (2015) Secure Hash Standard 4519 
(SHS). (U.S. Department of Commerce, Washington, DC), Federal Information 4520 
Processing Standards Publication (FIPS) NIST FIPS 180-4. 4521 
https://doi.org/10.6028/NIST.FIPS.180-4  4522 
[FIPS186] National Institute of Standards and Technology (2023) Digital Signature 4523 
Standard (DSS). (U.S. Department of Commerce, Washington, DC), Federal 4524

<!-- page 148 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
130 
Information Processing Standards Publication (FIPS) NIST FIPS 186-5. 4525 
https://doi.org/10.6028/NIST.FIPS.186-5  4526 
[FIPS197] National Institute of Standards and Technology (2001) Advanced Encryption 4527 
Standard (AES). (U.S. Department of Commerce, Washington, DC), Federal 4528 
Information Processing Standards Publication (FIPS) NIST FIPS 197-upd1, 4529 
updated May 9, 2023. https://doi.org/10.6028/NIST.FIPS.197-upd1  4530 
[FIPS199] National Institute of Standards and Technology (2004) Standards for Security 4531 
Categorization of Federal Information and Information Systems. (U.S. 4532 
Department of Commerce, Washington, DC), Federal Information Processing 4533 
Standards Publication (FIPS) NIST FIPS 199. 4534 
https://doi.org/10.6028/NIST.FIPS.199  4535 
[FIPS200] National Institute of Standards and Technology (2006) Minimum Security 4536 
Requirements for Federal Information and Information Systems. (U.S. 4537 
Department of Commerce, Washington, DC), Federal Information Processing 4538 
Standards Publication (FIPS) NIST FIPS 200. 4539 
https://doi.org/10.6028/NIST.FIPS.200  4540 
[FIPS201] National Institute of Standards and Technology (2022) Personal Identity 4541 
Verification (PIV) of Federal Employees and Contractors. (U.S. Department of 4542 
Commerce, Washington, DC), Federal Information Processing Standards 4543 
Publication (FIPS) NIST FIPS 201-3. https://doi.org/10.6028/NIST.FIPS.201-3  4544 
[FIPS202] National Institute of Standards and Technology (2015) SHA-3 Standard: 4545 
Permutation-Based Hash and Extendable-Output Functions. (U.S. 4546 
Department of Commerce, Washington, DC), Federal Information Processing 4547 
Standards Publication (FIPS) NIST FIPS 202. 4548 
https://doi.org/10.6028/NIST.FIPS.202  4549 
[FISMA] Federal Information Security Modernization Act of 2014, Pub. L. 113-283, 128 4550 
Stat. 3073. https://www.govinfo.gov/app/details/PLAW-113publ283 4551 
[IEC61511] International Electrotechnical Commission (2016) Functional safety – Safety 4552 
instrumented systems for the process industry sector – Part 1: Framework, 4553 
definitions, system, hardware and application programming requirements, 4554 
IEC 61511-1:2016. Available at https://webstore.iec.ch/publication/24241  4555 
[IEC62264] International Electrotechnical Commission (2013) Enterprise-control system 4556 
integration - Part 1: Models and terminology, IEC 62264-1:2013. Available at 4557 
https://webstore.iec.ch/publication/6675  4558 
[IIC1] Canavan L (2019) What is IIoT? The Industrial Internet of Things Primer 4559 
Industrial IoT Consortium (IIC), Available at 4560 
https://www.iiconsortium.org/2019/09/what-is-iiot-the-industrial-internet-4561 
of-things-primer/ 4562

<!-- page 149 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
131 
[IIRA19] Industry IoT Consortium (2019) The Industrial Internet of Things Volume G1: 4563 
Reference Architecture, Version 1.9. Available at 4564 
https://www.iiconsortium.org/pdf/IIRA-v1.9.pdf  4565 
[IICSMM] Security Maturity Model (2022) Industry IoT Consortium (IIC). Available at 4566 
https://www.iiconsortium.org/smm/ 4567 
[IR6859] Falco J, Stouffer K, Wavering A, Proctor F (2002) IT Security for Industrial 4568 
Control Systems. (National Institute of Standards and Technology, 4569 
Gaithersburg, MD), NIST Interagency Report (IR) NIST IR 6859. Available at 4570 
https://doi.org/10.6028/NIST.IR.6859  4571 
[IR8062] Brooks SW, Garcia ME, Lefkovitz NB, Lightman S, Nadeau EM (2017) An 4572 
Introduction to Privacy Engineering and Risk Management in Federal 4573 
Systems. (National Institute of Standards and Technology, Gaithersburg, MD), 4574 
NIST Internal or Interagency Report (IR) NIST IR 8062. 4575 
https://doi.org/10.6028/NIST.IR.8062  4576 
[IR8183A] Stouffer KA, Zimmerman T, Tang C, Pease M, Cichonski JA, Shah N, Downard 4577 
W (2019) Cybersecurity Framework Manufacturing Profile Low Impact Level 4578 
Example Implementations Guide: Volume 1 – General Implementation 4579 
Guidance. (National Institute of Standards and Technology, Gaithersburg, 4580 
MD), NIST Interagency or Internal Report (IR) NIST IR 8183Av1. 4581 
https://doi.org/10.6028/NIST.IR.8183A-1  4582 
 Stouffer KA, Zimmerman T, Tang C, Pease M, Cichonski JA, Shah N, Downard 4583 
W (2019) Cybersecurity Framework Manufacturing Profile Low Impact Level 4584 
Example Implementations Guide: Volume 2 – Process-based Manufacturing 4585 
System Use Case. (National Institute of Standards and Technology, 4586 
Gaithersburg, MD), NIST Interagency or Internal Report (IR) NIST IR 8183Av2. 4587 
https://doi.org/10.6028/NIST.IR.8183A-2  4588 
 Stouffer KA, Zimmerman T, Tang C, Pease M, Cichonski JA, Shah N, Downard 4589 
W (2019) Cybersecurity Framework Manufacturing Profile Low Impact Level 4590 
Example Implementations Guide: Volume 3 – Discrete-based Manufacturing 4591 
System Use Case. (National Institute of Standards and Technology, 4592 
Gaithersburg, MD), NIST Interagency or Internal Report (IR) NIST IR 8183Av3. 4593 
https://doi.org/10.6028/NIST.IR.8183A-3  4594 
[IR8228] Boeckl K, Fagan M, Fisher W, Lefkovitz N, Megas K, Nadeau E, O’Rourke D, 4595 
Piccarreta B, Scarfone K (2019) Considerations for Managing Internet of 4596 
Things (IoT) Cybersecurity and Privacy Risks. (National Institute of Standards 4597 
and Technology, Gaithersburg, MD), NIST Interagency or Internal Report (IR) 4598 
NIST IR 8228. https://doi.org/10.6028/NIST.IR.8228 4599 
[IR8428] Salfati E, Pease M (2022) Digital Forensics and Incident Response (DFIR) 4600 
Framework for Operational Technology (OT). (National Institute of Standards 4601

<!-- page 150 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
132 
and Technology, Gaithersburg, MD), NIST Interagency or Internal Report (IR) 4602 
NIST IR 8428. https://doi.org/10.6028/NIST.IR.8428 4603 
[ISA62443] International Society of Automation (2020) Security for industrial automation 4604 
and control systems (all parts), ISA-62443. Available at 4605 
https://www.isa.org/standards-and-publications/isa-standards/isa-iec-4606 
62443-series-of-standards  4607 
[ISADICT] International Society of Automation (2002) The Automation, Systems, and 4608 
Instrumentation Dictionary, 4th Edition. International Society of Automation. 4609 
[ISO7498-1] ISO/IEC 7498-1:1994, Available at https://www.iso.org/standard/20269.html  4610 
[Knapp] Knapp E (2011) Industrial Network Security: Securing Critical Infrastructure 4611 
Networks for Smart Grid, SCADA, and Other Industrial Control Systems, 4612 
(Syngress, Waltham, Massachusetts). 4613 
[NIST-DT] National Institute of Standards and Technology. Digital Twins. Available at 4614 
https://www.nist.gov/digital-twins 4615 
[OMB-A130] Office of Management and Budget (2016) Managing Information as a 4616 
Strategic Resource. (The White House, Washington, DC), OMB Circular A-130, 4617 
July 28, 2016. Available at 4618 
https://www.federalregister.gov/documents/2016/07/28/2016-4619 
17872/revision-of-omb-circular-no-a-130-managing-information-as-a-4620 
strategic-resource  4621 
[OMB-M1917] Office of Management and Budget (2019) Enabling Mission Delivery through 4622 
Improved Identity, Credential, and Access Management. (The White House, 4623 
Washington, DC), OMB Memorandum M-19-17, May 21, 2019. Available at 4624 
https://www.whitehouse.gov/wp-content/uploads/2019/05/M-19-17.pdf  4625 
[Peerenboom] Peerenboom J (2001) “Infrastructure Interdependencies: Overview of 4626 
Concepts and Terminology.” (NSF/OSTP Workshop on Critical Infrastructure: 4627 
Needs in Interdisciplinary Research and Graduate Training, Washington, DC). 4628 
[PF] National Institute of Standards and Technology (2020) NIST Privacy 4629 
Framework: A Tool for Improving Privacy Through Enterprise Risk 4630 
Management, Version 1.0. (National Institute of Standards and Technology, 4631 
Gaithersburg, MD). https://doi.org/10.6028/NIST.CSWP.10  4632 
[PPD-21] Presidential Policy Directive 21 (2013) Critical Infrastructure Security and 4633 
Resilience. (The White House, Washington, DC), February 12, 2013. Available 4634 
at https://obamawhitehouse.archives.gov/the-press-4635 
office/2013/02/12/presidential-policy-directive-critical-infrastructure-4636 
security-and-resil  4637 
[PPD-41] Presidential Policy Directive 41 (2016) United States Cyber Incident 4638 
Coordination. (The White House, Washington, DC), July 26, 2016. Available at 4639

<!-- page 151 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
133 
https://obamawhitehouse.archives.gov/the-press-4640 
office/2016/07/26/presidential-policy-directive-united-states-cyber-incident  4641 
[RFC4949] Shirey R (2007) Internet Security Glossary, Version 2. (Internet Engineering 4642 
Task Force (IETF)), IETF Request for Comments (RFC) 4949. 4643 
https://doi.org/10.17487/RFC4949  4644 
[Rinaldi] Rinaldi SM, Peerenboom JP, Kelly TK (2001) “Identifying, Understanding, and 4645 
Analyzing Critical Infrastructure Interdependencies,” IEEE Control Systems 4646 
Magazine, Vol. 21, No. 6, pp. 11-25, December 2001 4647 
https://doi.org/10.1109/37.969131 4648 
[SP1058] Falco JA, Hurd S, Teumim D (2006) Using Host-Based Anti-Virus Software on 4649 
Industrial Control Systems: Integration Guidance and a Test Methodology for 4650 
Assessing Performance Impacts. (National Institute of Standards and 4651 
Technology, Gaithersburg, MD), NIST Special Publication (SP) NIST SP 1058. 4652 
https://doi.org/10.6028/NIST.SP.1058  4653 
[SP800-100] Bowen P, Hash J, Wilson M (2006) Information Security Handbook: A Guide 4654 
for Managers. (National Institute of Standards and Technology, Gaithersburg, 4655 
MD), NIST Special Publication (SP) NIST SP 800-100, Includes updates as of 4656 
March 7, 2007. https://doi.org/10.6028/NIST.SP.800-100  4657 
[SP800-150] Johnson CS, Waltermire DA, Badger ML, Skorupka C, Snyder J (2016) Guide to 4658 
Cyber Threat Information Sharing. (National Institute of Standards and 4659 
Technology, Gaithersburg, MD), NIST Special Publication (SP) NIST SP 800-4660 
150. https://doi.org/10.6028/NIST.SP.800-150  4661 
[SP800-160v2r1] Ross R, Pillitteri V, Graubart R, Bodeau D, McQuaid R (2021) Developing 4662 
Cyber-Resilient Systems: A Systems Security Engineering Approach. (National 4663 
Institute of Standards and Technology, Gaithersburg, MD), NIST Special 4664 
Publication (SP) NIST SP 800-160v2r1. https://doi.org/10.6028/NIST.SP.800-4665 
160v2r1 4666 
[SP800-161] Boyens JM, Smith AM, Bartol N, Winkler K, Holbrook A, Fallon M (2022) 4667 
Cybersecurity Supply Chain Risk Management Practices for Systems and 4668 
Organizations. (National Institute of Standards and Technology, 4669 
Gaithersburg, MD), NIST Special Publication (SP) NIST SP 800-161r1. 4670 
https://doi.org/10.6028/NIST.SP.800-161r1 4671 
[SP800-167] Sedgewick A, Souppaya MP, Scarfone KA (2015) Guide to Application 4672 
Whitelisting. (National Institute of Standards and Technology, Gaithersburg, 4673 
MD), NIST Special Publication (SP) NIST SP 800-167. 4674 
https://doi.org/10.6028/NIST.SP.800-167   4675 
[SP800-175A] Barker E, Barker W (2016) Guideline for Using Cryptographic Standards in the 4676 
Federal Government: Directives, Mandates and Policies. (National Institute of 4677 
Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 4678 
NIST SP 800-175A. https://doi.org/10.6028/NIST.SP.800-175A 4679

<!-- page 152 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
134 
[SP800-18r1] Swanson MA, Hash J, Bowen P (2006) Guide for Developing Security Plans for 4680 
Federal Information Systems. (National Institute of Standards and 4681 
Technology, Gaithersburg, MD), NIST Special Publication (SP) NIST SP 800-4682 
18r1. https://doi.org/10.6028/NIST.SP.800-18r1  4683 
[SP800-207] Rose SW, Borchert O, Mitchell S, Connelly S (2020) Zero Trust Architecture. 4684 
(National Institute of Standards and Technology, Gaithersburg, MD), NIST 4685 
Special Publication (SP) NIST SP 800-207. 4686 
https://doi.org/10.6028/NIST.SP.800-207  4687 
[SP800-213]           Fagan M, Marron J, Brady K, Cuthill B, Megas K, Herold R, Lemire D, Hoehn B 4688 
(2021) IoT Device Cybersecurity Guidance for the Federal Government: 4689 
Establishing IoT Device Cybersecurity Requirements. (National Institute of 4690 
Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 4691 
NIST SP 800-213. https://doi.org/10.6028/NIST.SP.800-213 4692 
[SP800-28v2] Jansen W, Winograd T, Scarfone KA (2008) Guidelines on Active Content and 4693 
Mobile Code. (National Institute of Standards and Technology, Gaithersburg, 4694 
MD), NIST Special Publication (SP) NIST SP 800-28ver2. 4695 
https://doi.org/10.6028/NIST.SP.800-28ver2  4696 
[SP800-30r1] Joint Task Force Transformation Initiative (2012) Guide for Conducting Risk 4697 
Assessments. (National Institute of Standards and Technology, Gaithersburg, 4698 
MD), NIST Special Publication (SP) NIST SP 800-30r1. 4699 
https://doi.org/10.6028/NIST.SP.800-30r1  4700 
[SP800-34r1] Swanson MA, Bowen P, Phillips AW, Gallup D, Lynes D (2010) Contingency 4701 
Planning Guide for Federal Information Systems. (National Institute of 4702 
Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 4703 
NIST SP 800-34r1, Includes updates as of November 11, 2010. 4704 
https://doi.org/10.6028/NIST.SP.800-34r1  4705 
[SP800-37r2] Joint Task Force (2018) Risk Management Framework for Information 4706 
Systems and Organizations: A System Life Cycle Approach for Security and 4707 
Privacy. (National Institute of Standards and Technology, Gaithersburg, MD), 4708 
NIST Special Publication (SP) NIST SP 800-37r2. 4709 
https://doi.org/10.6028/NIST.SP.800-37r2  4710 
[SP800-39] Joint Task Force Transformation Initiative (2011) Managing Information 4711 
Security Risk: Organization, Mission, and Information System View. (National 4712 
Institute of Standards and Technology, Gaithersburg, MD), NIST Special 4713 
Publication (SP) NIST SP 800-39. https://doi.org/10.6028/NIST.SP.800-39  4714 
[SP800-40r4] Souppaya MP, Scarfone KA (2022) Guide to Enterprise Patch Management 4715 
Planning: Preventive Maintenance for Technology. (National Institute of 4716 
Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 4717 
NIST SP 800-40r4. https://doi.org/10.6028/NIST.SP.800-40r4  4718

<!-- page 153 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
135 
[SP800-41r1] Scarfone KA, Hoffman P (2009) Guidelines on Firewalls and Firewall Policy. 4719 
(National Institute of Standards and Technology, Gaithersburg, MD), NIST 4720 
Special Publication (SP) NIST SP 800-41r1. 4721 
https://doi.org/10.6028/NIST.SP.800-41r1  4722 
[SP800-47r1] Grance T, Hash J, Peck S, Smith J, Korow-Diks K (2021) Managing the Security 4723 
of Information Exchanges. (National Institute of Standards and Technology, 4724 
Gaithersburg, MD), NIST Special Publication (SP) NIST SP 800-47r1. 4725 
https://doi.org/10.6028/NIST.SP.800-47r1  4726 
[SP800-53Ar5] Joint Task Force (2022) Assessing Security and Privacy Controls in Information 4727 
Systems and Organizations. (National Institute of Standards and Technology, 4728 
Gaithersburg, MD), NIST Special Publication (SP) NIST SP 800-53Ar5. 4729 
https://doi.org/10.6028/NIST.SP.800-53Ar5  4730 
[SP800-53B] Joint Task Force (2020) Control Baselines for Information Systems and 4731 
Organizations. (National Institute of Standards and Technology, 4732 
Gaithersburg, MD), NIST Special Publication (SP) NIST SP 800-53B, Includes 4733 
updates as of December 10, 2020. https://doi.org/10.6028/NIST.SP.800-53B  4734 
[SP800-53r5] Joint Task Force (2020) Security and Privacy Controls for Information Systems 4735 
and Organizations. (National Institute of Standards and Technology, 4736 
Gaithersburg, MD), NIST Special Publication (SP) NIST SP 800-53r5. Includes 4737 
updates as of December 10, 2020. https://doi.org/10.6028/NIST.SP.800-53r5  4738 
[SP800-55v1] Schroeder K, Trinh H, Pillitteri VY (2024) Measurement Guide for Information 4739 
Security: Volume 1 – Identifying and Selecting Measures. (National Institute 4740 
of Standards and Technology, Gaithersburg, MD), NIST Special Publication 4741 
(SP) NIST SP 800-55v1. https://doi.org/10.6028/NIST.SP.800-55v1 4742 
[SP800-60v1r1] Stine KM, Kissel RL, Barker WC, Fahlsing J, Gulick J (2008) Guide for Mapping 4743 
Types of Information and Information Systems to Security Categories. 4744 
(National Institute of Standards and Technology, Gaithersburg, MD), NIST 4745 
Special Publication (SP) NIST SP 800-60v1r1. 4746 
https://doi.org/10.6028/NIST.SP.800-60v1r1  4747 
[SP800-60v2r1] Stine KM, Kissel RL, Barker WC, Lee A, Fahlsing J (2008) Guide for Mapping 4748 
Types of Information and Information Systems to Security Categories: 4749 
Appendices. (National Institute of Standards and Technology, Gaithersburg, 4750 
MD), NIST Special Publication (SP) NIST SP 800-60v2r1. 4751 
https://doi.org/10.6028/NIST.SP.800-60v2r1  4752 
[SP800-61] Grance T, Kent K, Kim B (2004) Computer Security Incident Handling Guide. 4753 
(National Institute of Standards and Technology, Gaithersburg, MD), NIST 4754 
Special Publication (SP) NIST SP 800-61. https://doi.org/10.6028/NIST.SP.800-4755 
61  4756 
[SP800-61r3] Nelson A, Rekhi S, Souppaya M, Scarfone KA (2012) Incident Response 4757 
Recommendations and Considerations for Cybersecurity Risk Management. 4758

<!-- page 154 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
136 
(National Institute of Standards and Technology, Gaithersburg, MD), NIST 4759 
Special Publication (SP) NIST SP 800-61r3. 4760 
https://doi.org/10.6028/NIST.SP.800-61r3 4761 
[SP800-73-4] Cooper DA, Ferraiolo H, Mehta KL, Francomacaro S, Chandramouli R, Mohler 4762 
J (2015) Interfaces for Personal Identity Verification. (National Institute of 4763 
Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 4764 
NIST SP 800-73-4, Includes updates as of February 8, 2016. 4765 
https://doi.org/10.6028/NIST.SP.800-73-4  4766 
[SP800-76-2] Grother PJ, Salamon WJ, Chandramouli R (2013) Biometric Specifications for 4767 
Personal Identity Verification. (National Institute of Standards and 4768 
Technology, Gaithersburg, MD), NIST Special Publication (SP) NIST SP 800-76-4769 
2. https://doi.org/10.6028/NIST.SP.800-76-2  4770 
[SP800-78-4] Polk WT, Dodson DF, Burr WE, Ferraiolo H, Cooper DA (2015) Cryptographic 4771 
Algorithms and Key Sizes for Personal Identity Verification. (National Institute 4772 
of Standards and Technology, Gaithersburg, MD), NIST Special Publication 4773 
(SP) NIST SP 800-78-4. https://doi.org/10.6028/NIST.SP.800-78-4  4774 
[SP1800-45] Tang C, Marron J, Saravia S, Fenimore P, Stea B, White C, Wiltberger J (2026) 4775 
Cybersecurity for the Water and Wastewater Sector. (National Institute of 4776 
Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 4777 
NIST SP 1800-45. https://doi.org/10.6028/NIST.SP.1800-45  4778 
[UFC4-010-06] U.S. Army Corps of Engineers, Naval Facilities Engineering Systems 4779 
Command, Air Force Civil Engineer Center (2023) Cybersecurity of Facility-4780 
Related Control Systems (FRCS). Unified Facilities Criteria (UFC) 4-010-06. 4781 
Available a: https://www.wbdg.org/ffc/dod/unified-facilities-criteria-ufc/ufc-4782 
4-010-06 4783 
[USC44-3552] “Definitions,” Title 44 U.S. Code, Sec. 3552. 2018 ed. Available at 4784 
https://www.govinfo.gov/app/details/USCODE-2020-title44/USCODE-2020-4785 
title44-chap35-subchapII-sec3552  4786 
[Williams] Williams TJ (1989) A Reference Model For Computer Integrated 4787 
Manufacturing (CIM). (Instrument Society of America, Research Triangle 4788 
Park, NC). Available at 4789 
http://www.pera.net/Pera/PurdueReferenceModel/ReferenceModel.html 4790 
 4791

<!-- page 155 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
137 
Appendix A. List of Symbols, Abbreviations, and Acronyms 4792 
Selected acronyms and abbreviations used in this paper are defined below. 4793 
A3 4794 
Association for Advancing Automation 4795 
ABAC 4796 
Attribute-Based Access Control 4797 
ACC 4798 
American Chemistry Council 4799 
ACI 4800 
Aviation Cyber Initiative 4801 
ACL 4802 
Access Control List 4803 
AES 4804 
Advanced Encryption Standard 4805 
AFPM 4806 
American Fuel and Petrochemical Manufacturers 4807 
AGA 4808 
American Gas Association 4809 
AHA 4810 
American Hospital Association 4811 
AI 4812 
Artificial Intelligence 4813 
AMA 4814 
American Medical Association 4815 
AMI 4816 
Advanced Metering Infrastructure 4817 
AMWA 4818 
Association of Metropolitan Water Agencies 4819 
AO 4820 
Authorizing Official 4821 
APCP 4822 
American Hospital Association Preferred Cybersecurity Provider 4823 
API 4824 
American Petroleum Institute, Application Programming Interface  4825 
APPA 4826 
American Public Power Association 4827 
APT 4828 
Advanced Persistent Threat 4829

<!-- page 156 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
138 
ASDSO 4830 
Association of State Dam Safety Officials 4831 
ASHRAE 4832 
American Society of Heating, Refrigerating and Air-Conditioning Engineers 4833 
ATO 4834 
Air Traffic Organization 4835 
AWWA 4836 
American Water Works Association 4837 
BAD 4838 
Behavioral Anomaly Detection 4839 
BACS 4840 
Building Automation and Control System 4841 
BCP 4842 
Business Continuity Plan 4843 
BES 4844 
Bulk Electric System 4845 
BPCS 4846 
Basic Process Control System 4847 
C-SCRM 4848 
Cybersecurity Supply Chain Risk Management 4849 
CCE 4850 
Consequence-Driven Cyber-Informed Engineering 4851 
CCTV 4852 
Closed-Circuit Television 4853 
CD 4854 
Compact Disc 4855 
CDC 4856 
Cybersecurity Defense Community 4857 
CEO 4858 
Chief Executive Officer 4859 
CERT 4860 
Computer Emergency Response Team 4861 
CESER 4862 
Cybersecurity, Energy Security, and Emergency Response 4863 
CFATS 4864 
Chemical Facility Anti-Terrorism Standards 4865 
CI 4866 
Critical Infrastructure 4867

<!-- page 157 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
139 
CIE 4868 
Cyber-Informed Engineering 4869 
CIGRE 4870 
International Council on Large Electric Systems 4871 
CIM 4872 
Computer Integrated Manufacturing 4873 
CIO 4874 
Chief Information Officer 4875 
CIP 4876 
Common Industrial Protocol, Critical Infrastructure Protection 4877 
CIPAC 4878 
Critical Infrastructure Partnership Advisory Council 4879 
CISA 4880 
Cybersecurity and Infrastructure Security Agency 4881 
CISO 4882 
Chief Information Security Officer 4883 
CMVP 4884 
Cryptographic Module Validation Program 4885 
CNSS 4886 
Committee on National Security Systems 4887 
CNSSI 4888 
Committee on National Security Systems Instruction 4889 
COO 4890 
Chief Operating Officer 4891 
COTS 4892 
Commercial Off-the-Shelf 4893 
CPNI 4894 
Centre for the Protection of National Infrastructure 4895 
CPS 4896 
Cyber-Physical System 4897 
CPU 4898 
Central Processing Unit 4899 
CRISP 4900 
Cybersecurity Risk Information Sharing Program 4901 
CSET 4902 
Cyber Security Evaluation Tool 4903 
CSF 4904 
Cybersecurity Framework 4905

<!-- page 158 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
140 
CSO 4906 
Chief Security Officer 4907 
CSRC 4908 
Computer Security Resource Center 4909 
CSRIC 4910 
Communications Security, Reliability, and Interoperability Council  4911 
CTI 4912 
Cyber Threat Intelligence 4913 
CVE 4914 
Common Vulnerabilities and Exposures 4915 
CyTRICS 4916 
Cyber Testing for Resilient Industrial Control Systems 4917 
DCS 4918 
Distributed Control System 4919 
DDC 4920 
Direct Digital Control 4921 
DES 4922 
Data Encryption Standard 4923 
DHCP 4924 
Dynamic Host Configuration Protocol 4925 
DHS 4926 
Department of Homeland Security 4927 
DICWG 4928 
Digital Instrumentation and Control Working Group 4929 
DLP 4930 
Data Loss Prevention 4931 
DMZ 4932 
Demilitarized Zone 4933 
DNP3 4934 
DNP3 Distributed Network Protocol (published as IEEE 1815) 4935 
DNS 4936 
Domain Name System 4937 
DOE 4938 
Department of Energy 4939 
DoS 4940 
Denial of Service 4941 
DOT 4942 
United States Department of Transportation 4943

<!-- page 159 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
141 
DRP 4944 
Disaster Recovery Plan 4945 
DSS 4946 
Digital Signature Standard 4947 
DVD 4948 
Digital Video Disc 4949 
EDR 4950 
Endpoint Detection and Response 4951 
E-ISAC 4952 
Electricity Information Sharing and Analysis Center 4953 
EM 4954 
Electromagnetic 4955 
EMBS 4956 
IEEE Engineering in Medicine and Biology Society 4957 
EMP 4958 
Electromagnetic Pulse 4959 
EMS 4960 
Energy Management System 4961 
EOL 4962 
End of Life 4963 
EOS 4964 
End of Support 4965 
EPA 4966 
United States Environmental Protection Agency 4967 
EPRI 4968 
Electric Power Research Institute 4969 
ERM 4970 
Enterprise Risk Management 4971 
ERP 4972 
Enterprise Resource Planning 4973 
ESD 4974 
Emergency Shutdown 4975 
ESS 4976 
Electronic Security Systems 4977 
FAA 4978 
Federal Aviation Administration 4979 
FCC 4980 
Federal Communications Commission 4981 
FDA 4982 
United States Food and Drug Administration 4983

<!-- page 160 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
142 
FEMA 4984 
Federal Emergency Management Agency 4985 
FGS 4986 
Fire and Gas System 4987 
FHWA 4988 
Federal Highway Administration 4989 
FIPS 4990 
Federal Information Processing Standards 4991 
FISMA 4992 
Federal Information Security Modernization Act 4993 
FMCSA 4994 
Federal Motor Carrier Safety Administration 4995 
FMEA 4996 
Failure Mode and Effects Analysis 4997 
FRA 4998 
Federal Railroad Administration 4999 
FRCS 5000 
Facility-Related Control Systems 5001 
FTA 5002 
Federal Transit Administration 5003 
FTP 5004 
File Transfer Protocol 5005 
GCC 5006 
Government Coordinating Council 5007 
GCIP 5008 
GIAC Critical Infrastructure Protection 5009 
GIAC 5010 
Global Information Assurance Certification 5011 
GICSP 5012 
Global Industrial Cyber Security Professional 5013 
GPS 5014 
Global Positioning System 5015 
GRID 5016 
GIAC Response and Industrial Defense 5017 
HART 5018 
Highway Addressable Remote Transducer Protocol 5019 
HC3 5020 
Health Sector Cybersecurity Coordination Center 5021

<!-- page 161 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
143 
HHS 5022 
Health and Human Services 5023 
HMI 5024 
Human-Machine Interface 5025 
HR 5026 
Human Resources 5027 
HSE 5028 
Health, Safety, and Environment 5029 
HSIN 5030 
Homeland Security Information Network 5031 
HSIN-CI 5032 
Homeland Security Information Network - Critical Infrastructure 5033 
HSPD 5034 
Homeland Security Presidential Directive 5035 
HTTP 5036 
Hypertext Transfer Protocol 5037 
HTTPS 5038 
Hypertext Transfer Protocol Secure 5039 
HVAC 5040 
Heating, Ventilation, and Air Conditioning 5041 
I/O 5042 
Input/Output 5043 
IAARC 5044 
International Association for Automation and Robotics in Construction  5045 
IACS 5046 
Industrial Automation and Control System 5047 
IAEA 5048 
International Atomic Energy Agency 5049 
IAM 5050 
Identity and Access Management 5051 
ICCP 5052 
Inter-Control Center Communications Protocol 5053 
ICS 5054 
Industrial Control System 5055 
ICSS 5056 
Integrated Control and Safety Systems 5057 
ID 5058 
Identification 5059

<!-- page 162 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
144 
IDS 5060 
Intrusion Detection System 5061 
IEC 5062 
International Electrotechnical Commission 5063 
IED 5064 
Intelligent Electronic Device 5065 
IEEE 5066 
Institute of Electrical and Electronics Engineers 5067 
IES 5068 
IEEE Industrial Electronics Society 5069 
IETF 5070 
Internet Engineering Task Force 5071 
IFIP 5072 
International Federation for Information Processing 5073 
IIC 5074 
Industry IoT Consortium, Industrial Internet of Things Consortium 5075 
IIoT 5076 
Industrial Internet of Things 5077 
INL 5078 
Idaho National Laboratory 5079 
IoT 5080 
Internet of Things 5081 
IP 5082 
Internet Protocol 5083 
IPS 5084 
Intrusion Prevention System 5085 
IPsec 5086 
Internet Protocol Security 5087 
IR 5088 
Incident Response 5089 
ISA 5090 
International Society of Automation 5091 
ISAC 5092 
International Sharing and Analysis Center 5093 
ISCM 5094 
Information Security Continuous Monitoring 5095 
ISO 5096 
International Organization for Standardization 5097

<!-- page 163 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
145 
IT 5098 
Information Technology 5099 
ITL 5100 
Information Technology Laboratory 5101 
KPI 5102 
Key Performance Indicator 5103 
KRI 5104 
Key Risk Indicator 5105 
LAN 5106 
Local Area Network 5107 
LDAP 5108 
Lightweight Directory Access Protocol 5109 
LTE 5110 
Long-Term Evolution 5111 
MAC 5112 
Media Access Control 5113 
MARAD 5114 
Maritime Administration 5115 
MBR 5116 
Master Boot Record 5117 
MCAA 5118 
Measurement, Control, & Automation Association 5119 
MES 5120 
Manufacturing Execution System 5121 
MFA 5122 
Multi-Factor Authentication 5123 
MIB 5124 
Management Information Base 5125 
ML 5126 
Machine Learning 5127 
MTTD 5128 
Mean Time to Detect 5129 
MTTR 5130 
Mean Time to Respond 5131 
MTU 5132 
Master Terminal Unit 5133 
NAM 5134 
National Association of Manufacturers 5135 
NAWC 5136 
National Association of Water Companies 5137

<!-- page 164 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
146 
NCC 5138 
National Coordinating Center for Communications 5139 
NEA 5140 
Nuclear Energy Agency 5141 
NEI 5142 
Nuclear Energy Institute 5143 
NERC 5144 
North American Electric Reliability Corporation 5145 
NESCOR 5146 
National Electric Sector Cybersecurity Resource 5147 
NFS 5148 
Network File System 5149 
NFU 5150 
National Farmers Union 5151 
NGFW 5152 
Next Generation Firewall 5153 
NHTSA 5154 
National Highway Traffic Safety Administration 5155 
NICE 5156 
National Initiative for Cybersecurity Education 5157 
NIH 5158 
National Institutes of Health 5159 
NIMS 5160 
National Incident Management System 5161 
NIST 5162 
National Institute of Standards and Technology 5163 
NIST IR 5164 
National Institute of Standards and Technology Internal or Interagency Report 5165 
NITAAC 5166 
National Institutes of Health Information Technology Acquisition and Assessment Center  5167 
NLR 5168 
National Laboratory of the Rockies 5169 
NOC 5170 
Network Operations Center 5171 
NRC 5172 
United States Nuclear Regulatory Commission 5173 
NTAS 5174 
National Terrorism Advisory System 5175

<!-- page 165 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
147 
NTP 5176 
Network Time Protocol 5177 
NTSB 5178 
National Transportation Safety Board 5179 
NVD 5180 
National Vulnerability Database 5181 
OEM 5182 
Original Equipment Manufacturer 5183 
OMB 5184 
Office of Management and Budget 5185 
OPC 5186 
Open Platform Communications 5187 
OS 5188 
Operating System 5189 
OSI 5190 
Open Systems Interconnection 5191 
OSINT 5192 
Open-Source Intelligence 5193 
OT 5194 
Operational Technology 5195 
PACE 5196 
Primary, Alternate, Contingency, and Emergency 5197 
PACS 5198 
Physical Access Control System, Picture Archiving and Communications Systems 5199 
PAM 5200 
Privileged Access Management 5201 
PC 5202 
Personal Computer 5203 
PERA 5204 
Purdue Enterprise Reference Architecture 5205 
PES 5206 
IEEE Power & Energy Society 5207 
PHA 5208 
Process Hazard Analysis 5209 
PHM4SM 5210 
Prognostics and Health Management for Reliable Operations in Smart Manufacturing  5211 
PHMSA 5212 
Pipeline and Hazardous Materials Safety Administration 5213

<!-- page 166 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
148 
PID 5214 
Proportional-Integral-Derivative 5215 
PIN 5216 
Personal Identification Number 5217 
PIV 5218 
Personal Identity Verification 5219 
PLC 5220 
Programmable Logic Controller 5221 
PNNL 5222 
Pacific Northwest National Laboratory 5223 
PNT 5224 
Positioning, Navigation, and Timing 5225 
PPD 5226 
Presidential Policy Directive 5227 
PQC 5228 
Post-Quantum Cryptography 5229 
PRAM 5230 
Privacy Risk Assessment Methodology 5231 
PSCCC 5232 
IEEE Power System Communications and Cybersecurity 5233 
PSS 5234 
Process Safety Shutdown 5235 
PT 5236 
Pressure Transmitter 5237 
PTP 5238 
Precision Time Protocol 5239 
R&D 5240 
Research and Development 5241 
RAS 5242 
IEEE Robotics and Automation Society 5243 
RBAC 5244 
Role-Based Access Control 5245 
RDP 5246 
Remote Desktop Protocol 5247 
RF 5248 
Radio Frequency 5249 
RFC 5250 
Request for Comments 5251

<!-- page 167 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
149 
RFID 5252 
Radio Frequency Identification 5253 
RMF 5254 
Risk Management Framework 5255 
RPC 5256 
Remote Procedure Call 5257 
RPO 5258 
Recovery Point Objective 5259 
RTO 5260 
Recovery Time Objective 5261 
RTOS 5262 
Real-Time Operating System 5263 
RTU 5264 
Remote Terminal Unit 5265 
S4 5266 
SCADA Security Scientific Symposium 5267 
SANS 5268 
SysAdmin, Audit, Network, and Security 5269 
SBOM 5270 
Software Bill of Materials 5271 
SBU 5272 
Sensitive But Unclassified 5273 
SC 5274 
Security Category 5275 
SCADA 5276 
Supervisory Control and Data Acquisition 5277 
SCAI 5278 
Safety, Controls, Alarms, and Interlocks 5279 
SCC 5280 
Sector Coordinating Council 5281 
SD 5282 
Secure Digital 5283 
SDLC 5284 
Software Development Life Cycle, System Development Life Cycle 5285 
SDN 5286 
Software-Defined Networking 5287 
SEPA 5288 
Smart Electric Power Alliance 5289

<!-- page 168 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
150 
SGCC 5290 
Smart Grid Cybersecurity Committee 5291 
SHA 5292 
Secure Hash Algorithm 5293 
SIEM 5294 
Security Information and Event Management 5295 
SIF 5296 
Safety Instrumented Function 5297 
SIS 5298 
Safety Instrumented System 5299 
SOC 5300 
Security Operations Center 5301 
SOCMA 5302 
Society of Chemical Manufacturers and Affiliates 5303 
SP 5304 
Special Publication 5305 
SPAN 5306 
Switched Port Analyzer 5307 
SQL 5308 
Structured Query Language 5309 
SSA 5310 
Sector-Specific Agency 5311 
SSCP 5312 
Secure SCADA Communications Protocol 5313 
SSH 5314 
Secure Shell 5315 
SSID 5316 
Service Set Identifier 5317 
SSL 5318 
Secure Sockets Layer 5319 
SSPP 5320 
Substation Serial Protection Protocol 5321 
TAP 5322 
Test Access Point 5323 
TC 5324 
Technical Committee 5325 
TCP 5326 
Transmission Control Protocol 5327

<!-- page 169 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
151 
TCP/IP 5328 
Transmission Control Protocol/Internet Protocol 5329 
TFTP 5330 
Trivial File Transfer Protocol 5331 
TIP 5332 
Technical Information Paper 5333 
TLS 5334 
Transport Layer Security 5335 
TLV 5336 
Type, Length, Value 5337 
TPM 5338 
Trusted Platform Module 5339 
TSA 5340 
Transportation Security Administration 5341 
TT 5342 
Temperature Transmitter 5343 
UDP 5344 
User Datagram Protocol 5345 
UFC 5346 
Unified Facilities Criteria 5347 
UPS 5348 
Uninterruptible Power Supply 5349 
U.S. 5350 
United States 5351 
USB 5352 
Universal Serial Bus 5353 
USDA 5354 
United States Department of Agriculture 5355 
VAV 5356 
Variable Air Volume 5357 
VDP 5358 
Vulnerability Disclosure Policy 5359 
VLAN 5360 
Virtual Local Area Network 5361 
VoIP 5362 
Voice over Internet Protocol 5363 
VPN 5364 
Virtual Private Network 5365

<!-- page 170 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
152 
VTS 5366 
IEEE Vehicular Technology Society 5367 
WAF 5368 
Web Application Firewall 5369 
WAN 5370 
Wide Area Network 5371 
WG 5372 
Working Group 5373 
Wi-Fi 5374 
Wireless Fidelity 5375 
WINS 5376 
World Institute of Nuclear Security 5377 
ZTA 5378 
Zero Trust Architecture 5379 
ZTNA 5380 
Zero Trust Network Access 5381 
 5382

<!-- page 171 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
153 
Appendix B. Glossary 5383 
Selected terms used in this publication are defined below. Source references are included for 5384 
certain definitions. 5385 
access control list 5386 
A mechanism that implements access control for a system resource by enumerating the identities of the system 5387 
entities that are permitted to access the resources. [RFC4949] (adapted) 5388 
actuator 5389 
A device for moving or controlling a mechanism or system. It is operated by a source of energy, typically electric 5390 
current, hydraulic fluid pressure, or pneumatic pressure, and converts that energy into motion. An actuator is the 5391 
mechanism by which a control system acts upon an environment. The control system can be simple (a fixed 5392 
mechanical or electronic system), software-based (e.g., a printer driver, robot control system), or a human or other 5393 
agent. 5394 
advanced metering infrastructure 5395 
An integrated system of smart meters, communications networks, and data management systems that enables  5396 
two-way communication between utilities and customers. [DOE-AMI] 5397 
advanced persistent threat 5398 
An adversary with sophisticated levels of expertise and significant resources that pursues its objectives repeatedly 5399 
over an extended period, adapting to defenders' efforts to resist it. [SP800 -39] (adapted) 5400 
alarm 5401 
A device or function that signals the existence of an abnormal condition by making an audible or visible discrete 5402 
change, or both, so as to attract attention to that condition. [ANSI-ISA-5-1] 5403 
antivirus tools 5404 
Software products and technology used to detect malicious code, prevent it from infecting a system, and remove 5405 
malicious code that has infected the system. 5406 
attack 5407 
An attempt to gain unauthorized access to system services, resources, or information or an attempt to 5408 
compromise system integrity, availability, or confidentiality. 5409 
authentication 5410 
Verifying the identity of a user, process, or device, often as a prerequisite to allowing access to resources in an 5411 
information system. [FIPS200] 5412 
authorization 5413 
The right or permission that is granted to a system entity to access a system resource.  [RFC4949] (adapted) 5414 
backdoor 5415 
An undocumented way of gaining access to a computer system. A backdoor is a potential security risk.  5416 
buffer overflow 5417 
A condition at an interface under which more input can be placed into a buffer or data holding area than the 5418 
capacity allocated, overwriting other information. Adversaries exploit such a condition to crash a system or to 5419 
insert specially crafted code that allows them to gain control of the system.  [SP800-28v2] 5420 
building automation and control system 5421 
A type of OT system used to manage critical building infrastructure and optimize facility operations, overseeing 5422 
systems such as heating, ventilation, and air conditioning (HVAC), fire safety, electrical and lighting, physical 5423 
security and access control, and energy management. 5424

<!-- page 172 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
154 
cleartext 5425 
Information that is not encrypted. 5426 
closed-circuit television 5427 
A system of video cameras used to transmit signals to a specific, limited set of monitors for surveillance and 5428 
monitoring purposes. 5429 
communications router 5430 
A communications device that transfers messages between two networks. Common uses for routers include 5431 
connecting a LAN to a WAN and connecting MTUs and RTUs to a long -distance network medium for SCADA 5432 
communication. 5433 
confidentiality 5434 
Preserving authorized restrictions on information access and disclosure, including means for protecting personal 5435 
privacy and proprietary information. [USC44-3552] (adapted) 5436 
configuration (of a system or device) 5437 
Step in system design; for example, selecting functional units, assigning their locations, and defining their 5438 
interconnections. 5439 
configuration control 5440 
Process for controlling modifications to hardware, firmware, software, and documentation to ensure the 5441 
information system is protected against improper modifications before, during, and after system implementation.  5442 
[CNSS4009] (adapted) 5443 
control 5444 
The part of the OT system used to monitor and control the physical process. This includes all control servers, field 5445 
devices, actuators, sensors, and their supporting communication systems.   5446 
control algorithm 5447 
A mathematical representation of the control action to be performed. [ISADICT] 5448 
control center 5449 
An equipment structure or group of structures from which a process is measured, controlled, and/or monitored.  5450 
[ANSI-ISA-51-1] 5451 
control loop 5452 
A control loop consists of sensors for measurement, controller hardware (e.g., PLCs), actuators (e.g., control 5453 
valves, breakers, switches, and motors), and the communication of variables. Controlled variables are transmitted 5454 
to the controller from the sensors. The controller interprets the signals and generates corresponding manipulated 5455 
variables based on set points, which it transmits to the actuators. Process changes from disturbances result in new 5456 
sensor signals, identifying the state of the process, to again be transmitted to the controller.   5457 
control network 5458 
Those networks of an enterprise typically connected to equipment that controls physical processes and that is 5459 
time- or safety-critical. The control network can be subdivided into zones, and there can be multiple separate 5460 
control networks within one enterprise and site. 5461 
control server 5462 
A controller that also acts as a server that hosts the control software that communicates with lower -level control 5463 
devices, such as remote terminal units (RTUs) and programmable logic controllers (PLCs), over an OT network. In a 5464 
SCADA system, this is often called a SCADA server, MTU, or supervisory controller.  5465 
control system 5466 
A system in which deliberate guidance or manipulation is used to achieve a prescribed value for a variable. Control 5467 
systems include SCADA, DCS, PLCs, BAS, and other types of OT measurement and control systems. 5468

<!-- page 173 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
155 
controlled variable 5469 
The variable that the control system attempts to keep at the set point value. The set point may be constant or 5470 
variable. [ISADICT] 5471 
controller 5472 
A device or program that operates automatically to regulate a controlled variable.  [ANSI-ISA-51-1] 5473 
cyber threat intelligence 5474 
Cyber threat information that has been aggregated, transformed, analyzed, interpreted, or enriched to provide the 5475 
necessary context for decision-making processes. [SP800-61r3] (adapted) 5476 
cycle time 5477 
The time, usually expressed in seconds, for a controller to complete one control loop where sensor signals are read 5478 
into memory, control algorithms are executed, and corresponding control signals are transmitted to actuators that 5479 
create changes to the process resulting in new sensor signals. [ISADICT] 5480 
data diode 5481 
A network appliance or device that allows data to travel only in one direction. Also referred to as a unidirectional 5482 
gateway, deterministic one-way boundary device, or unidirectional network. 5483 
data historian 5484 
A centralized database that supports data analysis using statistical process control techniques. 5485 
database 5486 
A repository of information that usually holds plant-wide information including process data, recipes, personnel 5487 
data, and financial data. [IR6859] (adapted) 5488 
demilitarized zone 5489 
An interface on a routing firewall that is similar to the interfaces found on the firewall’s protected side. Traffic 5490 
moving between the DMZ and other interfaces on the protected side of the firewall still goes through the firewall 5491 
and can have firewall protection policies applied. [SP800-41r1] 5492 
denial of service 5493 
The prevention of authorized access to a system resource or the delaying of system operations and functions.  5494 
[RFC4949] 5495 
diagnostics 5496 
Information concerning known failure modes and their characteristics. Such information can be used in 5497 
troubleshooting and failure analysis to help pinpoint the cause of a failure and help define suitable corrective 5498 
measures. [ISADICT] 5499 
digital twin 5500 
A computer model of a physical system, such as a machine or building, used to monitor status, detect anomalies, 5501 
and predict system behavior. [NIST-DT] (adapted) 5502 
direct digital control 5503 
A control approach in which a digital computer or controller directly manages building equipment (e.g., HVAC 5504 
components) through software logic rather than analog control loops.  5505 
disaster recovery plan 5506 
A written plan for processing critical applications in the event of a major hardware or software failure or 5507 
destruction of facilities. [SP800-34r1] (adapted) 5508 
discrete process 5509 
A type of process where a specified quantity of material moves as a unit (part or group of parts) between 5510 
workstations, and each unit maintains its unique identity. [ISADICT] 5511

<!-- page 174 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
156 
distributed control system 5512 
In a control system, refers to control achieved by intelligence that is distributed about the process to be controlled, 5513 
rather than by a centrally located single unit. [ISADICT] 5514 
disturbance 5515 
An undesired change in a variable being applied to a system that tends to adversely affect the value of a controlled 5516 
variable. [ANSI-ISA-51-1] 5517 
domain 5518 
An environment or context that includes a set of system resources and a set of system entities that have the right 5519 
to access the resources as defined by a common security policy, security model, or security architecture.  [RFC4949] 5520 
(adapted) 5521 
electronic security systems 5522 
Systems used to monitor and control access to a facility, such as intrusion detection, video surveillance, and 5523 
physical access control systems. 5524 
encryption 5525 
Cryptographic transformation of data (called “plaintext”) into a form (called “ciphertext”) that conceals the data’s 5526 
original meaning to prevent it from being known or used. If the transformation is reversible, the corresponding 5527 
reversal process is called “decryption,” which is a transformation that restores encrypted data to its original state.  5528 
[RFC4949] (adapted) 5529 
endpoint detection and response 5530 
A category of tools that continuously monitor endpoint behavior and collect telemetry to detect and respond to 5531 
threats. 5532 
end of life 5533 
The point at which a vendor stops selling or actively supporting a product, often signaling that security patches and 5534 
updates will no longer be provided. 5535 
end of support 5536 
The point at which a vendor ceases all technical support and maintenance for a product, including security 5537 
updates. 5538 
enterprise 5539 
An organization that coordinates the operation of one or more processing sites.  5540 
enterprise resource planning 5541 
A category of business management software that integrates core organizational processes, such as finance, 5542 
procurement, and supply chain, into a unified system. 5543 
facility-related control systems 5544 
A subset of control systems used to monitor and control equipment and systems related to DoD real property 5545 
facilities, such as building control systems, utility control systems, electronic security systems, and fire and life 5546 
safety systems. [UFC 4-010-06] 5547 
fault tolerant 5548 
A system having the built-in capability to provide continued, correct execution of its assigned function in the 5549 
presence of a hardware and/or software fault. 5550 
field device 5551 
Equipment that is connected to the field side on an ICS. Types of field devices include RTUs, PLCs, actuators, 5552 
sensors, HMIs, and associated communications.  5553

<!-- page 175 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
157 
field site 5554 
A subsystem that is identified by physical, geographical, or logical segmentation within the ICS. A field site may 5555 
contain RTUs, PLCs, actuators, sensors, HMIs, and associated communications.   5556 
fieldbus 5557 
A digital, serial, multi-drop, two-way data bus or communication path or link between low-level industrial field 5558 
equipment, such as sensors, transducers, actuators, local controllers, and even control room devices. Use of 5559 
fieldbus technologies eliminates the need for point-to-point wiring between the controller and each device. A 5560 
protocol is used to define messages over the fieldbus network, and each message identifies a particular sensor on 5561 
the network.  5562 
firewall 5563 
An inter-network gateway that restricts data communication traffic to and from one of the connected networks 5564 
(the one said to be “inside” the firewall) and thus protects that network’s system resources against threats from 5565 
the other network (the one that is said to be “outside” the firewall).  [RFC4949] 5566 
health, safety, and environment 5567 
A category of risk impact involving potential harm to personnel, the public, or the environment.  5568 
human-machine interface 5569 
The hardware or software through which an operator interacts with a controller. An HMI can range from a physical 5570 
control panel with buttons and indicator lights to an industrial PC with a color graphics display running dedicated 5571 
HMI software. [IR6859] 5572 
identification 5573 
The process of verifying the identity of a user, process, or device, usually as a prerequisite for granting access to 5574 
resources in an IT system.  5575 
identity and access management 5576 
Broadly refers to the administration of individual identities within a system, such as a company, a network, or even 5577 
a country. [SP800-175A] (adapted) 5578 
incident 5579 
An occurrence that actually or potentially jeopardizes the confidentiality, integrity, or availability of an information 5580 
system or the information the system processes, stores, or transmits or that constitutes a violation or imminent 5581 
threat of violation of security policies, security procedures, or acceptable use policies.  [FIPS200] 5582 
industrial control system 5583 
A general term that encompasses several types of control systems, including supervisory control and data 5584 
acquisition (SCADA) systems, distributed control systems (DCS), and other control system configurations that are 5585 
often found in the industrial sectors and critical infrastructures, such as programmable logic controllers (PLC). An 5586 
ICS consists of combinations of control components (e.g., electrical, mechanical, hydraulic, pneumatic) that act 5587 
together to achieve an industrial objective (e.g., manufacturing, transportation of matter or energy).   5588 
information security program plan 5589 
A formal document that provides an overview of the security requirements for an organization -wide information 5590 
security program and describes the program management controls and common controls in place or planned for 5591 
meeting those requirements. [OMB-A130] 5592 
input/output 5593 
A general term for the equipment that is used to communicate with a computer as well as the data involved in the 5594 
communications. [ISADICT] 5595 
insider 5596 
An entity inside the security perimeter that is authorized to access system resources but uses them in a way that is 5597 
not approved by those who granted the authorization. 5598

<!-- page 176 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
158 
integrity 5599 
Guarding against improper information modification or destruction, which  includes ensuring information non-5600 
repudiation and authenticity. [USC44-3552] (adapted) 5601 
intelligent electronic device 5602 
Any device incorporating one or more processors with the capability to receive or send data/control from or to an 5603 
external source (e.g., electronic multifunction meters, digital relays, controllers).  [AGA12] 5604 
internet 5605 
The single interconnected worldwide system of commercial, government, educational, and other computer 5606 
networks that share the set of protocols specified by the Internet Architecture Board (IAB) and the name and 5607 
address spaces managed by the Internet Corporation for Assigned Names and Numbers (ICANN).  [RFC4949] 5608 
(adapted)  5609 
intrusion detection system 5610 
A security service that monitors and analyzes network or system events for the purpose of finding and providing 5611 
real-time or near-real-time warning of attempts to access system resources in an unauthorized manner.  [RFC4949] 5612 
(adapted) 5613 
intrusion prevention system 5614 
A system that can detect an intrusive activity and also attempt to stop the activity, ideally before it reaches its 5615 
targets. 5616 
jitter 5617 
The time or phase difference between the data signal and the ideal clock.  5618 
key performance indicator 5619 
A measurable value that demonstrates how effectively an organization is achieving key business or security 5620 
objectives. 5621 
key risk indicator 5622 
A metric used to signal an increasing exposure to risk in various areas of an organization, providing early warning 5623 
of potential issues. 5624 
local area network 5625 
A group of computers and other devices dispersed over a relatively limited area and connected by a 5626 
communications link that enables any device to interact with any other on the network.  5627 
long-term evolution 5628 
A standard for wireless broadband communication for mobile devices and data terminals, sometimes used for 5629 
remote or cellular-based OT connectivity. 5630 
machine controller 5631 
A control system/motion network that electronically synchronizes drives within a machine system instead of 5632 
relying on synchronization via mechanical linkage. [IR6859] 5633 
machine learning 5634 
The development and use of computer systems that adapt and learn from data with the goal of improving 5635 
accuracy. [SP800-55v1] 5636 
maintenance 5637 
Any act that either prevents the failure or malfunction of equipment or restores its operating capability.  [ISADICT] 5638 
malware 5639 
Software or firmware intended to perform an unauthorized process that will have adverse impact on the 5640 
confidentiality, integrity, or availability of an information system. A virus, worm, Trojan horse, or other code -based 5641 
entity that infects a host. [SP800-53r5] (adapted)  5642

<!-- page 177 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
159 
manipulated variable 5643 
In a process that is intended to regulate some condition, a quantity or a condition that the control alters to initiate 5644 
a change in the value of the regulated condition. [ISADICT]  5645 
manufacturing execution system 5646 
A system that uses network computing to automate production control and process automation. By downloading 5647 
recipes and work schedules and uploading production results, a MES bridges the gap between business and plant -5648 
floor or process-control systems. [IR6859] 5649 
master terminal unit 5650 
See Control Server.  5651 
mean time to detect 5652 
A metric that tracks the average amount of time that a problem exists before it is found.  [SP800-55v1] 5653 
mean time to respond 5654 
The average time it takes an organization to respond to a security incident after detection.  5655 
network operations center 5656 
A centralized location from which an organization monitors, manages, and maintains its network infrastructure.  5657 
open-source intelligence 5658 
Information collected from publicly available sources and analyzed to produce actionable intelligence.  5659 
operating system 5660 
An integrated collection of service routines for supervising the sequencing of programs by a computer. An 5661 
operating system may perform the functions of input/output control, resource scheduling, and data management. 5662 
It provides application programs with the fundamental commands for controlling the computer.  [ISADICT] 5663 
operational controls 5664 
The security controls (i.e., safeguards or countermeasures) for an information system that are primarily 5665 
implemented and executed by people (as opposed to systems). [FIPS200] 5666 
operational technology 5667 
A broad range of programmable systems and devices that interact with the physical environment or manage 5668 
devices that interact with the physical environment. These systems and devices detect or cause a direct change 5669 
through the monitoring and/or control of devices, processes, and events. Examples include industrial control 5670 
systems, building automation systems, transportation systems, physical access control systems, physical 5671 
environment monitoring systems, and physical environment measurement systems.   5672 
password 5673 
A string of characters (letters, numbers, and other symbols) used to authenticate an identity or to verify access 5674 
authorization. [FIPS140-2] 5675 
phishing 5676 
Tricking individuals into disclosing sensitive personal information by claiming to be a trustworthy entity in an 5677 
electronic communication (e.g., internet websites). 5678 
plant 5679 
The physical elements necessary to support the physical process. This can include many of the static components 5680 
not controlled by the ICS. However, the operation of the ICS may impact the adequacy, strength, and durability of 5681 
the plant’s components. 5682 
port 5683 
The entry or exit point from a computer for connecting communications or peripheral devices.  5684 
post-quantum cryptography 5685 
An area of cryptography focused on quantum-resistant primitives, with the goal of keeping existing public key 5686

<!-- page 178 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
160 
infrastructure intact in a future era of quantum computing. Also referred to as quantum -resistant cryptography. 5687 
[CSRC-PQC] 5688 
predisposing condition  5689 
A condition that exists within an organization, a mission/business process, enterprise architecture, or information 5690 
system including its environment of operation, which contributes to (i.e., increases or decreases) the likelihood 5691 
that one or more threat events, once initiated, will result in undesirable consequences or adverse impact to 5692 
organizational operations and assets, individuals, other organizations, or the Nation.  [SP800-30r1] 5693 
pressure regulator  5694 
A device used to control the pressure of a gas or liquid. [IR6859] 5695 
pressure sensor 5696 
A sensor system that produces an electrical signal related to the pressure acting on it by its surrounding medium. 5697 
Pressure sensors can also use differential pressure to obtain level and flow measurements.  [IR6859] (adapted) 5698 
primary, alternate, contingency, and emergency 5699 
A methodology that helps organizations prepare backup communications capabilities and establish options for 5700 
redundant communications if primary capabilities are disrupted or degraded. [CISA -PACE] (adapted) 5701 
privileged access management 5702 
The policies, processes, and technologies used to control, monitor, and secure access to an organization's most 5703 
sensitive accounts and systems. 5704 
process controller  5705 
A type of computer system, typically rack-mounted, that processes sensor input, executes control algorithms, and 5706 
computes actuator outputs. [IR6859] (adapted) 5707 
programmable logic controller 5708 
A solid-state control system that has a user-programmable memory for storing instructions for the purpose of 5709 
implementing specific functions such as I/O control, logic, timing, counting, three -mode (PID) control, 5710 
communication, arithmetic, and data and file processing. [ISADICT] 5711 
protocol 5712 
A set of rules (i.e., formats and procedures) to implement and control some type of association (e.g., 5713 
communication) between systems. [RFC4949] 5714 
protocol analyzer 5715 
A device or software application that enables the user to analyze the performance of network data so as to ensure 5716 
that the network and its associated hardware/software are operating within network specifications.  [ISADICT] 5717 
real time 5718 
Pertaining to the performance of a computation during the actual time that the related physical process transpires 5719 
so that the results of the computation can be used to guide the physical process.   5720 
redundant control server 5721 
A backup to the control server that maintains the current state of the control server at all times.  [IR6859] 5722 
relay 5723 
An electromechanical device that completes or interrupts an electrical circuit by physically moving conductive 5724 
contacts. The resultant motion can be coupled to another mechanism such as a valve or breaker.  [ISADICT]  5725 
remote access 5726 
Access to an organizational system by a user (or a process acting on behalf of a user) communicating through an 5727 
external network. [SP800-53r5] 5728

<!-- page 179 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
161 
remote diagnostics 5729 
Diagnostic activities conducted by individuals who are outside of an information system security perimeter.  5730 
remote maintenance 5731 
Maintenance activities conducted by individuals communicating through an external network. [SP800 -53r5] 5732 
remote terminal unit 5733 
A computer with radio interfacing used in remote situations where communications via wire is unavailable. Usually 5734 
used to communicate with remote field equipment. PLCs with radio communication capabilities are also used in 5735 
place of RTUs. [IR6859] 5736 
risk 5737 
The level of impact on agency operations (including mission, functions, image, or reputation), agency assets, or 5738 
individuals resulting from the operation of an information system, given the potential impact of a threat and the 5739 
likelihood of that threat occurring. [FIPS200] (adapted) 5740 
risk assessment 5741 
The process of identifying risks to agency operations (including mission, functions, image, or reputation), agency 5742 
assets, or individuals by determining the probability of occurrence, the resulting impact, and additional security 5743 
controls that would mitigate this impact. Part of risk management, synonymous with risk analysis. Incorporates 5744 
threat and vulnerability analyses. [SP800-39] (adapted) 5745 
risk management 5746 
The process of managing risks to organizational operations (including mission, functions, image, reputation), 5747 
organizational assets, individuals, other organizations, and the Nation, resulting from the operation of an 5748 
information system, and includes: (i) the conduct of a risk assessment; (ii) the implementation of a risk mitigation 5749 
strategy; and (iii) employment of techniques and procedures for the continuous monitoring of the security state of 5750 
the information system. [FIPS200] (adapted) 5751 
router 5752 
A computer that is a gateway between two networks at OSI layer 3 and that relays and directs data packets 5753 
through that inter-network. The most common form of router operates on IP packets.  [RFC4949] (adapted) 5754 
safety instrumented system 5755 
A system that is composed of sensors, logic solvers, and final control elements whose purpose is to take the 5756 
process to a safe state when predetermined conditions are violated. Other terms commonly used include 5757 
emergency shutdown system (ESS), safety shutdown system (SSD), and safety interlock system (SIS).  [ANSI-ISA-84] 5758 
SCADA server 5759 
The device that acts as the master in a SCADA system. 5760 
security audit 5761 
Independent review and examination of a system’s records and activities to determine the adequacy of system 5762 
controls, ensure compliance with established security policy and procedures, detect breaches in security services, 5763 
and recommend any changes that are indicated for countermeasures. [ISO7498-1] 5764 
security controls 5765 
The management, operational, and technical controls (i.e., safeguards or countermeasures) prescribed for an 5766 
information system to protect the confidentiality, integrity, and availability of the system and its information. 5767 
[FIPS199] 5768 
security plan 5769 
A formal document that provides an overview of the security requirements for an  information system and 5770 
describes the security controls in place or planned for meeting those requirements.  [SP800-18r1] 5771

<!-- page 180 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
162 
security policy 5772 
Security policies define the objectives and constraints for the security program. Policies are created at several 5773 
levels, ranging from organization or corporate policy to specific operational constraints (e.g., remote access). In 5774 
general, policies provide answers to the questions “what” and “why” without dealing with “how.” Policies are 5775 
normally stated in terms that are technology-independent. 5776 
sensor 5777 
A device that produces a voltage or current output that is representative of some physical property being 5778 
measured (e.g., speed, temperature, flow). [ISADICT] 5779 
set point 5780 
An input variable that sets the desired value of the controlled variable. This variable may be manually set, 5781 
automatically set, or programmed. [ISADICT] 5782 
single loop controller 5783 
A controller that controls a very small process or a critical process. [IR6859] 5784 
social engineering 5785 
An attempt to trick someone into revealing information (e.g., a password) that can be used to attack systems or 5786 
networks. [800-115] 5787 
supervisory control 5788 
A term that is used to imply that the output of a controller or computer program is used as input to other 5789 
controllers. See Control Server. [ISADICT] 5790 
supervisory control and data acquisition  5791 
A generic name for a computerized system that is capable of gathering and processing data and applying 5792 
operational controls over long distances. Typical uses include power transmission and distribution and pipeline 5793 
systems. SCADA was designed for the unique communication challenges (e.g., delays, data integrity) posed by the 5794 
various media that must be used, such as phone lines, microwave, and satellite. Usually shared rather than 5795 
dedicated. [ISADICT] 5796 
technical controls  5797 
The security controls (i.e., safeguards or countermeasures) for an information system that are primarily 5798 
implemented and executed by the information system through mechanisms contained in the hardware, software, 5799 
or firmware components of the system. [FIPS200] 5800 
test access point 5801 
A hardware device inserted into a network to passively capture and monitor traffic without disrupting the flow of 5802 
data. 5803 
threat 5804 
Any circumstance or event with the potential to adversely impact agency operations (including safety, mission, 5805 
functions, image, or reputation), agency assets, or individuals through an information system via unauthorized 5806 
access, destruction, disclosure, modification of information, and/or denial of service.  [FIPS200] (adapted) 5807 
threat event 5808 
An event or situation that has the potential for causing undesirable consequences or impact.  [SP800-30r1] 5809 
threat source  5810 
The intent and method targeted at the intentional exploitation of a vulnerability or a situation and method that 5811 
may accidentally trigger a vulnerability. Synonymous with threat agent.  [FIPS200] 5812

<!-- page 181 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
163 
Trojan horse 5813 
A computer program that appears to have a useful function, but also has a hidden and potentially malicious 5814 
function that evades security mechanisms, sometimes by exploiting legitimate authorizations of a system entity 5815 
that invokes the program. [RFC4949] 5816 
unauthorized access 5817 
A person gains logical or physical access without permission to a network, system, application, data, or other 5818 
resource. [SP800-61] 5819 
unidirectional gateway 5820 
Unidirectional gateways are a combination of hardware and software. The hardware permits data to flow from one 5821 
network to another but is physically unable to send any information back to the source network. The software 5822 
replicates databases and emulates protocol servers and devices.  5823 
valve 5824 
An in-line device in a fluid-flow system that can interrupt flow, regulate the rate of flow, or divert flow to another 5825 
branch of the system. [ISADICT] 5826 
virtual private network 5827 
A restricted-use, logical (i.e., artificial or simulated) computer network that is constructed from the system 5828 
resources of a relatively public, physical (i.e., real) network (such as the Internet), often by using encryption 5829 
(located at hosts or gateways), and often by tunneling links of the virtual network across the real network.  5830 
[RFC4949] (adapted) 5831 
virus 5832 
A hidden, self-replicating section of computer software, usually malicious logic, that propagates by infecting (i.e., 5833 
inserting a copy of itself into and becoming part of) another program. A virus cannot run by itself; it requires that 5834 
its host program be run to make the virus active. [RFC4949] (adapted) 5835 
vulnerability 5836 
Weakness in an information system, system security procedures, internal controls, or implementation that could 5837 
be exploited or triggered by a threat source. [FIPS200]  5838 
wide area network 5839 
A physical or logical network that provides data communications to a larger number of independent users than are 5840 
typically served by a local area network (LAN) and that is usually spread over a larger geographic area than that of 5841 
a LAN.  5842 
wireless device 5843 
Any device that can connect to an OT network via radio or infrared waves, usually to collect or monitor data but 5844 
also to modify control set points in some cases.  5845 
workstation  5846 
A computer used for tasks such as programming, engineering, and design.  [IR6859] 5847 
worm 5848 
A computer program that can run independently, can propagate a complete working version of itself onto other 5849 
hosts on a network, and may consume computer resources destructively.  [RFC4949] (adapted) 5850 
zero trust architecture 5851 
A security model and cybersecurity strategy based on the premise that threats exist both inside and outside 5852 
traditional network boundaries. It eliminates implicit trust in any element, component, or service,  requiring 5853 
continuous verification before granting access. [SP800-160v2r1] 5854

<!-- page 182 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
164 
zero trust network access 5855 
A security model and set of technologies that grant access to applications and services based on defined access 5856 
control policies, rather than implicit trust based on network location. 5857 
 5858

<!-- page 183 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
165 
Appendix C. Threat Sources, Vulnerabilities, and Incidents 5859 
Several terms are used to describe the interrelated concepts of threat, threat source, threat 5860 
event, and incident. A threat is any circumstance or event with the potential to adversely 5861 
impact organizational operations (including mission, functions, image, or reputation), 5862 
organizational assets, individuals, other organizations, or the Nation through an information 5863 
system via unauthorized access, destruction, disclosure, modification of information, and/or 5864 
denial of service. Threats have some intent or method that may exploit a vulnerability through 5865 
either intentional or unintentional means. This intent or method is referred to as the threat 5866 
source. A vulnerability is a weakness in an information system (including an OT), system security 5867 
procedures, internal controls, or implementation that could be exploited or triggered by a 5868 
threat source. A threat event is an event or situation that has the potential to cause undesirable 5869 
consequences or impacts. When a threat event occurs, it becomes an incident that actually or 5870 
potentially jeopardizes the confidentiality, integrity, or availability of an information system or 5871 
the information the system processes, stores, or transmits or that constitutes a violation or 5872 
imminent threat of violation of security policies, security procedures, or acceptable use policies.  5873 
This appendix explores OT-specific threat sources, vulnerabilities, and incidents. It also cites 5874 
examples of OT-specific incidents to illustrate their potential impacts. Each organization 5875 
calculates risk based on the specific threats, vulnerabilities, impacts, and likelihood of incidents 5876 
within its environment.  5877 
C.1. Threat Sources 5878 
Threats to OT can come from numerous sources that can be classified as adversarial, accidental, 5879 
structural, or environmental. These threat sources should be well-understood and considered 5880 
part of the risk management strategy to define and implement adequate protection. For 5881 
example, environmental events (e.g., floods, earthquakes) are well-understood but may vary in 5882 
magnitude, frequency, and their ability to compound with other interconnected events. 5883 
However, adversarial threats depend on the resources available to the adversary and the 5884 
emergence of previously unknown vulnerabilities or attacks. Table 10 lists and defines known 5885 
threat sources to OT. 5886 
Table 10. Threats to OT 5887 
Type of Threat Source Description Characteristics 
ADVERSARIAL  
Bot network operators 
Criminal groups 
Hackers/hacktivists 
Insiders 
Nations 
Terrorists 
Individuals, groups, organizations, or nation-states that 
seek to exploit the organization’s dependence on cyber 
resources (e.g., information in electronic form, 
information and communications technologies, and the 
communications and information-handling capabilities 
provided by those technologies). 
Capability, Intent, 
Targeting

<!-- page 184 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
166 
Type of Threat Source Description Characteristics 
ACCIDENTAL  
• User  
• Privileged user or 
administrator 
Erroneous actions taken by individuals in the course of 
executing their everyday responsibilities (e.g., operator 
accidentally typing 100 instead of 10 as a set point; 
engineer making a change in the production 
environment while thinking that they are in the 
development environment). 
Range of effects  
 
STRUCTURAL  
• Hardware failure 
o Processors, 
input/output cards, 
communications 
cards 
o Networking 
equipment 
o Power supply 
o Sensor, final element 
o HMI, displays 
• Software failure 
o OS 
o General-purpose 
applications 
o Mission-specific 
applications 
• Environmental controls failure 
o Temperature control 
o Humidity control 
• Communications degradation 
o Wireless 
o Wired 
Failures of equipment, environmental controls, or 
software due to aging, resource depletion, or other 
circumstances that exceed expected operating 
parameters, including failures of critical infrastructures 
within the control of the organization. 
 
Range of effects  
 
ENVIRONMENTAL  
• Natural or human-caused 
disaster  
o Fire  
o Flood/tsunami  
o Windstorm/tornado 
o Hurricane 
o Earthquake  
o Bombing 
o Animal interference 
o Solar flares, 
meteorites  
• Critical infrastructure failure 
o Telecommunications  
o Electrical power 
o Transportation 
o Water/wastewater 
Natural disasters and failures of critical infrastructures 
on which the organization depends but that are outside 
of the control of the organization.  
 
Natural and human-caused disasters can also be 
characterized in terms of their severity and/or duration. 
However, because the threat source and the threat 
event are strongly identified, severity and duration can 
be included in the description of the threat event (e.g., 
Category 5 hurricane causes extensive damage to the 
facilities that house mission-critical systems, making 
those systems unavailable for three weeks).  
 
Range of effects

<!-- page 185 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
167 
C.2. Vulnerabilities and Predisposing Conditions 5888 
Vulnerabilities are weaknesses in information systems, system procedures, controls, or 5889 
implementations that can be exploited by a threat source. Predisposing conditions are 5890 
properties of the organization, mission, or business process, architecture, or information 5891 
systems that contribute to the likelihood of a threat event. The order of these vulnerabilities 5892 
and predisposing conditions does not reflect priority in terms of likelihood of occurrence or 5893 
severity of impact. Additionally, the vulnerabilities and predisposing conditions identified in this 5894 
appendix should not be considered a complete list, nor should they be assumed to occur in 5895 
every OT environment.  5896 
Vulnerabilities and predisposing conditions are grouped according to where they exist (e.g., in 5897 
the organization’s policy and procedures) or the inadequacy of security mechanisms 5898 
implemented in hardware, firmware, and software. The former is referred to as being “in the 5899 
organization” and the latter as being “in the system.” Understanding the source of 5900 
vulnerabilities and predisposing conditions can help identify optimal mitigation strategies. 5901 
Deeper analysis may uncover that causes and observations are not one-to-one. That is, some 5902 
underlying causes may exhibit multiple symptoms, and some symptoms may come from more 5903 
than one cause.  5904 
Any given OT will usually exhibit a subset of the identified vulnerabilities in this appendix, but 5905 
may also contain additional vulnerabilities and predisposing conditions that are unique to a 5906 
particular technology or implementation. Specific current information on OT vulnerabilities can 5907 
be found on the CISA website, though many vendors publish notifications and patches that are 5908 
not always found on the CISA website. It is beneficial to maintain relationships with vendors in 5909 
order to stay up to date with known vulnerabilities.  5910 
Some vulnerabilities and predisposing conditions can be mitigated. Others can only be accepted 5911 
and controlled by appropriate countermeasures but will result in some residual risk to the OT 5912 
environment. For example, some existing policies and procedures may be changed with a level 5913 
of effort that the organization considers acceptable, while others may be addressed more 5914 
expeditiously by instituting additional policies and procedures.  5915 
Vulnerabilities in the products and services acquired from outside of the organization are rarely 5916 
under the direct control of the organization. Changes may be influenced by market forces, but 5917 
this is a slow and indirect approach. Instead, the organization may change predisposing 5918 
conditions to reduce the likelihood that a systemic vulnerability will be exploited.  5919 
C.2.1. Policy and Procedure Vulnerabilities and Predisposing Conditions 5920 
Vulnerabilities and predisposing conditions are often introduced into the OT environment due 5921 
to incomplete, inappropriate, or nonexistent security policies, including documentation, 5922 
implementation guides (e.g., procedures), and enforcement. Management support of security 5923 
policy and procedures is the cornerstone of any security program. An organization’s security 5924 
policy can reduce vulnerabilities by mandating and enforcing proper conduct. Written policies 5925 
and procedures are mechanisms for informing staff and stakeholders of decisions regarding 5926

<!-- page 186 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
168 
behaviors that benefit the organization. From this perspective, policy is an educational and 5927 
instructive way to reduce vulnerabilities. Enforcement is a partner to policy and encourages 5928 
people to do the proper thing. Various forms of corrective action are the usual consequences to 5929 
personnel not following policy and procedures. Policies should be explicit about the 5930 
consequences to individuals or organizations that do not conform.  5931 
There is usually a complex policy and procedure environment that includes laws, regulations, 5932 
overlapping jurisdictions and spheres of influence, economics, customs, and history. Larger 5933 
enterprises are often subdivided into organizational units that work together to reduce 5934 
vulnerabilities. The scope and hierarchical relationship among policies and procedures need to 5935 
be managed for maximum effectiveness.  5936 
Table 11 presents examples of observed policy and procedure vulnerabilities and predisposing 5937 
conditions for OT.  5938 
Table 11. Policy and procedure vulnerabilities and predisposing conditions 5939 
Vulnerability Description 
Inadequate organizational 
ownership of risk assessments 
Risk assessments should be performed with acknowledgement from 
appropriate levels within the organization. The lack of understanding of risk 
could lead to under-mitigated scenarios or inadequate funding and 
selection of controls. 
Inadequate security policy for OT Vulnerabilities are often introduced into the OT environment due to 
inadequate policies or the lack of policies specifically for OT system security. 
Controls and countermeasures should be derived from a risk assessment or 
policy to ensure uniformity and accountability. 
Inadequate OT security training and 
awareness program 
A documented formal OT security training and awareness program is 
designed to keep staff up to date on organizational security policies and 
procedures, threats, industry cybersecurity standards, and recommended 
practices. Without adequate ongoing training on specific OT policies and 
procedures, staff cannot be expected to maintain a secure OT environment.  
Lack of inventory management 
policy 
Inventory policy and procedures should include installation, removal, and 
changes made to hardware, firmware, and software. An incomplete 
inventory could lead to unmanaged and unprotected devices within the OT 
environment. 
Lack of configuration management 
policy 
Lack of policy and procedures for OT configuration management can lead to 
an unmanageable and highly vulnerable inventory of hardware, firmware, 
and software. 
Inadequate OT equipment 
implementation guidelines 
Equipment implementation guidelines should be kept up to date and readily 
available. These guidelines are an integral part of security procedures in the 
event of an OT malfunction. 
Lack of administrative mechanisms 
for security policy enforcement 
Without accountability for enforcing policy, there is limited ability to ensure 
that security policies are followed adequately. Administrative mechanisms 
should be in place to ensure accountability. 
Inadequate review of the 
effectiveness of the OT security 
controls 
Procedures and schedules should exist to determine the extent to which the 
security program and its constituent controls are implemented correctly, 
operating as intended, and producing the desired outcome with respect to 
meeting the security requirements of the OT. The examination is sometimes 
called an “audit,” “evaluation,” or “assessment.” Policy should address the 
stage of the life cycle, purpose, technical expertise, methodology, and level 
of independence.

<!-- page 187 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
169 
Vulnerability Description 
No OT-specific contingency plan  A contingency plan (e.g., business continuity plan, disaster recovery plan) 
should be prepared, tested, and available in the event of a major hardware 
or software failure or destruction of facilities. The lack of a specific plan for 
the OT could lead to extended downtimes and production losses. 
Lack of adequate access control 
policy  
Access control enforcement depends on policy that correctly models roles, 
responsibilities, and authorizations. The policy model must enable the way 
the organization functions. 
Lack of adequate authentication 
policy 
Authentication policies are needed to define when authentication 
mechanisms (e.g., passwords, smart cards) must be used, how strong they 
must be, and how they must be maintained. Without this policy, systems 
may not have appropriate authentication controls, making unauthorized 
access to systems more likely. Authentication policies should be developed 
as part of an overall OT security program, taking into account the 
capabilities of the OT and its personnel to handle more complex passwords 
and other mechanisms. 
Inadequate incident detection and 
response plan and procedures 
Incident detection and response plans, procedures, and methods are 
necessary for rapidly detecting incidents, minimizing loss and destruction, 
preserving evidence for later forensic examination, mitigating the 
weaknesses that were exploited, and restoring services. Establishing a 
successful incident response capability includes continually monitoring for 
anomalies, prioritizing the handling of incidents, and implementing effective 
methods for collecting, analyzing, and reporting data. 
Lack of redundancy for critical 
components 
Lack of redundancy in critical components could provide single-point-of-
failure possibilities. 
Lack of policies and procedures for 
AI-enhanced social engineering 
Generative AI enables adversaries to craft highly targeted and convincing 
phishing emails, voice calls, and video communications that are 
indistinguishable from legitimate correspondence. Unlike traditional social 
engineering awareness training, addressing this threat requires 
organizations to establish and enforce procedural verification mechanisms 
for sensitive requests that do not rely solely on perceived legitimacy.  
Lack of supply chain security policy OT hardware, software, and firmware sourced from vendors, integrators, 
and third-party suppliers may contain compromised, counterfeit, or 
vulnerable components. Without policies governing vendor vetting, 
component integrity verification, and oversight of third-party access, 
organizations may unknowingly introduce malicious code or exploitable 
vulnerabilities into critical systems. Vendors and integrators often require 
privileged access to OT systems for installation and maintenance, making 
unvetted third-party involvement a significant supply chain risk. 
C.2.2. System Vulnerabilities and Predisposing Conditions 5940 
Security controls must clearly identify the systems to which they apply. Systems range widely in 5941 
size, scope, and capability. At the small end of the spectrum, a system may be an individual 5942 
hardware or software product or service. At the other end of the spectrum are large and 5943 
complex systems, systems-of-systems, and networks, all of which incorporate hardware 5944 
architectures and software frameworks (including application frameworks) to support 5945 
operations. An organization may choose to identify security zones such that security controls 5946 
may be applied to all systems within the security zone.  5947

<!-- page 188 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
170 
System vulnerabilities can occur in the hardware, firmware, and software used to build the OT. 5948 
Sources of vulnerabilities include design flaws, development flaws, misconfigurations, poor 5949 
maintenance, poor administration, and connections with other systems and networks. Many of 5950 
the controls in the SP 800-53 and the OT overlay in Appendix E specify what the system must do 5951 
to mitigate these vulnerabilities.  5952 
Vulnerabilities can also exist in the auxiliary components that support the OT systems. The 5953 
potential vulnerabilities and predisposing conditions commonly found within OT systems are 5954 
categorized into the following tables:  5955 
• Table 12. Architecture and design vulnerabilities and predisposing conditions  5956 
• Table 13. Configuration and maintenance vulnerabilities and predisposing conditions  5957 
• Table 14. Physical vulnerabilities and predisposing conditions  5958 
• Table 15. Software development vulnerabilities and predisposing conditions  5959 
• Table 16. Communication and network configuration vulnerabilities and predisposing 5960 
conditions  5961 
• Table 17. Sensor, final element, and asset management vulnerabilities and predisposing 5962 
conditions  5963 
Table 12. Architecture and design vulnerabilities and predisposing conditions 5964 
Vulnerability Description 
Inadequate incorporation of security 
into architecture and design 
Incorporating security into the OT architecture and design must start with a 
budget and schedule designated for OT. The architectures must address the 
identification and authorization of users, access control mechanism, 
network topologies, and system configuration and integrity mechanisms.  
Inadequate management of change 
that allows insecure architecture to 
evolve 
The network infrastructure within the OT environment has often been 
developed and modified based on business and operational requirements 
with little consideration for the potential security impacts of the changes. 
Over time, security gaps may have been inadvertently introduced within the 
infrastructure. Without remediation, these gaps may represent backdoors 
into the OT. 
 
Sensors and controllers that were historically simple devices are now often 
manufactured as intelligent devices. In some cases, sensors and controllers 
may be replaced with IIoT devices that allow direct internet connections. 
Security should be incorporated into change management for all OT 
devices, not just traditional IT components. 
No security perimeter defined If the OT does not have a security perimeter clearly defined, it is not 
possible to ensure that the necessary security controls are deployed and 
configured properly. This can lead to unauthorized access to systems and 
data as well as other problems. 
Control networks used for non-
control traffic 
Control and non-control traffic have different requirements, such as 
determinism and reliability. Having both types of traffic on a single network 
creates challenges for meeting the requirements of control traffic. For 
example, non-control traffic could inadvertently consume resources that 
control traffic needs, causing disruptions in OT functions.

<!-- page 189 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
171 
Vulnerability Description 
Control network services dependent 
on a non-control network 
When IT services (e.g., DNS, DHCP) are used by control networks, they are 
often implemented in the IT network. This causes the OT network to 
become dependent on the IT network, which may not have the reliability 
and availability requirements needed by OT. 
Inadequate collection of event data 
history 
Forensic analysis depends on the collection and retention of sufficient data. 
Without proper and accurate data collection, it may be impossible to 
determine what caused a security incident to occur. Incidents might go 
unnoticed, leading to additional damage and/or disruption. Regular security 
monitoring is also needed to identify problems with security controls, such 
as misconfigurations and failures. Event data for an OT environment could 
include physical process data, system use data, and network data. 
Inadequate security architecture 
considerations for IoT and IIoT 
device integration 
IoT and IIoT devices often have limited built-in security capabilities and may 
introduce new network pathways and communication channels that have 
not been accounted for. Without adequate network segmentation and 
access controls, the integration of these devices can significantly expand the 
OT attack surface and provide adversaries with additional entry points into 
the environment. 
Inadequate security architecture 
considerations for cloud-connected 
OT environments 
When cloud integration is not adequately accounted for in the OT security 
architecture, it introduces dependencies on external infrastructure outside 
of the organization’s direct control and may create network pathways that 
bypass existing perimeter controls. 
Lack of post-quantum cryptography 
consideration in OT architecture 
Advances in quantum computing are expected to render widely used 
asymmetric encryption algorithms obsolete, posing a long -term risk to OT 
systems that cannot be updated or replaced. Organizations should consider 
cryptographic agility as a requirement when procuring new OT systems to 
ensure that cryptographic standards can be updated without requiring full 
hardware replacement. 
Inadequate security considerations 
for AI systems integrated into OT 
environments 
AI systems are susceptible to manipulation through prompt injection and 
compromised training data, which can cause models to produce incorrect 
outputs, develop blind spots that allow unsafe conditions or malicious 
activity to go undetected, or reveal sensitive information to unauthorized 
users. The data pipelines and external connectivity required to support AI 
systems can also introduce new network pathways into the OT environment 
that may not be properly secured. 
Inadequate consideration of AI 
behavior in deterministic OT 
environments 
OT control systems are designed around deterministic logic, meaning that a 
given input reliably produces the same expected output. AI systems operate 
probabilistically, meaning that outputs are based on statistical inference 
and may vary under different conditions. Deploying AI in safety-critical OT 
environments without accounting for this fundamental difference 
introduces the risk of unpredictable outputs that could result in incorre ct 
process recommendations, missed anomalies, or unsafe operational 
decisions.

<!-- page 190 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
172 
Table 13. Configuration and maintenance vulnerabilities and predisposing conditions  5965 
Vulnerability Description 
Hardware, firmware, and software 
that are not under asset 
management 
The organization does not know what it has (e.g., make, model), where they 
are, or what version it is, resulting in an inconsistent and ineffective defense 
posture. To properly secure an OT, there should be an accurate inventory of 
the assets in the environment. Procedures should be in place to manage 
additions, deletions, and modifications of assets, which include asset 
inventory management. These procedures are critical to executing business 
continuity and disaster recovery plans.  
Hardware, firmware, and software 
are not under configuration 
management 
The organization does not know the patch management status, security 
settings, or configuration versions that it has, resulting in an inconsistent 
and ineffective defense posture. A lack of configuration change 
management procedures can lead to security oversights, exposures, and 
risks. A process for controlling modifications to hardware, firmware, 
software, and documentation should be implemented to ensure that an OT 
is protected against inadequate or improper modifications before, during, 
and after system implementation. To properly secure an OT, there should 
be an accurate listing or repository of the current configurations. 
OS and vendor software patches 
may not be developed until long 
after security vulnerabilities are 
found 
Because of the tight coupling between OT software and the underlying OT, 
changes must undergo expensive and time-consuming comprehensive 
regression testing. The elapsed time for such testing and the subsequent 
distribution of updated software provides a long window of vulnerability. 
Vulnerability management procedures should include flexibility for interim 
alternative mitigations. 
Vendor declines to develop patches 
for vulnerability 
Out-of-date OSs and applications may contain newly discovered 
vulnerabilities that could be exploited. Security patch support may not be 
available for legacy OT, so vulnerability management procedures should 
include contingency plans for mitigating vulnerabilities where patches may 
never be available or replacement plans. 
Lack of a vulnerability management 
program  
Vulnerability management procedures should be in place to determine a 
plan of action or inaction upon the discovery of a vulnerability. Some OT -
specific considerations regarding patching include general availability (e.g., 
patching delayed to the next planned operational downtime), security 
patch support being unavailable for OT systems that use outdated OSs, 
isolated systems that may not require immediate patching, and prioritizing 
patching for OT that is exposed to the internet. 
Inadequate testing of security 
changes 
Modifications to hardware, firmware, and software deployed without 
testing could compromise normal operation of the OT. Documented 
procedures should be developed for testing all changes for security impacts. 
The live operational systems should never be used for testing. The testing of 
system modifications may need to be coordinated with system vendors a nd 
integrators. 
Poor remote access controls There are many reasons why an OT may need to be remotely accessed, 
including vendors and system integrators performing system maintenance 
functions or OT engineers accessing geographically remote system 
components. The concept of least privilege should be applied to remote 
access controls. Remote access capabilities must be adequately controlled 
to prevent unauthorized individuals from gaining access or authorized 
individuals from gaining excessive access to the OT.

<!-- page 191 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
173 
Vulnerability Description 
Poor configurations are used Improperly configured systems may leave unnecessary ports and protocols 
open. These unnecessary functions may contain vulnerabilities that increase 
the overall risk to the system. Using default configurations often exposes 
vulnerabilities and exploitable services. All settings should be examined.  
Critical configurations are not stored 
or backed up 
Procedures should be available for restoring OT configuration settings in 
the event of accidental or adversary-initiated configuration changes to 
maintain system availability and prevent the loss of data. Documented 
procedures should be developed for maintaining configuration settings. 
Data unprotected on portable device System security could be compromised if sensitive data (e.g., passwords, 
dial-up numbers) is stored in cleartext on lost or stolen portable devices, 
such as laptops and mobile devices. Policy, procedures, and mechanisms 
are required for protection. 
Vendor default passwords are used Most vendor default passwords are easy to discover within vendor product 
manuals, which are also available to adversaries. Using the default 
password can drastically increase OT vulnerability. 
Password generation, use, and 
protection do not comply with policy 
Password policy and procedures must be followed to be effective. 
Violations of password policy and procedures can increase OT vulnerability.  
Inadequate access controls applied Access controls must match how the organization allocates responsibilities 
and privilege to its personnel. Poorly specified access controls can result in 
an OT user having too many or too few privileges. For example: 
• System configured with default access control settings gives an 
operator administrative privileges. 
• System configured improperly results in an operator being unable to 
take corrective actions in an emergency situation. 
Improper data linking OT data storage systems may be linked to non-OT data sources. For 
example, database links allow data from one database (e.g., data historian) 
to be automatically replicated on others. Data linkage may create a 
vulnerability if it is not properly configured and may allow unauthorized 
data access or manipulation.  
Malware protection is not installed 
or up to date 
The installation of malware (i.e., malicious software) is a common attack. 
Malware protection software (e.g., antivirus software) should be kept 
current in a dynamic environment. Outdated malware protection software 
and definitions leave the system open to malware threats. 
Malware protection implemented 
without sufficient testing 
Malware protection software that is deployed without sufficient testing 
could impact the normal operation of the OT and block the system from 
performing necessary control actions.  
Denial of service (DoS)   OT software could be vulnerable to DoS attacks, resulting in the prevention 
of authorized access to a system resource or delaying system operations 
and functions. 
Intrusion detection and prevention 
software is not installed 
Incidents can result in the loss of system availability and integrity; the 
capture, modification, and deletion of data; and the incorrect execution of 
control commands. IDS/IPS software may stop or prevent various types of 
attacks, including DoS attacks, and also identify attacked internal hosts, 
such as those infected with worms. IDS/IPS software must be tested prior to 
deployment to ensure that it does not compromise normal operation of the 
OT. 
Logs are not maintained Without proper and accurate logs, it might be impossible to determine 
what caused a security event to occur and perform adequate forensics.

<!-- page 192 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
174 
Vulnerability Description 
Inadequate security configuration 
management for IoT and IIoT devices 
Unlike traditional OT devices that support centralized configuration 
management, many IoT and IIoT devices run proprietary embedded 
firmware that can only be configured through vendor-specific interfaces, 
making it difficult to consistently enforce security settings or audit device 
configurations at scale. These devices are also often deployed with vendor 
default credentials and unnecessary services enabled that cannot be 
disabled due to device limitations. 
Limited organizational control over 
cloud platforms and services in OT 
environments 
Cloud-connected OT systems introduce gaps that organizations have limited 
visibility into and control over (e.g., specific security settings and 
configurations within the cloud platform). These gaps increase the risk of 
misconfigured services, inadequate access controls, and limited visibility 
that could hinder monitoring and detection, expose operational data, or 
provide adversaries with unintended access pathways into the OT 
environment. 
Table 14. Physical vulnerabilities and predisposing conditions 5966 
Vulnerability Description 
Unauthorized personnel have 
physical access to equipment 
Physical access to OT equipment should be restricted to only the necessary 
personnel while taking safety requirements into account, such as 
emergency shutdown or restarts. Improper access to OT equipment can 
lead to any of the following: 
• Physical theft of data and hardware 
• Physical damage to or destruction of data and hardware 
• Modification of the operational process 
• Unauthorized changes to the functional environment (e.g., data 
connections, unauthorized use of removable media, adding/removing 
resources) 
• Disconnection of physical data links  
• Undetectable interception of data (e.g., keystroke, other input logging) 
Radio frequency, electromagnetic 
pulse (EMP), static discharge, 
brownouts, and voltage spikes 
Some hardware used for OT systems is vulnerable to radio frequency, 
electromagnetic pulses (EMP), static discharge, brownouts, and voltage 
spikes. The impacts can range from the temporary disruption of command 
and control to permanent damage to circuit boards. Proper shielding, 
grounding, power conditioning, and/or surge suppression is recommended. 
Lack of backup power Without backup power to critical assets, a general loss of power will shut 
down the OT and could create an unsafe situation. Loss of power could also 
lead to insecure default settings. If the program file or data is stored in 
volatile memory, the process may not be able to restart after a power 
outage without appropriate backup power. 
Loss of environmental control The loss of environmental control (e.g., temperatures, humidity) could lead 
to equipment damage, such as processors overheating. Some processors 
will shut down to protect themselves. Others may continue to operate in a 
minimal capacity and produce intermittent errors, continually reboot, or 
become permanently inoperable. 
Unsecured physical ports  Unsecured universal serial bus (USB) and PS/2 ports could allow 
unauthorized connection of thumb drives or keystroke loggers.

<!-- page 193 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
175 
Table 15. Software development vulnerabilities and predisposing conditions  5967 
Vulnerability Description 
Improper data validation OT software may not properly validate user inputs or received data to 
ensure validity. Invalid data may result in numerous vulnerabilities, 
including buffer overflows, command injections, cross-site scripting, and 
path traversals. 
Installed security capabilities are not 
enabled by default 
Security capabilities that were installed with the product are useless if they 
are not enabled or at least identified as being disabled. 
Inadequate authentication, 
privileges, and access control in 
software 
Unauthorized access to configuration and programming software could 
provide the ability to corrupt a device. 
Table 16. Communication and network configuration vulnerabilities and predisposing conditions  5968 
Vulnerability Description 
Data flow controls are not employed Data flow controls based on data characteristics are needed to restrict the 
information that is permitted between systems. These controls can prevent 
the exfiltration of information and illegal operations. 
Firewalls are nonexistent or 
improperly configured 
A lack of properly configured firewalls could permit unnecessary data to 
pass between networks, such as control and enterprise networks, thus 
allowing attacks and malware to spread between networks, making 
sensitive data susceptible to monitoring/eavesdropping, and providing 
individuals with unauthorized access to systems. 
Inadequate firewall and router logs Without proper and accurate logs, it might be impossible to determine what 
caused a security incident to occur. 
Standard, well-documented 
communication protocols are used 
in plaintext 
Adversaries that can monitor the OT network activity can use a protocol 
analyzer or other utilities to decode the data transferred by protocols, such 
as telnet, FTP, HTTP, and NFS. The use of such protocols also makes it easier 
for adversaries to perform attacks against the OT and manipulate OT 
network activity. 
Authentication of users, data, or 
devices is substandard or 
nonexistent 
Many OT protocols have no authentication at any level. Without 
authentication, there is the potential to replay, modify, or spoof data or 
devices, such as sensors and user identities. 
Use of unsecure OT protocols OT protocols often have few or no security capabilities, such as 
authentication and encryption, to protect data from unauthorized access or 
tampering. The incorrect implementation of the protocols can also lead to 
additional vulnerabilities. 
Lack of integrity checking for 
communications 
Integrity checks are not built into most OT protocols, so adversaries could 
manipulate communications undetected. To ensure integrity, the OT can 
use lower-layer protocols (e.g., IPsec) that offer data integrity protection 
when traversing untrusted physical media. 
Inadequate authentication between 
wireless clients and access points 
Strong mutual authentication between wireless clients and access points is 
needed to ensure that legitimate OT clients do not connect to a rogue 
access point deployed by an adversary and that adversary clients do not 
connect to any of the OT wireless networks. 
Inadequate data protection between 
wireless clients and access points 
Sensitive data between wireless clients and access points should be 
protected using strong encryption to ensure that adversaries cannot gain 
unauthorized access to the unencrypted data.

<!-- page 194 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
176 
Vulnerability Description 
Insecure or unnecessary 
communications between OT 
systems and cloud platforms 
Communications between OT systems and cloud platforms may lack 
adequate encryption, authentication, or integrity verification, leaving 
operational data susceptible to interception and unauthorized access. 
Unnecessary outbound connections to external domains initiated by cloud 
platform agents or services may not be accounted for in existing firewall 
rules or network monitoring configurations, creating uncontrolled pathways 
outside the OT environment. 
Overreliance on third-party 
communication infrastructure for OT 
connectivity 
Many OT environments rely on third-party carrier networks such as cellular 
and private LTE for communications between remote sites and central 
control systems. Third-party communication links are subject to outages, 
degraded performance, and compromise events outside the organization's 
control. Organizations that have not accounted for the unavailability or 
compromise of third-party communication links may find themselves unable 
to monitor or control remote sites during an incident. 
Table 17. Sensor, final element, and asset management vulnerabilities and predisposing conditions  5969 
Vulnerability Description 
Unauthorized physical access to 
sensors or final elements 
Physical access to sensors and final elements allows for direct manipulation 
of the physical process. Many devices are configured on a fieldbus such that 
physical access to the sensor network allows for manipulation of controlling 
parameters. Physical access to the whole loop should be managed to 
prevent incidents.  
Unauthorized wireless access to 
sensors or final elements 
Wireless access to sensors and final elements allows for direct manipulation 
of the physical process. Many smart devices allow for wireless configuration 
(e.g., Bluetooth, Wi-Fi, WirelessHART). Wireless access should be securely 
configured or disabled using hardware write-protect where possible to 
prevent unauthorized modification of the sensors and final elements that 
are connected to both the physical process and the OT environment.  
Inappropriate segmentation of the 
asset management system 
Most architectures are designed for PLCs, RTUs, DCS, and SCADA controllers 
to manipulate the process and for asset management systems to monitor 
the assets connected to the controllers. Many asset management systems 
also have the technical ability to modify the configuration of sensors and 
final elements, although modification may not be their primary function. 
The asset management system should be controlled appropriately based on 
its ability (or lack of ability) to manipulate the process. 
 5970 
C.3. Threat Events and Incidents 5971 
A threat event is an event or situation that could potentially cause an undesirable consequence 5972 
or impact to operations resulting from some threat source. [SP800-30r1] Appendix E identifies a 5973 
broad set of threat events that could potentially impact information systems. The properties of 5974 
OT may also present unique threat events, such as how the threat events can manipulate OT 5975 
processes to cause physical damage. 5976 
Understanding how these threat events manifest in OT environments can be informed by 5977 
MITRE ATT&CK for ICS, which is a knowledge base of adversary tactics and techniques observed 5978 
in threat events targeting ICS [ATTACK-ICS]. ATT&CK for ICS provides detailed insight into the 5979 
activities and software that threat actors have used in prior attacks against ICS environments. 5980

<!-- page 195 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
177 
The knowledge base catalogs common ICS assets found in ICS environments, including control 5981 
servers, PLCs, and remote terminal units. It maps observed adversarial techniques to those 5982 
assets based on their technical capabilities and operational functions [ATTACK-ICS]. This 5983 
mapping helps organizations identify which techniques are most likely to target a given asset 5984 
and prioritize defensive measures accordingly. 5985 
Numerous OT incidents have been reported and documented. Descriptions of these events help 5986 
demonstrate the severity of the threat sources, vulnerabilities, and impacts within the OT 5987 
domain. The four broad categories of threat sources are adversarial, accidental, structural, and 5988 
environmental (see Appendix C.1). Often, an incident can be the result of multiple threat 5989 
sources (e.g., an environmental event causes a system failure that an operator incorrectly 5990 
responds to, leading to an accidental event).  5991 
Below is a limited selection of reported incidents that fall into each of the four categories. The 5992 
incidents have been additionally categorized into malicious or non-malicious and direct or 5993 
indirect to further distinguish the possible causes of OT incidents. 5994 
• M = Malicious. The event was initiated by someone for a harmful purpose. The initiator 5995 
may or may not have been targeting the OT or known the potential consequences. 5996 
• N = Non-malicious. There does not appear to be evidence that the initiating event was 5997 
intended to cause an incident. 5998 
• D = Direct. The event was designed to discover, inhibit, impair, or otherwise impact the 5999 
OT system. 6000 
• I = Indirect. The event was not believed to be designed to discover, inhibit, impair, or 6001 
otherwise impact the OT system. The OT system shut down or caused disruption as a 6002 
result of an impact on the supporting infrastructure. 6003 
C.3.1. Adversarial Events 6004 
Adversarial events include: 6005 
• [M][D] Marconi wireless hack.7 In 1903, Italian radio pioneer Guglielmo Marconi was 6006 
preparing for his first public demonstration of long-distance secure wireless 6007 
communications from Cornwall to Professor Fleming at the Royal Institution of London. 6008 
Inventor and magician Nevil Maskelyne hacked the system and sent a comical message 6009 
in Morse code referencing “rats.” Maskelyne then published an explanation of his hack 6010 
in the trade journal The Electrician.  6011 
• [M][I] Worcester air traffic communications.8 In March 1997, a teenager in Worcester, 6012 
Massachusetts, disabled part of the public switched telephone network using a dial-up 6013 
modem connected to the system. This disabled phone service at the control tower, 6014 
airport security, the airport fire department, the weather service, and carriers that use 6015 
 
7 Additional information on the Marconi wireless hack incident can be found at https://www.osti.gov/biblio/1505628. 
8 Additional information on the Worcester air traffic communications incident can be found at 
http://www.cnn.com/TECH/computing/9803/18/juvenile.hacker/index.html

<!-- page 196 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
178 
the airport. The tower’s main radio transmitter and another transmitter that activated 6016 
runway lights were also shut down as well as a printer that controllers used to monitor 6017 
flight progress. The attack also disabled phone service to 600 homes and businesses in 6018 
the nearby town of Rutland.  6019 
• [M][D] Maroochy Shire sewage spill.9 In the spring of 2000, a former employee of an 6020 
Australian organization that developed manufacturing software applied for a job with 6021 
the local government but was rejected. Over a two-month period, the disgruntled 6022 
employee reportedly used a radio transmitter on as many as 46 occasions to remotely 6023 
break into the controls of a sewage treatment system. He altered electronic data for 6024 
specific sewerage pumping stations, causing malfunctions in their operations and 6025 
ultimately releasing about 264,000 gallons of raw sewage into nearby rivers and parks.  6026 
• [M][I] Night Dragon.10 McAfee reported a series of attacks that were designed to steal 6027 
sensitive data from global oil, energy, and petrochemical industries. Adversaries 6028 
exfiltrated proprietary operations data and project financing information with regard to 6029 
oil and gas field bids and operations.  6030 
• [M][D] Iranian centrifuge, Stuxnet.11 Stuxnet was a Microsoft Windows computer worm 6031 
discovered in July 2010 that specifically targeted industrial software and equipment. The 6032 
worm initially spread indiscriminately but included a highly specialized malware payload 6033 
that was designed to target only particular SCADA systems that were configured to 6034 
control and monitor specific industrial processes.  6035 
• [M][D] German steel mill attack.12 In 2014, hackers manipulated and disrupted control 6036 
systems to such a degree that a blast furnace could not be properly shut down, resulting 6037 
in unspecified “massive” damage.  6038 
• [M][I] Shamoon.13 In 2012, Saudi Aramco experienced a malware attack that targeted 6039 
its refineries and overwrote the attacked systems’ master boot records (MBRs), 6040 
partition tables, and other data files. This caused the systems to become unusable.  6041 
• [M][D] New York dam.14 In 2013, an Iranian computer security company obtained 6042 
remote access to a computer that controlled the SCADA system for the Bowman Dam 6043 
located in Rye, New York. The adversary was able to view water levels, temperature, 6044 
and the status of the sluice gate. The sluice gate control was disconnected for 6045 
maintenance at the time of adversarial remote access, so the dam could not be 6046 
remotely controlled.  6047 
 
9 Additional information on the Maroochy Shire sewage spill incident can be found at 
http://www.theregister.co.uk/2001/10/31/hacker_jailed_for_revenge_sewage/. 
10 Additional information on Night Dragon was published as a McAfee white paper at https://www.mcafee.com/blogs/wp-
content/uploads/2011/02/McAfee_NightDragon_wp_draft_to_customersv1-1.pdf?msockid=073127cb95da6704354e31b3940f661e. 
11 Additional information on the Stuxnet worm can be found at https://www.wired.com/2014/11/countdown-to-zero-day-stuxnet/.  
12 Additional information on the German steel mill incident can be found at http://www.wired.com/2015/01/german-steel-mill-hack-
destruction/. 
13 Additional information on the Saudi Aramco incident can be found at https://www.ibm.com/think/x-force/the-full-shamoon-how-the-
devastating-malware-was-inserted-into-networks. 
14 The U.S. Department of Justice indictment for the New York dam attacks can be found at 
https://www.justice.gov/opa/file/834996/download.

<!-- page 197 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
179 
• [M][D] Dragonfly campaign, Havex.15 The energy sector was targeted during a multi-6048 
year cyber-espionage campaign that primarily used Havex malware. Havex was a remote 6049 
access Trojan that used the Open Platform Communications (OPC) standard to gather 6050 
information about connected ICS devices on a network. The campaigns were 6051 
exploratory.  6052 
• [M][D] Ukrainian power grid, BlackEnergy3.16 On December 23, 2015, Ukrainian power 6053 
companies experienced a cyber attack that caused power outages affecting over 6054 
225,000 customers in Ukraine. Over 50 regional substations experienced malicious 6055 
remote operation of their breakers. KillDisk malware was used to erase files on targeted 6056 
systems, including at least one Windows-based HMI. The actors also corrupted the 6057 
firmware of serial-to-Ethernet devices at the substations. This was the first known cyber 6058 
attack on a power grid.  6059 
• [M][D] Ukrainian power grid, Industroyer.17 On December 17, 2016, a cyber attack 6060 
occurred at a substation outside Kyiv, Ukraine, resulting in an outage for customers of 6061 
that substation for approximately one hour. This attack was the first known malware 6062 
specifically designed to attack the power grid. 6063 
• [M][I] Maersk, NotPetya. In 2017, the NotPetya malware encrypted computers 6064 
worldwide with no known decryption method. Although the malware initially targeted 6065 
Ukrainian companies, it spread throughout the world with significant impacts to Maersk, 6066 
FedEx, Merck, and Saint-Gobain. The malware destroyed data and disrupted shipping 6067 
operations for Maersk, costing the company over $300 million in repairs and recovery 6068 
efforts. 6069 
• [M][D] Saudi Petrochem, TRITON.18 A petrochemical facility in Saudi Arabia was 6070 
attacked using malicious software that targeted the industrial SIS. The SIS initiated a 6071 
safe shutdown of the petrochemical process in 2017 when the triple-redundant 6072 
processors identified mismatched code among the processors.  6073 
• [M][I] Norsk Hydro, LockerGoga.19 In March 2019, Norsk Hydro experienced a cyber 6074 
attack that used LockerGoga ransomware to encrypt its computer files. The aluminum 6075 
and renewable energy company transitioned to manual operations and was transparent 6076 
with the public on its progress to recovery. Norsk Hydro’s transparency throughout the 6077 
discovery and recovery process is well regarded by the security industry.  6078 
• [M][I] Talman Software Ransomware Attack.20 In February 2020, a ransomware attack 6079 
encrypted the central production systems of Talman Software, the primary technology 6080 
 
15 Additional information on the Dragonfly/Energetic Bear Campaign can be found at https://www.osti.gov/servlets/purl/1505628. 
16 Additional information about the first Ukrainian power grid attack can be found at https://info.publicintelligence.net/NCCIC-
UkrainianPowerAttack.pdf. 
17 Additional information on Industroyer malware can be found at https://us-cert.cisa.gov/ncas/alerts/TA17-163A. 
18 Additional information on the TRITON attack can be found at https://www.mandiant.com/resources/triton-actor-ttp-profile-custom-attack-
tools-detections. 
19 Additional information on Norsk Hydro attack can be found at https://news.microsoft.com/transform/hackers-hit-norsk-hydro-ransomware-
company-responded-transparency/ and https://doublepulsar.com/how-lockergoga-took-down-hydro-ransomware-used-in-targeted-attacks-
aimed-at-big-business-c666551f5880. 
20 Additional information on Talman Software Ransomware attack can be found at https://theconversation.com/ransomware-attack-on-sheep-
farmers-shows-theres-no-room-for-woolly-thinking-in-cyber-security-132882

<!-- page 198 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
180 
provider for the Australasian textile sector. Because more than 75 % of the wool trade 6081 
across Australia and New Zealand relied on Talman’s proprietary platform, the blackout 6082 
created a systemic single point of failure. The Australian Wool Exchange was forced to 6083 
abruptly cancel regional auctions, freezing sales and stranding an estimated 70,000 6084 
bales of wool worth tens of millions of dollars. 6085 
• [M][I] Colonial Pipeline.21 In May 2021, over 5,500 miles of pipeline transporting more 6086 
than 100 million gallons per day of refined products to the East Coast of the U.S. shut 6087 
down operations because of a ransomware attack. Colonial Pipeline was a victim of a 6088 
ransomware cyber attack that encrypted its IT systems by exploiting a legacy VPN 6089 
profile. Colonial made the decision to shut down the physical operations on the pipeline 6090 
to contain any potential damage. Colonial Pipeline also decided to pay the ransom to 6091 
the cybercriminal group Darkside in order to have all possible tools, including the 6092 
decryption tools, available to bring the pipeline system back online. The U.S. 6093 
Government was able to recover some of the ransom payment.22 6094 
• [M][I] Ransomware targeting healthcare.23 A string of malware delivered via phishing 6095 
attacks targeted the healthcare and public health sectors to disrupt services and steal 6096 
data. In fall 2020, a CISA Alert (AA20-302A) was issued to warn healthcare and public 6097 
health sector companies of the prevalence of these attacks.  6098 
• [M][I] NEW Cooperative, BlackMatter.24 In September 2021, Iowa-based agricultural 6099 
cooperative NEW Cooperative was targeted by a ransomware attack from the Russia-6100 
linked BlackMatter group. The hackers demanded a $5.9 million payment and disrupted 6101 
IT systems used to manage food supply chains and livestock feeding schedules across 6102 
many locations. The cooperative proactively took its networks offline to contain the 6103 
malware and refused to pay the ransom. During the digital outage, growers and 6104 
operators successfully maintained food supply continuity by reverting to manual paper 6105 
hand tickets to weigh grain and track moisture. Investigators later determined the 6106 
adversaries gained access by exploiting weak, shared employee credentials. 6107 
• [M][I] Viasat KA-SAT, AcidRain.25 In February 2022, a destructive cyber attack targeted 6108 
the ground management infrastructure of Viasat’s KA-SAT satellite network to coincide 6109 
with the Russian invasion of Ukraine. Adversaries deployed a novel data-wiping malware 6110 
called “AcidRain” to overwrite the flash storage of tens of thousands of satellite 6111 
modems, blinding communications. While intended to degrade military command-and-6112 
control, the attack caused massive collateral damage to European critical infrastructure. 6113 
It knocked out remote monitoring, telemetry tracking, and automated SCADA controls 6114 
 
21 Additional information on the Colonial Pipeline incident can be found at https://www.c-span.org/video/?512247-1/senate-homeland-
security-hearing-colonial-pipeline-cyber-attack and https://www.hsgac.senate.gov/imo/media/doc/Testimony-Blount-2021-06-08.pdf. 
22 Additional information can be found at https://www.justice.gov/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-
ransomware-extortionists-darkside. 
23 Additional information on the series of malware targeting healthcare can be found at https://www.cisa.gov/news-events/cybersecurity-
advisories/aa20-302a. 
24 Additional information on the NEW Cooperative BlackMatter ransomware attack can be found at https://www.msspalert.com/news/new-
cooperative-ransomware-attack-timeline-status-updates 
25 Additional information on the Viasat KA-SAT AcidRain attack can be found at https://www.sentinelone.com/labs/acidrain-a-modem-wiper-
rains-down-on-europe/

<!-- page 199 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
181 
for 5,800 Enercon wind turbines in Germany. Additionally, the widespread network 6115 
blackout halted satellite-linked precision tracking, automated machinery, and data feeds 6116 
for thousands of regional agricultural operations dependent on the network. 6117 
• [M][D] Ukrainian power grid, Industroyer2.26 In April 2022, Sandworm deployed 6118 
Industroyer2 against a Ukrainian high-voltage electrical substation operator in a 6119 
coordinated attack. Unlike the original Industroyer, which used multiple protocol 6120 
modules, Industroyer2 was a single executable targeting the IEC 104 protocol used to 6121 
communicate with industrial equipment. The attack also deployed CaddyWiper malware 6122 
to destroy data on Windows systems and erase evidence of the intrusion. Ukrainian 6123 
CERT and ESET identified and disrupted the attack before the substation outage could 6124 
be fully executed, preventing a larger-scale power disruption. 6125 
• [M][D] Unitronics defacement campaign.27 In November 2023, an Iranian-linked threat 6126 
actor group known as CyberAv3ngers targeted internet-exposed Unitronics Vision Series 6127 
PLCs across multiple countries, primarily at water and wastewater facilities, but also 6128 
affecting other critical infrastructure sectors. The attackers exploited default credentials 6129 
to gain access and used the legitimate Unitronics VisiLogic engineering software to 6130 
download malicious projects to the devices, defacing HMI screens with politically 6131 
motivated messaging and causing operational disruptions at multiple facilities. 6132 
• [M][D] Ukrainian municipal district heating, FrostyGoop.28 In January 2024, a Russia-6133 
linked threat actor group targeted a municipal district energy company in Ukraine using 6134 
FrostyGoop, the first known ICS malware to directly interact with OT systems via the 6135 
Modbus TCP protocol. The attackers deployed malware that directly communicated 6136 
with ENCO heating system controllers using the Modbus protocol to manipulate 6137 
temperature measurements and cause system malfunctions. The attack left over 600 6138 
apartment buildings without heat during sub-zero temperatures for nearly two days 6139 
before remediation was complete. The incident highlighted the risks of internet-exposed 6140 
ICS devices communicating over Modbus and the limitations of traditional antivirus 6141 
tools in detecting ICS-specific malware. 6142 
• [M][I] Swiss Dairy Farm Robotic Milking Ransomware Attack.29 In August 2024, a 6143 
ransomware attack encrypted the on-site computer systems of a dairy operation in 6144 
Hagendorn, Switzerland. While the facility’s automated milking robots continued 6145 
functioning offline, the ransomware locked the farmer out of the localized server 6146 
tracking the herd’s vital signs and reproductive timelines. Because this critical data layer 6147 
was blinded, the farmer failed to identify a pregnant cow in labor distress. The unborn 6148 
calf died, and the mother cow suffered irreversible health deterioration and was 6149 
euthanized. 6150 
 
26 Additional information on Industroyer2 can be found at https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/ 
27 Additional information on Unitronics Defacement Campaign can be found at https://www.cisa.gov/news-events/cybersecurity-
advisories/aa23-335a 
28 Additional information on FrostyGoop can be found at https://www.sans.org/blog/whats-the-scoop-on-frostygoop-the-latest-ics-malware-
and-ics-controls-considerations 
29 Additional information on Swiss Farm Ransomware attack can be found at https://www.csoonline.com/article/3484349/ransomware-attack-
paralyzes-milking-robots-cow-dead.html

<!-- page 200 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
182 
• [M][D] Poland energy sector cyber incident.30 In December 2025, coordinated cyber 6151 
attacks targeted over 30 distributed energy resources in Poland, including wind and 6152 
solar farms, a combined heat and power plant, and a manufacturing company. Attackers 6153 
gained initial access through internet-facing edge devices that lacked multi-factor 6154 
authentication and used a combination of default-credential exploitation and wiper 6155 
malware to corrupt firmware, destroy data, and disrupt visibility and communications 6156 
between facilities and distribution system operators. The activity is attributed to a 6157 
Russian state-sponsored threat cluster and represents the first publicly described 6158 
destructive attack targeting distributed renewable energy resources at scale. 6159 
C.3.2. Structural Events 6160 
• [N][D] Bellingham, Washington, gasoline pipeline failure.31 In June 1999, 237,000 6161 
gallons of gasoline leaked from a 16-inch pipeline and ignited 1.5 hours later, causing 6162 
three deaths, eight injuries, and extensive property damage. The pipeline failure was 6163 
exacerbated by control systems that were unable to perform control and monitoring 6164 
functions. Immediately prior to and during the incident, the SCADA system exhibited 6165 
poor performance, inhibiting the pipeline controllers from recognizing and responding 6166 
to the development of an abnormal pipeline operation. A key recommendation from the 6167 
NTSB report issued in October 2002 was to use an offline development and testing 6168 
system to implement and test changes to the SCADA database.  6169 
• [M][I] CSX train signaling system.32 In August 2003, the Sobig computer virus was 6170 
blamed for shutting down train signaling systems throughout the East Coast of the U.S. 6171 
The virus infected the computer system at CSX Corp.’s Jacksonville, Florida, 6172 
headquarters and shut down signaling, dispatching, and other systems. According to 6173 
Amtrak spokesman Dan Stessel, 10 Amtrak trains were affected in the morning. Trains 6174 
between Pittsburgh, Pennsylvania, and Florence, South Carolina, were halted due to 6175 
dark signals, and one regional Amtrak train from Richmond, Virginia, to Washington and 6176 
New York was delayed by more than two hours. Long-distance trains were also delayed 6177 
between four and six hours.  6178 
• [N][D] Browns Ferry-3 PLC failure.33 In August 2006, TVA was forced to manually shut 6179 
down one of its plant’s two reactors after unresponsive PLC problems caused two water 6180 
pumps to fail and threatened the stability of the plant itself. Although there were dual 6181 
redundant PLCs, they were connected to the same Ethernet network. Later testing on 6182 
the failed devices discovered that they would crash when they encountered excessive 6183 
network traffic.  6184 
 
30 Additional information on Poland Energy Sector Cyber Incident can be found at 
https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf 
31 Additional information on the Bellingham, Washington, gasoline pipeline failure incident can be found at 
https://www.ntsb.gov/investigations/AccidentReports/Reports/PAR0202.pdf. 
32 Additional information on the CSX train signaling system incident can be found at https://www.informationweek.com/cyber-
resilience/computer-virus-brings-down-train-signals. 
33 Additional information on the Browns Ferry -3 PLC failure incident can be found at  
https://www.informationweek.com/cyber-resilience/2006-shutdown-spurs-call-for-investigation-of-nuclear-cybersecurity.

<!-- page 201 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
183 
C.3.3. Environmental Events 6185 
• [N][I] Fukushima Daiichi nuclear disaster.34 The Great East Japan Earthquake on March 6186 
11, 2011, struck off the coast of Japan and sent a massive tsunami inland toward the 6187 
nuclear plant. The tsunami compromised the plant’s seawall, flooding much of the plant, 6188 
including the location housing the emergency generators. This emergency power was 6189 
critical for operating the control rooms and providing coolant water for the reactors. 6190 
The loss of coolant caused the reactor cores to overheat to the point where the fuel’s 6191 
zirconium cladding reacted with water, releasing hydrogen gas and fueling large 6192 
explosions in three of the four reactor buildings. This resulted in large-scale radiation 6193 
leakage that has impacted plant employees, nearby citizens, and the local environment. 6194 
Post-event analysis found that the plant’s emergency response center lacked sufficient 6195 
secure communication lines to provide information to other areas of the plant on key 6196 
safety-related instrumentation. 6197 
• [N][I] Global Navigation Satellite Systems (GNSS), Gannon Storm.35 On May 10, 2024, 6198 
an extreme G5 geomagnetic storm impacted Earth’s atmosphere, creating severe 6199 
plasma disturbances in the ionosphere. The resulting space-weather anomalies severely 6200 
degraded or entirely knocked out the Real-Time Kinematic (RTK) GPS tracking networks 6201 
relied upon by modern precision agriculture. During the height of the spring corn-6202 
planting season, autonomous tractors and automated seeding machinery across the U.S. 6203 
Midwest and Canada lost positional accuracy as RTK receivers drifted several feet off 6204 
course, causing steering equipment to drive in circles. Because precision rows require 6205 
sub-inch mapping to prevent crop gaps or fertilizer overlap, thousands of farmers were 6206 
forced to completely suspend fieldwork and park their fleets. The non-cyber signal 6207 
blackout ultimately caused an estimated $500 million in cumulative field damages and 6208 
economic operational losses due to delayed planting windows. 6209 
C.3.4. Accidental Events 6210 
• [N][I] NERC Enforcement Action.36 In 2019, a U.S. energy company was fined $10 6211 
million by NERC for cybersecurity violations that took place between 2015 and 2018. 6212 
The inability to comply with U.S. standards for cybersecurity was seen as a risk to the 6213 
security and reliability of the overall power system.  6214 
• [N][D] NASA fire.37 A security patch was applied to an OT component that controlled a 6215 
large engineering oven. The patch and associated reboot caused the oven to stop 6216 
running, which led to a fire that destroyed the spacecraft hardware. The reboot also 6217 
impeded alarm activation, which allowed the fire to go undetected for 3.5 hours before 6218 
discovery. 6219 
 
34 Additional information can be found at http://www-pub.iaea.org/MTCD/meetings/PDFplus/2011/cn200/documentation/cn200_Final-
Fukushima-Mission_Report.pdf and http://pbadupws.nrc.gov/docs/ML1414/ML14140A185.pdf. 
35 Additional information on Gannon Storm can be found at https://www.agmanager.info/sites/default/files/pdf/Gannon_Corn_03-05-25.pdf 
36 For additional information about fines imposed on energy companies, see Enforcement Actions 2019 (nerc.com). 
37 For additional information on accidental OT losses from applying IT security controls in NASA, see Final Report - IG-17-011 (nasa.gov).

<!-- page 202 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
184 
• [N][D] Hatch Nuclear Power Plant.38 In 2008, the Hatch nuclear power plant in Georgia 6220 
was forced into an emergency shutdown for forty-eight hours after a software update 6221 
was installed on a single Windows computer. When the updated computer rebooted, it 6222 
reset the data on the control system, causing safety systems to errantly interpret the 6223 
lack of data as a drop in water reservoirs that cool the plant’s radioactive nuclear fuel 6224 
rods. As a result, the plant’s automated safety systems triggered a shutdown.  6225 
 6226 
  6227 
 
38 Additional information can be found at https://www.homelandsecuritynewswire.com/cyber-mishap-causes-nuclear-power-plant-shutdown

<!-- page 203 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
185 
Appendix D. OT Security Organizations, Research, and Activities 6228 
This appendix contains abstracts of some of the many activities that address OT cybersecurity. 6229 
Organization descriptions and the related information provided in this appendix have been 6230 
drawn primarily from the listed organizations’ websites and other reliable public sources but 6231 
have not been verified. Readers are encouraged to contact the organizations directly for the 6232 
most up-to-date and complete information. 6233 
D.1. Consortia and Standards 6234 
D.1.1. International Electrotechnical Commission (IEC) 6235 
IEC is a standards organization that prepares and publishes international standards for all 6236 
electrical, electronic, and related technologies. These standards serve as a basis for creating 6237 
national standards and as references for drafting international tenders and contracts. IEC’s 6238 
members include manufacturers, providers, distributors, vendors, consumers, users, and all 6239 
levels of governmental agencies, professional societies, trade associations, and standards 6240 
developers from over 60 countries. Below are relevant IEC Technical Committees (TCs) that 6241 
contribute to the field of OT security.  6242 
https://www.iec.ch  6243 
D.1.1.1. IEC Technical Committee 57 6244 
The scope of TC 57 is to prepare international standards for power systems control equipment 6245 
and systems, including energy management systems (EMSs), SCADA, distribution automation, 6246 
teleprotection, and associated information exchange for real-time and non-real-time 6247 
information used in the planning, operation, and maintenance of power systems.  6248 
https://www.iec.ch/dyn/www/f?p=103:7:3323052731869::::FSP_ORG_ID,FSP_LANG_ID:1273,26249 
5 6250 
The list of current working groups (WGs) within TC 57 includes: 6251 
• WG 3: Telecontrol protocols  6252 
• WG 10: Power system IED communication and associated data models  6253 
• WG 13: Software interfaces for operation and planning of the electric grid  6254 
• WG 14: Enterprise business function interfaces for utility operations  6255 
• WG 15: Data and communication security  6256 
• WG 16: Deregulated energy market communications  6257 
• WG 17: Power system intelligent electronic device communication and associated data 6258 
models for microgrids, distributed energy resources and distribution automation  6259 
• WG 18: Hydroelectric power plants - Communication for monitoring and control  6260

<!-- page 204 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
186 
• WG 19: Interoperability within TC 57 in the long term  6261 
• WG 20: Power Line Carrier Communication Systems  6262 
• WG 21: Interfaces and protocol profiles relevant to systems connected to the electrical 6263 
grid  6264 
D.1.1.2. IEC Technical Committee 65 6265 
The scope of TC 65 is to prepare international standards for the systems and elements used for 6266 
industrial process measurement, control, and automation to coordinate standardization 6267 
activities that affect the integration of components and functions into such systems, including 6268 
safety and security aspects. This work of standardization is to be carried out in the international 6269 
fields for equipment and systems.  6270 
https://www.iec.ch/dyn/www/f?p=103:7:3323052731869::::FSP_ORG_ID,FSP_LANG_ID:1250,26271 
5  6272 
D.1.2. Institute of Electrical and Electronics Engineers, Inc. (IEEE) 6273 
IEEE inspires the global community to innovate for a better tomorrow through its more than 6274 
400,000 members in over 160 countries and its highly cited publications, conferences, 6275 
technology standards, and professional and educational activities.  6276 
https://www.ieee.org/  6277 
Below are relevant IEEE subsocieties that contribute to the field of OT security. 6278 
D.1.2.1. IEEE Engineering in Medicine and Biology Security (EMBS) 6279 
EMBS is the world’s largest international society of biomedical engineers who design the 6280 
electrical circuits that make a pacemaker run, create the software that reads an MRI, and help 6281 
develop the wireless technologies that allow patients and doctors to communicate over long 6282 
distances.  6283 
https://www.embs.org/  6284 
D.1.2.2. IEEE Industrial Electronics Society (IES) 6285 
IES members focus on the theory and application of electronics, controls, communications, 6286 
instrumentation, and computational intelligence for industrial and manufacturing systems and 6287 
processes.  6288 
http://www.ieee-ies.org/  6289

<!-- page 205 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
187 
D.1.2.3. IEEE Power and Energy Society (PES) 6290 
IEEE PES is the world’s largest forum for sharing the latest in technological developments in the 6291 
electric power industry, for developing standards that guide the development and construction 6292 
of equipment and systems, and for educating members of the industry and the general public.  6293 
https://www.ieee-pes.org/  6294 
D.1.2.4. IEEE Technical Committee on Power System Communications and Cybersecurity 6295 
(PSCCC) 6296 
IEEE PSCCC Cybersecurity Subcommittee (SO) leads numerous working groups dedicated to 6297 
maintaining standards within the field of OT security.  6298 
https://site.ieee.org/pes-pscc/cybersecurity-subcommittee-s0/  6299 
• IEEE Std 1686, Standard for Intelligent Electronic Devices Cyber Security Capabilities  6300 
• IEEE Std 1711.1, Standard for a Cryptographic Protocol for Cyber Security of Substation 6301 
Serial Links: Substation Serial Protection Protocol (SSPP)  6302 
• IEEE Std 2030.102.1-2020, Standard for Interoperability of Internet Protocol Security 6303 
(IPsec) Utilized within Utility Control Systems  6304 
• IEEE Std 1711.2-2019, Standard for Secure SCADA Communications Protocol (SSCP)  6305 
• IEEE Std C37.240, Standard Cybersecurity Requirements for Power System Automation, 6306 
Protection and Control Systems  6307 
• IEEE Std 2808, Standard for Function Designations used in Electrical Power Systems for 6308 
Cyber Services and Cybersecurity  6309 
• IEEE Std 2658, Guide for Cybersecurity Testing in Electric Power Systems  6310 
• IEEE Std 1547.3, Guide for Cybersecurity of DERs Interface with Electric Power Systems  6311 
• IEEE Std 1815-2012, Standard for Electric Power Systems Communications-Distributed 6312 
Network Protocol (DNP3) 6313 
D.1.2.5. IEEE Robotics and Automation Society (RAS) 6314 
RAS members foster the development and facilitate the exchange of scientific and technological 6315 
knowledge in robotics and automation that benefits the profession and humanity.  6316 
https://www.ieee-ras.org/  6317 
D.1.2.6. IEEE Vehicular Technology Society (VTS) 6318 
The Vehicular Technology Society (VTS) is composed of engineers, scientists, students, and 6319 
technicians interested in advancing the theory and practice of electrical engineering as it 6320

<!-- page 206 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
188 
applies to mobile communications, land transportation, railroad/mass transit, vehicular electro-6321 
technology equipment and systems, and land, airborne, and maritime mobile services.  6322 
https://vtsociety.org  6323 
D.1.3. International Society of Automation (ISA) 6324 
The International Society of Automation (ISA) is a non-profit professional association founded in 6325 
1945 to create a better world through automation. ISA advances technical competence by 6326 
connecting the automation community to achieve operational excellence. It is the trusted 6327 
provider of standards-based foundational technical resources, driving the advancement of 6328 
individual careers and the overall profession. ISA develops widely used global standards, 6329 
certifies professionals, provides education and training, publishes books and technical articles, 6330 
hosts conferences and exhibits, and provides networking and career development programs for 6331 
its members and customers around the world.  6332 
https://www.isa.org  6333 
D.1.3.1. ISA95, Enterprise-Control System Integration 6334 
The ISA95 standards development committee defines the interface between control functions 6335 
and other enterprise functions based upon the Purdue Reference Model for Computer 6336 
Integrated Manufacturing (CIM). The ISA95 standard grew from the Purdue Enterprise 6337 
Reference Architecture (PERA), first published by ISA in 1992. Since then, it has served as a 6338 
common reference for defining the interfaces between the enterprise and control networks 6339 
across all OT sectors.  6340 
https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa95  6341 
D.1.3.2. ISA99, Industrial Automation and Control Systems Security 6342 
The ISA99 standards development committee brings together industrial cybersecurity experts 6343 
from across the globe to develop ISA standards on industrial automation and control systems 6344 
security. This original and ongoing ISA99 work is being used by the International 6345 
Electrotechnical Commission to produce the multi-standard ISA/IEC 62443 series, which are 6346 
currently organized into four categories: General, Policies and Procedures, System, and 6347 
Component.  6348 
https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa99  6349 
D.1.3.3. ISASecure 6350 
The ISASecure program is a certification scheme certifying off-the-shelf automation and control 6351 
systems to the ISA/IEC 62443 series of standards. 6352 
https://isasecure.org/  6353

<!-- page 207 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
189 
D.1.3.4. ISAGCA 6354 
ISAGCA is a collaborative forum to advance cybersecurity awareness, education, readiness, and 6355 
knowledge sharing. The objectives of ISAGCA include the acceleration and expansion of 6356 
standards, certification, education programs, advocacy efforts, and thought leadership. 6357 
https://isagca.org/  6358 
D.1.3.5. ISA-TR84.00.09, Cybersecurity Related to the Functional Safety Lifecycle 6359 
This document provides guidance on integrating the cybersecurity life cycle with the safety life 6360 
cycle, as they relate to Safety Controls, Alarms, and Interlocks (SCAI), including safety 6361 
instrumented systems (SISs). This scope includes the work processes and countermeasures 6362 
used to reduce the risk posed by cybersecurity threats to the industrial automation and control 6363 
system (IACS) network.  6364 
https://www.isa.org/products/isa-tr84-00-09-2017-cybersecurity-related-to-the-f  6365 
D.1.4. International Organization for Standardization (ISO) 6366 
The International Organization for Standardization (ISO) is an independent, non-governmental 6367 
international organization with 165-member national standards bodies. Through its members, 6368 
it brings together experts to share knowledge and develop voluntary, consensus-based, and 6369 
market-relevant international standards that support innovation and provide solutions to global 6370 
challenges. While the 27001/27002 standards are defined for IT systems and environments, 6371 
they still have many applications to OT security.  6372 
https://www.iso.org/home.html  6373 
D.1.4.1. ISO 27001 6374 
ISO/IEC 27001 specifies the requirements for establishing, implementing, maintaining, and 6375 
continually improving an information security management system within the context of the 6376 
organization. It also includes requirements for assessing and treating information security risks 6377 
tailored to the organization’s needs. The requirements set out in ISO/IEC 27001 are generic and 6378 
intended to be applicable to all organizations, regardless of type, size, or nature.  6379 
https://www.iso.org/standard/54534.html  6380 
D.1.4.2. ISO 27002:2022 6381 
ISO/IEC 27002:2022 provides guidelines for organizational information security standards and 6382 
information security management practices, including the selection, implementation, and 6383 
management of controls while taking into account the organization’s risk environment.  6384 
https://www.iso.org/standard/75652.html  6385

<!-- page 208 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
190 
D.1.5. National Council of Information Sharing and Analysis Centers (ISACs) 6386 
Formed in 2003, the NCI is composed of 25 organizations and is a coordinating body designed 6387 
to maximize information flow across private-sector critical infrastructures and with 6388 
government. ISACs help critical infrastructure owners and operators protect their facilities, 6389 
personnel, and customers from cyber and physical security threats and other hazards. ISACs 6390 
collect, analyze, and disseminate actionable threat information to their members and provide 6391 
tools to mitigate risks and enhance resiliency. ISACs reach deep into their sectors, 6392 
communicating critical information far and wide and maintaining sector-wide situational 6393 
awareness.  6394 
https://www.nationalisacs.org/member-isacs-3  6395 
D.1.6. National Institute of Standards and Technology (NIST) 6396 
NIST promotes U.S. innovation and industrial competitiveness by advancing measurement 6397 
science, standards, and technology in ways that enhance economic security and improve 6398 
quality of life. From the smart electric power grid and electronic health records to atomic 6399 
clocks, advanced nanomaterials, and computer chips, innumerable products and services rely 6400 
on NIST’s technology, measurements, and standards. NIST’s Information Technology Laboratory 6401 
(ITL) develops and maintains an extensive collection of computer security standards, guidelines, 6402 
recommendations, and research, which are released through SPs and other reporting mediums.  6403 
https://csrc.nist.gov/publications/  6404 
D.1.6.1. NIST SP 800 Series Cybersecurity Guidelines 6405 
The NIST SP 800 series on information technology reports on NIST ITL’s research, guidance, and 6406 
outreach efforts in computer security, as well as its collaborative activities with industry, 6407 
government, and academic organizations. Focus areas include cryptographic technology and 6408 
applications, advanced authentication, public-key infrastructure, internetworking security, 6409 
criteria and assurance, and security management and support.  6410 
https://csrc.nist.gov/publications/sp800  6411 
D.1.6.2. NIST SP 1800 Series Cybersecurity Practice Guides 6412 
The NIST SP 1800 series presents practical and usable solutions for applying standards-based 6413 
cybersecurity approaches and best practices in the real world. The guides are designed to help 6414 
organizations gain efficiencies in implementing cybersecurity technologies while saving them 6415 
research and proof-of-concept costs. An 1800 document can map capabilities to the 6416 
Cybersecurity Framework and outline the steps needed for another entity or organization to 6417 
recreate an example solution.  6418 
https://csrc.nist.gov/publications/sp1800  6419

<!-- page 209 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
191 
D.1.6.3. NIST Internal or Interagency Reports 6420 
NIST IR series documents are reports on research findings, including background information 6421 
for FIPS and SPs.  6422 
https://csrc.nist.gov/publications/ir  6423 
D.1.7. NERC Critical Infrastructure Protection (CIP) Standards 6424 
The mission of the North American Electric Reliability Corporation (NERC) is to improve the 6425 
reliability and security of the bulk power system in North America. To achieve that, NERC 6426 
develops and enforces reliability standards; monitors the bulk power system; assesses future 6427 
adequacy; audits owners, operators, and users for preparedness; and educates and trains 6428 
industry personnel. NERC is a self-regulatory organization that relies on the diverse and 6429 
collective expertise of industry participants. As the Electric Reliability Organization, NERC is 6430 
subject to audit by the U.S. Federal Energy Regulatory Commission and governmental 6431 
authorities in Canada.  6432 
NERC has issued a set of cybersecurity standards to reduce the risk of compromise to electrical 6433 
generation resources and high-voltage transmission systems above 100 kV, also referred to as 6434 
bulk electric systems. Bulk electric systems include balancing authorities, reliability 6435 
coordinators, interchange authorities, transmission providers, transmission owners, 6436 
transmission operators, generation owners, generation operators, and load serving entities. 6437 
The cybersecurity standards include audit measures and levels of non-compliance that can be 6438 
tied to penalties. NERC currently maintains Critical Infrastructure Protection (CIP) standards 6439 
subject to enforcement with two additional standards that are filed and pending regulatory 6440 
approval.  6441 
https://www.nerc.com/pa/Stand/Pages/ReliabilityStandards.aspx 6442 
D.1.8. Operational Technology Cybersecurity Coalition 6443 
The Operational Technology Cybersecurity Coalition’s mission is to promote open, vendor-6444 
neutral, interoperable, standards-based cybersecurity solutions for OT.  6445 
https://www.otcybercoalition.org/  6446 
D.2. Research Initiatives and Programs 6447 
D.2.1. Clean Energy Cybersecurity Accelerator Initiative 6448 
This initiative is led by the U.S. Department of Energy (DOE) and the National Renewable Energy 6449 
Laboratory (NREL) and brings together federal infrastructure and expertise, asset owners in the 6450 
energy sector, and technology innovators in a unified effort to catalyze the development of new 6451 
cybersecurity solutions for the Nation’s future clean energy grid.  6452

<!-- page 210 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
192 
The Cybersecurity Accelerator program offers a world-class facility for asset owners of all sizes 6453 
and types to work jointly to develop and deploy renewable, modern, and secure grid 6454 
technologies that are cost-competitive. These innovative technologies will also advance the 6455 
state of the practice in demonstrating “security by design,” thus ensuring that cybersecurity is 6456 
built into renewable technologies and architectures at the start of the design and development 6457 
process, not bolted on after deployment.  6458 
https://www.energy.gov/ceser/department-energy-clean-energy-accelerator-initiative  6459 
D.2.2. Cybersecurity Risk Information Sharing Program (CRISP) 6460 
The Cybersecurity Risk Information Sharing Program (CRISP) is a public-private partnership that 6461 
is co-funded by DOE and industry and managed by the Electricity Information Sharing and 6462 
Analysis Center (E-ISAC) at NERC. The purpose of CRISP is to collaborate with energy-sector 6463 
partners to facilitate the timely bidirectional sharing of unclassified and classified threat 6464 
information and to develop situational awareness tools that enhance the sector’s ability to 6465 
identify, prioritize, and coordinate the protection of critical infrastructure and key resources. 6466 
CRISP leverages DOE’s advanced sensors, threat analysis techniques, and expertise to better 6467 
inform the energy sector of high-level cyber risks. This information is shared with voluntary 6468 
utility participants who collectively deliver more than 80 % of the Nation’s electricity. The 6469 
Pacific Northwest National Laboratory (PNNL) plays a lead role at CRISP.  6470 
https://www.energy.gov/sites/default/files/2021-12/CRISP%20Fact%20Sheet_508.pdf  6471 
D.2.3. Cyber Testing for Resilient Industrial Control Systems (CyTRICS) 6472 
DOE CESER has partnered with the Idaho National Laboratory and other stakeholders to identify 6473 
high-priority OT components, perform expert testing, share information about vulnerabilities in 6474 
the digital supply chain, and inform improvements in component design and manufacturing.  6475 
https://inl.gov/cytrics/  6476 
D.2.4. Homeland Security Information Network Critical Infrastructure (HSIN-CI) 6477 
The Homeland Security Information Network (HSIN) is the trusted network for homeland 6478 
security mission operations to share Sensitive But Unclassified (SBU) information. The critical 6479 
infrastructure community on HSIN (HSIN-CI) is the primary system through which private-sector 6480 
owners and operators, DHS, and other federal, state, and local government agencies 6481 
collaborate to protect the Nation’s critical infrastructure. HSIN-CI provides real-time 6482 
collaboration tools at no charge, including a virtual meeting space, document sharing, alerts, 6483 
and instant messaging.  6484 
https://www.dhs.gov/hsin-critical-infrastructure  6485

<!-- page 211 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
193 
D.2.5. INL Cyber-Informed Engineering (CIE) and Consequence-Driven CIE (CCE) 6486 
The DOE and the Idaho National Laboratory have developed a framework to guide the 6487 
application of cybersecurity principles across the engineering design life cycle. The Cyber-6488 
Informed Engineering (CIE) framework and body of knowledge drive the inclusion of 6489 
cybersecurity as a foundational element of risk management for engineering functions that are 6490 
aided by digital technology. Consequence-Driven Cyber-Informed Engineering (CCE) is a 6491 
rigorous process for applying CIE’s core principles to a specific organization, facility, or mission 6492 
by identifying its most critical functions and methods, as well as the means by which an 6493 
adversary would likely use to manipulate or compromise them, and determining the most 6494 
effective means of removing or mitigating those risks.  6495 
CIE emphasizes “engineering out” potential risk in key areas and ensuring resiliency and 6496 
response maturity within the design of the engineered system. CCE walks an organization 6497 
through core components of CIE in CCE’s 4-phase process to evaluate and remove or mitigate 6498 
weaknesses in their critical functions.  6499 
https://inl.gov/cie/  6500 
D.2.6. NIST Cyber-Physical Systems and Internet of Things Program 6501 
The definitions of cyber-physical systems (CPS) and IoT are converging over time to include a 6502 
common emphasis on the interaction of digital, analog, physical, and human components in 6503 
systems engineered for function through integrated physics and logic. CPS and IoT enable 6504 
innovative applications in important economic sectors, such as smart cities, energy, 6505 
manufacturing, transportation, and emergency response. The CPS/IoT Program develops and 6506 
demonstrates new measurement science and promotes the emergence of consensus standards 6507 
and protocols for advanced cyber-physical systems and IoT that are scalable, effective, 6508 
measurable, interoperable, trustworthy, and assured. The Engineering Laboratory’s Smart Grid 6509 
and Cyber-Physical Systems Program Office also provides leadership to support NIST-wide 6510 
CPS/IoT program coordination with the Information Technology, Communications Technology, 6511 
and Physical Measurement Laboratories.  6512 
https://www.nist.gov/programs-projects/cyber-physical-systems-and-internet-things-program  6513 
D.2.7. NIST Cybersecurity for Smart Grid Systems Project 6514 
Smart grid cybersecurity must address both inadvertent compromises of the electric 6515 
infrastructure due to user error, equipment failures, and natural disasters as well as deliberate 6516 
attacks, such as from disgruntled employees, industrial espionage, and terrorists. NIST will 6517 
address these challenges through research conducted in the NIST Smart Grid Testbed facility 6518 
and leadership within the Smart Electric Power Alliance (SEPA) Cybersecurity Committee (SGCC) 6519 
to evaluate cybersecurity policies and measures in industry standards and develop relevant 6520 
guidance documents for the smart grid cybersecurity community. The primary goal is to 6521 
develop a cybersecurity risk management strategy for the smart grid to enable secure 6522 
interoperability of solutions across different domains and components. The Cybersecurity for 6523

<!-- page 212 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
194 
Smart Grid Systems Project is moving forward to address critical cybersecurity needs by 6524 
promoting the technology transfer of best practices, standards, voluntary guidance, and 6525 
research in the areas of applied cryptography and cybersecurity for microgrids. This project will 6526 
provide foundational cybersecurity guidance, cybersecurity reviews, and recommendations for 6527 
standards and requirements, outreach, and collaborations in the cross-cutting issue of 6528 
cybersecurity in the smart grid.  6529 
https://www.nist.gov/programs-projects/cybersecurity-smart-grid-systems  6530 
D.2.8. NIST Cybersecurity for Smart Manufacturing Systems Project 6531 
The Cybersecurity for Smart Manufacturing Systems project develops cybersecurity 6532 
implementation methods, metrics, and tools to enable manufacturers to implement 6533 
cybersecurity capabilities in smart manufacturing systems while addressing the demanding 6534 
performance, reliability, and safety requirements of these systems.  6535 
https://www.nist.gov/programs-projects/cybersecurity-smart-manufacturing-systems  6536 
D.2.9. NIST Reliable, High-Performance Wireless Systems for Factory Automation 6537 
The Reliable, High-Performance Wireless Systems for Factory Automation project develops 6538 
robust requirements, system models, recommended architectures, and guidelines for the 6539 
integration of trustworthy wireless systems within a factory workcell, where wireless is the 6540 
primary mode of communication, enabling robot mobility and ease of installation of edge 6541 
devices.  6542 
https://www.nist.gov/programs-projects/reliable-high-performance-wireless-systems-factory-6543 
automation  6544 
D.2.10. NIST Prognostics and Health Management for Reliable Operations in Smart 6545 
Manufacturing (PHM4SM) 6546 
The NIST Prognostics and Health Management for Reliable Operations in Smart Manufacturing 6547 
(PHM4SM) project develops and deploys measurement science to promote the 6548 
implementation, verification, and validation of advanced monitoring, diagnostic, and prognostic 6549 
technologies to increase reliability and decrease downtime in smart manufacturing systems.  6550 
https://www.nist.gov/programs-projects/prognostics-and-health-management-reliable-6551 
operations-smart-manufacturing-phm4sm  6552 
D.2.11. NIST Supply Chain Traceability for Agri-Food Manufacturing 6553 
The NIST Supply Chain Traceability for Agri-Food Manufacturing project develops and deploys 6554 
new standards, tools, and guidelines for traceability and cybersecurity that increase trust 6555 
among participants and customers of agri-food manufacturing supply chains.  6556 
https://www.nist.gov/programs-projects/supply-chain-traceability-agri-food-manufacturing  6557

<!-- page 213 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
195 
D.2.12. NIST AI RMF Trustworthy AI in Critical Infrastructure Profile 6558 
NIST is developing an AI Risk Management Framework Profile that is tailored to critical 6559 
infrastructure environments across IT and OT. It is intended to help operators apply the AI RMF 6560 
to AI-enabled capabilities and communicate trustworthiness requirements to developers and 6561 
stakeholders. 6562 
https://www.nist.gov/programs-projects/concept-note-ai-rmf-profile-trustworthy-ai-critical-6563 
infrastructure 6564 
D.2.13. NIST AI in Manufacturing 6565 
In December 2025, NIST awarded $20 million to the MITRE Corporation to establish two centers 6566 
advancing AI-based technology solutions for U.S. manufacturing productivity and critical 6567 
infrastructure cybersecurity, including AI-driven capabilities for detecting and responding to 6568 
cyberthreats targeting essential services. 6569 
https://www.nist.gov/news-events/news/2025/12/nist-launches-centers-ai-manufacturing-6570 
and-critical-infrastructure 6571 
D.3. Tools and Training 6572 
D.3.1. CISA Cyber Security Evaluation Tool (CSET®) 6573 
CISA’s Cyber Security Evaluation Tool (CSET®) provides a systematic, disciplined, and repeatable 6574 
approach for evaluating an organization’s security posture. CSET is a desktop software tool that 6575 
guides asset owners and operators through a step-by-step process to evaluate ICS and IT 6576 
network security practices. Users can evaluate their own cybersecurity stance using many 6577 
recognized government and industry standards and recommendations.  6578 
https://github.com/cisagov/cset/releases  6579 
D.3.2. CISA Cybersecurity Framework Guidance 6580 
Sector-specific guidance has been completed by all six critical infrastructure sectors for which 6581 
the Department of Homeland Security’s Office of Infrastructure Protection is the Sector-Specific 6582 
Agency (SSA): Chemical, Commercial Facilities, Critical Manufacturing, Dams, Emergency 6583 
Services, and Nuclear. Guidance is developed in close collaboration with the SSA alongside the 6584 
Sector Coordinating Councils (SCC) and Government Coordinating Councils (GCC) to provide a 6585 
holistic view of a sector’s cybersecurity risk environment.  6586 
https://www.cisa.gov/resources-tools/resources/commercial-facilities-sector-cybersecurity-6587 
framework-implementation 6588 
https://www.cisa.gov/resources-tools/resources/critical-manufacturing-sector-cybersecurity-6589 
framework-implementation-guidance 6590

<!-- page 214 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
196 
https://www.cisa.gov/resources-tools/resources/dams-sector-cybersecurity-framework-6591 
implementation-guidance-2020 6592 
https://www.cisa.gov/resources-tools/resources/emergency-services-sector-cybersecurity-6593 
framework-implementation-guidance 6594 
https://www.cisa.gov/resources-tools/resources/nuclear-sector-cybersecurity-framework-6595 
implementation-guidance 6596 
D.3.3. CISA ICS Alerts, Advisories, and Reports 6597 
CISA Alert is intended to provide timely notification to critical infrastructure owners and 6598 
operators concerning threats or activities with the potential to impact critical infrastructure 6599 
computing networks, including current security issues, vulnerabilities, and exploits. CISA 6600 
maintains a list of ICS-related Technical Information Papers (TIPs), Annual Reports (Year in 6601 
Review), and third-party products that it considers to be of interest to persons engaged in 6602 
protecting ICS.  6603 
https://www.cisa.gov/topics/industrial-control-systems 6604 
D.3.4. CISA ICS Training Courses 6605 
CISA offers both self-paced virtual online training courses via a virtual learning portal as well as 6606 
instructor-led classes provided at various venues. All CISA training courses are offered at no 6607 
cost to the attendee.  6608 
https://www.cisa.gov/uscert/ics/Training-Available-Through-CISA  6609 
D.3.5. CISA Known Exploited Vulnerabilities (KEV) Catalog 6610 
CISA’s KEV catalog is a continuously updated list of CVEs with confirmed evidence of active 6611 
exploitation, including ICS and SCADA-specific entries, and is regularly referenced in vendor 6612 
advisories and OT security assessments. For OT asset owners, the catalog offers a more 6613 
operationally relevant basis for prioritization based on confirmed exploitation activity, rather 6614 
than relying on vulnerability scoring alone. 6615 
https://www.cisa.gov/known-exploited-vulnerabilities-catalog 6616 
D.3.6. CISA/NCSC Secure Connectivity Principles for Operational Technology 6617 
Published in January 2026 by the UK National Cyber Security Centre (NCSC) in partnership with 6618 
CISA, the FBI, and cybersecurity agencies across Australia, Canada, Germany, and the 6619 
Netherlands, this joint guidance establishes eight principles for designing, securing, and 6620 
managing connectivity in OT environments. The principles address remote access, boundary 6621 
protection, network segmentation, and hardware-enforced controls, and provide architectural 6622 
recommendations for OT environments. 6623

<!-- page 215 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
197 
https://www.ncsc.gov.uk/sites/default/files/documents/ncsc-secure-connectivity-for-6624 
operational-technology.pdf 6625 
D.3.7. CISA Secure by Design/Secure by Default 6626 
Initially published in April 2023 and updated in October 2023 with expanded principles and 17 6627 
international partner agencies, this joint guidance from CISA, the FBI, and NSA urges technology 6628 
manufacturers to build security into products by default rather than leaving it to customers. For 6629 
OT environments, the guidance is most directly applicable in the procurement context, giving 6630 
asset owners a framework for evaluating and demanding that security be built into vendor 6631 
products. 6632 
https://www.cisa.gov/securebydesign 6633 
D.3.8. MITRE ATT&CK for ICS 6634 
MITRE ATT&CK for ICS is a curated knowledge base for cyber adversary behavior in the ICS 6635 
technology domain. It reflects the various phases of an adversary’s attack life cycle and the 6636 
assets and systems they are known to target. ATT&CK for ICS originated from MITRE internal 6637 
research focused on applying the ATT&CK methodology to the ICS technology domain.  6638 
https://attack.mitre.org/matrices/ics/ 6639 
D.3.9. MITRE D3FEND for OT 6640 
MITRE D3FEND is a knowledge graph cataloging defensive cybersecurity countermeasures and 6641 
their relationships to adversary techniques, serving as a complement to ATT&CK. In December 6642 
2025, MITRE expanded D3FEND to cover OT environments with OT-specific artifacts, 6643 
countermeasures, and mappings to ATT&CK for ICS. 6644 
https://d3fend.mitre.org/domain/ot/ 6645 
D.3.10. MITRE EMB3D 6646 
EMB3D is a MITRE threat model that catalogs cybersecurity threats targeting embedded 6647 
devices across critical infrastructure and OT environments, organizing threats by device 6648 
hardware, system software, application software, and networking properties to help vendors 6649 
and asset owners build tailored threat models. It cross-references ATT&CK for ICS, CWE, and 6650 
CVE, and is maintained as a living, publicly available framework. 6651 
https://emb3d.mitre.org/ 6652 
D.3.11. NIST Cybersecurity Framework 2.0 6653 
Recognizing that the national and economic security of the United States depends on the 6654 
reliable functioning of critical infrastructure, the President issued Executive Order 13636, 6655

<!-- page 216 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
198 
Improving Critical Infrastructure Cybersecurity, in February 2013 [EO13636]. It directed NIST to 6656 
work with stakeholders to develop a voluntary framework for reducing cyber risks to critical 6657 
infrastructure based on existing standards, guidelines, and practices. In February of 2024, NIST 6658 
published Version 2.0 of the Cybersecurity Framework.  6659 
https://www.nist.gov/cyberframework/framework  6660 
D.3.12. SANS ICS Security Courses 6661 
SANS offers several courses that provide hands-on training focused on the cybersecurity of OT 6662 
environments. These courses equip both security professionals and control system engineers 6663 
with the knowledge and skills needed to safeguard critical infrastructure.  6664 
https://www.sans.org/industrial-control-systems-security/  6665 
D.3.13. OWASP Operational Technology (OT) Top 10 6666 
The OWASP OT Top 10 is a community-developed reference document cataloging the most 6667 
significant security risks facing OT environments, including industrial control systems and 6668 
critical infrastructure. In contrast to the traditional OWASP Top 10, which is scoped to web 6669 
applications, the OT Top 10 addresses the distinct threat landscape of cyber-physical 6670 
environments, where security failures can result in physical damage, safety hazards, and 6671 
operational disruption. 6672 
https://ot.owasp.org/ 6673 
D.3.14. UFC 4-010-06, Cybersecurity of Facility-Related Control Systems (FRCS) 6674 
UFC 4-010-06 is a mandatory Core Unified Facilities Criteria document published by the 6675 
Department of Defense in October 2023 that establishes cybersecurity requirements for the 6676 
planning, design, and construction of facility-related control systems, including building control, 6677 
utility, electronic security, and fire and life safety systems. It defines a five-step process for 6678 
applying Risk Management Framework security controls to control system design, embedding 6679 
cybersecurity into the design phase rather than retrofitting it after construction. 6680 
https://www.wbdg.org/FFC/DOD/UFC/ufc_4_010_06_2023.pdf 6681 
D.4. Sector-Specific Resources 6682 
D.4.1. Chemical 6683 
• Chemical Facility Anti-Terrorism Standards (CFATS) – https://www.cisa.gov/chemical-6684 
facility-anti-terrorism-standards  6685 
• ChemLock – https://www.cisa.gov/chemlock  6686 
• American Chemistry Council (ACC) – https://www.americanchemistry.com  6687

<!-- page 217 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
199 
• American Petroleum Institute (API) – https://www.api.org  6688 
• American Gas Association (AGA) – https://www.aga.org  6689 
• American Fuel and Petrochemical Manufacturers (AFPM) – https://www.afpm.org  6690 
• Society of Chemical Manufacturers and Affiliates (SOCMA) – https://www.socma.org  6691 
D.4.2. Communications 6692 
• Federal Communications Commission (FCC) – https://www.fcc.gov  6693 
o Cybersecurity and Communications Reliability Division 6694 
o Communications Security, Reliability, and Interoperability Council (CSRIC) 6695 
D.4.3. Critical Manufacturing 6696 
• National Association of Manufacturers (NAM) – https://www.nam.org 6697 
• NAM Cyber Cover  6698 
• Association for Advancing Automation (A3) – https://www.automate.org 6699 
• Measurement, Control & Automation Association (MCAA) – https://www.themcaa.org 6700 
• International Association for Automation and Robotics in Construction (IAARC) – 6701 
https://www.iaarc.org 6702 
• ODVA – https://www.odva.org 6703 
D.4.4. Dams 6704 
• Association of State Dam Safety Officials (ASDSO) – http://www.damsafety.org  6705 
D.4.5. Energy 6706 
• U.S. Department of Energy (DOE) – https://www.energy.gov  6707 
o The Office of Cybersecurity, Energy Security, and Emergency Response (CESER) 6708 
• International Council on Large Electric Systems (CIGRE) – https://www.cigre.org 6709 
• American Public Power Association (APPA) – https://www.publicpower.org 6710 
o Cybersecurity Defense Community (CDC) 6711 
• Electric Power Research Institute (EPRI) – https://www.epri.com 6712 
o National Electric Sector Cybersecurity Resource (NESCOR) 6713

<!-- page 218 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
200 
D.4.6. Food and Agriculture 6714 
• U.S. Department of Agriculture (USDA) – https://www.usda.gov  6715 
• U.S. Food and Drug Administration (FDA) – https://www.fda.gov  6716 
• National Farmers Union (NFU) – https://www.nfu.org  6717 
o Farm Crisis Center 6718 
D.4.7. Healthcare and Public Health 6719 
• U.S. Food and Drug Administration (FDA) – https://www.fda.gov  6720 
o Digital Health Center of Excellence 6721 
• Department of Health and Human Services (HHS) – https://www.hhs.gov  6722 
o Health Sector Cybersecurity Coordination Center (HC3) 6723 
• American Hospital Association (AHA) – https://www.aha.org/  6724 
o AHA Preferred Cybersecurity Provider (APCP) Program 6725 
• National Institutes of Health (NIH) – https://www.nih.gov  6726 
o NIH Information Technology Acquisition and Assessment Center (NITAAC) 6727 
• American Medical Association (AMA) – https://www.ama-assn.org  6728 
D.4.8. Nuclear Reactors, Materials, and Waste 6729 
• U.S. Nuclear Regulatory Commission (NRC) – https://www.nrc.gov  6730 
o Office of Nuclear Security and Incident Response Cyber Security Branch (CSB) 6731 
• International Atomic Energy Agency (IAEA) – https://www.iaea.org  6732 
• Nuclear Energy Agency (NEA) – https://www.oecd-nea.org  6733 
o Digital Instrumentation and Control Working Group (DICWG) 6734 
o Nuclear Energy Institute (NEI) – https://www.nei.org  6735 
• World Institute of Nuclear Security (WINS) – https://www.wins.org  6736 
D.4.9. Transportation Systems 6737 
• U.S. Department of Transportation (DOT) – https://www.transportation.gov  6738 
o Intelligent Transportation Systems Joint Program Office 6739 
• Federal Aviation Administration (FAA) – https://www.faa.gov 6740 
o Aviation Cyber Initiative (ACI) 6741

<!-- page 219 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
201 
o Air Traffic Organization (ATO) Cybersecurity Group 6742 
• Federal Highway Administration (FHWA) – https://highways.dot.gov 6743 
o FHWA Office of Operations Research, Development, and Technology 6744 
• Federal Motor Carrier Safety Administration (FMCSA) – https://www.fmcsa.dot.gov 6745 
• Federal Railroad Administration (FRA) – https://railroads.dot.gov 6746 
o FRA Office of Research, Development, and Technology 6747 
• Federal Transit Administration (FTA) – https://www.transit.dot.gov 6748 
• Maritime Administration (MARAD) – https://www.maritime.dot.gov 6749 
o Office of Maritime Security 6750 
• Pipeline and Hazardous Materials Safety Administration (PHMSA) – 6751 
https://www.phmsa.dot.gov  6752 
• National Highway Traffic Safety Administration (NHTSA) – https://www.nhtsa.gov 6753 
• Transportation Security Administration (TSA) – https://www.tsa.gov/for-industry 6754 
o Surface Transportation Cybersecurity Resource Toolkit 6755 
o SD Pipeline-2021-01G - Enhancing Pipeline Cybersecurity. Transportation 6756 
Security Administration – 6757 
https://www.tsa.gov/sites/default/files/signed_security-directive-pipeline-2021-6758 
01g-and-transmittal-memo_508c.pdf 6759 
o SD 1580-21-01E - Enhancing Rail Cybersecurity. Transportation Security 6760 
Administration – https://www.tsa.gov/sites/default/files/signed_security-6761 
directive-1580-21-01e-and-transmittal-memo_508c.pdf 6762 
• Association of American Railroads – https://www.aar.org 6763 
• International Maritime Organization (IMO) – https://www.imo.org 6764 
o Resolution MSC.428(98) - Maritime Cyber Risk Management in Safety 6765 
Management Systems – 6766 
https://wwwcdn.imo.org/localresources/en/OurWork/Security/Documents/Reso6767 
lution%20MSC.428(98).pdf 6768 
o MSC-FAL.1/Circ.3/Rev.3 - Guidelines on Maritime Cyber Risk Management – 6769 
https://wwwcdn.imo.org/localresources/en/OurWork/Security/Documents/MSC6770 
-FAL.1-Circ.3-Rev.3.pdf 6771 
• International Association of Classification Societies (IACS) – https://iacs.org.uk 6772 
o UR E26 - Cyber Resilience of Ships – https://iacs.org.uk/resolutions/ur-e/ur-e26-6773 
new/ur-e26-new 6774 
o UR E27 - Cyber Resilience of Onboard Systems and Equipment – 6775 
https://iacs.org.uk/resolutions/unified-requirements/ur-e/ur-e27-rev1 6776

<!-- page 220 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
202 
• SAE International – https://www.sae.org 6777 
o ISO/SAE 21434:2021 - Road Vehicles - Cybersecurity Engineering – 6778 
https://www.iso.org/standard/70918.html 6779 
o SAE J1939 - Serial Control and Communications Heavy Duty Vehicle Network - 6780 
Top Level Document – https://www.sae.org/standards/j1939_202603-serial-6781 
control-communications-heavy-duty-vehicle-network-top-level-document 6782 
• Department of Defense (DoD) – https://www.war.gov/ 6783 
o MIL-STD-1553 - Digital Time Division Command/Response Multiplex Data Bus – 6784 
https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=36973 6785 
D.4.10. Water and Wastewater 6786 
• U.S. Environmental Protection Agency (EPA) – https://www.epa.gov 6787 
o Drinking Water and Wastewater Resilience 6788 
• American Water Works Association (AWWA) – https://www.awwa.org 6789 
o AWWA Cybersecurity Tool 6790 
• Association of Metropolitan Water Agencies (AMWA) – https://www.amwa.net 6791 
• National Association of Water Companies (NAWC) – https://www.nawc.org 6792 
• WaterISAC – https://www.waterisac.org/ 6793 
D.5. Conferences and Working Groups 6794 
D.5.1. Digital Bond’s SCADA Security Scientific Symposium (S4) 6795 
Since 2007, S4 has hosted an ICS security conference that was initially founded to showcase 6796 
advanced and highly technical content to the ICS audience. S4 has since grown to accommodate 6797 
other ICS security content but remains a premier venue to present technical findings within OT 6798 
security. 6799 
https://s4xevents.com/ 6800 
D.5.2. IFIP Working Group 11.10 on Critical Infrastructure Protection 6801 
The International Federation for Information Processing (IFIP) Working Group 11.10 is an active 6802 
international community of scientists, engineers, and practitioners dedicated to advancing 6803 
state-of-the-art research and practices in the emerging field of critical infrastructure protection. 6804 
http://ifip1110.org/Conferences/ 6805

<!-- page 221 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
203 
D.5.3. SecurityWeek’s ICS Cyber Security Conference 6806 
Since 2002, SecurityWeek has held an annual conference focused on cybersecurity for the 6807 
industrial control systems sector, where ICS users, vendors, system security providers, and 6808 
government representatives can meet to discuss the latest cyber incidents, analyze their 6809 
causes, and cooperate on solutions. 6810 
https://www.icscybersecurityconference.com/ 6811

<!-- page 222 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
204 
Appendix E. OT Overlay 6812 
The OT overlay is a partial tailoring of the controls and control baselines 6813 
in SP 800-53r5 and adds supplementary guidance specific to OT. The 6814 
concept of overlays is discussed in Appendix C of SP 800-53B. The OT 6815 
overlay is intended to be applicable to all OT systems in all industrial 6816 
sectors and to serve as a model for other overlays. Further tailoring can 6817 
add specificity to a particular sector (e.g., pipeline, energy). Ultimately, 6818 
an overlay may be produced for a specific system (e.g., the XYZ 6819 
company). 6820 
This OT overlay constitutes supplemental guidance and tailoring for SP 6821 
800-53r5. Duplicating Appendix F of SP 800-53 would increase the size 6822 
of this publication significantly, so it is not included here.  6823 
O
verlays provide a structured approach to help organizations tailor control baselines and 6824 
develop specialized security plans that can be applied to specific mission and business 6825 
functions, environments of operation, and/or technologies. This specialization approach is 6826 
important as the number of threat-driven controls and control enhancements in the catalog 6827 
increases and organizations develop risk management strategies to address their specific 6828 
protection needs within defined risk tolerances. 6829 
A repository of overlays may be found at https://csrc.nist.gov/Projects/risk-6830 
management/sp800-53-controls/overlay-repository. This overlay may be referenced as the SP 6831 
800-82r4 Operational Technology Overlay (“NIST SP 800-82r4 OT Overlay”). It is based on SP 6832 
800-53r5 [SP800-53r5].  6833 
NIST developed this overlay in furtherance of its statutory responsibilities under the Federal 6834 
Information Security Modernization Act (FISMA) of 2014 (Public Law 113-283) [FISMA], 6835 
Presidential Policy Directive 21 (PPD-21) [PPD-21], and Executive Order 13636 [EO13636]. NIST 6836 
is responsible for developing standards and guidelines, including minimum requirements, for 6837 
providing adequate information security for all agency operations and assets, but such 6838 
standards and guidelines shall not apply to national security systems without the express 6839 
approval of appropriate federal officials exercising policy authority over such systems.  6840 
E.1. Overlay Characteristics 6841 
OT encompasses a broad range of programmable systems and devices that interact with the 6842 
physical environment or manage devices that interact with the physical environment. These 6843 
systems and devices detect or cause a direct change through the monitoring and/or control of 6844 
devices, processes, and events. Examples include industrial control systems, building 6845 
automation systems, transportation systems, physical access control systems, physical 6846 
environment monitoring systems, and physical environment measurement systems. 6847 
ICS consists of combinations of control components (e.g., electrical, mechanical, hydraulic, 6848 
pneumatic) that act together to achieve an objective (e.g., manufacturing, transportation of 6849 
matter or energy). The part of the system primarily concerned with producing an output is 6850

<!-- page 223 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
205 
referred to as the process. The control part of the system includes the specification of the 6851 
desired output or performance. Control can be fully automated or may include a human in the 6852 
loop.  6853 
Section 2.4 provides an overview of various OT systems, such as SCADA, DCS, PLCs, BASs, PACSs, 6854 
and IIoT. 6855 
E.2. Applicability 6856 
The purpose of this overlay is to provide guidance for securing OT systems. This overlay has 6857 
been prepared for use by federal agencies. It may be used by non-governmental organizations 6858 
on a voluntary basis.  6859 
Privacy is a risk consideration for OT systems. For additional guidance, refer to the NIST Privacy 6860 
Framework [PF]. The application of privacy in OT will depend on sector and organizational risks, 6861 
so controls that are exclusively related to privacy have not been included in this OT overlay. 6862 
Each organization will need to independently determine applicability. All controls and control 6863 
enhancements that only appear in the privacy baseline have been removed from this OT 6864 
overlay according to this rationale.  6865 
E.3. Overlay Summary 6866 
Table 18 provides a summary of the controls and control enhancements from SP 800-53r5, 6867 
Appendix F [SP800-53r5] that have been allocated to the initial control baselines (i.e., Low, 6868 
Moderate, and High) along with indications of OT discussion and OT tailoring. The table uses 6869 
the following conventions:  6870 
• Bold indicates controls and control enhancements with OT discussions.  6871 
• Underline indicates that this overlay has added a control to the baseline that is 6872 
supplemental to the baselines provided in SP 800-53B.  6873 
• Strikethrough indicates that a control or control enhancement has been removed from 6874 
this baseline compared to the baselines provided in SP 800-53B.  6875 
In the following example, OT discussion was added to Control Enhancement 1 of AU-4 (bolded). 6876 
In addition, Control Enhancement 1 of AU-4 was added to the Low, Moderate (Mod), and High 6877 
baselines (underlined) compared with the 800-53B baseline, which did not include AU-4 Control 6878 
Enhancement 1.  6879 
AU-4 Audit Storage Capacity AU-4 (1) AU-4 (1) AU-4 (1) 
Some controls and control enhancements are useful to many OT environments but are not 6880 
applicable across all OT sectors or architectures. Such controls may have additional OT 6881 
discussion. These will appear in the individual control tables. Controls and control 6882 
enhancements without baselines are not included in Table 18.  6883

<!-- page 224 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
206 
Table 18. Control baselines 6884 
CNTL 
NO. CONTROL NAME 
INITIAL CONTROL BASELINES 
LOW MOD HIGH 
AC-1 Policy and Procedures  AC-1 AC-1 AC-1 
AC-2 Account Management AC-2 
AC-2 (1) (2) 
(3) (4) (5) 
(13) 
AC-2 (1) (2) (3) 
(4) (5) (11) 
(12) (13) 
AC-3 Access Enforcement AC-3 AC-3 AC-3 (11) 
AC-4 Information Flow Enforcement  AC-4 AC-4 (4) 
AC-5 Separation of Duties  AC-5 AC-5 
AC-6 Least Privilege  
AC-6 (1) (2) 
(5) (7) (9) 
(10) 
AC-6 (1) (2) (3) 
(5) (7) (9) (10) 
AC-7 Unsuccessful Logon Attempts AC-7 AC-7 AC-7 
AC-8 System Use Notification AC-8 AC-8 AC-8 
AC-10 Concurrent Session Control   AC-10 
AC-11 Device Lock  AC-11 (1) AC-11 (1) 
AC-12 Session Termination  AC-12 AC-12 
AC-14 Permitted Actions without Identification or Authentication AC-14 AC-14 AC-14 
AC-17 Remote Access AC-17 (9) 
AC-17 (1) (2) 
(3) (4) (9) 
(10) 
AC-17 (1) (2) 
(3) (4) (9) (10) 
AC-18 Wireless Access AC-18 AC-18 (1) (3) AC-18 (1) (3) (4) (5) 
AC-19 Access Control for Mobile Devices AC-19 AC-19 (5) AC-19 (5) 
AC-20 Use of External Systems AC-20 AC-20 (1) (2) AC-20 (1) (2) 
AC-21 Information Sharing  AC-21 AC-21 
AC-22 Publicly Accessible Content AC-22 AC-22 AC-22 
AT-1 Policy and Procedures AT-1 AT-1 AT-1 
AT-2 Literacy Training and Awareness AT-2 (2) AT-2 (2) (3) (4) AT-2 (2) (3) (4) 
AT-3 Role-Based Training AT-3 AT-3 AT-3 
AT-4 Training Records AT-4 AT-4 AT-4

<!-- page 225 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
207 
CNTL 
NO. CONTROL NAME 
INITIAL CONTROL BASELINES 
LOW MOD HIGH 
AU-1 Policy and Procedures AU-1 AU-1 AU-1 
AU-2 Event Logging AU-2 AU-2 AU-2 
AU-3 Content of Audit Records AU-3 AU-3 (1) AU-3 (1) 
AU-4 Audit Log Storage Capacity AU-4 (1) AU-4 (1) AU-4 (1) 
AU-5 Response to Audit Logging Process Failures AU-5 AU-5 AU-5 (1) (2) 
AU-6 Audit Record Review, Analysis, and Reporting AU-6 AU-6 (1) (3) AU-6 (1) (3) (5) (6) 
AU-7 Audit Record Reduction and Report Generation  AU-7 (1) AU-7 (1) 
AU-8 Time Stamps AU-8 AU-8 AU-8 
AU-9 Protection of Audit Information AU-9 AU-9 (4) AU-9 (2) (3) (4) 
AU-10 Non-repudiation   AU-10 
AU-11 Audit Record Retention AU-11 AU-11 AU-11 
AU-12 Audit Generation AU-12 AU-12 AU-12 (1) (3) 
CA-1 Policy and Procedures CA-1 CA-1 CA-1 
CA-2 Control Assessments CA-2 CA-2 (1) CA-2 (1) (2) 
CA-3 Information Exchange CA-3 CA-3 CA-3 (6) 
CA-5 Plan of Action and Milestones CA-5 CA-5 CA-5 
CA-6 Authorization CA-6 CA-6 CA-6 
CA-7 Continuous Monitoring CA-7 (4) CA-7 (1) (4) CA-7 (1) (4) 
CA-8 Penetration Testing   CA-8 (1) 
CA-9 Internal System Connections CA-9 CA-9 CA-9 
CM-1 Policy and Procedures CM-1 CM-1 CM-1 
CM-2 Baseline Configuration CM-2 CM-2 (2) (3) (7) CM-2 (2) (3) (7) 
CM-3 Configuration Change Control  CM-3 (2) (4) CM-3 (1) (2) (4) (6) 
CM-4 Impact Analysis CM-4 CM-4 (2) CM-4 (1) (2) 
CM-5 Access Restrictions for Change CM-5 CM-5 CM-5 (1)

<!-- page 226 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
208 
CNTL 
NO. CONTROL NAME 
INITIAL CONTROL BASELINES 
LOW MOD HIGH 
CM-6 Configuration Settings CM-6 CM-6 CM-6 (1) (2) 
CM-7 Least Functionality CM-7 CM-7 (1) (2) (5) CM-7 (1) (2) (5) 
CM-8 System Component Inventory CM-8 CM-8 (1) (3) CM-8 (1) (2) (3) (4) 
CM-9 Configuration Management Plan  CM-9 CM-9 
CM-10 Software Usage Restrictions CM-10 CM-10 CM-10 
CM-11 User-Installed Software CM-11 CM-11 CM-11 
CM-12 Information Location  CM-12 (1) CM-12 (1) 
CP-1 Policy and Procedures CP-1 CP-1 CP-1 
CP-2 Contingency Plan CP-2 CP-2 (1) (3) (8) CP-2 (1) (2) (3) (5) (8) 
CP-3 Contingency Training CP-3 CP-3 CP-3 (1) 
CP-4 Contingency Plan Testing CP-4 CP-4 (1) CP-4 (1) (2) 
CP-6 Alternate Storage Site  CP-6 (1) (3) CP-6 (1) (2) (3) 
CP-7 Alternate Processing Site  CP-7 (1) (2) (3) CP-7 (1) (2) (3) (4) 
CP-8 Telecommunications Services  CP-8 (1) (2) CP-8 (1) (2) (3) (4) 
CP-9 System Backup CP-9 CP-9 (1) (8) CP-9 (1) (2) (3) (5) (8) 
CP-10 System Recovery and Reconstitution CP-10 CP-10 (2) (6) CP-10 (2) (4) (6) 
CP-12 Safe Mode CP-12 CP-12 CP-12 
IA-1 Policy and Procedures IA-1 IA-1 IA-1 
IA-2 Identification and Authentication (Organizational Users) IA-2 (1) (2) (8) (12) IA-2 (1) (2) (8) (12) IA-2 (1) (2) (5) (8) (12) 
IA-3 Device Identification and Authentication IA-3 IA-3 IA-3 
IA-4 Identifier Management IA-4 IA-4 (4) IA-4 (4) 
IA-5 Authenticator Management IA-5 (1) IA-5 (1) (2) (6) IA-5 (1) (2) (6) 
IA-6 Authentication Feedback IA-6 IA-6 IA-6

<!-- page 227 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
209 
CNTL 
NO. CONTROL NAME 
INITIAL CONTROL BASELINES 
LOW MOD HIGH 
IA-7 Cryptographic Module Authentication IA-7 IA-7 IA-7 
IA-8 Identification and Authentication (Non-Organizational Users) IA-8 (1) (2) (4) IA-8 (1) (2) (4) IA-8 (1) (2) (4) 
IA-11 Re-authentication IA-11 IA-11 IA-11 
IA-12 Identity Proofing  IA-12 (2) (3) (5) IA-12 (1) (2) (3) (4) (5) 
IR-1 Policy and Procedures IR-1 IR-1 IR-1 
IR-2 Incident Response Training IR-2 IR-2 IR-2 (1) (2) 
IR-3 Incident Response Testing  IR-3 (2) IR-3 (2) 
IR-4 Incident Handling IR-4 IR-4 (1) IR-4 (1) (4) (11) 
IR-5 Incident Monitoring IR-5 IR-5 IR-5 (1) 
IR-6 Incident Reporting IR-6 IR-6 (1) (3) IR-6 (1) (3) 
IR-7 Incident Response Assistance IR-7 IR-7 (1) IR-7 (1) 
IR-8 Incident Response Plan IR-8 IR-8 IR-8 
MA-1 Policy and Procedures MA-1 MA-1 MA-1 
MA-2 Controlled Maintenance MA-2 MA-2 MA-2 (2) 
MA-3 Maintenance Tools  MA-3 (1) (2) (3) MA-3 (1) (2) (3) 
MA-4 Nonlocal Maintenance MA-4 MA-4 (1) MA-4 (1) (3) 
MA-5 Maintenance Personnel MA-5 MA-5 MA-5 (1) 
MA-6 Timely Maintenance  MA-6 MA-6 
MA-7 Field Maintenance MA-7 MA-7 MA-7 
MP-1 Policy and Procedures MP-1 MP-1 MP-1 
MP-2 Media Access MP-2 MP-2 MP-2 
MP-3 Media Marking  MP-3 MP-3 
MP-4 Media Storage  MP-4 MP-4 
MP-5 Media Transport  MP-5 MP-5 
MP-6 Media Sanitization MP-6 MP-6 MP-6 (1) (2) (3)

<!-- page 228 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
210 
CNTL 
NO. CONTROL NAME 
INITIAL CONTROL BASELINES 
LOW MOD HIGH 
MP-7 Media Use MP-7 MP-7 MP-7 
PE-1 Policy and Procedures PE-1 PE-1 PE-1 
PE-2 Physical Access Authorizations PE-2 PE-2 PE-2 
PE-3 Physical Access Control PE-3 PE-3 PE-3 (1) 
PE-4 Access Control for Transmission  PE-4 PE-4 
PE-5 Access Control for Output Devices  PE-5 PE-5 
PE-6 Monitoring Physical Access PE-6 PE-6 (1) (4) PE-6 (1) (4) 
PE-8 Visitor Access Records PE-8 PE-8 PE-8 (1) 
PE-9 Power Equipment and Cabling  PE-9 PE-9 
PE-10 Emergency Shutoff  PE-10 PE-10 
PE-11 Emergency Power  PE-11 PE-11 (1) 
PE-12 Emergency Lighting PE-12 PE-12 PE-12 
PE-13 Fire Protection PE-13 PE-13 (1) PE-13 (1) (2) 
PE-14 Environmental Controls PE-14 PE-14 PE-14 
PE-15 Water Damage Protection PE-15 PE-15 PE-15 (1) 
PE-16 Delivery and Removal PE-16 PE-16 PE-16 
PE-17 Alternate Work Site  PE-17 PE-17 
PE-18 Location of System Components   PE-18 
PE-22 Component Marking  PE-22 PE-22 
PL-1 Policy and Procedures PL-1 PL-1 PL-1 
PL-2 System Security and Privacy Plans PL-2 PL-2 PL-2 
PL-4 Rules of Behavior PL-4 (1) PL-4 (1) PL-4 (1) 
PL-8 Security and Privacy Architecture  PL-8 PL-8 
PL-10 Baseline Selection PL-10 PL-10 PL-10 
PL-11 Baseline Tailoring PL-11 PL-11 PL-11 
PM-1 Information Security Program Plan PM-1

<!-- page 229 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
211 
CNTL 
NO. CONTROL NAME 
INITIAL CONTROL BASELINES 
LOW MOD HIGH 
PM-2 Information Security Program Leadership Role PM-2 
PM-3 Information Security and Privacy Resources PM-3 
PM-4 Plan of Action and Milestones Process PM-4 
PM-5 System Inventory PM-5 
PM-6 Measures of Performance PM-6 
PM-7 Enterprise Architecture PM-7 
PM-8 Critical Infrastructure Plan PM-8 
PM-9 Risk Management Strategy PM-9 
PM-10 Authorization Process PM-10 
PM-11 Mission and Business Process Definition PM-11 
PM-12 Insider Threat Program PM-12 
PM-13 Security and Privacy Workforce PM-13 
PM-14 Testing, Training, and Monitoring PM-14 
PM-15 Security and Privacy Groups and Associations PM-15 
PM-16 Threat Awareness Program PM-16 
PM-17 Protecting Controlled Unclassified Information on External Systems PM-17 
PM-18 Privacy Program Plan PM-18 
PM-19 Privacy Program Leadership Role PM-19 
PM-20 Dissemination of Privacy Program Information PM-20 (1) 
PM-21 Accounting of Disclosures PM-21 
PM-22 Personally Identifiable Information Quality Management PM-22 
PM-23 Data Governance Body PM-23 
PM-24 Data Integrity Board PM-24

<!-- page 230 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
212 
CNTL 
NO. CONTROL NAME 
INITIAL CONTROL BASELINES 
LOW MOD HIGH 
PM-25 
Minimization of Personally 
Identifiable Information Used in 
Testing, Training, and Research 
PM-25 
PM-26 Complaint Management PM-26 
PM-27 Privacy Reporting PM-27 
PM-28 Risk Framing PM-28 
PM-29 Risk Management Program Leadership Roles PM-29 
PM-30 Supply Chain Risk Management Strategy PM-30 (1) 
PM-31 Continuous Monitoring Strategy PM-31 
PM-32 Purposing PM-32 
PS-1 Policy and Procedures PS-1 PS-1 PS-1 
PS-2 Position Risk Designation PS-2 PS-2 PS-2 
PS-3 Personnel Screening PS-3 PS-3 PS-3 
PS-4 Personnel Termination PS-4 PS-4 PS-4 (2) 
PS-5 Personnel Transfer PS-5 PS-5 PS-5 
PS-6 Access Agreements PS-6 PS-6 PS-6 
PS-7 External Personnel Security PS-7 PS-7 PS-7 
PS-8 Personnel Sanctions PS-8 PS-8 PS-8 
PS-9 Position Descriptions PS-9 PS-9 PS-9 
RA-1 Policy and Procedures RA-1 RA-1 RA-1 
RA-2 Security Categorization RA-2 RA-2 RA-2 
RA-3 Risk Assessment RA-3 (1) RA-3 (1) RA-3 (1) 
RA-5 Vulnerability Monitoring and Scanning RA-5 (2) (11) RA-5 (2) (5) (11) RA-5 (2) (4) (5) (11) 
RA-7 Risk Response RA-7 RA-7 RA-7 
RA-9 Criticality Analysis  RA-9 RA-9 
SA-1 Policy and Procedures SA-1 SA-1 SA-1 
SA-2 Allocation of Resources SA-2 SA-2 SA-2

<!-- page 231 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
213 
CNTL 
NO. CONTROL NAME 
INITIAL CONTROL BASELINES 
LOW MOD HIGH 
SA-3 System Development Life Cycle SA-3 SA-3 SA-3 
SA-4 Acquisition Process SA-4 (10) (12) SA-4 (1) (2) (9) (10) (12) SA-4 (1) (2) (5) (9) (10) (12) 
SA-5 System Documentation SA-5 SA-5 SA-5 
SA-8 Security and Privacy Engineering Principles SA-8 SA-8 SA-8 
SA-9 External System Services SA-9 SA-9 (2) SA-9 (2) 
SA-10 Developer Configuration Management  SA-10 SA-10 
SA-11 Developer Testing and Evaluation  SA-11 SA-11 
SA-15 Development Process, Standards, and Tools  SA-15 (3) SA-15 (3) 
SA-16 Developer-Provided Training   SA-16 
SA-17 Developer Security Architecture and Design   SA-17 
SA-21 Developer Screening   SA-21 
SA-22 Unsupported System Components SA-22 SA-22 SA-22 
SC-1 Policy and Procedures SC-1 SC-1 SC-1 
SC-2 Separation of System and User Functionality  SC-2 SC-2 
SC-3 Security Function Isolation   SC-3 
SC-4 Information in System Shared Resources  SC-4 SC-4 
SC-5 Denial-of-Service Protection SC-5 SC-5 SC-5 
SC-7 Boundary Protection SC-7 (28) (29) SC-7 (3) (4) (5) (7) (8) (18) (28) (29) SC-7 (3) (4) (5) (7) (8) (18) (21) (28) (29) 
SC-8 Transmission Confidentiality and Integrity  SC-8 (1) SC-8 (1) 
SC-10 Network Disconnect  SC-10 SC-10 
SC-12 Cryptographic Key Establishment and Management SC-12 SC-12 SC-12 (1) 
SC-13 Cryptographic Protection SC-13 SC-13 SC-13

<!-- page 232 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
214 
CNTL 
NO. CONTROL NAME 
INITIAL CONTROL BASELINES 
LOW MOD HIGH 
SC-15 Collaborative Computing Devices and Applications SC-15 SC-15 SC-15 
SC-17 Public Key Infrastructure Certificates  SC-17 SC-17 
SC-18 Mobile Code  SC-18 SC-18 
SC-20 
Secure Name /Address Resolution 
Service 
(Authoritative Source) 
SC-20 SC-20 SC-20 
SC-21 
Secure Name /Address Resolution 
Service 
(Recursive or Caching Resolver) 
SC-21 SC-21 SC-21 
SC-22 Architecture and Provisioning for Name/Address Resolution Service SC-22 SC-22 SC-22 
SC-23 Session Authenticity  SC-23 SC-23 
SC-24 Fail in Known State  SC-24 SC-24 
SC-28 Protection of Information at Rest  SC-28 (1) SC-28 (1) 
SC-39 Process Isolation SC-39 SC-39 SC-39 
SC-41 Port and I/O Device Access SC-41 SC-41 SC-41 
SC-45 System Time Synchronization SC-45 SC-45 SC-45 
SC-47 Alternate Communications Path   SC-47 
SI-1 Policy and Procedures SI-1 SI-1 SI-1 
SI-2 Flaw Remediation SI-2 SI-2 (2) SI-2 (2) 
SI-3 Malicious Code Protection SI-3 SI-3 SI-3 
SI-4 System Monitoring SI-4 SI-4 (2) (4) (5) SI-4 (2) (4) (5) (10) (12) (14) (20) (22) 
SI-5 Security Alerts, Advisories, and Directives SI-5 SI-5 SI-5 (1) 
SI-6 Security and Privacy Function Verification   SI-6 
SI-7 Software, Firmware, and Information Integrity  SI-7 (1) (7) SI-7 (1) (2) (5) (7) (15) 
SI-8 Spam Protection  SI-8 (2) SI-8 (2) 
SI-10 Information Input Validation  SI-10 SI-10

<!-- page 233 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
215 
CNTL 
NO. CONTROL NAME 
INITIAL CONTROL BASELINES 
LOW MOD HIGH 
SI-11 Error Handling  SI-11 SI-11 
SI-12 Information Handling and Retention SI-12 SI-12 SI-12 
SI-13 Predictable Failure Prevention   SI-13 
SI-16 Memory Protection  SI-16 SI-16 
SI-17 Fail-Safe Procedures SI-17 SI-17 SI-17 
SR-1 Policy and Procedures SR-1 SR-1 SR-1 
SR-2 Supply Chain Risk Management Plan SR-2 (1) SR-2 (1) SR-2 (1) 
SR-3 Supply Chain Controls and Processes SR-3 SR-3 SR-3 
SR-5 Acquisition Strategies, Tools, and Methods SR-5 SR-5 (1) SR-5 (1) 
SR-6 Supplier Assessments and Reviews  SR-6 SR-6 
SR-8 Notification Agreements SR-8 SR-8 SR-8 
SR-9 Tamper Resistance and Detection   SR-9 (1) 
SR-10 Inspection of Systems or Components SR-10 SR-10 SR-10 
SR-11 Component Authenticity SR-11 (1) (2) SR-11 (1) (2) SR-11 (1) (2) 
SR-12 Component Disposal SR-12 SR-12 SR-12 
E.4. Tailoring Considerations 6885 
The OT overlay in this publication leverages the SP 800-53B control baselines that account for 6886 
the unique characteristics of OT systems, such as an increased need for availability, safety, and 6887 
environmental or operating environment considerations. Additionally, OT systems vary widely 6888 
in their architecture and technology selection. The SP 800-53B control baselines were tailored 6889 
for these general considerations, including the addition of controls that are relevant for OT 6890 
environments. Organizations can use this overlay as a starting point and further tailor controls 6891 
to meet specific operational needs to address the variability of OT systems.  6892 
As organizations further tailor controls to meet their internal security requirements, limitations 6893 
(e.g., technology, operational constraints, environmental considerations) may necessitate the 6894 
selection of compensating controls. Compensating controls in the OT environment may be 6895 
required when the OT cannot support certain controls or control enhancements or when the 6896 
organization determines that it is not advisable to implement controls or control enhancements 6897 
due to potential adverse impacts to performance, safety, or reliability. Compensating controls 6898 
may supplement the baseline or act as alternatives that provide equivalent or comparable 6899

<!-- page 234 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
216 
protection. For example, if controls or control enhancements require automated mechanisms 6900 
that are not readily available, cost-effective, or technically feasible in OT environments, 6901 
compensating controls implemented through nonautomated mechanisms or procedures may 6902 
be acceptable to meet the intent of the control.  6903 
Compensating controls implemented in accordance with PL-11 from SP 800-53r5 are not 6904 
considered exceptions or waivers to the baseline controls. Rather, they are alternative 6905 
safeguards and countermeasures employed within the OT environment that accomplish the 6906 
intent of the original controls (see “Control Tailoring” in Sec. 3.3 of [SP800-37r2]).  6907 
Every use of compensating controls should involve a risk-based determination of how much 6908 
residual risk to accept and how much functionality to reduce. Additionally, when compensating 6909 
controls are employed, organizations should document the rationale documented in the 6910 
security plan for the OT and describe: 6911 
• Why the baseline control could not be implemented 6912 
• How the compensating controls provide equivalent security capabilities for OT systems  6913 
• The risk acceptance for any residual risk that results from using the compensating 6914 
controls instead of the baseline control 6915 
Controls that contain assignments (e.g., Assignment: organization-defined conditions or trigger 6916 
events) may be tailored out of the baseline. This is equivalent to assigning a value of “none.” 6917 
The assignment may take on different values for different impact baselines.  6918 
E.5. OT Communication Protocols 6919 
The unique network properties within OT may warrant specific attention when applying certain 6920 
controls. Many of the controls in SP 800-53r5 that pertain to communication, devices, and 6921 
interfaces implicitly assume the applicability of network routing or communication between 6922 
network segments or zones. Some devices or subsystems used in OT may be configured or 6923 
architected in a way that creates an exception to this assumption. As a result, controls for 6924 
devices that communicate using standards and protocols that do not include network 6925 
addressing generally require tailoring. An RS-232 (serial) interface is an example of a non-6926 
network addressable or routable communication method that is commonly employed in OT 6927 
equipment.  6928 
E.6. Definitions 6929 
Terms used in this overlay are listed in the CSRC glossary.  6930 
E.7. Detailed Overlay Control Specifications 6931 
This overlay is based on [SP800-53r5], which provides a catalog of security and privacy controls, 6932 
and [SP800-53B]. The controls are customizable and implemented as part of an organization-6933 
wide process that manages security and privacy risks. The controls address a diverse set of 6934

<!-- page 235 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
217 
security and privacy requirements across the Federal Government and critical infrastructure 6935 
and are derived from legislation, Executive Orders, policies, directives, regulations, standards, 6936 
and mission and business needs. The documents also describe how to develop specialized sets 6937 
of controls or overlays that are tailored for specific types of mission and business functions, 6938 
technologies, or environments of operation. Finally, the catalog controls address security from 6939 
both a functionality perspective (i.e., the strength of security and privacy functions and 6940 
mechanisms provided) and an assurance perspective (i.e., the measures of confidence in the 6941 
implemented capability). Addressing both functionality and assurance helps to ensure that 6942 
component products and the systems built from those products use sound system and security 6943 
engineering principles and are sufficiently trustworthy.  6944 
In preparation for selecting and specifying the appropriate controls for organizational systems 6945 
and their respective environments of operation, organizations should first determine the 6946 
criticality and sensitivity of the information to be processed, stored, or transmitted by those 6947 
systems. This process is known as security categorization. FIPS 199 [FIPS199] enables federal 6948 
agencies to establish security categories for both information and information systems. Other 6949 
documents, such as those produced by ISA and CNSS, also provide guidance for defining low, 6950 
moderate, and high levels of security based on impact. The security categories are based on the 6951 
potential impacts on an organization or people (i.e., employees and/or the public) should 6952 
certain events occur that jeopardize the information and systems needed by the organization to 6953 
accomplish its assigned mission, such as protecting its assets, fulfilling its legal responsibilities, 6954 
maintaining its day-to-day functions, and protecting individuals’ safety, health, and life. Security 6955 
categories are to be used in conjunction with vulnerability and threat information to assess the 6956 
risk to an organization.  6957 
This overlay provides OT Discussions for the controls and control enhancements prescribed for 6958 
a system or an organization designed to protect the confidentiality, integrity, and availability of 6959 
its data and to meet a set of defined security requirements. Discussions for all controls and 6960 
control enhancements in Sec. 3 of SP 800-53r5 should be used in conjunction with the OT 6961 
Discussions in this overlay. This overlay contains a tailoring of the control baselines, and its 6962 
specification may be more stringent or less stringent than the original control baseline 6963 
specification. It is high-level, applicable to all OT environments, can be applied to multiple 6964 
systems, and may be used as the basis for more specific overlays. Use cases for specific systems 6965 
in specific environments may be separately published (e.g., as a NIST IR).  6966 
Figure 21 uses the AU-4 control as an example of the format and content of the detailed 6967 
overlay control specifications, including:  6968 
 Control number and title 6969 
 Column for control and control enhancement number 6970 
 Column for control and control enhancement name 6971 
 Columns for baselines. If the baselines have been supplemented, then SUPPLEMENTED 6972 
appears. 6973 
 A row for each control or control enhancement 6974

<!-- page 236 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
218 
 Columns for LOW, MODERATE, and HIGH baselines 6975 
 “Select” indicates that the control is selected in SP 800-53r5. “Add” indicates that the 6976 
control is added to a baseline in the OT overlay. A blank cell indicates that the control is 6977 
not selected. “R emove” indicates that the control is removed from the baseline. 6978 
 The OT Discussion. If there is none, that is stated. 6979 
 The control enhancement OT Discussion. If there is none, that is stated. 6980 
 The rationale for changing the presence of a control or control enhancement in the 6981 
baseline  6982 
 
➊AC-3 ACCESS ENFORCEMENT 
 
➋CNTL 
NO. 
➌CONTROL NAME 
Control Enhancement Name 
➍SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
AC-3 Access Enforcement Select Select Select 
AC-3 (11) ACCESS ENFORCEMENT | RESTRICT ACCESS TO SPECIFIC INFORMATION TYPES   Add 
 
➑ OT Discussion: The organization ensures that access enforcement mechanisms do 
not adversely impact the operational performance of the OT. Example compensating 
controls include encapsulation. The policy for logical access control to non-addressable 
and non-routable system resources and the associated information is made explicit. 
Access control mechanisms include hardware, firmware, and software that control the 
device or have device access, such as device drivers and communications controllers. 
Physical access control may serve as a compensating control for logical access control. 
However, it may not provide sufficient granularity when users require access to 
different functions.  
➒ Control Enhancement: (11) OT Discussion: The organization identifies and restricts 
access to information that could impact the OT environment and accounts for 
information types that are sensitive, proprietary, contain trade secrets, or support 
safety functions. 
➓ Rationale for adding AC-3 (11) to HIGH baseline: The loss of availability, integrity, and 
confidentiality of certain types of information that reside on a high-impact OT system 
may result in severe or catastrophic adverse effects on operations, assets, or 
individuals, including severe degradation or loss of mission capability, major damage to 
organizational assets, or harm to individuals involving the loss of life or life-threatening 
injuries.   
Fig. 21. Detailed overlay control specifications illustrated  6983

<!-- page 237 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
219 
E.7.1. ACCESS CONTROL – AC 6984 
E.7.1.1. Tailoring Considerations for the Access Control Family  6985 
Before implementing controls in the AC family, consider the trade-offs among security, privacy, 6986 
latency, performance, throughput, and reliability. For example, the organization considers 6987 
whether latency induced from the use of confidentiality and integrity mechanisms that employ 6988 
cryptographic mechanisms would adversely impact the operational performance of the OT.  6989 
When the OT cannot support the specific access control requirements of a control, the 6990 
organization employs compensating controls in accordance with the general tailoring guidance. 6991 
Examples of compensating controls are given with each control as appropriate.  6992 
AC-1 ACCESS CONTROL POLICY AND PROCEDURES 6993 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 6994 
and the relationship to non-OT systems. OT access by vendors and maintenance staff can occur 6995 
over a large facility footprint or geographic area and into unobserved spaces, such as 6996 
mechanical or electrical rooms, ceilings, floors, field substations, switch and valve vaults, and 6997 
pump stations. 6998 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-2 Account Management Select Select Select 
AC-2 (1) ACCOUNT MANAGEMENT | AUTOMATED SYSTEM ACCOUNT MANAGEMENT  Select Select 
AC-2 (2) ACCOUNT MANAGEMENT | AUTOMATED TEMPORARY AND EMERGENCY ACCOUNT MANAGEMENT  Select Select 
AC-2 (3) ACCOUNT MANAGEMENT | DISABLE ACCOUNTS  Select Select 
AC-2 (4) ACCOUNT MANAGEMENT | AUTOMATED AUDIT ACTIONS  Select Select 
AC-2 (5) ACCOUNT MANAGEMENT | INACTIVITY LOGOUT  Select Select 
AC-2 (11) ACCOUNT MANAGEMENT | USAGE CONDITIONS   Select 
AC-2 (12) ACCOUNT MANAGEMENT | ACCOUNT MONITORING FOR ATYPICAL USAGE   Select 
AC-2 (13) ACCOUNT MANAGEMENT | DISABLE ACCOUNTS FOR HIGH-RISK INDIVIDUALS  Select Select 
OT Discussion: In OT systems, physical security, personnel security, intrusion detection, or 6999 
auditing measures may support this control objective. 7000

<!-- page 238 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
220 
Control Enhancement: (1) (3) (4) No OT Discussion for this control. 7001 
Control Enhancement: (2) OT Discussion: When the OT (e.g., field devices) cannot support 7002 
temporary or emergency accounts, this enhancement does not apply. Example compensating 7003 
controls include employing nonautomated mechanisms or procedures. 7004 
Control Enhancement: (5) OT Discussion: This control enhancement defines situations or time 7005 
frames in which users log out of accounts in the policy. Automatic enforcement is not 7006 
addressed by this control enhancement. Organizations determine whether this control 7007 
enhancement is appropriate for the mission and/or functions of the OT system and define the 7008 
timeframe or scenarios. If no time frames or scenarios apply, the organization-defined 7009 
parameter reflects as much. 7010 
Control Enhancement: (11) (12) No OT Discussion for this control. 7011 
Control Enhancement: (13) OT Discussion: Close coordination occurs between OT, HR, IT, and 7012 
physical security personnel to ensure the timely removal of high-risk individuals. 7013 
AC-3 ACCESS ENFORCEMENT 7014 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
AC-3 Access Enforcement Select Select Select 
AC-3 (11) ACCESS ENFORCEMENT | RESTRICT ACCESS TO SPECIFIC INFORMATION TYPES   Add 
OT Discussion: The organization ensures that access enforcement mechanisms do not adversely 7015 
affect OT operational performance. Example compensating controls include encapsulation. The 7016 
policy for logical access control to non-addressable and non-routable system resources and the 7017 
associated information is made explicit. Access control mechanisms include hardware, 7018 
firmware, and software that control the device or have device access, such as device drivers 7019 
and communications controllers. Physical access control may serve as a compensating control 7020 
for logical access control. However, it may not provide sufficient granularity when users require 7021 
access to different functions. 7022 
Control Enhancement: (11) OT Discussion: The organization identifies and restricts access to 7023 
information that could impact the OT environment and accounts for information types that are 7024 
sensitive, proprietary, contain trade secrets, or support safety functions. 7025 
Rationale for adding AC-3 (11) to HIGH baseline: The loss of availability, integrity, and 7026 
confidentiality of certain types of information that reside on a high-impact OT system may 7027 
result in severe or catastrophic adverse effects on operations, assets, or individuals, including 7028 
severe degradation or loss of mission capability, major damage to organizational assets, or 7029 
harm to individuals involving the loss of life or life-threatening injuries. 7030

<!-- page 239 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
221 
AC-4 INFORMATION FLOW ENFORCEMENT 7031 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-4 Information Flow Enforcement  Select Select 
AC-4 (4) INFORMATION FLOW ENFORCEMENT | FLOW CONTROL OF ENCRYPTED INFORMATION   Select 
OT Discussion: Information flow policy may be achieved using a combination of logical and 7032 
physical flow restriction techniques. The inspection of message content may enforce 7033 
information flow policy. For example, industrial OT protocols may be restricted by using 7034 
inbound and outbound traffic rules on a network control device between OT and IT networks. 7035 
For non-routable communication (e.g., serial connections), devices may be configured to limit 7036 
commands to and from specific tags within the OT device. The information flow policy may be 7037 
supported by labeling or coloring physical connectors to aid in connecting networks. Devices 7038 
that do not have a business need to communicate should not be connected (i.e., air-gapped). 7039 
Control Enhancement: (4) No OT discussion for this control. 7040 
AC-5 SEPARATION OF DUTIES 7041 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-5 Separation of Duties  Select Select 
OT Discussion: Example compensating controls include providing increased personnel security 7042 
and auditing. The organization carefully considers the appropriateness of a single individual 7043 
performing multiple critical roles. 7044 
AC-6 LEAST PRIVILEGE 7045 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-6 Least Privilege  Select Select 
AC-6 (1) LEAST PRIVILEGE | AUTHORIZE ACCESS TO SECURITY FUNCTIONS  Select Select 
AC-6 (2) LEAST PRIVILEGE | NON-PRIVILEGED ACCESS FOR NONSECURITY FUNCTIONS  Select Select 
AC-6 (3) LEAST PRIVILEGE | NETWORK ACCESS TO PRIVILEGED COMMANDS   Select 
AC-6 (5) LEAST PRIVILEGE | PRIVILEGED ACCOUNTS  Select Select 
AC-6 (7) LEAST PRIVILEGE | REVIEW OF USER PRIVILEGES  Select Select 
AC-6 (9) LEAST PRIVILEGE | LOG USE OF PRIVILEGED FUNCTIONS  Select Select

<!-- page 240 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
222 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-6 (10) LEAST PRIVILEGE | PROHIBIT NON-PRIVILEGED USERS FROM EXECUTING PRIVILEGED FUNCTIONS  Select Select 
OT Discussion: Example compensating controls include providing increased personnel security 7046 
and auditing. The organization carefully considers the appropriateness of a single individual 7047 
having multiple critical privileges. System privilege models may be tailored to enforce integrity 7048 
and availability (e.g., lower privileges include read access, and higher privileges include write 7049 
access). 7050 
Control Enhancement: (1) (2) (3) (5) (9) OT Discussion: When OT components (e.g., PLCs) cannot 7051 
support the logging of privileged functions, other system components within the authorization 7052 
boundary may be used (e.g., engineering workstations, physical access monitoring). 7053 
Control Enhancement: (7) No OT Discussion for this control.  7054 
Control Enhancement: (10) OT Discussion: Example compensating controls include enhanced 7055 
auditing.  7056 
AC-7 UNSUCCESSFUL LOGON ATTEMPTS 7057 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-7 Unsuccessful Logon Attempts Select Select Select 
OT Discussion: Many OT systems remain in continuous operation, and operators remain logged 7058 
onto the system at all times. A “log-over” capability may be employed. Example compensating 7059 
controls include logging or recording all unsuccessful logon attempts and alerting OT security 7060 
personnel through alarms or other means when the number of organization-defined 7061 
consecutive invalid access attempts is exceeded. Unsuccessful logon attempt limits are 7062 
enforced for accounts (e.g., administrator) or systems (e.g., engineering workstations) that are 7063 
not required for continuous operation. 7064 
AC-8 SYSTEM USE NOTIFICATION 7065 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-8 System Use Notification Select Select Select 
OT Discussion: Many OT systems must remain in continuous operation, and system use 7066 
notification may not be supported or effective. Example compensating controls include posting 7067 
physical notices in OT facilities or providing recurring training on system use prior to permitting 7068 
access. 7069

<!-- page 241 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
223 
AC-10 CONCURRENT SESSION CONTROL 7070 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-10 Concurrent Session Control   Select 
OT Discussion: The number, account type, and privileges of concurrent sessions consider the 7071 
roles and responsibilities of the affected individuals. Example compensating controls include 7072 
providing increased auditing measures. 7073 
AC-11 DEVICE LOCK 7074 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-11 Device Lock  Select Select 
AC-11 (1) DEVICE LOCK | PATTERN-HIDING DISPLAYS  Select Select 
OT Discussion: This control assumes a staffed environment in which users interact with system 7075 
displays. This control may be tailored appropriately if systems do not have displays configured, 7076 
systems are placed in an access-controlled facility or locked enclosure, or immediate operator 7077 
response is required in emergency situations. Example compensating controls include locating 7078 
the display in an area with physical access controls that limit access to individuals with 7079 
permission and a need to know the displayed information. 7080 
Control Enhancement: (1) OT Discussion: Physical protection may be employed to prevent 7081 
access to a display or the attachment of a display. When the OT cannot conceal displayed 7082 
information, the organization employs nonautomated mechanisms or procedures as 7083 
compensating controls in accordance with the general tailoring guidance. 7084 
AC-12 SESSION TERMINATION 7085 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-12 Session Termination  Select Select 
OT Discussion: Example compensating controls include providing increased auditing measures 7086 
or limiting remote access privileges to key personnel. 7087

<!-- page 242 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
224 
AC-14 PERMITTED ACTIONS WITHOUT IDENTIFICATION OR AUTHENTICATION 7088 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-14 Permitted Actions without Identification or Authentication Select Select Select 
OT Discussion: No OT Discussion for this control. 7089 
AC-17 REMOTE ACCESS 7090 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
AC-17 Remote Access Select Select Select 
AC-17 (1) REMOTE ACCESS | AUTOMATED MONITORING / CONTROL  Select Select 
AC-17 (2) REMOTE ACCESS | PROTECTION OF CONFIDENTIALITY / INTEGRITY USING ENCRYPTION  Select Select 
AC-17 (3) REMOTE ACCESS | MANAGED ACCESS CONTROL POINTS  Select Select 
AC-17 (4) REMOTE ACCESS | PRIVILEGED COMMANDS / ACCESS  Select Select 
AC-17 (9) REMOTE ACCESS | DISCONNECT OR DISABLE ACCESS Add Add Add 
AC-17 (10) REMOTE ACCESS | AUTHENTICATE REMOTE COMMANDS  Add Add 
OT Discussion: When the OT cannot implement any or all of the components of this control, the 7091 
organization employs other mechanisms or procedures as compensating controls in accordance 7092 
with the general tailoring guidance. 7093 
Control Enhancement: (1) OT Discussion: Example compensating controls include employing 7094 
nonautomated mechanisms or procedures as compensating controls. Compensating controls 7095 
could include limiting remote access to a specified period of time or placing a call from the OT 7096 
site to the authenticated remote entity.  7097 
Control Enhancement: (2) OT Discussion: Encryption-based technologies should be used to 7098 
support the confidentiality and integrity of remote access sessions. If OT devices lack the ability 7099 
to support modern encryption, additional devices (e.g., VPNs) can be added. This control should 7100 
not be confused with SC-8 – Transmission Confidentiality and Integrity, which discusses 7101 
confidentiality and integrity requirements for general communications, including between OT 7102 
devices.  7103 
Control Enhancement: (3) OT Discussion: Example compensating controls include connection-7104 
specific manual authentication of the remote entity.  7105 
Control Enhancement: (4) (10) No OT Discussion for this control. 7106

<!-- page 243 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
225 
Control Enhancement: (9) OT Discussion: Implementation of the remote access disconnect 7107 
should not impact OT operations. OT personnel should be trained on how to use the remote 7108 
access disconnect. 7109 
Rationale for adding AC-17 (9) to LOW, MOD, and HIGH baselines: As more OT systems become 7110 
accessible remotely, the capability to disconnect or disable remote access is critical to 7111 
managing risk and may be required to provide stable and safe operations.  7112 
Rationale for adding AC-17 (10) to MOD and HIGH baselines: The ability to authenticate remote 7113 
commands is important to prevent unauthorized commands that may have immediate or 7114 
serious consequences, such as injury, death, property damage, the loss of high-value assets, the 7115 
failure of mission or business functions, or compromise of sensitive information.  7116 
AC-18 WIRELESS ACCESS 7117 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-18 Wireless Access Select Select Select 
AC-18 (1) WIRELESS ACCESS | AUTHENTICATION AND ENCRYPTION  Select Select 
AC-18 (3) WIRELESS ACCESS | DISABLE WIRELESS NETWORKING  Select Select 
AC-18 (4) WIRELESS ACCESS | RESTRICT CONFIGURATIONS BY USERS   Select 
AC-18 (5) WIRELESS ACCESS | ANTENNAS AND TRANSMISSION POWER LEVELS   Select 
OT Discussion: When OT cannot implement any or all of the components of this control, the 7118 
organization employs other mechanisms or procedures as compensating controls in accordance 7119 
with the general tailoring guidance.  7120 
Control Enhancement: (1) OT Discussion: The implementation of authentication and encryption 7121 
is driven by the OT environment. If devices and users cannot all be authenticated and encrypted 7122 
due to operational or technology constraints, compensating controls may include providing 7123 
increased auditing for wireless access, limiting wireless access privileges to key personnel, or 7124 
using AC-18 (5) to reduce the boundary of wireless access.  7125 
Control Enhancement: (3) (4) No OT Discussion for this control.  7126 
Control Enhancement: (5) Availability and interference for wireless signals may be a concern 7127 
within OT environments. Antennas and power levels should be designed to overcome and 7128 
achieve availability goals. If confidentiality is a concern, antennas and power levels can also be 7129 
designed to minimize signal exposure outside of the facility. 7130

<!-- page 244 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
226 
AC-19 ACCESS CONTROL FOR MOBILE DEVICES 7131 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-19 Access Control for Mobile Devices Select Select Select 
AC-19 (5) ACCESS CONTROL FOR MOBILE DEVICES | FULL DEVICE / CONTAINER-BASED ENCRYPTION  Select Select 
OT Discussion: No OT Discussion for this control. 7132 
AC-20 USE OF EXTERNAL SYSTEMS 7133 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-20 Use of External Systems Select Select Select 
AC-20 (1) USE OF EXTERNAL SYSTEMS | LIMITS ON AUTHORIZED USE  Select Select 
AC-20 (2) USE OF EXTERNAL SYSTEMS | PORTABLE STORAGE MEDIA  Select Select 
OT Discussion: Organizations refine the definition of “external” to reflect lines of authority and 7134 
responsibility, the granularity of an organization entity, and their relationships. An organization 7135 
may consider a system to be external if that system performs different functions, implements 7136 
different policies, falls under different management authorities, or does not provide sufficient 7137 
visibility into the implementation of controls to establish a satisfactory trust relationship. For 7138 
example, an OT system and a business data processing system may be considered external to 7139 
each other, depending on the organization’s system boundaries.  7140 
Access to an OT for support by a business partner (e.g., vendor, support contractor) is another 7141 
common example. The definition and trustworthiness of external systems is reexamined with 7142 
respect to OT functions, purposes, technology, and limitations to establish a clearly 7143 
documented technical or business case for use and an acceptance of the risk inherent in the use 7144 
of an external system.  7145 
Control Enhancement: (1) (2) No OT Discussion for this control. 7146 
AC-21 INFORMATION SHARING  7147 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-21 Information Sharing  Select Select 
OT Discussion: No OT Discussion for this control.  7148

<!-- page 245 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
227 
AC-22 PUBLICLY ACCESSIBLE CONTENT  7149 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AC-22 Publicly Accessible Content Select Select Select 
OT Discussion: Generally, public access to OT systems is not permitted. Select information may 7150 
be transferred to a publicly accessible system, possibly with added controls. The organization 7151 
should review what information is being made accessible prior to publication. 7152 
E.7.2. AWARENESS AND TRAINING – AT 7153 
AT-1 POLICY AND PROCEDURES  7154 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AT-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7155 
and the relationship to non-OT systems.  7156 
AT-2 LITERACY TRAINING AND AWARENESS  7157 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
AT-2 Literacy Training and Awareness Select Select Select 
AT-2 (2) LITERACY TRAINING AND AWARENESS | INSIDER THREAT Select Select Select 
AT-2 (3) LITERACY TRAINING AND AWARENESS | SOCIAL ENGINEERING AND MINING  Select Select 
AT-2 (4) LITERACY TRAINING AND AWARENESS | SUSPICIOUS COMMUNICATIONS AND ANOMALOUS SYSTEM BEHAVIOR  Add Add 
OT Discussion: Security awareness training includes initial and periodic reviews of OT-specific 7158 
policies, standard operating procedures, security trends, and vulnerabilities. The OT security 7159 
awareness program is consistent with the requirements of the security awareness and training 7160 
policy established by the organization. 7161 
Control Enhancement: (2) (3) No OT Discussion for this control.  7162 
Control Enhancement: (4) OT Discussion: Identify and communicate suspicious and anomalous 7163 
behaviors within the OT environment, such as a PLC still in programming mode when it is 7164 
expected to be in run mode, process trips with an undetermined root cause, malware on an 7165

<!-- page 246 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
228 
HMI, unexpected mouse movement, or process changes that are not being performed by the 7166 
operator.  7167 
Rationale for adding AT-2 (4) to MOD and HIGH baselines: Training OT personnel on identifying 7168 
potentially suspicious communications and anomalous behaviors as well as the actions to take 7169 
if anomalous system behavior occurs can supplement system detection and protection 7170 
mechanisms for improved response.  7171 
AT-3 ROLE-BASED TRAINING  7172 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AT-3 Role-Based Training Select Select Select 
OT Discussion: Security training includes initial and periodic reviews of OT-specific policies, 7173 
standard operating procedures, security trends, and vulnerabilities. The OT security training 7174 
program is consistent with the requirements of the security awareness and training policy 7175 
established by the organization. The training may be customized for specific OT roles, which 7176 
could include operators, maintainers, engineers, supervisors, and administrators.  7177 
AT-4 TRAINING RECORDS  7178 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AT-4 Training Records Select Select Select 
OT Discussion: No OT Discussion for this control.  7179 
E.7.3. AUDITING AND ACCOUNTABILITY – AU 7180 
E.7.3.2. Tailoring Considerations for the Audit Family 7181 
When OT cannot support the specific audit and accountability requirements of a control, the 7182 
organization employs compensating controls in accordance with the general tailoring guidance. 7183 
For example, organizations may want to consider whether security audit information is 7184 
available from separate systems or system components (e.g., the historian, firewall logs, 7185 
physical security systems). Additional examples of compensating controls are given with each 7186 
control as appropriate.  7187

<!-- page 247 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
229 
AU-1 AUDIT AND ACCOUNTABILITY POLICY AND PROCEDURES  7188 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AU-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7189 
and the relationship to non-OT systems. 7190 
AU-2 EVENT LOGGING 7191 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AU-2 Event Logging Select Select Select 
OT Discussion: Organizations may want to include relevant OT events (e.g., alerts, alarms, 7192 
configuration and status changes, operator actions) in their event logging, which may be 7193 
designated as audit events. 7194 
AU-3 CONTENT OF AUDIT RECORDS  7195 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AU-3 Content of Audit Records Select Select Select 
AU-3 (1) CONTENT OF AUDIT RECORDS | ADDITIONAL AUDIT INFORMATION  Select Select 
OT Discussion: No OT Discussion for this control. 7196 
AU-4 AUDIT LOG STORAGE CAPACITY 7197 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
AU-4 Audit Log Storage Capacity Select Select Select 
AU-4 (1) AUDIT LOG STORAGE CAPACITY | TRANSFER TO ALTERNATE STORAGE Add Add Add 
OT Discussion: No OT Discussion for this control.  7198 
Rationale for adding AU-4 (1) to LOW, MOD, and HIGH baselines: Organizational requirements 7199 
may require the storage of very large amounts of data, which OT components may not be able 7200 
to support directly.  7201

<!-- page 248 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
230 
AU-5 RESPONSE TO AUDIT LOGGING PROCESS FAILURES  7202 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AU-5 Response to Audit Logging Process Failures Select Select Select 
AU-5 (1) RESPONSE TO AUDIT LOGGING PROCESS FAILURES | AUDIT STORAGE CAPACITY   Select 
AU-5 (2) RESPONSE TO AUDIT LOGGING PROCESS FAILURES | REAL-TIME ALERTS   Select 
OT Discussion: No OT Discussion for this control. 7203 
AU-6 AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING  7204 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AU-6 Audit Review, Analysis, and Reporting Select Select Select 
AU-6 (1) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | AUTOMATED PROCESS INTEGRATION  Select Select 
AU-6 (3) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | CORRELATE AUDIT RECORD REPOSITORIES  Select Select 
AU-6 (5) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | INTEGRATED ANALYSIS OF AUDIT RECORDS   Select 
AU-6 (6) AUDIT RECORD REVIEW, ANALYSIS, AND REPORTING | CORRELATION WITH PHYSICAL MONITORING   Select 
OT Discussion: No OT Discussion for this control. 7205 
Control Enhancement: (1) OT Discussion: Compensating controls may include manual 7206 
mechanisms or procedures. If audit records cannot be feasibly collected for devices, periodic 7207 
manual review may be necessary. 7208 
Control Enhancement: (3) (5) (6) No OT Discussion for this control.  7209 
AU-7 AUDIT RECORD REDUCTION AND REPORT GENERATION  7210 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AU-7 Audit Record Reduction and Report Generation  Select Select 
AU-7 (1) AUDIT RECORD REDUCTION AND REPORT GENERATION | AUTOMATIC PROCESSING  Select Select 
OT Discussion: No OT Discussion for this control.  7211

<!-- page 249 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
231 
AU-8 TIME STAMPS  7212 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AU-8 Time Stamps Select Select Select 
OT Discussion: Compensating controls may include using a separate system designated as an 7213 
authoritative time source (see related control SC-45). 7214 
AU-9 PROTECTION OF AUDIT INFORMATION 7215 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AU-9 Protection of Audit Information Select Select Select 
AU-9 (2) PROTECTION OF AUDIT INFORMATION | STORE ON SEPARATE PHYSICAL SYSTEMS OR COMPONENTS   Select 
AU-9 (3) PROTECTION OF AUDIT INFORMATION | CRYPTOGRAPHIC PROTECTION   Select 
AU-9 (4) PROTECTION OF AUDIT INFORMATION | ACCESS BY SUBSET OF PRIVILEGED USERS  Select Select 
OT Discussion: No OT Discussion for this control. 7216 
AU-10 NON-REPUDIATION 7217 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AU-10 Non-Repudiation   Select 
OT Discussion: OT devices may not enforce non-repudiation of audit records and may require 7218 
compensating controls, such as physical security systems, cameras to monitor user access, or a 7219 
separate device for log collection. 7220 
AU-11 AUDIT RECORD RETENTION 7221 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AU-11 Audit Record Retention Select Select Select 
OT Discussion: No OT Discussion for this control.  7222

<!-- page 250 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
232 
AU-12 AUDIT RECORD GENERATION 7223 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
AU-12 Audit Record Generation Select Select Select 
AU-12 (1) AUDIT RECORD GENERATION | SYSTEM-WIDE AND TIME-CORRELATED AUDIT TRAIL   Select 
AU-12 (3) AUDIT RECORD GENERATION | CHANGES BY AUTHORIZED INDIVIDUALS   Select 
OT Discussion: No OT Discussion for this control. 7224 
Control Enhancement: (1) OT Discussion: Compensating controls may include providing time-7225 
correlated audit records on a separate system. 7226 
Control Enhancement: (3) OT Discussion: Compensating controls may include employing 7227 
nonautomated mechanisms or procedures.  7228 
E.7.4. ASSESSMENT, AUTHORIZATION, AND MONITORING – CA 7229 
E.7.4.3. Tailoring Considerations for the Security Assessment and Authorization Family 7230 
When the OT cannot support the specific assessment, authorization, and monitoring 7231 
requirements of a control, the organization employs compensating controls in accordance with 7232 
the general tailoring guidance. Examples of compensating controls are given with each control 7233 
as appropriate.  7234 
CA-1 POLICY AND PROCEDURES  7235 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CA-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7236 
and the relationship to non-OT systems.  7237 
CA-2 CONTROL ASSESSMENTS  7238 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CA-2 Control Assessments Select Select Select 
CA-2 (1) CONTROL ASSESSMENTS | INDEPENDENT ASSESSORS  Select Select 
CA-2 (2) CONTROL ASSESSMENTS | SPECIALIZED ASSESSMENTS   Select

<!-- page 251 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
233 
OT Discussion: Assessments are performed and documented by qualified assessors (i.e., 7239 
experienced in assessing OT) authorized by the organization. The individual or group conducting 7240 
the assessment fully understands the organizational information security policies and 7241 
procedures, the OT security policies and procedures, and the specific health, safety, and 7242 
environmental risks associated with a particular facility and/or process. The organization 7243 
ensures that the assessment does not affect system operation or result in unintentional system 7244 
modification. If assessment activities must be performed on the production OT, it may need to 7245 
be taken offline before an assessment can be conducted, or the assessment should be 7246 
scheduled to occur during planned OT outages whenever possible. 7247 
Control Enhancement: (1) No OT Discussion for this control.  7248 
Control Enhancement: (2) OT Discussion: The organization conducts risk analysis to support the 7249 
selection of an assessment target (e.g., the live system, an offline replica, lab system).  7250 
CA-3 INFORMATION EXCHANGE 7251 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CA-3 Information Exchange Select Select Select 
CA-3 (6) INFORMATION EXCHANGE | TRANSFER AUTHORIZATION   Select 
OT Discussion: Organizations perform a risk-benefit analysis to determine whether an OT 7252 
should be connected to other systems. The authorizing official (AO) fully understands the 7253 
organizational information security policies and procedures; the OT security policies and 7254 
procedures; the risks to organizational operations and assets, individuals, other organizations, 7255 
and the Nation associated with the connection to other systems; the individuals and 7256 
organizations that operate and maintain the systems, including maintenance contractors or 7257 
service providers; and the specific health, safety, and environmental risks associated with a 7258 
particular interconnection. Connections from the OT environment to other security zones may 7259 
cross the authorization boundary such that two different authorizing officials may be required 7260 
to approve the connection. Decisions to accept risk are documented.  7261 
Control Enhancement: (6) No OT Discussion for this control.  7262 
CA-5 PLAN OF ACTION AND MILESTONES  7263 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CA-5 Plan of Action and Milestones Select Select Select 
OT Discussion: Corrective actions identified in assessments may not be immediately actionable 7264 
in an OT environment. Therefore, short-term mitigations may be implemented to reduce risk as 7265 
part of the gap closure plan or plan of action and milestones.   7266

<!-- page 252 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
234 
CA-6 AUTHORIZATION  7267 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CA-6 Authorization Select Select Select 
OT Discussion: No OT Discussion for this control.  7268 
CA-7 CONTINUOUS MONITORING   7269 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CA-7 Continuous Monitoring Select Select Select 
CA-7 (1) CONTINUOUS MONITORING | INDEPENDENT ASSESSMENT  Select Select 
CA-7 (4) CONTINUOUS MONITORING | RISK MONITORING Select Select Select 
OT Discussion: Continuous monitoring programs for OT are designed, documented, and 7270 
implemented with input from OT personnel. The organization ensures that continuous 7271 
monitoring does not interfere with OT functions. The individual or group designing and 7272 
conducting the continuous monitoring for the OT systems implements a monitoring program 7273 
that is consistent with the organizational information security policies and procedures, the OT 7274 
security policies and procedures, and the specific health, safety, and environmental risks 7275 
associated with a particular facility and/or process. Continuous monitoring can be automated 7276 
or manual at a frequency sufficient to support risk-based decisions. For example, the 7277 
organization may monitor event logs manually on a specified frequency less often for lower-7278 
risk, isolated systems than for higher-risk, networked systems.  7279 
Control Enhancement: (1) (4) No OT Discussion for this control.  7280 
CA-8 PENETRATION TESTING  7281 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CA-8 Penetration Testing   Select 
CA-8 (1) PENETRATION TESTING | INDEPENDENT PENETRATION TESTING AGENT OR TEAM   Remove 
OT Discussion: Penetration testing is used with care on OT networks to ensure that OT 7282 
functions are not adversely impacted by the testing process. In general, OT systems are highly 7283 
sensitive to timing constraints and have limited resources. Example compensating controls 7284 
include employing a replicated, virtualized, or simulated system to conduct penetration testing. 7285 
Production OT may need to be taken offline before testing can be conducted. If OT systems are 7286 
taken offline for testing, tests are scheduled to occur during planned OT outages whenever 7287

<!-- page 253 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
235 
possible. If penetration testing is performed on non-OT networks, extra care is taken to ensure 7288 
that tests do not propagate into the OT network.  7289 
Rationale for removing CA-8 (1) from HIGH baseline: Specific expertise is necessary to conduct 7290 
effective penetration testing on OT systems, and it may not be feasible to identify independent 7291 
personnel with the appropriate skillset or knowledge to perform penetration testing on an OT 7292 
environment. While an independent penetration test agent or team is recommended, it may 7293 
not be feasible for all high-impact OT systems.  7294 
CA-9 INTERNAL SYSTEM CONNECTIONS  7295 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CA-9 Internal System Connections Select Select Select 
OT Discussion: Organizations perform risk-benefit analysis to determine whether OT equipment 7296 
should be connected to other internal system components and then document those 7297 
connections. The AO fully understands the potential risks associated with approving individual 7298 
connections or approving a class of components to be connected. For example, the AO may 7299 
broadly approve the connection of any sensors limited to 4 to 20 milliamp (mA) 7300 
communication, while other connection types (e.g., serial, Ethernet) require individual 7301 
approval. Decisions to accept risk are documented. 7302 
E.7.5. CONFIGURATION MANAGEMENT – CM 7303 
E.7.5.4. Tailoring Considerations for the Configuration Management Family 7304 
When the OT cannot be configured to restrict the use of unnecessary functions or cannot 7305 
support the use of automated mechanisms to implement configuration management functions, 7306 
the organization employs nonautomated mechanisms or procedures as compensating controls 7307 
in accordance with the general tailoring guidance. Examples of compensating controls are given 7308 
with each control as appropriate. 7309 
CM-1 POLICY AND PROCEDURES  7310 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CM-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7311 
and the relationship to non-OT systems.  7312

<!-- page 254 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
236 
CM-2 BASELINE CONFIGURATION 7313 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CM-2 Baseline Configuration Select Select Select 
CM-2 (2) BASELINE CONFIGURATION | AUTOMATION SUPPORT FOR ACCURACY / CURRENCY  Select Select 
CM-2 (3) BASELINE CONFIGURATION | RETENTION OF PREVIOUS CONFIGURATIONS  Select Select 
CM-2 (7) BASELINE CONFIGURATION | CONFIGURE SYSTEMS, COMPONENTS, OR DEVICES FOR HIGH-RISK AREAS  Select Select 
OT Discussion: No OT Discussion for this control. 7314 
CM-3 CONFIGURATION CHANGE CONTROL 7315 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CM-3 Configuration Change Control  Select Select 
CM-3 (1) CONFIGURATION CHANGE CONTROL | AUTOMATED DOCUMENT / NOTIFICATION / PROHIBITION OF CHANGES   Select 
CM-3 (2) CONFIGURATION CHANGE CONTROL | TEST / VALIDATE / DOCUMENT CHANGES  Select Select 
CM-3 (4) CONFIGURATION CHANGE CONTROL | SECURITY AND PRIVACY REPRESENTATIVES  Select Select 
CM-3 (6) CONFIGURATION CHANGE CONTROL | CRYPTOGRAPHY MANAGEMENT   Select 
CM-3 (7) CONFIGURATION CHANGE CONTROL | REVIEW SYSTEM CHANGES    
CM-3 (8) CONFIGURATION CHANGE CONTROL | PREVENT OR RESTRICT CONFIGURATION CHANGES    
OT Discussion: Configuration change control procedures should align with the organization’s 7316 
management of change practices. 7317 
Control Enhancement: (1) (2) (4) (6) No OT Discussion for this control. 7318 
Control Enhancement: (7) OT Discussion: The organization considers OT-specific requirements 7319 
when determining the frequency and/or circumstances for reviewing system changes. For 7320 
example, safety instrumented systems may be justified for the review of system changes on a 7321 
predetermined frequency to ensure that no inadvertent changes have been made to the logic 7322 
solver portion of a safety instrumented function.  7323 
Control Enhancement: (8) OT Discussion: The organization prevents or restricts configuration 7324 
changes based on a risk determination that the system should not be modified without 7325 
additional permission. For example, some PLCs have physical key switches that are used to 7326 
place the PLC in a mode that allows for programming changes. Physical key switches can restrict 7327 
configuration changes so that physical access is required to make a modification to the system.   7328

<!-- page 255 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
237 
CM-4 IMPACT ANALYSES  7329 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CM-4 Impact Analyses Select Select Select 
CM-4 (1) IMPACT ANALYSES | SEPARATE TEST ENVIRONMENTS   Select 
CM-4 (2) IMPACT ANALYSES | VERIFICATION OF CONTROLS  Select Select 
OT Discussion: The organization considers OT safety and security interdependencies. OT 7330 
security and safety personnel are included in change process management if the change to the 7331 
system may impact safety or security. 7332 
Control Enhancement: (1) (2) No OT Discussion for this control. 7333 
CM-5 ACCESS RESTRICTIONS FOR CHANGE 7334 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CM-5 Access Restrictions for Change Select Select Select 
CM-5 (1) ACCESS RESTRICTIONS FOR CHANGE | AUTOMATED ACCESS ENFORCEMENT / AUDITING   Select 
OT Discussion: Some OT devices allow for the configuration and use of mode change switches. 7335 
Where available, these should be used to prevent unauthorized changes. For example, many 7336 
PLCs have key switches that allow the device to be placed in a programming mode or running 7337 
mode. Those PLCs should be placed in a running or remote mode to prevent unauthorized 7338 
programming changes, and the key should be removed from the key switch and managed 7339 
appropriately. 7340 
Control Enhancement: (1) No OT Discussion for this control. 7341 
CM-6 CONFIGURATION SETTINGS 7342 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CM-6 Configuration Settings Select Select Select 
CM-6 (1) CONFIGURATION SETTINGS | AUTOMATED CENTRAL MANAGEMENT / APPLICATION / VERIFICATION   Select 
CM-6 (2) CONFIGURATION SETTINGS | RESPOND TO UNAUTHORIZED CHANGES   Select 
OT Discussion: No OT Discussion for this control.  7343

<!-- page 256 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
238 
CM-7 LEAST FUNCTIONALITY 7344 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CM-7 Least Functionality Select Select Select 
CM-7 (1) LEAST FUNCTIONALITY | PERIODIC REVIEW  Select Select 
CM-7 (2) LEAST FUNCTIONALITY | PREVENT PROGRAM EXECUTION  Select Select 
CM-7 (5) LEAST FUNCTIONALITY | AUTHORIZED SOFTWARE — ALLOW-BY-EXCEPTION  Select Select 
OT Discussion: The organization implements least functionality by allowing only the specified 7345 
functions, protocols, and/or services required for OT operations. For non-routable protocols 7346 
(e.g., serial communications), interrupts could be disabled or set points could be made read-7347 
only except for privileged users to limit functionality. Ports are part of the address space in 7348 
network protocols and are often associated with specific protocols or functions. For routable 7349 
protocols, ports can be disabled on many networking devices to limit functionality to the 7350 
minimum required for operation. 7351 
Control Enhancement: (1) (2) No OT Discussion. 7352 
Control Enhancement: (5) OT Discussion: The set of applications that run in OT is relatively 7353 
static, making allowlisting practical. DHS recommends using application allowlisting for OT 7354 
equipment.  7355 
CM-8 SYSTEM COMPONENT INVENTORY  7356 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CM-8 System Component Inventory Select Select Select 
CM-8 (1) SYSTEM COMPONENT INVENTORY | UPDATES DURING INSTALLATIONS / REMOVALS  Select Select 
CM-8 (2) SYSTEM COMPONENT INVENTORY | AUTOMATED MAINTENANCE   Select 
CM-8 (3) SYSTEM COMPONENT INVENTORY | AUTOMATED UNAUTHORIZED COMPONENT DETECTION  Select Select 
CM-8 (4) SYSTEM COMPONENT INVENTORY | PROPERTY ACCOUNTABILITY INFORMATION   Select 
OT Discussion: No OT Discussion for this control. 7357 
CM-9 CONFIGURATION MANAGEMENT PLAN 7358 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CM-9 Configuration Management Plan  Select Select

<!-- page 257 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
239 
OT Discussion: Configuration management plans apply to the internal and external resources 7359 
(e.g., contractors, integrators) responsible for device configuration. 7360 
CM-10 SOFTWARE USAGE RESTRICTIONS 7361 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CM-10 Software Usage Restrictions Select Select Select 
OT Discussion: No OT Discussion for this control. 7362 
CM-11 USER-INSTALLED SOFTWARE 7363 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CM-11 User-Installed Software Select Select Select 
OT Discussion: No OT Discussion for this control. 7364 
CM-12 INFORMATION LOCATION 7365 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CM-12 Information Location  Select Select 
CM-12 (1) INFORMATION LOCATION | AUTOMATED TOOLS TO SUPPORT INFORMATION 
LOCATION  Select Select 
OT Discussion: Organizations identify specific information types or components to track where 7366 
information is being processed and stored. Information to consider in the OT environment may 7367 
include shared account passwords, PLC backup files, detailed network drawings, and risk 7368 
assessments that identify specific threats with the environment.  7369 
Control Enhancement: (1) No OT Discussion for this control.  7370 
E.7.6. CONTINGENCY PLANNING – CP 7371 
E.7.6.5. Tailoring Considerations for the Contingency Planning Family 7372 
OT systems often contain a physical component at a fixed location that may not be relocated 7373 
logically, and some replacement components may not be readily available. The continuance of 7374 
essential mission and business functions with little or no loss of operational continuity may not 7375 
be possible. When the organization cannot provide necessary essential services, support, or 7376 
automated mechanisms during contingency operations, it should provide nonautomated 7377 
mechanisms or predetermined procedures as compensating controls in accordance with the 7378

<!-- page 258 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
240 
general tailoring guidance. Examples of compensating controls are given with each control as 7379 
appropriate. 7380 
CP-1 POLICY AND PROCEDURES 7381 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CP-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7382 
and the relationship to non-OT systems.  7383 
CP-2 CONTINGENCY PLAN  7384 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CP-2 Contingency Plan Select Select Select 
CP-2 (1) CONTINGENCY PLAN | COORDINATE WITH RELATED PLANS  Select Select 
CP-2 (2) CONTINGENCY PLAN | CAPACITY PLANNING   Select 
CP-2 (3) CONTINGENCY PLAN | RESUME MISSION AND BUSINESS FUNCTIONS  Select Select 
CP-2 (5) CONTINGENCY PLAN | CONTINUE MISSION AND BUSINESS FUNCTIONS   Select 
CP-2 (8) CONTINGENCY PLAN | IDENTIFY CRITICAL ASSETS  Select Select 
OT Discussion: The organization defines contingency plans for categories of disruptions or 7385 
failures. In the case of a contingency, the OT equipment executes preprogrammed functions, 7386 
such as alerting the operator of the failure and then doing nothing, alerting the operator and 7387 
then safely shutting down the industrial process, or alerting the operator and then maintaining 7388 
the last operational setting prior to failure. Contingency plans for widespread disruption may 7389 
involve specialized organizations (e.g., FEMA, emergency services, regulatory authorities).  7390 
Control Enhancement: (1) (2) (3) (5) (8) No OT Discussion for this control.  7391 
CP-3 CONTINGENCY TRAINING  7392 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CP-3 Contingency Training Select Select Select 
CP-3 (1) CONTINGENCY TRAINING | SIMULATED EVENTS   Select 
OT Discussion: No OT Discussion for this control. 7393

<!-- page 259 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
241 
CP-4 CONTINGENCY PLAN TESTING 7394 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CP-4 Contingency Plan Testing Select Select Select 
CP-4 (1) CONTINGENCY PLAN TESTING | COORDINATE WITH RELATED PLANS  Select Select 
CP-4 (2) CONTINGENCY PLAN TESTING | ALTERNATE PROCESSING SITE   Select 
OT Discussion: No OT Discussion for this control. 7395 
Control Enhancement: (1) No OT Discussion for this control.  7396 
Control Enhancement: (2) OT Discussion: Not all systems will have alternate processing sites, as 7397 
discussed in CP-7.  7398 
CP-6 ALTERNATE STORAGE SITE  7399 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CP-6 Alternate Storage Site  Select Select 
CP-6 (1) ALTERNATE STORAGE SITE | SEPARATION FROM PRIMARY SITE  Select Select 
CP-6 (2) ALTERNATE STORAGE SITE | RECOVERY TIME AND RECOVERY POINT OBJECTIVES   Select 
CP-6 (3) ALTERNATE STORAGE SITE | ACCESSIBILITY  Select Select 
OT Discussion: No OT Discussion for this control. 7400 
CP-7 ALTERNATE PROCESSING SITE 7401 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CP-7 Alternate Processing Site  Select Select 
CP-7 (1) ALTERNATE PROCESSING SITE | SEPARATION FROM PRIMARY SITE  Select Select 
CP-7 (2) ALTERNATE PROCESSING SITE | ACCESSIBILITY  Select Select 
CP-7 (3) ALTERNATE PROCESSING SITE | PRIORITY OF SERVICE  Select Select 
CP-7 (4) ALTERNATE PROCESSING SITE | PREPARATION FOR USE   Select 
OT Discussion: Many site-wide supervisory or optimization servers (i.e., Level 3 and above of 7402 
the Purdue model) can be supported from an alternate processing site. It is likely not feasible 7403

<!-- page 260 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
242 
for control systems or field devices, such as sensors or final elements (i.e., Level 1 and 0 of the 7404 
Purdue model), to be made available from an alternate processing site. 7405 
Control Enhancement: (1) (2) (3) (4) No OT Discussion for this control. 7406 
CP-8 TELECOMMUNICATIONS SERVICES  7407 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CP-8 Telecommunications Services  Select Select 
CP-8 (1) TELECOMMUNICATIONS SERVICES | PRIORITY OF SERVICE PROVISIONS  Select Select 
CP-8 (2) TELECOMMUNICATIONS SERVICES | SINGLE POINTS OF FAILURE  Select Select 
CP-8 (3) TELECOMMUNICATIONS SERVICES | SEPARATION OF PRIMARY AND ALTERNATE PROVIDERS   Select 
CP-8 (4) TELECOMMUNICATIONS SERVICES | PROVIDER CONTINGENCY PLAN   Select 
OT Discussion: Quality of service factors for OT include latency and throughput. 7408 
Control Enhancement: (1) (2) (3) (4) No OT Discussion for this control. 7409 
CP-9 SYSTEM BACKUP 7410 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
CP-9 System Backup Select Select Select 
CP-9 (1) SYSTEM BACKUP | TESTING FOR RELIABILITY AND INTEGRITY  Select Select 
CP-9 (2) SYSTEM BACKUP | TEST RESTORATION USING SAMPLING   Select 
CP-9 (3) SYSTEM BACKUP | SEPARATE STORAGE FOR CRITICAL INFORMATION   Select 
CP-9 (5) SYSTEM BACKUP | TRANSFER TO ALTERNATE STORAGE SITE   Select 
CP-9 (8) SYSTEM BACKUP | CRYPTOGRAPHIC PROTECTION  Select Select 
OT Discussion: No OT Discussion for this control. 7411 
Control Enhancement: (1) (2) OT Discussion: Testing for reliability and integrity increases 7412 
confidence that the system can be restored after an incident and minimizes the impact 7413 
associated with downtime and outages. The ability to test backups often depends on the 7414 
resources needed to appropriately represent the environment, such as the availability of spare 7415 
devices and testing equipment. Testing backup and restoration on OT is often limited to 7416 
systems with redundancy or spare equipment. In certain cases, sampling will be limited to those 7417 
redundant systems. Compensating controls may include alternative methods for testing 7418 
backups, such as hash or checksum validations.  7419

<!-- page 261 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
243 
Control Enhancement: (3) (5) (8) No OT Discussion for this control.  7420 
CP-10 SYSTEM RECOVERY AND RECONSTITUTION  7421 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
CP-10 System Recovery and Reconstitution Select Select Select 
CP-10 (2) SYSTEM RECOVERY AND RECONSTITUTION | TRANSACTION RECOVERY  Select Select 
CP-10 (4) SYSTEM RECOVERY AND RECONSTITUTION | RESTORE WITHIN TIME PERIOD   Select 
CP-10 (6) SYSTEM RECOVERY AND RECONSTITUTION | COMPONENT PROTECTION  Add Add 
OT Discussion: Reconstitution of the OT includes considering whether system state variables 7422 
should be restored to their initial values or to the values before the disruption (e.g., valves 7423 
restored to full open, full closed, or to settings prior to the disruption). Restoring system state 7424 
variables may be disruptive to ongoing physical processes (e.g., valves initially closed may 7425 
adversely affect system cooling).  7426 
Control Enhancement: (2) (4) No OT Discussion for this control.  7427 
Control Enhancement: (6) OT Discussion: Organizations should consider recovery and 7428 
reconstitution time frames when storing spare equipment, including environmental hazards 7429 
that could damage the equipment. Storage locations and environments should be chosen 7430 
appropriately for the type of backup equipment.  7431 
Rationale for adding CP-10 (6) to MOD and HIGH baselines: OT system components stored 7432 
without protection against environmental threats and unauthorized physical or logical access 7433 
can be susceptible to compromise or damage. Certain system components may include 7434 
embedded electronics that must be protected from environmental hazards.  7435 
CP-12 SAFE MODE  7436 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
CP-12 Safe Mode Add Add Add 
OT Discussion: No OT Discussion for this control.  7437 
Rationale for adding CP-12 to LOW, MOD, and HIGH baselines: This control provides a 7438 
framework for the organization to plan its policy and procedures for dealing with IT and OT 7439 
conditions beyond its control in the environment of operations to minimize potential safety and 7440 
environmental impacts.  7441

<!-- page 262 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
244 
E.7.7. IDENTIFICATION AND AUTHENTICATION – IA 7442 
E.7.7.6. Tailoring Considerations for the Identification and Authentication Family 7443 
Before implementing controls in the IA family, consider the trade-offs among security, privacy, 7444 
latency, performance, and throughput. For example, the organization considers whether 7445 
latency induced from the use of authentication mechanisms that employ cryptography would 7446 
adversely impact the operational performance of the OT.  7447 
When the OT cannot support the specific identification and authentication requirements of a 7448 
control, the organization employs compensating controls in accordance with the general 7449 
tailoring guidance. Examples of compensating controls are given with each control as 7450 
appropriate.  7451 
IA-1 POLICY AND PROCEDURES  7452 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IA-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7453 
and the relationship to non-OT systems.  7454 
IA-2 IDENTIFICATION AND AUTHENTICATION (ORGANIZATIONAL USERS)  7455 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IA-2 Identification and Authentication (Organizational Users) Select Select Select 
IA-2 (1) IDENTIFICATION AND AUTHENTICATION | MULTI-FACTOR AUTHENTICATION TO PRIVILEGED ACCOUNTS Select Select Select 
IA-2 (2) IDENTIFICATION AND AUTHENTICATION | MULTI-FACTOR AUTHENTICATION TO NON-PRIVILEGED ACCOUNTS Select Select Select 
IA-2 (5) IDENTIFICATION AND AUTHENTICATION | INDIVIDUAL AUTHENTICATION WITH GROUP AUTHENTICATION   Select 
IA-2 (8) IDENTIFICATION AND AUTHENTICATION | ACCESS TO ACCOUNTS - REPLAY RESISTANT Select Select Select 
IA-2 (12) IDENTIFICATION AND AUTHENTICATION | ACCEPTANCE OF PIV CREDENTIALS Select Select Select 
OT Discussion: When shared accounts are required, compensating controls include providing 7456 
increased physical security, personnel security, and auditing measures. For certain OT, the 7457 
capability for immediate operator interaction is critical. Local emergency actions for OT are not 7458 
hampered by identification or authentication requirements. Access to these systems may be 7459 
restricted by appropriate physical controls.  7460

<!-- page 263 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
245 
Control Enhancement: (1) (2) OT Discussion: As a compensating control, physical access 7461 
restrictions may sufficiently represent one authentication factor, provided that the system is 7462 
not remotely accessible.  7463 
Control Enhancement: (5) OT Discussion: For local access, physical access controls and logging 7464 
may be used as an alternative to individual authentication on an OT system. For remote access, 7465 
the remote access authentication mechanism will be used to identify, permit, and log individual 7466 
access before permitting the use of shared accounts.  7467 
Control Enhancement: (8) No OT Discussion for this control.  7468 
Control Enhancement: (12) OT Discussion: The acceptance of PIV credentials is only required for 7469 
federal organizations, as defined by OMB Memorandum M-19-17 [OMB-M1917]. Non-federal 7470 
organizations should refer to IA-2 (1) (2) for guidance on multi-factor authentication 7471 
credentials. Furthermore, many OT systems do not have the ability to accept PIV credentials 7472 
and will require compensating controls.  7473 
IA-3 DEVICE IDENTIFICATION AND AUTHENTICATION  7474 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
IA-3 Device Identification and Authentication Add Select Select 
IA-3 (1) DEVICE IDENTIFICATION AND AUTHENTICATION | CRYPTOGRAPHIC BIDIRECTIONAL AUTHENTICATION     
IA-3 (4) DEVICE IDENTIFICATION AND AUTHENTICATION | DEVICE ATTESTATION     
OT Discussion: OT devices may not inherently support device authentication. If devices are local 7475 
to one another, physical security measures that prevent unauthorized communication between 7476 
devices can be used as compensating controls. For remote communication, additional hardware 7477 
may be required to meet authentication requirements. 7478 
Control Enhancement: (1) (4) OT Discussion: For OT systems that include IIoT devices, these 7479 
enhancements may be needed to protect device-to-device communication.  7480 
Rationale for adding IA-3 to LOW baseline: Given the variety of OT devices and physical 7481 
locations of OT devices, organizations may consider whether OT devices that may be vulnerable 7482 
to tampering or spoofing require unique identification and authentication and for what types of 7483 
connections.  7484 
IA-4 IDENTIFIER MANAGEMENT  7485 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IA-4 Identifier Management Select Select Select 
IA-4 (4) IDENTIFIER MANAGEMENT | IDENTIFY USER STATUS   Select Select

<!-- page 264 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
246 
OT Discussion: No OT Discussion for this control.  7486 
Control Enhancement: (4) OT Discussion: This control enhancement is typically implemented by 7487 
the organization rather than at the system level. However, to manage risk in certain OT 7488 
environments, identifiers (e.g., badges) may have different markings that indicate the status of 7489 
individuals, such as contractors, foreign nationals, and non-organizational users.  7490 
IA-5 AUTHENTICATOR MANAGEMENT 7491 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IA-5 Authenticator Management Select Select Select 
IA-5 (1) AUTHENTICATOR MANAGEMENT | PASSWORD-BASED AUTHENTICATION Select Select Select 
IA-5 (2) AUTHENTICATOR MANAGEMENT | PUBLIC KEY-BASED AUTHENTICATION  Select Select 
IA-5 (6) AUTHENTICATOR MANAGEMENT | PROTECTION OF AUTHENTICATORS  Select Select 
OT Discussion: Example compensating controls include physical access control and 7492 
encapsulating the OT to provide authentication external to the OT. 7493 
Control Enhancement: (1) (2) (6) No OT Discussion for this control.  7494 
IA-6 AUTHENTICATION FEEDBACK  7495 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IA-6 Authentication Feedback Select Select Select 
OT Discussion: This control assumes a visual interface that provides feedback about 7496 
authentication information during the authentication process. When OT authentication uses an 7497 
interface that does not support visual feedback (e.g., protocol-based authentication), this 7498 
control may be tailored out. 7499 
IA-7 CRYPTOGRAPHIC MODULE AUTHENTICATION 7500 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IA-7 Cryptographic Module Authentication Select Select Select 
OT Discussion: No OT Discussion for this control. 7501

<!-- page 265 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
247 
IA-8 IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) 7502 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IA-8 Identification and Authentication (Non-Organizational Users) Select Select Select 
IA-8 (1) IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) | ACCEPTANCE OF PIV CREDENTIALS FROM OTHER AGENCIES Select Select Select 
IA-8 (2) IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) | ACCEPTANCE OF EXTERNAL AUTHENTICATORS Select Select Select 
IA-8 (4) IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) | USE OF DEFINED PROFILES Select Select Select 
OT Discussion: The OT Discussion for IA-2, Identification and Authentication (Organizational 7503 
Users), is applicable for non-organizational users. 7504 
Control Enhancement: (1) OT Discussion: Acceptance of PIV credentials is only required for 7505 
organizations that follow OMB Memorandum M-19-17 [OMB-M1917] (e.g., federal agencies 7506 
and contractors). 7507 
Control Enhancement: (2) (4) OT Discussion: Compensating controls may include implementing 7508 
support that is external to the OT and multi-factor authentication. 7509 
IA-11 RE-AUTHENTICATION 7510 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IA-11 Re-authentication Select Select Select 
OT Discussion: No OT Discussion for this control. 7511 
IA-12 IDENTITY PROOFING 7512 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
IA-12 Identity Proofing  Select Select 
IA-12 (1) IDENTITY PROOFING | SUPERVISOR AUTHORIZATION   Add 
IA-12 (2) IDENTITY PROOFING | IDENTITY EVIDENCE  Select Select 
IA-12 (3) IDENTITY PROOFING | IDENTITY EVIDENCE VALIDATION AND VERIFICATION  Select Select 
IA-12 (4) IDENTITY PROOFING | IN-PERSON VALIDATION AND VERIFICATION   Select 
IA-12 (5) IDENTITY PROOFING | ADDRESS CONFIRMATION  Select Select

<!-- page 266 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
248 
OT Discussion: Identity proofing is likely performed by different departments within the 7513 
organization. Existing organizational systems (e.g., HR or IT processes) should be leveraged to 7514 
perform this control.  7515 
Control Enhancement: (1) OT Discussion: Maintenance, engineering, or third-party 7516 
organizations may require OT access in order to support operations. The organization should 7517 
determine the AO for proving identity prior to allowing access to the OT environment. Consider 7518 
obtaining supervisor or sponsor authorization, where the sponsor may be someone within 7519 
operations.  7520 
Control Enhancement: (2) (3) (4) (5) OT Discussion: If the organization already performs these 7521 
controls, existing organizational processes should be leveraged. For example, HR may provide a 7522 
system for tracking identity evidence. OT does not need to develop an independent system for 7523 
achieving this control.  7524 
Rationale for adding IA-12 (1) to HIGH baseline: A supervisor or sponsor should be made aware 7525 
of any access that an employee has to the OT environment since unauthorized or accidental 7526 
access could affect the physical process.  7527 
E.7.8. INCIDENT RESPONSE – IR 7528 
E.7.8.7. Tailoring Considerations for the Incident Response Family  7529 
The automated mechanisms used to support the tracking of security incidents are typically not 7530 
part of or connected to the OT.  7531 
IR-1 POLICY AND PROCEDURES  7532 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IR-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7533 
and the relationship to non-OT systems. 7534 
IR-2 INCIDENT RESPONSE TRAINING 7535 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IR-2 Incident Response Training Select Select Select 
IR-2 (1) INCIDENT RESPONSE TRAINING | SIMULATED EVENTS   Select 
IR-2 (2) INCIDENT RESPONSE TRAINING | AUTOMATED TRAINING ENVIRONMENTS   Select 
OT Discussion: No OT Discussion for this control. 7536

<!-- page 267 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
249 
IR-3 INCIDENT RESPONSE TESTING 7537 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IR-3 Incident Response Testing  Select Select 
IR-3 (2) INCIDENT RESPONSE TESTING | COORDINATION WITH RELATED PLANS  Select Select 
OT Discussion: No OT Discussion for this control. 7538 
IR-4 INCIDENT HANDLING 7539 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IR-4 Incident Handling Select Select Select 
IR-4 (1) INCIDENT HANDLING | AUTOMATED INCIDENT HANDLING PROCESSES  Select Select 
IR-4 (4) INCIDENT HANDLING | INFORMATION CORRELATION   Select 
IR-4 (11) INCIDENT HANDLING | INTEGRATED INCIDENT RESPONSE TEAM   Select 
OT Discussion: As part of the incident handling capability, the organization coordinates with 7540 
external vendors, integrators, or suppliers as necessary to ensure that they have the capability 7541 
to address events that are specific to embedded components and devices.  7542 
Control Enhancement: (1) (4) (11) No OT Discussion for this control.  7543 
IR-5 INCIDENT MONITORING  7544 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IR-5 Incident Monitoring Select Select Select 
IR-5 (1) INCIDENT MONITORING | AUTOMATED TRACKING, DATA COLLECTION, AND ANALYSIS   Select 
OT Discussion: No OT Discussion for this control. 7545 
IR-6 INCIDENT REPORTING  7546 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IR-6 Incident Reporting Select Select Select 
IR-6 (1) INCIDENT REPORTING | AUTOMATED REPORTING  Select Select

<!-- page 268 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
250 
IR-6 (3) INCIDENT REPORTING | SUPPLY CHAIN COORDINATION  Select Select 
OT Discussion: The organization should report incidents on a timely basis. CISA collaborates 7547 
with international and private-sector computer emergency response teams (CERTs) to share 7548 
control systems-related security incidents and mitigation measures. 7549 
Control Enhancement: (1) OT Discussion: The automated mechanisms used to support the 7550 
incident reporting process are not necessarily part of or connected to the OT.  7551 
Control Enhancement: (3) No OT Discussion for this control.  7552 
IR-7 INCIDENT RESPONSE ASSISTANCE  7553 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IR-7 Incident Response Assistance Select Select Select 
IR-7 (1) INCIDENT RESPONSE ASSISTANCE | AUTOMATION SUPPORT FOR AVAILABILITY OF INFORMATION AND SUPPORT  Select Select 
OT Discussion: No OT Discussion for this control.  7554 
IR-8 INCIDENT RESPONSE PLAN 7555 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
IR-8 Incident Response Plan Select Select Select 
OT Discussion: No OT Discussion for this control.  7556 
E.7.9. MAINTENANCE – MA 7557 
E.7.9.8. Tailoring Considerations for the Maintenance Family  7558 
The automated mechanisms used to schedule, conduct, and document maintenance and 7559 
repairs are not necessarily part of or connected to the OT.  7560 
When the OT cannot support the specific maintenance requirements of a control, the 7561 
organization employs compensating controls in accordance with the general tailoring guidance. 7562 
Examples of compensating controls are given with each control as appropriate.  7563

<!-- page 269 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
251 
MA-1 POLICY AND PROCEDURES  7564 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
MA-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7565 
and the relationship to non-OT systems.  7566 
MA-2 CONTROLLED MAINTENANCE  7567 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
MA-2 Controlled Maintenance Select Select Select 
MA-2 (2) CONTROLLED MAINTENANCE | AUTOMATED MAINTENANCE ACTIVITIES   Select 
OT Discussion: No OT Discussion for this control.  7568 
MA-3 MAINTENANCE TOOLS  7569 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
MA-3 Maintenance Tools  Select Select 
MA-3 (1) MAINTENANCE TOOLS | INSPECT TOOLS  Select Select 
MA-3 (2) MAINTENANCE TOOLS | INSPECT MEDIA  Select Select 
MA-3 (3) MAINTENANCE TOOLS | PREVENT UNAUTHORIZED REMOVAL  Select Select 
OT Discussion: No OT Discussion for this control.  7570 
MA-4 NONLOCAL MAINTENANCE 7571 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
MA-4 Nonlocal Maintenance Select Select Select 
MA-4 (1) NONLOCAL MAINTENANCE | LOGGING AND REVIEW  Add Add 
MA-4 (3) NONLOCAL MAINTENANCE | COMPARABLE SECURITY AND SANITIZATION   Select 
OT Discussion: No OT Discussion for this control.  7572 
Control Enhancement: (1) No OT Discussion for this control.  7573

<!-- page 270 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
252 
Control Enhancement: (3) OT Discussion: The organization may need access to nonlocal 7574 
maintenance and diagnostic services in order to restore essential OT operations or services. 7575 
Example compensating controls include limiting the extent of the maintenance and diagnostic 7576 
services to the minimum essential activities and carefully monitoring and auditing the nonlocal 7577 
maintenance and diagnostic activities.  7578 
Rationale for adding MA-4 (1) to MOD and HIGH baselines: OT environments often depend on 7579 
nonlocal maintenance providers, so organizations should have the ability to review logs about 7580 
relevant maintenance activities.  7581 
MA-5 MAINTENANCE PERSONNEL  7582 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
MA-5 Maintenance Personnel Select Select Select 
MA-5 (1) MAINTENANCE PERSONNEL | INDIVIDUALS WITHOUT APPROPRIATE ACCESS   Select 
OT Discussion: No OT Discussion for this control. 7583 
MA-6 TIMELY MAINTENANCE  7584 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
MA-6 Timely Maintenance  Select Select 
OT Discussion: No OT Discussion for this control. 7585 
MA-7 FIELD MAINTENANCE  7586 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
MA-7 Field Maintenance Add Add Add 
OT Discussion: Organizations identify OT systems and system components with specific 7587 
calibration, maintenance, or other requirements and limit maintenance to specific facilities. 7588 
Some examples may include safety-critical systems or systems involved in custody transfer 7589 
where accuracy tolerances are limited and additional quality control checks are required. 7590 
Rationale for adding MA-7 to LOW, MOD, and HIGH baselines: Some OT equipment have 7591 
specific requirements for calibration, maintenance, and modification to meet regulatory or 7592 
safety standards. Different deployed locations may impact the quality and precision of field 7593 
maintenance.  7594

<!-- page 271 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
253 
E.7.10. MEDIA PROTECTION – MP 7595 
MP-1 POLICY AND PROCEDURES 7596 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
MP-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7597 
and the relationship to non-OT systems. 7598 
MP-2 MEDIA ACCESS 7599 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
MP-2 Media Access Select Select Select 
OT Discussion: No OT Discussion for this control. 7600 
MP-3 MEDIA MARKING 7601 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
MP-3 Media Marking  Select Select 
OT Discussion: No OT Discussion for this control. 7602 
MP-4 MEDIA STORAGE 7603 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
MP-4 Media Storage  Select Select 
OT Discussion: No OT Discussion for this control. 7604 
MP-5 MEDIA TRANSPORT 7605 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
MP-5 Media Transport  Select Select 
OT Discussion: No OT Discussion for this control. 7606

<!-- page 272 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
254 
MP-6 MEDIA SANITIZATION 7607 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
MP-6 Media Sanitization Select Select Select 
MP-6 (1) MEDIA SANITIZATION | REVIEW, APPROVE, TRACK, DOCUMENT, AND VERIFY   Select 
MP-6 (2) MEDIA SANITIZATION | EQUIPMENT TESTING   Select 
MP-6 (3) MEDIA SANITIZATION | NONDESTRUCTIVE TECHNIQUES   Select 
OT Discussion: No OT Discussion for this control. 7608 
MP-7 MEDIA USE 7609 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
MP-7 Media Use Select Select Select 
OT Discussion: No OT Discussion for this control. 7610 
E.7.11. PHYSICAL AND ENVIRONMENTAL PROTECTION – PE 7611 
E.7.11.9. Tailoring Considerations for the Physical and Environmental Protection Family 7612 
Physical and environmental protections are often used as a compensating control for many OT 7613 
systems, so physical and environmental protection controls are especially important. Any 7614 
selected compensating control mitigates risk to an acceptable level. 7615 
PE-1 POLICY AND PROCEDURES 7616 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7617 
and the relationship to non-OT systems. The OT components can be distributed over a large 7618 
facility footprint or geographic area and can be an entry point into the entire organizational 7619 
network OT. Regulatory controls may also apply. 7620

<!-- page 273 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
255 
PE-2 PHYSICAL ACCESS AUTHORIZATIONS 7621 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-2 Physical Access Authorizations Select Select Select 
OT Discussion: No OT Discussion for this control. 7622 
PE-3 PHYSICAL ACCESS CONTROL 7623 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-3 Physical Access Control Select Select Select 
PE-3 (1) PHYSICAL ACCESS CONTROL | SYSTEM ACCESS   Select 
OT Discussion: The organization considers OT safety and security interdependencies and access 7624 
requirements in emergency situations. During an emergency, the organization may restrict 7625 
access to OT facilities and assets to authorized individuals only. OT systems are often 7626 
constructed of devices that do not have or cannot use comprehensive access control 7627 
capabilities due to time-restrictive safety constraints. Physical access controls and defense-in-7628 
depth measures are used by the organization when necessary and possible to supplement OT 7629 
security when electronic mechanisms are unable to fulfill the security requirements of the 7630 
organization’s security plan. 7631 
Control Enhancement: (1) No OT Discussion for this control. 7632 
PE-4 ACCESS CONTROL FOR TRANSMISSION 7633 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-4 Access Control for Transmission  Select Select 
OT Discussion: No OT Discussion for this control. 7634 
PE-5 ACCESS CONTROL FOR OUTPUT DEVICES 7635 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-5 Access Control for Output Devices  Select Select 
OT Discussion: No OT Discussion for this control. 7636

<!-- page 274 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
256 
PE-6 MONITORING PHYSICAL ACCESS 7637 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
PE-6 Monitoring Physical Access Select Select Select 
PE-6 (1) MONITORING PHYSICAL ACCESS | INTRUSION ALARMS AND SURVEILLANCE EQUIPMENT  Select Select 
PE-6 (4) MONITORING PHYSICAL ACCESS | MONITORING PHYSICAL ACCESS TO SYSTEMS  Add Select 
OT Discussion: No OT Discussion for this control. 7638 
Control Enhancement: (1) (4) No OT Discussion for this control. 7639 
Rationale for adding PE-6 (4) to MOD baseline: Many of the OT components are in remote 7640 
geographical and dispersed locations. Other components may be in ceilings, floors, or 7641 
distribution closets. Furthermore, physical access controls are frequently used as compensating 7642 
controls when devices lack the ability to enforce logical access restrictions.  7643 
PE-8 VISITOR ACCESS RECORDS 7644 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-8 Visitor Access Records Select Select Select 
PE-8 (1) VISITOR ACCESS RECORDS | AUTOMATED RECORDS MAINTENANCE AND REVIEW   Select 
OT Discussion: No OT Discussion for this control. 7645 
PE-9 POWER EQUIPMENT AND CABLING 7646 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-9 Power Equipment and Cabling  Select Select 
OT Discussion: No OT Discussion for this control. 7647 
PE-10 EMERGENCY SHUTOFF 7648 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-10 Emergency Shutoff  Select Select 
OT Discussion: It may not be possible or advisable to shut off power to some OT. The 7649 
organizational-defined parameters for this control should be implemented in consultation with 7650

<!-- page 275 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
257 
safety and operational personnel. Example compensating controls include failing to a known 7651 
state and emergency procedures.  7652 
PE-11 EMERGENCY POWER 7653 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
PE-11 Emergency Power  Select Select 
PE-11 (1) EMERGENCY POWER | ALTERNATE POWER SUPPLY - MINIMAL OPERATIONAL CAPABILITY   Select 
PE-11 (2) EMERGENCY POWER | ALTERNATE POWER SUPPLY - SELF-CONTAINED    
OT Discussion: No OT Discussion for this control. 7654 
PE-12 EMERGENCY LIGHTING 7655 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-12 Emergency Lighting Select Select Select 
OT Discussion: No OT Discussion for this control. 7656 
PE-13 FIRE PROTECTION 7657 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-13 Fire Protection Select Select Select 
PE-13 (1) FIRE PROTECTION | DETECTION SYSTEMS – AUTOMATIC ACTIVATION AND NOTIFICATION  Select Select 
PE-13 (2) FIRE PROTECTION | SUPPRESSION SYSTEMS – AUTOMATIC ACTIVATION AND NOTIFICATION   Select 
OT Discussion: Fire suppression mechanisms should take the OT environment into account (e.g., 7658 
water sprinkler systems could be hazardous in specific environments). 7659 
Control Enhancement: (1) (2) No OT Discussion for this control. 7660 
PE-14 ENVIRONMENTAL CONTROLS 7661 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-14 Environmental Controls Select Select Select

<!-- page 276 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
258 
OT Discussion: Temperature and humidity controls are typically components of other OT 7662 
systems (e.g., HVAC, process, or lighting systems) or can be a stand-alone and unique OT 7663 
system. OT can operate in extreme environments and both interior and exterior locations. For a 7664 
specific OT, the temperature and humidity design and operational parameters dictate the 7665 
performance specifications. Power circuits, distribution closets, routers, and switches that 7666 
support fire protection and life safety systems must be maintained at the proper temperature 7667 
and humidity. When environmental controls cannot be implemented, use hardware that is 7668 
engineered to withstand the OT’s unique environmental hazards. 7669 
PE-15 WATER DAMAGE PROTECTION 7670 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-15 Water Damage Protection Select Select Select 
PE-15 (1) WATER DAMAGE PROTECTION | AUTOMATION SUPPORT   Select 
OT Discussion: Water damage protection and the use of shutoff and isolation valves are 7671 
procedural actions and specific types of OT. OT used in the manufacturing, hydropower, 7672 
transportation/navigation, water, and wastewater industries rely on the movement of water 7673 
and are specifically designed to manage the quantity, flow, and pressure of water. Power 7674 
circuits, distribution closets, routers, and switches that support fire protection and life safety 7675 
systems should ensure that water will not disable the system (e.g., a fire that activates the 7676 
sprinkler system does not spray onto the fire control servers, routers, or switches or short out 7677 
the alarms, egress systems, emergency lighting, or suppression systems). 7678 
Control Enhancement: (1) No OT Discussion for this control. 7679 
PE-16 DELIVERY AND REMOVAL 7680 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-16 Delivery and Removal Select Select Select 
OT Discussion: No OT Discussion for this control. 7681 
PE-17 ALTERNATE WORK SITE 7682 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-17 Alternate Work Site  Select Select 
OT Discussion: No OT Discussion for this control. 7683

<!-- page 277 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
259 
PE-18 LOCATION OF SYSTEM COMPONENTS 7684 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-18 Location of System Components   Select 
OT Discussion: No OT Discussion for this control. 7685 
PE-21 ELECTROMAGNETIC PULSE PROTECTION 7686 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PE-21 Electromagnetic Pulse Protection    
OT Discussion: Organizations that manage OT equipment may choose to use EMP protection to 7687 
prevent electromagnetic threats from adversaries or the environment. Organizations may 7688 
select to follow National Coordinating Center for Communications (NCC) guidelines on EM pulse 7689 
protection. 7690 
PE-22 COMPONENT MARKING 7691 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
PE-22 Component Marking  Add Add 
OT Discussion: Hardware components are marked or labeled to indicate information that is 7692 
processed, stored, or transmitted. Component markings can be useful for differentiating 7693 
between safety and control systems, OT and IT equipment, and internally and externally 7694 
connected systems. Marking components reduces the probability of mismanaging the system 7695 
or performing maintenance on an incorrect device.  7696 
Rationale for adding PE-22 to MOD and HIGH baselines: OT is unique in that it may look like an 7697 
IT component but perform a very different function. Visible differentiation between 7698 
components that perform different functions can help reduce reliability incidents due to 7699 
maintenance errors.  7700

<!-- page 278 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
260 
E.7.12. PLANNING – PL 7701 
PL-1 POLICY AND PROCEDURES 7702 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PL-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7703 
and the relationship to non-OT systems. 7704 
PL-2 SYSTEM SECURITY AND PRIVACY PLANS 7705 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PL-2 System Security and Privacy Plans Select Select Select 
OT Discussion: When systems are highly interconnected, coordinated planning is essential. A 7706 
low-impact system could adversely affect a higher-impact system. 7707 
PL-4 RULES OF BEHAVIOR 7708 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PL-4 Rules of Behavior Select Select Select 
PL-4 (1) RULES OF BEHAVIOR | SOCIAL MEDIA AND EXTERNAL SITE / APPLICATION USAGE RESTRICTIONS Select Select Select 
OT Discussion: No OT Discussion for this control. 7709 
PL-7 CONCEPT OF OPERATIONS 7710 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
PL-7 Concept of Operations    
OT Discussion: Organizations need to document known operational procedures and explore 7711 
how they relate to the combination of IT and OT technologies within the environment. 7712

<!-- page 279 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
261 
PL-8 SECURITY AND PRIVACY ARCHITECTURES 7713 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
PL-8 Security and Privacy Architectures  Select Select 
PL-8 (1) SECURITY AND PRIVACY ARCHITECTURES | DEFENSE IN DEPTH    
OT Discussion: No OT Discussion for this control. 7714 
Control Enhancement: (1) OT Discussion: Defense in depth is considered a common practice for 7715 
security architecture within OT environments. 7716 
PL-9 CENTRAL MANAGEMENT 7717 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PL-9 Central Management    
OT Discussion: If the architecture allows for it, consider centrally managing flaw remediation, 7718 
malicious code protection, logging, and incident detection. 7719 
PL-10 BASELINE SELECTION 7720 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PL-10 Baseline Selection Select Select Select 
OT Discussion: No OT Discussion for this control. 7721 
PL-11 BASELINE TAILORING 7722 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PL-11 Baseline Tailoring Select Select Select 
OT Discussion: No OT Discussion for this control.  7723

<!-- page 280 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
262 
E.7.13. ORGANIZATION-WIDE INFORMATION SECURITY PROGRAM MANAGEMENT CONTROLS 7724 
– PM 7725 
E.7.13.10. Characteristics of the Organization-Wide Information Security Program 7726 
Management Control Family 7727 
Organization-wide information security program management controls are deployed to support 7728 
the information security program. They are not associated with control baselines and are 7729 
independent of any system impact level. 7730 
Program management controls should specifically address the unique properties and 7731 
requirements of OT, the relationship to non-OT systems, and the relationship to other 7732 
programs concerned with the operational characteristics of OT (e.g., safety, efficiency, 7733 
reliability, resilience). To achieve this, the security program should utilize interdisciplinary 7734 
teams that can help reconcile and balance conflicting equities, objectives, and responsibilities, 7735 
such as capability, adaptability, resilience, safety, security, usability, and efficiency. 7736 
PM-1 INFORMATION SECURITY PROGRAM PLAN 7737 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-1 Information Security Program Plan 
OT Discussion: No OT Discussion for this control. 7738 
PM-2 INFORMATION SECURITY PROGRAM LEADERSHIP ROLE 7739 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-2 Information Security Program Leadership Role 
OT Discussion: No OT Discussion for this control. 7740 
PM-3 INFORMATION SECURITY AND PRIVACY RESOURCES 7741 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-3 Information Security and Privacy Resources 
OT Discussion: No OT Discussion for this control.  7742

<!-- page 281 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
263 
PM-4 PLAN OF ACTION AND MILESTONES PROCESS 7743 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-4 Plan of Action and Milestones Process 
OT Discussion: No OT Discussion for this control. 7744 
PM-5 SYSTEM INVENTORY 7745 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-5 System Inventory 
OT Discussion: No OT Discussion for this control. 7746 
PM-6 MEASURES OF PERFORMANCE 7747 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-6 Measures of Performance 
OT Discussion: No OT Discussion for this control. 7748 
PM-7 ENTERPRISE ARCHITECTURE 7749 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-7 Enterprise Architecture 
OT Discussion: No OT Discussion for this control. 7750 
PM-8 CRITICAL INFRASTRUCTURE PLAN 7751 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-8 Critical Infrastructure Plan 
OT Discussion: Organizations should be familiar with the protection requirements and guidance 7752 
defined by Executive Orders, government sector-specific agencies (SSAs), and industry trade 7753 
organizations.  7754

<!-- page 282 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
264 
PM-9 RISK MANAGEMENT STRATEGY 7755 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-9 Risk Management Strategy 
OT Discussion: No OT Discussion for this control. 7756 
PM-10 AUTHORIZATION PROCESS 7757 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-10 Authorization Process 
OT Discussion: No OT Discussion for this control. 7758 
PM-11 MISSION AND BUSINESS PROCESS DEFINITION 7759 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-11 Mission and Business Process Definition 
OT Discussion: No OT Discussion for this control. 7760 
PM-12 INSIDER THREAT PROGRAM 7761 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-12 Insider Threat Program 
OT Discussion: No OT Discussion for this control. 7762 
PM-13 SECURITY AND PRIVACY WORKFORCE 7763 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-13 Security and Privacy Workforce 
OT Discussion: No OT Discussion for this control.  7764

<!-- page 283 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
265 
PM-14 TESTING, TRAINING, AND MONITORING 7765 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-14 Testing, Training, and Monitoring 
OT Discussion: No OT Discussion for this control. 7766 
PM-15 SECURITY AND PRIVACY GROUPS AND ASSOCIATIONS 7767 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-15 Security and Privacy Groups and Associations 
OT Discussion: Organizations should be familiar with relevant security-focused and industry-7768 
specific groups or associations, including government SSAs, ISACs, and industry trade 7769 
organizations. 7770 
PM-16 THREAT AWARENESS PROGRAM 7771 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-16 Threat Awareness Program 
OT Discussion: The organization should collaborate and share information about potential 7772 
incidents on a timely basis. CISA serves as a centralized location for coordinating and 7773 
integrating the operational elements involved in cybersecurity and communications reliance. 7774 
Organizations should consider having both an unclassified and classified information sharing 7775 
capability. 7776 
PM-17 PROTECTING CONTROLLED UNCLASSIFIED INFORMATION ON EXTERNAL SYSTEMS 7777 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-17 Protecting Controlled Unclassified Information on External Systems 
OT Discussion: This control applies to federal agencies and other organizations that support the 7778 
Government and process controlled unclassified information (CUI). 7779

<!-- page 284 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
266 
PM-18 PRIVACY PROGRAM PLAN 7780 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-18 Privacy Program Plan 
OT Discussion: No OT Discussion for this control. 7781 
PM-19 PRIVACY PROGRAM LEADERSHIP ROLE 7782 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-19 Privacy Program Leadership Role 
OT Discussion: No OT Discussion for this control. 7783 
PM-20 DISSEMINATION OF PRIVACY PROGRAM INFORMATION 7784 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-20 Dissemination of Privacy Program Information 
PM-20 (1) DISSEMINATION OF PRIVACY PROGRAM INFORMATION | PRIVACY POLICIES ON WEBSITES, APPLICATIONS, AND DIGITAL SERVICES 
OT Discussion: No OT Discussion for this control. 7785 
PM-21 ACCOUNTING OF DISCLOSURES 7786 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-21 Accounting of Disclosures 
OT Discussion: No OT Discussion for this control. 7787 
PM-22 PERSONALLY IDENTIFIABLE INFORMATION QUALITY MANAGEMENT 7788 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-22 Personally Identifiable Information Quality Management 
OT Discussion: No OT Discussion for this control. 7789

<!-- page 285 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
267 
PM-23 DATA GOVERNANCE BODY 7790 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-23 Data Governance Body 
OT Discussion: No OT Discussion for this control.  7791 
PM-24 DATA INTEGRITY BOARD 7792 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-24 Data Integrity Board 
OT Discussion: No OT Discussion for this control. 7793 
PM-25 MINIMIZATION OF PERSONALLY IDENTIFIABLE INFORMATION USED IN TESTING, 7794 
TRAINING, AND RESEARCH 7795 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-25 Minimization of Personally Identifiable Information Used in Testing, Training, and Research  
OT Discussion: No OT Discussion for this control. 7796 
PM-26 COMPLAINT MANAGEMENT 7797 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-26 Complaint Management 
OT Discussion: No OT Discussion for this control. 7798 
PM-27 PRIVACY REPORTING 7799 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-27 Privacy Reporting 
OT Discussion: No OT Discussion for this control. 7800

<!-- page 286 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
268 
PM-28 RISK FRAMING 7801 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-28 Risk Framing 
OT Discussion: No OT Discussion for this control. 7802 
PM-29 RISK MANAGEMENT PROGRAM LEADERSHIP ROLES 7803 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-29 Risk Management Program Leadership Roles 
OT Discussion: No OT Discussion for this control. 7804 
PM-30 SUPPLY CHAIN RISK MANAGEMENT STRATEGY 7805 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-30 Supply Chain Risk Management Strategy 
PM-30 (1) SUPPLY CHAIN RISK MANAGEMENT STRATEGY | SUPPLIERS OF CRITICAL OR MISSION-ESSENTIAL ITEMS 
OT Discussion: No OT Discussion for this control. 7806 
PM-31 CONTINUOUS MONITORING STRATEGY 7807 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-31 Continuous Monitoring Strategy 
OT Discussion: No OT Discussion for this control. 7808 
PM-32 PURPOSING 7809 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
PM-32 Purposing 
OT Discussion: No OT Discussion for this control.  7810

<!-- page 287 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
269 
E.7.14. PERSONNEL SECURITY – PS 7811 
E.7.14.11. Tailoring Considerations for the Personnel Security Family 7812 
Personnel security controls require collaboration between OT, IT, security, and HR personnel. 7813 
PS-1 POLICY AND PROCEDURES 7814 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PS-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7815 
and the relationship to non-OT systems. 7816 
PS-2 POSITION RISK DESIGNATION 7817 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PS-2 Position Risk Designation Select Select Select 
OT Discussion: Private organizations should utilize existing sector-specific regulations, laws, 7818 
policy, and guidance for determining appropriate risk designations for positions. 7819 
PS-3 PERSONNEL SCREENING 7820 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PS-3 Personnel Screening Select Select Select 
OT Discussion: No OT Discussion for this control. 7821 
PS-4 PERSONNEL TERMINATION 7822 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PS-4 Personnel Termination Select Select Select 
PS-4 (2) PERSONNEL TERMINATION | AUTOMATED ACTIONS   Select 
OT Discussion: No OT Discussion for this control.  7823

<!-- page 288 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
270 
PS-5 PERSONNEL TRANSFER 7824 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PS-5 Personnel Transfer Select Select Select 
OT Discussion: No OT Discussion for this control. 7825 
PS-6 ACCESS AGREEMENTS 7826 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PS-6 Access Agreements Select Select Select 
OT Discussion: No OT Discussion for this control. 7827 
PS-7 EXTERNAL PERSONNEL SECURITY 7828 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PS-7 External Personnel Security Select Select Select 
No OT Discussion for this control. 7829 
PS-8 PERSONNEL SANCTIONS 7830 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PS-8 Personnel Sanctions Select Select Select 
No OT Discussion for this control. 7831 
PS-9 POSITION DESCRIPTIONS 7832 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
PS-9 Position Descriptions Select Select Select 
No OT Discussion for this control.  7833

<!-- page 289 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
271 
E.7.15. RISK ASSESSMENT – RA 7834 
Many OT organizations have well-established risk assessment programs that can be leveraged 7835 
for cybersecurity risk analysis. 7836 
RA-1 POLICY AND PROCEDURES 7837 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
RA-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7838 
and the relationship to non-OT systems. 7839 
RA-2 SECURITY CATEGORIZATION 7840 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
RA-2 Security Categorization Select Select Select 
OT Discussion: PHA, functional safety assessments, and other organization-established risk 7841 
assessments can be referenced to identify the impact level of the OT systems. 7842 
RA-3 RISK ASSESSMENT 7843 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
RA-3 Risk Assessment Select Select Select 
RA-3 (1) RISK ASSESSMENT | SUPPLY CHAIN RISK ASSESSMENT Select Select Select 
OT Discussion: No OT Discussion for this control. 7844 
RA-5 VULNERABILITY MONITORING AND SCANNING 7845 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
RA-5 Vulnerability Monitoring and Scanning Select Select Select 
RA-5 (2) VULNERABILITY MONITORING AND SCANNING | UPDATE VULNERABILITIES TO BE SCANNED Select Select Select 
RA-5 (4) VULNERABILITY MONITORING AND SCANNING | DISCOVERABLE INFORMATION   Select 
RA-5 (5) VULNERABILITY MONITORING AND SCANNING | PRIVILEGED ACCESS  Select Select

<!-- page 290 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
272 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
RA-5 (11) VULNERABILITY MONITORING AND SCANNING | PUBLIC DISCLOSURE PROGRAM Select Select Select 
OT Discussion: The organization makes a risk-based determination about how to monitor or 7846 
scan its system for vulnerabilities. This may include active scanning, passive monitoring, or 7847 
compensating controls, depending on the system being scanned. For example, vulnerability 7848 
examination may be performed using passive monitoring and manual visual inspection to 7849 
maintain an up-to-date inventory of assets. That inventory can be cross-referenced against a list 7850 
of known vulnerabilities (e.g., CISA advisories, NIST NVD). Production may need to be taken 7851 
offline before active scans can be conducted. Scans are scheduled to occur during planned OT 7852 
outages whenever possible. If vulnerability scanning tools are used on adjacent non-OT 7853 
networks, extra care is taken to ensure that they do not mistakenly scan the OT network. 7854 
Automated network scanning is not applicable to non-routable communications, such as serial 7855 
networks. Compensating controls include providing a replicated or simulated system for 7856 
conducting scans or host-based vulnerability applications. 7857 
Control Enhancement: (2) (5) No OT Discussion for this control.  7858 
Control Enhancement: (4) OT Discussion: Examples of discoverable information in OT could 7859 
include information about key personnel or technical information related to systems and 7860 
configurations. Locations that may need to be monitored or scanned include technical forums, 7861 
blogs, and vendor or contractor websites.  7862 
Control Enhancement: (11) OT Discussion: For federal organizations, CISA Binding Operational 7863 
Directive 20-01 requires individual federal civilian executive branch agencies to develop and 7864 
publish a vulnerability disclosure policy (VDP) for their internet-accessible systems and services 7865 
and maintain processes to support their VDP. A VDP may be implemented at the organization 7866 
level rather than for each individual system. Federal and non-federal organizations could 7867 
achieve this control by creating and monitoring an email address published on a public-facing 7868 
website for contacting the organization regarding disclosures.  7869 
RA-7 RISK RESPONSE  7870 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
RA-7 Risk Response Select Select Select 
OT Discussion: No OT Discussion for this control. 7871

<!-- page 291 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
273 
RA-9 CRITICALITY ANALYSIS 7872 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
RA-9 Criticality Analysis  Select Select 
OT Discussion: No OT Discussion for this control. 7873 
E.7.16. SYSTEM AND SERVICES ACQUISITION – SA 7874 
E.7.16.12. Tailoring Considerations for the System and Services Acquisition Family 7875 
If the OT cannot support the specific system and services acquisition requirements of a control, 7876 
the organization employs compensating controls in accordance with the general tailoring 7877 
guidance. Examples of compensating controls are given with each control as appropriate. 7878 
SA-1 POLICY AND PROCEDURES 7879 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7880 
and the relationship to non-OT systems. 7881 
SA-2 ALLOCATION OF RESOURCES 7882 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-2 Allocation of Resources Select Select Select 
OT Discussion: No OT Discussion for this control. 7883 
SA-3 SYSTEM DEVELOPMENT LIFE CYCLE 7884 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-3 System Development Life Cycle Select Select Select 
SA-3 (1) SYSTEM DEVELOPMENT LIFE CYCLE | MANAGE PREPRODUCTION ENVIRONMENT    
SA-3 (3) SYSTEM DEVELOPMENT LIFE CYCLE | TECHNOLOGY REFRESH

<!-- page 292 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
274 
OT Discussion: No OT Discussion for this control. 7885 
Control Enhancements: (1) OT Discussion: Organizations that do not maintain local pre-7886 
production environments and utilize a third-party integrator should ensure that contracts are 7887 
developed to limit security and privacy risks. 7888 
Control Enhancements: (3) OT Discussion: Many OT systems have an expected life cycle that is 7889 
longer than most IT components. Technology refresh is addressed in budget planning to limit 7890 
the use of obsolete systems that present security or reliability risks. 7891 
SA-4 ACQUISITION PROCESS 7892 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SA-4 Acquisition Process Select Select Select 
SA-4 (1) ACQUISITION PROCESS | FUNCTIONAL PROPERTIES OF CONTROLS  Select Select 
SA-4 (2) ACQUISITION PROCESS | DESIGN AND IMPLEMENTATION INFORMATION FOR CONTROLS  Select Select 
SA-4 (5) ACQUISITION PROCESS | SYSTEM, COMPONENT, AND SERVICE CONFIGURATIONS   Select 
SA-4 (9) ACQUISITION PROCESS | FUNCTIONS, PORTS, PROTOCOLS, AND SERVICES IN USE  Select Select 
SA-4 (10) ACQUISITION PROCESS | USE OF APPROVED PIV PRODUCTS Select Select Select 
SA-4 (12) ACQUISITION PROCESS | DATA OWNERSHIP Add Add Add 
OT Discussion: Organizations engage with OT suppliers to raise awareness of cybersecurity 7893 
needs. The SCADA/Control Systems Procurement Project provides example cybersecurity 7894 
procurement language for OT. 7895 
Control Enhancements: (1) (2) (9) OT Discussion: When acquiring OT products, consideration for 7896 
security requirements may not have been incorporated into the design. Procurement may need 7897 
to consider alternative products or complementary hardware or plan for compensating 7898 
controls. 7899 
Control Enhancement: (10) OT Discussion: The use of approved PIV products is only required for 7900 
organizations that follow OMB Memorandum M-19-17 (e.g., federal agencies and contractors). 7901 
Example compensating controls include employing external products on the FIPS 201-approved 7902 
products list for PIV capabilities in conjunction with OT products.  7903 
Control Enhancement: (5) (12) No OT Discussion for this control. 7904 
Rationale for adding SA-4 (12) to LOW, MOD, and HIGH baselines: Organizationally sensitive or 7905 
proprietary OT data is often provided to contractors for project development or support, so 7906 
data ownership should be defined prior to exchanging data with a vendor or integrator. The 7907 
potential sharing of data with other parties and the potential deletion of the data after project 7908 
completion should be determined. OT systems that are operated by contractors on behalf of 7909

<!-- page 293 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
275 
the organization may be subject to the same requirements (e.g., legal, regulatory) for data 7910 
ownership and retention. 7911 
SA-5 SYSTEM DOCUMENTATION 7912 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-5 System Documentation Select Select Select 
OT Discussion: No OT Discussion for this control. 7913 
SA-8 SECURITY AND PRIVACY ENGINEERING PRINCIPLES 7914 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-8 Security and Privacy Engineering Principles Select Select Select 
OT Discussion: No OT Discussion for this control. 7915 
SA-9 EXTERNAL SYSTEM SERVICES 7916 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-9 External System Services Select Select Select 
SA-9 (2) EXTERNAL SYSTEM SERVICES | IDENTIFICATION OF FUNCTIONS, PORTS, PROTOCOLS, AND SERVICES  Select Select 
OT Discussion: No OT Discussion for this control. 7917 
SA-10 DEVELOPER CONFIGURATION MANAGEMENT 7918 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-10 Developer Configuration Management  Select Select 
OT Discussion: Personnel with knowledge of security and privacy requirements are included in 7919 
the developer’s change management process. 7920 
SA-11 DEVELOPER TESTING AND EVALUATION 7921 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-11 Developer Testing and Evaluation  Select Select

<!-- page 294 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
276 
OT Discussion: No OT Discussion for this control. 7922 
SA-15 DEVELOPMENT PROCESS, STANDARDS, AND TOOLS 7923 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-15 Development Process, Standards, and Tools  Select Select 
SA-15 (3) DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | CRITICALITY ANALYSIS  Select Select 
OT Discussion: No OT Discussion for this control. 7924 
SA-16 DEVELOPER-PROVIDED TRAINING 7925 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-16 Developer-Provided Training    Select 
OT Discussion: No OT Discussion for this control. 7926 
SA-17 DEVELOPER SECURITY AND PRIVACY ARCHITECTURE AND DESIGN 7927 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-17 Developer Security and Privacy Architecture and Design   Select 
OT Discussion: No OT Discussion for this control. 7928 
SA-21 DEVELOPER SCREENING 7929 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-21 Developer Screening   Select 
OT Discussion: No OT Discussion for this control. 7930 
SA-22 UNSUPPORTED SYSTEM COMPONENTS 7931 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SA-22 Unsupported System Components Select Select Select

<!-- page 295 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
277 
OT Discussion: OT systems may contain system components that are no longer supported by 7932 
the developer, vendor, or manufacturer and have not been replaced due to various operational, 7933 
safety, availability, or lifetime constraints. Organizations identify alternative methods to 7934 
continue supporting the operation of such system components and consider additional 7935 
compensating controls to mitigate against known threats and vulnerabilities to unsupported 7936 
system components.  7937 
E.7.17. SYSTEM AND COMMUNICATIONS PROTECTION – SC 7938 
E.7.17.13. Tailoring Considerations for the System and Communications Protection Family 7939 
The use of cryptography is determined after careful consideration of security needs and 7940 
potential ramifications on system performance. For example, the organization considers 7941 
whether latency induced from the use of cryptography would adversely impact the operational 7942 
performance of the OT. While the legacy devices commonly found within OT often lack direct 7943 
support for cryptographic functions, compensating controls (e.g., encapsulations) may be used 7944 
to meet the intent of the control.  7945 
When the OT cannot support the specific system and communications protection requirements 7946 
of a control, the organization employs compensating controls in accordance with the general 7947 
tailoring guidance. Examples of compensating controls are given with each control as 7948 
appropriate.  7949 
SC-1 POLICY AND PROCEDURES  7950 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 7951 
and the relationship to non-OT systems. 7952 
SC-2 SEPARATION OF SYSTEM AND USER FUNCTIONALITY 7953 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-2 Separation of System and User Functionality  Select Select 
OT Discussion: Physical separation includes using separate systems for managing the OT and for 7954 
operating OT components. Logical separation includes the use of different user accounts for 7955 
administrative and operator privileges. Example compensating controls include providing 7956 
increased auditing measures. 7957

<!-- page 296 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
278 
SC-3 SECURITY FUNCTION ISOLATION 7958 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-3 Security Function Isolation   Select 
OT Discussion: Organizations consider implementing this control when designing new 7959 
architectures or updating existing components. Compensating controls may include access 7960 
controls. 7961 
SC-4 INFORMATION IN SHARED SYSTEM RESOURCES 7962 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-4 Information in Shared System Resources  Select Select 
OT Discussion: This control is especially relevant for OT systems that process confidential data. 7963 
Compensating controls may include engineering use of the OT to prevent sharing system 7964 
resources. 7965 
SC-5 DENIAL- OF-SERVICE PROTECTION 7966 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-5 Denial-of-Service Protection Select Select Select 
OT Discussion: Some OT equipment may be more susceptible to DoS attacks due to the time 7967 
criticality of some OT applications. Risk-based analysis informs the prioritization of DoS 7968 
protection and the establishment of policy and procedure. 7969 
SC-7 BOUNDARY PROTECTION 7970 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SC-7 Boundary Protection Select Select Select 
SC-7 (3) BOUNDARY PROTECTION | ACCESS POINTS  Select Select 
SC-7 (4) BOUNDARY PROTECTION | EXTERNAL TELECOMMUNICATIONS SERVICES  Select Select 
SC-7 (5) BOUNDARY PROTECTION | DENY BY DEFAULT – ALLOW BY EXCEPTION  Select Select 
SC-7 (7) BOUNDARY PROTECTION | SPLIT TUNNELING FOR REMOTE DEVICES  Select Select

<!-- page 297 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
279 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SC-7 (8) BOUNDARY PROTECTION | ROUTE TRAFFIC TO AUTHENTICATED PROXY SERVERS  Select Select 
SC-7 (18) BOUNDARY PROTECTION | FAIL SECURE  Add Select 
SC-7 (21) BOUNDARY PROTECTION | ISOLATION OF SYSTEM COMPONENTS   Select 
SC-7 (28) BOUNDARY PROTECTION | CONNECTIONS TO PUBLIC NETWORKS Add Add Add 
SC-7 (29) BOUNDARY PROTECTION | SEPARATE SUBNETS TO ISOLATE FUNCTIONS Add Add Add 
OT Discussion: No OT Discussion for this control. 7971 
Control Enhancement: (3) (4) (5) (7) (8) (21) No OT discussion for this control. 7972 
Control Enhancement: (18) OT Discussion: The organization selects an appropriate failure mode 7973 
(e.g., permit or block all communications). 7974 
Control Enhancement: (28) OT Discussion: Organizations consider the need for a direct 7975 
connection to a public network for each OT system, including potential benefits, additional 7976 
threat vectors, and potential adverse impacts that are specifically relevant to the type of public 7977 
access that connection introduces. 7978 
Control Enhancement: (29) OT Discussion: Subnets can be used to isolate low-risk functions 7979 
from higher-risk ones and control from safety. Subnets should be considered along with other 7980 
boundary protection technologies.  7981 
Rationale for adding SC-7 (18) to MOD baseline: The ability to choose the failure mode for the 7982 
physical part of the OT differentiates the OT from other IT systems. This choice may be a 7983 
significant influence in mitigating the impact of a failure.  7984 
Rationale for adding SC-7 (28) to LOW, MOD, and HIGH baselines: Access to OT should be 7985 
restricted to the individuals required for operation. A connection made from the OT directly to 7986 
a public network has limited applicability in OT environments but significant potential risk.  7987 
Rationale for adding SC-7 (29) to LOW, MOD, and HIGH baselines: In OT environments, subnets 7988 
and zoning are common practices for isolating functions.  7989 
SC-8 TRANSMISSION CONFIDENTIALITY AND INTEGRITY  7990 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-8 Transmission Confidentiality and Integrity  Select Select 
SC-8 (1) TRANSMISSION CONFIDENTIALITY AND INTEGRITY | CRYPTOGRAPHIC PROTECTION  Select Select 
OT Discussion: No OT Discussion for this control.  7991

<!-- page 298 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
280 
Control Enhancement: (1) OT Discussion: When transmitting across untrusted network 7992 
segments, the organization explores all possible cryptographic integrity mechanisms (e.g., 7993 
digital signature, hash function) to protect the confidentiality and integrity of the information. 7994 
Compensating controls may include physical protections, such as a secure conduit (e.g., point-7995 
to-point link) between two system components.  7996 
SC-10 NETWORK DISCONNECT 7997 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-10 Network Disconnect  Remove Remove 
OT Discussion: No OT Discussion for this control. 7998 
Rationale for removing SC-10 from MOD and HIGH baselines: The intent of this control is 7999 
effectively covered by AC-17 (9) for OT systems.  8000 
SC-12 CRYPTOGRAPHIC KEY ESTABLISHMENT AND MANAGEMENT  8001 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-12 Cryptographic Key Establishment and Management  Select Select Select 
SC-12 (1) CRYPTOGRAPHIC KEY ESTABLISHMENT AND MANAGEMENT | AVAILABILITY   Select 
OT Discussion: No OT Discussion for this control. 8002 
SC-13 CRYPTOGRAPHIC PROTECTION 8003 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-13 Cryptographic Protection Select Select Select 
OT Discussion: No OT Discussion for this control.  8004 
SC-15 COLLABORATIVE COMPUTING DEVICES  8005 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-15 Collaborative Computing Devices Select Select Select 
OT Discussion: No OT Discussion for this control.  8006

<!-- page 299 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
281 
SC-17 PUBLIC-KEY INFRASTRUCTURE CERTIFICATES  8007 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-17 Public-Key Infrastructure Certificates  Select Select 
OT Discussion: No OT Discussion for this control. 8008 
SC-18 MOBILE CODE 8009 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-18 Mobile Code  Select Select 
OT Discussion: No OT Discussion for this control.  8010 
SC-20 SECURE NAME/ADDRESS RESOLUTION SERVICE (AUTHORITATIVE SOURCE) 8011 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-20 Secure Name/Address Resolution Service (Authoritative Source) Select Select Select 
OT Discussion: Secure name/address resolution services should be used only after careful 8012 
consideration and verification that they do not adversely affect the OT’s operational 8013 
performance. 8014 
SC-21 SECURE NAME/ADDRESS RESOLUTION SERVICE (RECURSIVE OR CACHING RESOLVER) 8015 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-21 Secure Name/Address Resolution Service (Recursive or Caching Resolver) Select Select Select 
OT Discussion: Secure name/address resolution services should be used only after careful 8016 
consideration and verification that they do not adversely affect the OT’s operational 8017 
performance. 8018 
SC-22 ARCHITECTURE AND PROVISIONING FOR NAME/ADDRESS RESOLUTION SERVICE 8019 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-22 Architecture and Provisioning for Name/Address Resolution Service Select Select Select

<!-- page 300 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
282 
OT Discussion: Secure name/address resolution services should be used only after careful 8020 
consideration and verification that they do not adversely affect the OT’s operational 8021 
performance. 8022 
SC-23 SESSION AUTHENTICITY 8023 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-23 Session Authenticity  Select Select 
OT Discussion: Example compensating controls include auditing measures. 8024 
SC-24 FAIL IN KNOWN STATE 8025 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SC-24 Fail in Known State  Add Select 
OT Discussion: The organization selects an appropriate failure state. Preserving OT state 8026 
information includes consistency among OT state variables and the physical state that the OT 8027 
represents (e.g., whether valves are open or closed, communication permitted or blocked, 8028 
continue operations). 8029 
Rationale for adding SC-24 to MOD baseline: As part of the architecture and design of the OT, 8030 
the organization selects an appropriate failure state in accordance with the function performed 8031 
by the OT and the operational environment. The ability to choose the failure mode for the 8032 
physical part of OT differentiates OT systems from other IT systems. This choice may be a 8033 
significant influence in mitigating the impact of a failure since it may be disruptive to ongoing 8034 
physical processes (e.g., valves failing in closed position may adversely affect system cooling).  8035 
SC-28 PROTECTION OF INFORMATION AT REST 8036 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-28 Protection of Information at Rest  Select Select 
SC-28 (1) PROTECTION OF INFORMATION AT REST |CRYPTOGRAPHIC PROTECTION  Select Select 
OT Discussion: Cryptographic mechanisms are implemented only after careful consideration 8037 
and verification that they do not adversely affect the OT’s operational performance. When 8038 
cryptographic mechanisms are not feasible on certain OT devices, compensating controls may 8039 
include relocating the data to a location that does support cryptographic mechanisms. 8040 
Control Enhancement: (1) No OT Discussion for this control.  8041

<!-- page 301 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
283 
SC-32 SYSTEM PARTITIONING 8042 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-32 System Partitioning    
SC-32 (1) SYSTEM PARTITIONING | SEPARATE PHYSICAL DOMAINS FOR PRIVILEGED FUNCTIONS    
OT Discussion: No OT Discussion for this control. 8043 
Control Enhancement: (1) OT Discussion: Organizations consider separate physical domains for 8044 
privileged functions, such as those that affect security and safety. 8045 
SC-39 PROCESS ISOLATION 8046 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SC-39 Process Isolation Select Select Select 
OT Discussion: Example compensating controls include partition processes to separate 8047 
platforms.  8048 
SC-41 PORT AND I/O DEVICE ACCESS 8049 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SC-41 Port and I/O Device Access Add Add Add 
OT Discussion: No OT discussion for this control. 8050 
Rationale for adding SC-41 to LOW, MOD, and HIGH baselines: OT functionality is generally 8051 
defined in advance and does not change often. 8052 
SC-45 SYSTEM TIME SYNCHRONIZATION 8053 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SC-45 System Time Synchronization Add Add Add 
SC-45 (1) SYSTEM TIME SYNCHRONIZATION | SYNCHRONIZATION WITH AUTHORITATIVE TIME SOURCE    
OT Discussion: Organizations coordinate time synchronization across OT systems to enable 8054 
accurate troubleshooting and forensic analysis. 8055

<!-- page 302 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
284 
Control Enhancement: (1) OT Discussion: Syncing with an authoritative time source may be 8056 
selected as a control when data is being correlated across organizational boundaries. OT 8057 
systems employ suitable mechanisms (e.g., GPS, IEEE 1588) for timestamps. 8058 
Rationale for adding SC-45 to LOW, MOD, and HIGH baselines: Organizations may find relative 8059 
system time beneficial for many OT systems to ensure the safe and reliable delivery of essential 8060 
functions. Time synchronization can also make root cause analysis more efficient by ensuring 8061 
that audit logs from different systems are aligned, enabling organizations to have an accurate 8062 
view of events across multiple systems when logs are aggregated.  8063 
SC-47 ALTERNATE COMMUNICATIONS PATHS 8064 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SC-47 Alternate Communications Paths   Add 
OT Discussion: Organizations consider which systems require alternate communication paths to 8065 
ensure that a loss of communication does not lead to an unacceptable loss of view or control or 8066 
to a safety event. 8067 
Rationale for adding SC-47 to HIGH baseline: For continuity of operations during an incident, 8068 
organizations should consider establishing alternate communication paths for command-and-8069 
control purposes to continue to operate and take appropriate actions for high-impact systems 8070 
when the loss of availability or integrity may result in severe or catastrophic adverse impacts, 8071 
including impacts to safety and critical service delivery. 8072 
SC-51 HARDWARE-BASED PROTECTION 8073 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SC-51 Hardware-Based Protection    
OT Discussion: Some OT systems support write-protection by implementing physical key 8074 
switches or write-protect switches. Organizations define the systems for which write-protection 8075 
will be enabled and develop a process for how to take the system out of write-protect mode. 8076 
E.7.18. SYSTEM AND INFORMATION INTEGRITY – SI 8077 
E.7.18.14. Tailoring Considerations for the System and Information Integrity Family 8078 
When the OT cannot support the specific system and information integrity requirements of a 8079 
control, the organization employs compensating controls in accordance with the general 8080 
tailoring guidance. Examples of compensating controls are given with each control as 8081 
appropriate. 8082

<!-- page 303 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
285 
SI-1 POLICY AND PROCEDURES 8083 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SI-1 Policy and Procedures Select Select Select 
OT Discussion: The policy specifically addresses the unique properties and requirements of OT 8084 
and the relationship to non-OT systems. 8085 
SI-2 FLAW REMEDIATION 8086 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SI-2 Flaw Remediation Select Select Select 
SI-2 (2) FLAW REMEDIATION | AUTOMATED FLAW REMEDIATION STATUS  Select Select 
OT Discussion: Flaw remediation, or patching, is complicated since many OT employ OSs and 8087 
other software that are no longer maintained by the vendors. OT operators may also lack the 8088 
resources or capability to test patches and depend on vendors to validate a patch’s operability. 8089 
Sometimes, the organization has no choice but to accept additional risk if no vendor patch is 8090 
available, if patching requires additional time to complete validation or testing, or if 8091 
deployment requires an unacceptable operations shutdown. In these situations, compensating 8092 
controls should be implemented (e.g., limiting the exposure of the vulnerable system, 8093 
restricting vulnerable services, implementing virtual patching). Other compensating controls 8094 
that do not decrease the residual risk but increase the ability to respond may be desirable (e.g., 8095 
provide a timely response in case of an incident, devise a plan to ensure that the OT can 8096 
identify exploitation of the flaw). Testing remediation of flaws in OT may exceed the 8097 
organization’s available resources. 8098 
Control Enhancement: (2) No OT discussion for this control.  8099 
SI-3 MALICIOUS CODE PROTECTION  8100 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SI-3 Malicious Code Protection Select Select Select 
OT Discussion: Malicious code protection should be deployed only after careful consideration 8101 
and verification that it does not adversely affect OT operations. Malicious code protection tools 8102 
should be configured to minimize their potential impact on OT (e.g., by employing notification 8103 
rather than quarantine). Compensating controls may include increased traffic monitoring and 8104 
auditing. 8105

<!-- page 304 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
286 
SI-4 SYSTEM MONITORING 8106 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SI-4 System Monitoring Select Select Select 
SI-4 (2) SYSTEM MONITORING | AUTOMATED TOOLS AND MECHANISMS FOR REAL-TIME ANALYSIS  Select Select 
SI-4 (4) SYSTEM MONITORING | INBOUND AND OUTBOUND COMMUNICATIONS TRAFFIC  Select Select 
SI-4 (5) SYSTEM MONITORING | SYSTEM-GENERATED ALERTS  Select Select 
SI-4 (10) SYSTEM MONITORING | VISIBILITY OF ENCRYPTED COMMUNICATIONS   Select 
SI-4 (12) SYSTEM MONITORING | AUTOMATED ORGANIZATION-GENERATED ALERTS   Select 
SI-4 (14) SYSTEM MONITORING | WIRELESS INTRUSION DETECTION   Select 
SI-4 (20) SYSTEM MONITORING | PRIVILEGED USERS   Select 
SI-4 (22) SYSTEM MONITORING | UNAUTHORIZED NETWORK SERVICES   Select 
OT Discussion: The organization ensures that the use of monitoring tools and techniques does 8107 
not adversely affect OT operational performance. Compensating controls may include 8108 
deploying sufficient network, process, and physical monitoring. 8109 
Control Enhancement: (2) OT Discussion: When the OT cannot support the use of automated 8110 
tools for near-real-time analysis of events, the organization employs compensating controls 8111 
(e.g., providing an auditing capability on a separate system, nonautomated mechanisms or 8112 
procedures) in accordance with the general tailoring guidance. 8113 
Control Enhancement: (4) (10) (12) (14) (20) (22) No OT Discussion for this control. 8114 
Control Enhancement: (5) OT Discussion: Example compensating controls include manually 8115 
generating alerts.  8116 
SI-5 SECURITY ALERTS, ADVISORIES, AND DIRECTIVES 8117 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SI-5 Security Alerts, Advisories, and Directives Select Select Select 
SI-5 (1) SECURITY ALERTS, ADVISORIES, AND DIRECTIVES | AUTOMATED ALERTS AND ADVISORIES   Select 
OT Discussion: CISA generates security alerts and advisories relative to OT at 8118 
https://www.cisa.gov/news-events/ics-advisories. Industry-specific ISACs often provide tailored 8119 
advisories and alerts, which can be found at https://www.nationalisacs.org/. 8120 
Control Enhancement: (1) No OT Discussion for this control. 8121

<!-- page 305 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
287 
SI-6 SECURITY AND PRIVACY FUNCTION VERIFICATION 8122 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SI-6 Security and Privacy Function Verification   Select 
OT Discussion: Shutting down and restarting the OT may not always be feasible upon the 8123 
identification of an anomaly. These actions should be scheduled in accordance with OT 8124 
operational requirements. 8125 
SI-7 SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY 8126 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SI-7 Software, Firmware, and Information Integrity  Select Select 
SI-7 (1) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | INTEGRITY CHECKS  Select Select 
SI-7 (2) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | AUTOMATED NOTIFICATIONS OF INTEGRITY VIOLATIONS   Select 
SI-7 (5) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | AUTOMATED RESPONSE TO INTEGRITY VIOLATIONS   Select 
SI-7 (7) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | INTEGRATION OF DETECTION AND RESPONSE  Select Select 
SI-7 (15) SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY | CODE AUTHENTICATION   Select 
OT Discussion: The organization determines whether the use of integrity verification 8127 
applications would adversely affect the operation of the ICS and employs compensating 8128 
controls (e.g., manual integrity verifications that do not affect performance). 8129 
Control Enhancements: (1) OT Discussion: The organization ensures that the use of integrity 8130 
verification applications does not adversely impact the operational performance of the OT. 8131 
Control Enhancement: (2) OT Discussion: When the organization cannot employ automated 8132 
tools that provide notifications about integrity discrepancies, the organization employs 8133 
nonautomated mechanisms or procedures. Example compensating controls include performing 8134 
scheduled manual inspections for integrity violations. 8135 
Control Enhancement: (5) OT Discussion: Shutting down and restarting the ICS may not always 8136 
be feasible upon identification of an anomaly. These actions should be scheduled in accordance 8137 
with ICS operational requirements. 8138 
Control Enhancement: (7) OT Discussion: When the ICS cannot detect unauthorized security-8139 
relevant changes, the organization employs compensating controls (e.g., manual procedures) in 8140 
accordance with the general tailoring guidance. 8141

<!-- page 306 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
288 
Control Enhancement: (15) OT Discussion: Code authentication provides assurance that the 8142 
software and firmware have not been tampered with. If automated mechanisms are not 8143 
available, organizations can manually verify code authenticity using a combination of 8144 
techniques, including verifying hashes, downloading from reputable sources, verifying version 8145 
numbers with the vendor, or testing software and firmware in offline or test environments. 8146 
SI-8 SPAM PROTECTION 8147 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SI-8 Spam Protection  Select Select 
SI-8 (2) SPAM PROTECTION | AUTOMATIC UPDATES  Remove Remove 
OT Discussion: OT organizations implement spam protection by removing spam transport 8148 
mechanisms, functions, and services (e.g., electronic mail, web browsing) from the OT.  8149 
Rationale for removing SI-8 (2) from MOD and HIGH baselines: Spam transport mechanisms are 8150 
disabled or removed from the OT, so automatic updates are not necessary.  8151 
SI-10 INFORMATION INPUT VALIDATION  8152 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SI-10 Information Input Validation  Select Select 
OT Discussion: No OT Discussion for this control. 8153 
SI-11 ERROR HANDLING 8154 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SI-11 Error Handling  Select Select 
OT Discussion: No OT Discussion for this control. 8155 
SI-12 INFORMATION MANAGEMENT AND RETENTION 8156 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SI-12 Information Management and Retention  Select Select Select 
OT Discussion: No OT Discussion for this control. 8157

<!-- page 307 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
289 
SI-13 PREDICTABLE FAILURE PREVENTION 8158 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SI-13 Predictable Failure Prevention   Add 
OT Discussion: No OT Discussion for this control.  8159 
Rationale for adding SI-13 control to HIGH baseline: OT are designed and built with certain 8160 
boundary conditions, design parameters, and assumptions about their environment and mode 8161 
of operation. OT may run much longer than conventional systems, allowing latent flaws that are 8162 
not manifest in other environments to become effective. For example, integer overflow might 8163 
never occur in systems that are re-initialized more frequently than the occurrence of the 8164 
overflow. Experience and forensic studies of anomalies and incidents in OT can lead to the 8165 
identification of emergent properties that were previously unknown, unexpected, or 8166 
unanticipated. Preventative and restorative actions (e.g., restarting the system or application) 8167 
are prudent but may not be acceptable in OT for operational reasons.  8168 
SI-16 MEMORY PROTECTION  8169 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SI-16 Memory Protection  Select Select 
OT Discussion: No OT Discussion for this control.  8170 
SI-17 FAIL-SAFE PROCEDURES  8171 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SI-17 Fail-Safe Procedures Add Add Add 
OT Discussion: The selected failure conditions and corresponding procedures may vary among 8172 
baselines. The same failure event may trigger different responses, depending on the impact 8173 
level. Mechanical and analog systems can be used to provide mechanisms to ensure fail-safe 8174 
procedures. Fail-safe states should account for potential impacts on human safety, physical 8175 
systems, and the environment. A related control is CP-6.  8176 
Rationale for adding SI-17 to LOW, MOD, and HIGH baselines: This control provides a 8177 
framework for the organization to define its policies and procedures for handling failures and 8178 
other incidents. Creating a written record of the decision process for selecting incidents and 8179 
appropriate responses in light of a changing operational environment is part of risk 8180 
management.  8181

<!-- page 308 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
290 
SI-22 INFORMATION DIVERSITY  8182 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SI-22 Information Diversity    
OT Discussion: Many OT systems incorporate information diversity into their designs to meet 8183 
reliability requirements. Some examples of information diversity for an OT system include 8184 
sensor voting and state estimation.  8185 
E.7.19. SUPPLY CHAIN RISK MANAGEMENT – SR 8186 
SR-1 POLICY AND PROCEDURES 8187 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SR-1 Policy and Procedures Select Select Select 
OT Discussion: Supply chain policies and procedures for OT should consider both components 8188 
received and components produced. Many OT systems use legacy components that cannot 8189 
meet modern supply chain expectations. Appropriate compensating controls should be 8190 
developed to achieve organizational supply chain expectations for legacy systems. 8191 
SR-2 SUPPLY CHAIN RISK MANAGEMENT PLAN  8192 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SR-2 Supply Chain Risk Management Plan Select Select Select 
SR-2 (1) SUPPLY CHAIN RISK MANAGEMENT PLAN | ESTABLISH SCRM TEAM Select Select Select 
OT Discussion: No OT Discussion for this control. 8193 
SR-3 SUPPLY CHAIN CONTROLS AND PROCESSES  8194 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SR-3 Supply Chain Controls and Processes Select Select Select 
SR-3 (1) SUPPLY CHAIN CONTROLS AND PROCESSES | DIVERSE SUPPLY BASE    
OT Discussion: No OT Discussion for this control.  8195

<!-- page 309 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
291 
Control Enhancement: (1) OT Discussion: Using a diverse set of suppliers in the OT environment 8196 
can improve reliability by reducing common cause failures. This is not always possible since 8197 
some technologies have limited supply options that meet the operational requirements. 8198 
SR-5 ACQUISITION STRATEGIES, TOOLS, AND METHODS  8199 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
SUPPLEMENTED 
CONTROL BASELINES 
LOW MOD HIGH 
SR-5 Acquisition Strategies, Tools, and Methods Select Select Select 
SR-5 (1) ACQUISITION STRATEGIES, TOOLS, AND METHODS | ADEQUATE SUPPLY  Add Add 
OT Discussion: No OT Discussion for this control.  8200 
Control Enhancement: (1) OT Discussion: Vendor relationships and spare parts strategies are 8201 
developed to ensure that an adequate supply of critical components is available to meet 8202 
operational needs.  8203 
Rationale for adding SR-5 (1) to MOD and HIGH baselines: OT systems and system components 8204 
are often built for purpose and have a limited number of vendors or suppliers for a specific 8205 
component. Organizations identify critical OT system components and controls to ensure an 8206 
adequate supply in the event of supply chain disruptions.  8207 
SR-6 SUPPLIER ASSESSMENTS AND REVIEWS  8208 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SR-6 Supplier Assessments and Reviews  Select Select 
OT Discussion: No OT Discussion for this control.  8209 
SR-8 NOTIFICATION AGREEMENTS  8210 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SR-8 Notification Agreements Select Select Select 
OT Discussion: No OT Discussion for this control. 8211 
SR-9 TAMPER RESISTANCE AND DETECTION 8212 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SR-9 Tamper Resistance and Detection   Select

<!-- page 310 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
292 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SR-9 (1) TAMPER RESISTANCE AND DETECTION | MULTIPLE STAGES OF SYSTEM DEVELOPMENT LIFE CYCLE   Select 
OT Discussion: No OT Discussion for this control.  8213 
SR-10 INSPECTION OF SYSTEMS OR COMPONENTS 8214 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SR-10 Inspection of Systems or Components Select Select Select 
OT Discussion: No OT Discussion for this control. 8215 
SR-11 COMPONENT AUTHENTICITY  8216 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SR-11 Component Authenticity Select Select Select 
SR-11 (1) COMPONENT AUTHENTICITY | ANTI-COUNTERFEIT TRAINING Select Select Select 
SR-11 (2) COMPONENT AUTHENTICITY | CONFIGURATION CONTROL FOR COMPONENT SERVICE AND REPAIR Select Select Select 
OT Discussion: No OT Discussion for this control.  8217 
SR-12 COMPONENT DISPOSAL 8218 
CNTL 
NO. 
CONTROL NAME 
Control Enhancement Name 
CONTROL BASELINES 
LOW MOD HIGH 
SR-12 Component Disposal Select Select Select 
OT Discussion: No OT Discussion for this control.  8219 
 8220

<!-- page 311 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
293 
Appendix F. Applying the Risk Management Framework to OT Systems 8221 
The NIST Risk Management Framework (RMF) applies the risk management process and 8222 
concepts (i.e., framing risk, assessing risk, responding to risk, and monitoring risk) to systems 8223 
and organizations. The following subsections describe the process of applying the RMF to OT 8224 
and include a brief description of each step and task, the intended outcome of each task, task 8225 
mappings to other standards and guidelines applicable to OT (e.g., CSF 2.0, IEC 62443), and OT-8226 
specific implementation guidance. Some tasks are optional, and not all tasks include OT-specific 8227 
considerations or guidance. 8228 
The RMF steps in Fig. 22, while shown sequentially, can be implemented in a different order to 8229 
be consistent with established management and system development life cycle processes. 8230 
 8231 
Fig. 22. Risk Management Framework steps 8232 
F.1. Prepare 8233 
The purpose of the Prepare step is to carry out essential activities at the organizational, mission 8234 
and business process, and system levels to help the organization manage its security and 8235 
privacy risks using the RMF. The Prepare step leverages activities that are already being 8236 
conducted within cybersecurity programs to emphasize the importance of having organization-8237 
wide governance and resources in place to support risk management. Table 19 provides details 8238 
on applying the Prepare step to OT. 8239 
Categorize 
System
Select 
Controls
Implement 
Controls
Assess 
Controls
Authorize 
System
Monitor 
Controls
Prepare*

<!-- page 312 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
294 
Table 19. Applying the RMF Prepare step to OT 8240 
Tasks Outcomes OT-Specific Guidance 
Organizational and Mission and Business Process Levels 
TASK P-1 
RISK MANAGEMENT ROLES 
Individuals are identified and assigned key 
roles for executing the RMF. 
[Cybersecurity Framework: GV.RR-02; GV.SC-
02]  
[IEC 62443-2-1: ORG 1.3] 
Establish and maintain personnel 
cybersecurity roles and 
responsibilities for both IT and 
OT systems. Include 
cybersecurity roles and 
responsibilities for third-party 
providers. Examples of OT 
personnel include the 
Process/Plant Manager, Process 
Control Engineer, Operator, 
Functional Safety Engineer, 
Maintenance Personnel, and 
Process Safety Manager. 
TASK P-2 
RISK MANAGEMENT STRATEGY 
A risk management strategy for the 
organization that includes a determination 
and expression of organizational risk 
tolerance is established. 
[Cybersecurity Framework: GV.RM; GV.SC-01; 
GV.OV-03] 
[IEC 62443-2-1: ORG 2.1] 
The risk management strategy 
encompasses the whole 
organization. Consider the 
unique regulatory requirements 
as it relates to organizations with 
OT systems.  
TASK P-3 
RISK ASSESSMENT—
ORGANIZATION 
An organization-wide risk assessment is 
completed, or an existing risk assessment is 
updated.  
[Cybersecurity Framework: ID.RA; GV.SC-07] 
[IEC 62443-2-1: Event1.9; ORG 1.3; 2.1] 
 
TASK P-4 
ORGANIZATIONALLY TAILORED 
CONTROL BASELINES AND 
CYBERSECURITY FRAMEWORK 
PROFILES (OPTIONAL) 
Organizationally tailored control baselines 
and/or Cybersecurity Framework profiles are 
established and made available. 
[Cybersecurity Framework: Profile] 
An organizationally tailored 
control baseline for OT systems 
can be developed to address 
mission and business needs, 
unique operating environments, 
and/or other requirements.  
TASK P-5 
COMMON CONTROL 
IDENTIFICATION 
Common controls that are available for 
inheritance by organizational systems are 
identified, documented, and published. 
Common controls available for 
inheritance may adversely 
impact OT system operation. 
Consider whether common 
controls can be applied to OT 
systems effectively, safely, and 
without adverse impacts on OT 
system operation. 
TASK P-6 
IMPACT-LEVEL PRIORITIZATION 
(OPTIONAL) 
A prioritization of organizational systems with 
the same impact level is conducted. 
[Cybersecurity Framework: ID.AM-05; GV.OC-
04] 
[IEC 62443-2-1: DATA 1.1] 
Criteria such as safety or critical 
service delivery can be used in 
the impact-level prioritization.

<!-- page 313 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
295 
Tasks Outcomes OT-Specific Guidance 
TASK P-7 
CONTINUOUS MONITORING 
STRATEGY – ORGANIZATION 
An organization-wide strategy for monitoring 
control effectiveness is developed and 
implemented. 
[Cybersecurity Framework: DE.CM; GV.SC-09] 
[IEC 62443-2-1: EVENT 1.1; COMP 2.2 USER 
1.06; EVENT 1.1.; ORG2.2 
  
System-Level 
TASK P-8 
MISSION OR BUSINESS FOCUS 
Mission and business functions and processes 
that the system is intended to support are 
identified. 
[Cybersecurity Framework: Profile; 
Implementation Tiers; GV.OC; ID.AM-03] 
[IEC 62443-2-1: ORG1.6; AVAIL 1.2; AVAIL 
1.1] 
When mapping OT and IT 
processes, the information flows 
and protocols should also be 
documented. 
TASK P-9 
SYSTEM STAKEHOLDERS 
The stakeholders with an interest in the 
system are identified. 
[Cybersecurity Framework: GV.OC-02; GV.RR-
02] 
Example OT personnel include 
the Process/Plant Manager, 
Process Control Engineer, 
Operator, Functional Safety 
Engineer, and Process Safety 
Manager. 
TASK P-10 
ASSET IDENTIFICATION 
Stakeholder assets are identified and 
prioritized. 
[Cybersecurity Framework: ID.AM] 
OT system components can 
include PLCs, sensors, actuators, 
robots, machine tools, firmware, 
network switches, routers, 
power supplies, and other 
networked components or 
devices.  
TASK P-11 
AUTHORIZATION BOUNDARY 
The authorization boundary (i.e., system) is 
determined.  
TASK P-12 
INFORMATION TYPES 
The types of information processed, stored, 
and transmitted by the system are identified. 
[Cybersecurity Framework: ID.AM-05] 
 
TASK P-13 
INFORMATION LIFE CYCLE 
All stages of the information life cycle are 
identified and understood for each 
information type processed, stored, or 
transmitted by the system. 
[Cybersecurity Framework: ID.AM-03; ID.AM-
04; ID-AM-08] 
 
TASK P-14 
RISK ASSESSMENT – SYSTEM 
A system-level risk assessment is completed, 
or an existing risk assessment is updated. 
[Cybersecurity Framework: ID.RA; GV.SC-07] 
Risk assessments, including 
performance/load testing and 
penetration testing, are 
conducted on the OT systems 
with care to ensure that OT 
operations are not adversely 
impacted by the testing process. 
TASK P-15 
REQUIREMENTS DEFINITION 
Security and privacy requirements are 
defined and prioritized. 
[Cybersecurity Framework: GV.PO-01; 
GV.OC-03]

<!-- page 314 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
296 
Tasks Outcomes OT-Specific Guidance 
TASK P-16 
ENTERPRISE ARCHITECTURE 
The placement of the system within the 
enterprise architecture is determined. 
Group OT components by 
function or sensitivity level to 
optimize cybersecurity control 
implementation. 
TASK P-17 
REQUIREMENTS ALLOCATION 
Security and privacy requirements are 
allocated to the system and the environment 
in which the system operates. 
[Cybersecurity Framework: GV.PO-01] 
As security and privacy 
requirements are allocated to 
the OT system, impacts on 
performance and safety are 
considered.  
TASK P-18 
SYSTEM REGISTRATION 
The system is registered for purposes of 
management, accountability, coordination, 
and oversight. 
[Cybersecurity Framework: GV.PO-01; ID.AM-
02] 
 
F.2. Categorize 8241 
In the Categorize step, the potential adverse impacts of the loss of confidentiality, integrity, and 8242 
availability of the information and system are determined. For each information type and 8243 
system under consideration, the three security objectives (i.e., confidentiality, integrity, and 8244 
availability) are associated with one of three levels of potential impacts of a security breach. Of 8245 
the three security objectives, availability is generally the greatest concern for an OT. The 8246 
standards and guidance for this categorization process can be found in FIPS 199 [FIPS199] and 8247 
SP 800-60 [SP800-60v1r1][SP800-60v2r1], respectively.  8248 
The following OT example is taken from FIPS 199: 8249 
OT-Specific Recommendations and Guidance 8250 
A power plant contains a SCADA system that controls the distribution of 8251 
electric power for a large military installation. The SCADA system 8252 
contains both real-time sensor data and routine administrative 8253 
information. The management at the power plant determines that (i) 8254 
for the sensor data being acquired by the SCADA system, there is no 8255 
potential impact from a loss of confidentiality, a high potential impact 8256 
from a loss of integrity, and a high potential impact from a loss of 8257 
availability; and (ii) for the administrative information being processed 8258 
by the system, there is a low potential impact from a loss of 8259 
confidentiality, a low potential impact from a loss of integrity, and a low 8260 
potential impact from a loss of availability. The resulting security 8261 
categories SC of these information types are expressed as:  8262 
SC sensor data = {(confidentiality, NA), (integrity, HIGH), (availability, 8263 
HIGH)}, and 8264 
SC administrative information = {(confidentiality, LOW), (integrity, 8265 
LOW), (availability, LOW)}. 8266

<!-- page 315 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
297 
The resulting security category of the system is initially expressed as: 8267 
SC SCADA system = {(confidentiality, LOW), (integrity, HIGH), 8268 
(availability, HIGH)} 8269 
representing the high-water mark or maximum potential impact values 8270 
for each security objective from the information types resident on the 8271 
SCADA system. The management at the power plant chooses to 8272 
increase the potential impact from a loss of confidentiality from low to 8273 
moderate, reflecting a more realistic view of the potential impact on the 8274 
system should there be a security breach due to the unauthorized 8275 
disclosure of system-level information or processing functions. The final 8276 
security category of the system is expressed as: 8277 
SC SCADA system = {(confidentiality, MODERATE), (integrity, HIGH), 8278 
(availability, HIGH)} 8279 
Table 20 provides details on applying the RMF Categorize step to OT. 8280 
Table 20. Applying the RMF Categorize step to OT 8281 
Tasks Outcomes OT-Specific Guidance 
TASK C-1 
SYSTEM DESCRIPTION 
The characteristics of the system are 
described and documented. 
[Cybersecurity Framework: Profile] 
 
TASK C-2 
SECURITY CATEGORIZATION 
A security categorization of the system, 
including the information processed by the 
system represented by the organization-
identified information types, is completed. 
[Cybersecurity Framework: ID.AM-01; ID.AM-
05; GV.OC-04] 
Security categorization results are 
documented in the security, privacy, and 
SCRM plans. 
[Cybersecurity Framework: Profile] 
Security categorization results are consistent 
with the enterprise architecture and 
commitment to protecting organizational 
missions, business functions, and mission and 
business processes. 
[Cybersecurity Framework: Profile] 
Security categorization results reflect the 
organization’s risk management strategy. 
OT and IT systems may have 
different categorization criteria. 
System information and the 
system process (e.g., chemical 
production) should be considered 
during the security 
categorization. 
TASK C-3 
SECURITY CATEGORIZATION 
REVIEW AND APPROVAL 
The security categorization results are 
reviewed, and the categorization decision is 
approved by senior leaders in the 
organization.

<!-- page 316 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
298 
F.3. Select 8282 
The purpose of the Select step is to select the initial controls to protect the system 8283 
commensurate with risk. The control baselines are the starting point for the control selection 8284 
process and are chosen based on the security category and associated impact level of the 8285 
systems identified in the Categorize step. SP 800-53B [SP800-53B] identifies the recommended 8286 
control baselines for federal systems and information. To address the need for developing 8287 
community-wide and specialized sets of controls for systems and organizations, the concept of 8288 
overlays is introduced. An overlay is a fully specified set of controls, control enhancements, and 8289 
supplemental guidance derived from the application of tailoring guidance to security control 8290 
baselines described in SP 800-53B, Appendix C.  8291 
In general, overlays are intended to reduce the ad hoc tailoring of baselines through the 8292 
selection of a set of controls and control enhancements that more closely correspond to 8293 
common circumstances, situations, and/or conditions. Appendix F of this publication includes 8294 
an OT-specific overlay of applicable SP 800-53 controls that provides tailored baselines for low-8295 
impact, moderate-impact, and high-impact OT. These tailored baselines are starting 8296 
specifications and recommendations that can be applied to specific OT by responsible 8297 
personnel.  8298 
OT owners can tailor the overlay from Appendix F when it is not possible or feasible to 8299 
implement specific controls. The use of overlays does not in any way preclude organizations 8300 
from performing further tailoring (i.e., overlays can also be subject to tailoring) to reflect 8301 
organization-specific needs, assumptions, or constraints. However, all tailoring activities should  8302 
primarily focus on meeting the intent of the original controls whenever possible or feasible. For 8303 
example, when the OT cannot support or the organization determines that it is not advisable to 8304 
implement particular controls or control enhancements in an OT (e.g., performance, safety, or 8305 
reliability are adversely impacted), the organization should provide a complete and convincing 8306 
rationale for how the selected compensating controls provide an equivalent security capability 8307 
or level of protection for the OT and why the related baseline controls could not be employed. 8308 
If the OT cannot support the use of automated mechanisms, the organization employs 8309 
nonautomated mechanisms or procedures as compensating controls in accordance with the 8310 
general tailoring guidance in Sec. 3.3 of SP 800-53. Compensating controls are not exceptions or 8311 
waivers to the baseline controls. Rather, they are alternative safeguards and countermeasures 8312 
employed within the OT that accomplish the intent of the original controls that could not be 8313 
effectively employed. Organizational decisions on the use of compensating controls are 8314 
documented in the security plan for the OT.  8315 
Table 21 provides additional details on applying the RMF Select step to OT.  8316

<!-- page 317 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
299 
Table 21. Applying the RMF Select step to OT 8317 
Tasks Outcomes OT-Specific Guidance 
TASK S-1 
CONTROL SELECTION 
Control baselines necessary to protect the 
system commensurate with risk are 
selected. 
[Cybersecurity Framework: Profile] 
OT systems can leverage the OT 
control baselines identified in 
Appendix F as a starting point or an 
organization-defined control 
selection approach.  
TASK S-2 
CONTROL TAILORING 
Controls are tailored to produce specific 
control baselines. 
[Cybersecurity Framework: Profile] 
Due to operational or technical 
constraints, it may not be feasible 
to implement certain controls. 
Organizations should consider the 
use of compensating controls to 
manage risk to an acceptable level. 
TASK S-3 
CONTROL ALLOCATION 
Controls are assigned as system-specific, 
hybrid, or common controls. Controls are 
allocated to the specific system elements 
(i.e., machine, physical, or human 
elements). 
[Cybersecurity Framework: Profile; PR.PS] 
 
TASK S-4 
DOCUMENTATION OF PLANNED 
CONTROL IMPLEMENTATIONS 
Controls and associated tailoring actions 
are documented in security and privacy 
plans or equivalent documents. 
[Cybersecurity Framework: Profile] 
 
TASK S-5 
CONTINUOUS MONITORING 
STRATEGY – SYSTEM 
A continuous monitoring strategy for the 
system that reflects the organizational risk 
management strategy is developed. 
[Cybersecurity Framework: GV.OV; DE.CM] 
An OT-specific continuous 
monitoring strategy to measure 
control effectiveness may be 
necessary due to unique 
operational, environmental, 
and/or availability constraints.  
TASK S-6 
PLAN REVIEW AND APPROVAL 
Security and privacy plans reflecting the 
selection of controls necessary to protect 
the system and the environment of 
operation commensurate with risk are 
reviewed and approved by the authorizing 
official. 
Review any potential impact to the 
OT system’s operational 
effectiveness and safety. 
F.4. Implement 8318 
The Implement step involves the implementation of controls in new or legacy systems. The 8319 
control selection process described in this section can be applied to OT from two perspectives: 8320 
new development and legacy.  8321 
For new development systems, the control selection process is applied from a requirements 8322 
definition perspective since the systems do not yet exist and organizations are conducting initial 8323 
security categorizations. The controls included in the security plans for the systems serve as 8324 
security specifications and are expected to be incorporated into the systems during the 8325 
development and implementation phases of the system development life cycle.  8326

<!-- page 318 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
300 
In contrast, the security control selection process for legacy systems is applied from a gap 8327 
analysis perspective when organizations anticipate significant changes to the systems (e.g., 8328 
during major upgrades, modifications, or outsourcing). Since the systems already exist, 8329 
organizations have likely completed the security categorization and security control selection 8330 
processes, resulting in the establishment of previously agreed-upon controls in the respective 8331 
security plans and the implementation of those controls within the systems.  8332 
Table 22 provides additional details on applying the RMF Implement step to OT.  8333 
Table 22. Applying the RMF Implement step to OT 8334 
Tasks Outcomes OT-Specific Guidance 
TASK I-1 
CONTROL 
IMPLEMENTATION 
Controls specified in the security and 
privacy plans are implemented. 
[Cybersecurity Framework: PR.PS-01] 
Systems security and privacy engineering 
methodologies are used to implement the 
controls in the system security and privacy 
plans. 
[Cybersecurity Framework: PR.PS-02] 
For existing (operational) OT systems, 
schedule control implementation during the 
OT system maintenance window. A complete 
verification is recommended to ensure that 
the controls are not affecting or degrading 
the performance and safety of the OT system. 
In some cases, it may not be feasible to 
immediately mitigate the risk due to 
scheduling issues. However, interim 
compensating controls can be leveraged. 
TASK I-2 
UPDATE CONTROL 
IMPLEMENTATION 
INFORMATION 
Changes to the planned implementation 
of controls are documented. 
[Cybersecurity Framework: PR.PS-01] 
The security and privacy plans are 
updated based on information obtained 
during the implementation of the 
controls. 
[Cybersecurity Framework: Profile] 
 
F.5. Assess 8335 
The Assess step of the RMF determines the extent to which the controls in the system are 8336 
effective in their application and producing the desired results. SP 800-53A [SP800-53Ar5] 8337 
provides guidance for assessing selected controls from SP 800-53 to ensure that they are 8338 
implemented correctly, operating as intended, and producing the desired outcome with respect 8339 
to meeting the security requirements of the system.  8340 
Table 23 provides additional details on applying the Assess step to OT. 8341 
Table 23. Applying the RMF Assess step to OT 8342 
Tasks Outcomes OT-Specific Guidance 
TASK A-1 
ASSESSOR SELECTION 
An assessor or assessment team is selected to 
conduct the control assessments. The appropriate 
level of independence is achieved for the assessor 
or assessment team selected. 
Include OT system personnel and 
operator in the assessment team.

<!-- page 319 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
301 
Tasks Outcomes OT-Specific Guidance 
TASK A-2 
ASSESSMENT PLAN 
The documentation needed to conduct the 
assessments is provided to the assessor or 
assessment team. Security and privacy assessment 
plans are developed and documented. Security and 
privacy assessment plans are reviewed and 
approved to establish the expectations for the 
control assessments and the level of effort required. 
 
TASK A-3 
CONTROL 
ASSESSMENTS 
Control assessments are conducted in accordance 
with the security and privacy assessment plans. 
Opportunities to reuse assessment results from 
previous assessments to make the risk management 
process timely and cost-effective are considered. 
The use of automation to conduct control 
assessments is maximized to increase speed, 
effectiveness, and efficiency of assessments. 
Consider the use of tabletop 
exercises or simulations to reduce 
the impact to production OT. Use 
automated tools to conduct 
assessments with care to ensure 
that the OT system is not 
adversely impacted by the testing 
process.  
TASK A-4 
ASSESSMENT REPORTS 
Security and privacy assessment reports that 
provide findings and recommendations are 
completed. 
[Cybersecurity Framework: ID.RA-01 and ID.RA-03] 
 
TASK A-5 
REMEDIATION ACTIONS 
Remediation actions to address deficiencies in the 
controls implemented in the system and 
environment of operation are taken. Security and 
privacy plans are updated to reflect the control 
implementation changes made based on the 
assessments and subsequent remediation actions. 
[Cybersecurity Framework: Profile] 
Ensure that remediation actions 
do not negatively impact the 
efficiency and safe operations of 
OT. Consider the use of 
compensating controls as one of 
the remediation actions.  
TASK A-6 
PLAN OF ACTION AND 
MILESTONES 
A plan of action and milestones detailing 
r
emediation plans for unacceptable risks identified 
in security and privacy assessment reports is 
developed. 
[Cybersecurity Framework: ID.RA-06] 
Consider the unique time 
constraints of the OT system in the 
plan of action and milestones, 
including planned schedule 
maintenance or shutdowns of the 
OT system.  
F.6. Authorize 8343 
The Authorize step involves a management decision to authorize the operation of a system and 8344 
explicitly accept the risks to operations, assets, and individuals based on the implementation of 8345 
an agreed-upon set of controls. A new system is not placed into production or operation until 8346 
the system is authorized.  8347 
Table 24 provides additional details on applying the Authorize step to OT. 8348 
Table 24. Applying the RMF Authorize step to OT 8349 
Tasks Outcomes OT-Specific Guidance 
TASK R-1 
AUTHORIZATION PACKAGE 
An authorization package is developed 
for submission to the authorizing official.

<!-- page 320 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
302 
Tasks Outcomes OT-Specific Guidance 
TASK R-2 
RISK ANALYSIS AND 
DETERMINATION 
A risk determination by the authorizing 
official that reflects the risk 
management strategy, including risk 
tolerance, is rendered. 
 
TASK R-3 
RISK RESPONSE 
Risk responses for determined risks are 
pr
ovided. 
[Cybersecurity Framework: ID.RA-06] 
Develop and implement a 
comprehensive strategy to manage risk 
to the OT system that includes the 
identification and prioritization of risk 
responses. 
TASK R-4 
AUTHORIZATION DECISION 
The authorization for the system or the 
c
ommon controls is approved or denied. 
Organizations may need to determine 
remediation strategies when system 
risks drift out of the acceptable range 
while considering OT-specific 
dependencies, such as the inability to 
take a system or component offline until 
remediated. 
TASK R-5 
AUTHORIZATION REPORTING 
Authorization decisions, significant 
vulnerabilities, and risks are reported to 
organizational officials. 
Ensure that decisions, vulnerabilities, 
and risks are reported to OT and 
operations personnel.  
F.7. Monitor 8350 
The Monitor step continuously tracks changes to the system that may affect controls and 8351 
assesses control effectiveness. SP 800-37r2 provides guidelines on cybersecurity continuous 8352 
monitoring [SP800-37r2].  8353 
Table 25 provides additional details on applying the Monitor step to OT.  8354 
Table 25. Applying the RMF Monitor step to OT 8355 
Tasks Outcomes OT-Specific Guidance 
TASK M-1 
SYSTEM AND ENVIRONMENT 
CHANGES 
The system and environment of 
operation are monitored in accordance 
with the continuous monitoring strategy. 
[Cybersecurity Framework: DE.CM; 
ID.RA-07] 
Leverage the OT-specific continuous 
monitoring strategy that considers 
performance impacts and safety systems 
to be critical.  
TASK M-2 
ONGOING ASSESSMENTS 
Ongoing assessments of control 
effectiveness are conducted in 
accordance with the continuous 
monitoring strategy. 
[Cybersecurity Framework: ID.IM-01; 
GV.SC-07; DE.CM-06] 
Conduct ongoing assessments that 
consider system performance and safety 
impacts.  
TASK M-3 
ONGOING RISK RESPONSE 
The output of continuous monitoring 
activities is analyzed and responded to 
appropriately. 
[Cybersecurity Framework: ID.IM] 
Correlate detected event information 
with risk assessment outcomes to 
achieve perspective on incident impact 
on the OT system.

<!-- page 321 -->

NIST SP 800-82r4 ipd (Initial Public Draft)  Guide to OT Security 
September 2026   
 
303 
Tasks Outcomes OT-Specific Guidance 
TASK M-4 
AUTHORIZATION PACKAGE 
UPDATES 
Risk management documents are 
updated based on continuous 
monitoring activities. 
[Cybersecurity Framework: GV.RM-01] 
 
TASK M-5 
SECURITY AND PRIVACY 
REPORTING 
A process is in place to report the 
security and privacy posture to the 
authorizing official and other senior 
leaders and executives. 
 
TASK M-6 
ONGOING AUTHORIZATION 
Authorizing officials conduct ongoing 
authorizations using the results of 
continuous monitoring activities and 
communicate changes in risk 
determination and acceptance decisions. 
 
TASK M-7 
SYSTEM DISPOSAL 
A system disposal strategy is developed 
a
nd implemented, as needed. 
[Cybersecurity Framework: ID.AM-08] 
Planned obsolescence found in IT 
components may not extend to OT 
components. Consider the maintenance 
and repair of OT components that are 
required to be sustained beyond IT 
component availability. 
 8356

