# Knowledge holes in the OT/ICS pentest knowledge base, and the sources that fill them (as of 2026-11-10)

Scope: an audit of `knowledge-base/` (68 entries; 0 advisories) against the workflow steps, protocols, asset classes, German/EU sources, evidence types and reference-device specifics. The 25 sources already listed in `research_notes/OT pentesting knowledge base/ot_gaps.md` (CRA, Machinery Reg., § 30 BSIG, ISA-62443 list, Samanis taxonomy, Sandia 2005, Malcolm, ICSNPP, CALDERA-OT, OpenPLC runtime, Volt Typhoon, CERT Polska, IOCONTROL, FrostyGoop, Dragos YIR 2026, CVSS v4, EPSS, INL CCE, CISA asset inventory, BVerfG, § 303b) are counted as **known but not yet entries**. They are not re-recommended below unless a gap depends on them. Verification method: HTTP status plus page `<title>` via curl (2026-11-10), WebFetch for content, and direct parsing of CSAF JSON. "yes" = fetched and content or title confirmed. "excerpt" = only a search snippet or secondary page was seen. "no" = could not be reached.

## 1. Reference device (AXC F 2152 / PLCnext): advisories, change notes, certificates, security docs

### Takeaway
This is the most severe hole. The knowledge base has no Phoenix Contact advisory, but there are at least six PLCnext advisories from 2025-2026. Four of them were published in 2026, after the firmware lines the KB discusses. A newer change-notes edition (en_52) and two IEC 62443-4-2 certificates also exist. Together these directly feed OWASP OT #2, #3, #9 and #10 and the vulnerability-correlation step.

### Cited Findings
- **VDE-2025-053**, "Multiple Vulnerabilities in PLCnext Firmware", released 2025-07-08, lists AXC F 2152 and 54 CVEs, mostly third-party Linux components such as curl, OpenSSH, rsync, unzip and patch. Remediation is "Update to the latest 2025.0.2 Firmware Release". This is directly useful as CSAF test data for SBOM-to-advisory correlation and VEX logic. — [Phoenix Contact CSAF VDE-2025-053](https://phoenixcontact.csaf-tp.certvde.com/.well-known/csaf/white/2025/vde-2025-053.json) (parsed 2026-11-10)
- **VDE-2025-054** (2025-07-08) covers CVE-2025-41665 to -41668 and lists AXC F 2152. Fix: firmware 2025.0.2. — [CSAF VDE-2025-054](https://phoenixcontact.csaf-tp.certvde.com/.well-known/csaf/white/2025/vde-2025-054.json)
- **VDE-2026-050** (2026-05-27), "PLCnext Firmware Security Issues Related to APPs and Configuration Files", covers CVE-2025-41669 and CVE-2025-41670 and lists AXC F 2152. Its remediation states that before 2026.0.3 "apps are installed via WBM (APP Manager) without enforced authenticity validation". 2026.0.3 enforces app signature verification by default. This bears on OWASP #3 (supply chain) and the container/app asset class. — [CSAF VDE-2026-050](https://phoenixcontact.csaf-tp.certvde.com/.well-known/csaf/white/2026/vde-2026-050.json)
- The CERT@VDE Phoenix Contact listing (page 1 of 15) also shows **VDE-2025-056**, "Improper Input Validation Vulnerabilities in PLCnext Firmware" (2026-08-12). It also shows **VDE-2026-084**, "CodeMeter Runtime … in the PLCnext Firmware", and **VDE-2026-121**, "GSDX SignatureValue verification, signed plug-in validation bypass and path traversal … in PLCnext Engineer", both 2026-11-04. — [CERT@VDE Phoenix Contact advisories](https://certvde.com/en/advisories/vendor/phoenixcontact/). Note: the guessed CSAF path for VDE-2025-056 returned HTTP 404, so its file name must be taken from the provider's index. A search summary attributed CVE-2025-41669/-41670 to VDE-2025-056, but the CSAF JSON places them in VDE-2026-050, so the summary was wrong.
- The Phoenix Contact PSIRT page resolves (HTTP 200). — [Phoenix Contact PSIRT](https://www.phoenixcontact.com/psirt)
- Older baseline: the US CISA advisory ICSA-19-155-01 for the PLCnext AXC F 2152 resolves (VDE-2019-009 equivalent; pre-2023, historical only). — [CISA ICSA-19-155-01](https://www.cisa.gov/news-events/ics-advisories/icsa-19-155-01)
- **Change notes en_52** exist (the KB stops at en_51). PDF metadata: "Change notes for the AXC F 2152 controller", created 2026-01-29. The internal file path names "Change Notes FW 2024.0.16 LTS". — [AXC F 2152 change notes 108427_en_52](https://www.plcnext-community.net/robohelp/security/assets/docs/ah_en_axc_f_2152_change_notes_108427_en_52.pdf)
- **IEC 62443-4-2 certificates.** A TÜV Rheinland certificate, 968/CSP 1037.00/25, is downloadable (HTTP 200, PDF). A search excerpt dates it 2025-07-04 and states IEC 62443-4-1 compliance plus SL-C 2 per 62443-4-2, "limited to the dedicated security context documented in the user manuals". — [TÜV Rheinland certificate PDF](https://www.plcnext-community.net/robohelp/security/assets/docs/968_CSP_1037_00_25_RL_2025-07-03%202.pdf). A TÜV SÜD certificate, IITS2 029429 0027 Rev. 03, is cited in search results as covering IEC 62443-4-1:2018, 62443-4-2:2019 and PPP 15003C:2024, valid only with the Security Profile active, but its URL returned HTTP 403/404 to curl. — [security.plcnext.help (excerpt only)](https://security.plcnext.help/assets/docs/IITS2%20029429%200027%20Rev.%2003.pdf)
- PLCnext "Industrial Cyber Security" help page (revision 103, reviewed 2026-11-09) has subpages on the firewall (WBM plus nftables filters), user authentication and authentication-failure handling, user rights, certificate authentication, LDAP/LDAPS, OpenVPN/IPsec, Security Profile, SD-card settings and Syslog. It does **not** cover SBOM, secure boot, TPM or app signing. — [PLCnext Info Center: Security](https://www.plcnext.help/te/Security/Security.htm)

### Inferences
- The KB's firmware baseline (2022.0.8, change notes en_51) is about two firmware generations behind current fixes (2025.0.2 and 2026.0.3). Any reachability profile built on the KB alone will mark fixed issues as open.
- VDE-2025-053's 54-CVE third-party list is a ready-made ground truth for checking the Syft/Grype/cve-bin-tool pipeline against vendor-confirmed CVEs.
- The certificates matter for reporting. Findings that contradict an SL-C 2 claim "with Security Profile active" must record whether the Security Profile was on.

### Gaps
- The full TÜV SÜD certificate text was not reached. The certificates' scope of firmware versions was not confirmed.
- There is still no vendor SBOM or VEX for the AXC F 2152. The product page (firmware download) remains 403 from this environment.

## 2. Protocol security specifications and testing guidance

### Takeaway
The KB covers Modbus at a 101 level only, and has no protocol security specification at all. Primary specs exist for OPC UA (BSI analysis), PROFINET (PI security classes), Modbus/TCP Security, CIP Security, BACnet/SC and IEC 62351. They matter for OWASP #9 (insecure protocols) and for writing accurate "protocol lacks authentication" findings without overclaiming. No public specification was found for the PLCnext remoting service on 41100/TCP.

### Cited Findings
- BSI "OPC UA Security Analysis" (spec 1.04, listed as 2021; the German PDF is dated 03.03.2022) is an official BSI landing page. A secondary summary reports that BSI found no systematic security vulnerabilities in OPC UA. — [BSI OPC UA 2022 EN](https://bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/Studies/OPCUA/OPCUA_2022_EN.pdf); BSI download list shows both the 2015 (1.02) and 2021 (1.04) studies — [BSI ICS downloads](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Industrielle-Steuerungs-und-Automatisierungssysteme/Download/download.html)
- The OPC Foundation security page and security-bulletins page returned HTTP 403 to curl, so they are not verified. — [opcfoundation.org/security](https://opcfoundation.org/security/)
- PROFINET defines Security Classes 1 to 3. Class 1 adds robustness (DCP read-only, signed GSD) with no cryptography. Class 2 adds integrity and authenticity of IO data. Class 3 adds IO-data confidentiality. A "PROFINET Design Guideline Security" (Nov 2025 version) is members-only. — [PI security page](https://profibus.com/security) (HTTP 200); class details from search excerpt of [PI PROFINET security guideline](https://profibus.com/download/profinet-security-guideline) and [IEB Media, 2026-01-05](https://iebmedia.com/news/tech-updates/profibus-security)
- The MODBUS/TCP Security Protocol Specification v3.6 (2021-07-30) uses TLS with X.509v3 mutual authentication on port 802. The PDF URL from search now returns 404, and the spec index is at modbus.org. — [Modbus specifications](https://modbus.org/modbus-specifications) (excerpt)
- ODVA CIP Security page resolves (EtherNet/IP). — [ODVA CIP Security](https://www.odva.org/technology-standards/distinct-cip-services/cip-security/)
- IEC 62351 (security for IEC 61850, 60870-5-104 and DNP3) now has a **2026** series edition, which is paywalled. — [IEC 62351:2026 SER](https://webstore.iec.ch/en/publication/6912)
- BACnet Secure Connect reference implementation page resolves. — [BACnet/SC](https://bacnet.org/bacnet-secure-connect/)
- DNP3 user-group overview resolves. — [DNP Users Group](https://www.dnp.org/About/Overview-of-DNP3-Protocol)
- Passive parsers exist for PROFINET IO-CM and OPC UA binary. — [icsnpp-profinet-io-cm](https://github.com/cisagov/icsnpp-profinet-io-cm); [icsnpp-opcua-binary](https://github.com/cisagov/icsnpp-opcua-binary)

### Inferences
- For the reference device, OPC UA (4840) and PROFINET are the activatable protocols with security modes. The BSI OPC UA analysis and PI security classes are the two highest-value protocol entries. Modbus/TCP Security, CIP Security, IEC 62351, BACnet/SC and DNP3 can be lower-priority, "for device-agnostic expansion" entries.

### Gaps
- No public protocol documentation or security analysis was found for the PLCnext/ProConOS remoting service on 41100/TCP. Its testing guidance has to come from bench observation and vendor docs under NDA.
- OPC Foundation security bulletins could not be fetched (403). MQTT/IIoT, IEC 61850 GOOSE and S7comm-plus have no primary security source verified here.

## 3. German/EU sources

### Takeaway
The KB holds only BSI IND.1 Umsetzungshinweise, the BSI pentest study and the 2016 Plattform I4.0 guide. The BSI ICS publication set is largely missing, including a 2026 publication. The most relevant pieces are the ICS Top 10 (2022), the supplier compendium with **test recommendations**, remote maintenance, and the 2026 "Risks Posed by Internet-Connected OT Systems". The binding German operator rule **TRBS 1115 Teil 1** (amended, in force 2026-01-15) bears directly on rules of engagement for safety-relevant control equipment.

### Cited Findings
- The BSI ICS download page lists: ICS Security Compendium; OPC UA analyses; BSI-CS 123 (education and qualification); BSI-CS 005 Top 10; **BSI CS 154 "Risks Posed by Internet-Connected OT Systems" (2026)**; BSI-CS 108 remote maintenance; BSI-CS 019 vulnerability handling; BSI-CS 067 "Requirements for Network-Connected Industrial Components" v1.1; the ICS Security Compendium for Manufacturers and Integrators; and the joint "Principles of operational technology cyber security". The page lists no stand-alone pentest guidance. — [BSI ICS downloads](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Industrielle-Steuerungs-und-Automatisierungssysteme/Download/download.html)
- The supplier compendium's landing page title reads "ICS Security Compendium Test recommendations …". It is the BSI's test-recommendation document for ICS components, the closest BSI analogue to a device test plan. — [BSI ICS-Security-Compendium-supplier](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/ICS/ICS-Security-Compendium-supplier.html) (title verified)
- ICS Top 10 Bedrohungen und Gegenmaßnahmen 2022 [Deutsch] v1.5. — [ACS BSI-CS 005](https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_005.pdf); English: [BSI-CS 005E](https://allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_005E.pdf) (titles verified; pre-2023)
- Remote maintenance in industrial environments v1.0. — [ACS BSI-CS 108E](https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_108E.html)
- Internet-connected OT risks (2026). — [BSI CS 154E](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/ICS/Operational-Technology_CS_154E.html)
- Requirements for network-connected industrial components v1.1. — [ACS BSI-CS 067E](https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_067E.pdf)
- The ICS-Security-Kompendium (German) landing page resolves. It dates from 2013 [OLD]. — [BSI ICS-Security-Kompendium](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ICS/ICS-Security_kompendium_pdf.pdf)
- **TRBS 1115 Teil 1** ("Cybersicherheit für sicherheitsrelevante MSR-Einrichtungen") is addressed to employers and operators under BetrSichV. It was announced in March 2023, and the amended version has applied since 2026-01-15, adding an Anhang 2 on "schutzbedürftige Einrichtungen". The BAuA page returned 403, so these facts rest on secondary pages. — [activemind.legal TRBS 1115-1 guide](https://www.activemind.legal/de/guides/trbs-1115-teil-1/); [umwelt-online TRBS 1115-1](https://www.umwelt-online.de/recht/t_regeln/trbs/1115_t1_in.htm) (excerpt)
- KRITIS: BSI "Orientierungshilfe zum Einsatz von Systemen zur Angriffserkennung" and "Konkretisierung der KRITIS-Anforderungen" landing pages resolve. — [BSI OH SzA](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/KRITIS/oh-sza.html); [BSI KRITIS Konkretisierung](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/KRITIS/Konkretisierung_Anforderungen_Massnahmen_KRITIS.html)
- The VDI/VDE 2182 Blatt 1 product page resolves (paywalled guideline). — [VDI/VDE 2182-1](https://www.vdi.de/richtlinien/details/vdivde-2182-blatt-1-informationssicherheit-in-der-industriellen-automatisierung-allgemeines-vorgehensmodell); DKE cybersecurity work area page resolves — [DKE Cybersecurity](https://www.dke.de/de/arbeitsfelder/industry/cybersecurity)
- ENISA Threat Landscape 2025 resolves. It is generic, not ICS-specific. — [ENISA ETL 2025](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025)

### Inferences
- BSI-CS 067 and the supplier test-recommendation compendium give a German, device-level requirement baseline that maps onto the targeted-testing step. They are better grounding for a device test plan than the generic OSSTMM entry.
- TRBS 1115-1 creates an operator obligation that a pentest touching safety-relevant MSR equipment must respect. It belongs in the scoping and RoE template next to § 303b StGB.

### Gaps
- The BAuA primary text of TRBS 1115-1 was not reachable (403). The ZVEI and VDMA cybersecurity pages tried returned 404, so no current ZVEI/VDMA source is verified. No current ENISA ICS-specific report was identified; ENISA's ICS output appears to be pre-2020.

## 4. Safety instrumented systems and other asset classes

### Takeaway
SIS/IEC 61511 is absent apart from mentions in broad references. That is a high-severity hole for OWASP #4 and the "assume breach" scope, because consequence-based reporting needs a safety-cyber bridge. Engineering workstations, historians, industrial wireless and IIoT gateways have no dedicated source. Container runtimes on PLCs have only a 2017 NIST guide, and the 2026 VDE-2026-050 app-signing advisory is the device-specific counterpart.

### Cited Findings
- HSE OG86 (March 2017) covers IACS including safety instrumented systems for COMAH sites. The HSE cyber security page resolves, and the old OG86 PDF URL returns 404. — [HSE cyber security](https://www.hse.gov.uk/eci/cyber-security.htm); background via [Capula 2026 (vendor, secondary)](https://capula.com/assets/images/Transitioning-from-OG86-to-ISAIEC-62443_2026-04-02-135508_qtfm.pdf)
- TRBS 1115-1 (section 3) is the German binding counterpart for safety-relevant MSR equipment.
- NIST SP 800-190 "Application Container Security Guide" (2017 [OLD]) resolves. — [NIST SP 800-190](https://csrc.nist.gov/pubs/sp/800/190/final)
- Remote access and jump hosts: BSI-CS 108 (section 3). Volt Typhoon AA24-038A is already in ot_gaps.
- Component selection (OWASP #9): CISA "Secure by Demand: Priority Considerations for OT Owners and Operators when Selecting Digital Products" resolves. — [CISA Secure by Demand OT](https://www.cisa.gov/resources-tools/resources/secure-demand-priority-considerations-operational-technology-owners-and-operators-when-selecting)

### Gaps
- ISA TR84.00.09 (cybersecurity in the functional-safety lifecycle) could not be verified (ISA URL 404). IEC 61511 is paywalled.
- No verified source was found for historians, engineering-workstation testing, industrial wireless (WirelessHART/ISA100) or hardware debug interfaces beyond the existing OWASP ISTG and jassics IoT-hardware entries.

## 5. Evidence types: incidents, peer-reviewed testing research, reporting templates, training

### Takeaway
Incident case studies are cheap to fill from MITRE ATT&CK for ICS and CISA primary pages. Peer-reviewed evidence on scan fragility exists (Brno University of Technology, Pospíšil et al.) and underpins the passive-first rule (OWASP #4). The 2026 LINICS paper is the one peer-reviewed OT pentest-platform paper found. No public OT-specific sample pentest report was found, which is a real residual gap.

### Cited Findings
- Incidents, ATT&CK for ICS pages (all resolve): [Stuxnet S0603](https://attack.mitre.org/software/S0603/), [Triton S1009](https://attack.mitre.org/software/S1009/), [Industroyer S0604](https://attack.mitre.org/software/S0604/), [Industroyer2 S1072](https://attack.mitre.org/software/S1072/), [INCONTROLLER/Pipedream S1045](https://attack.mitre.org/software/S1045/), [2022 Ukraine Electric Power Attack C0034](https://attack.mitre.org/campaigns/C0034/).
- CISA AA22-103A "APT Cyber Tools Targeting ICS/SCADA Devices" (Pipedream/INCONTROLLER) resolves. — [CISA AA22-103A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-103a). FrostyGoop (Dragos, datePublished 2024-07-23) — [Dragos](https://www.dragos.com/blog/protect-against-frostygoop-ics-malware-targeting-operational-technology)
- Scan-impact research: Pospíšil et al. tested Nmap and Zmap against PLCs on a testbed. Zmap cut off device communication, and Nmap caused delays and occasional outages. — [VUT record "Impact of Active Scanning on the Industrial Control Networks"](https://dspace.vut.cz/items/4ca50ea0-14b7-4237-a0b8-14d2f36464ad) (excerpt); a related SpaCCS 2020 paper compares five scanners on seven PLCs — [Springer](https://link.springer.com/chapter/10.1007/978-3-030-68884-4_46) (excerpt; paywalled; pre-2023)
- LINICS: Rashid, Gardiner and Evans, "Building an Open Source Operational Technology Pentesting Platform: Lessons from LINICS", IEEE Security & Privacy 24(2), May-June 2026; arXiv submission 2026-05-21. — [arXiv 2605.22590](https://arxiv.org/abs/2605.22590)
- Reporting tooling: SysReptor (open-source pentest reporting platform) — [Syslifters/sysreptor](https://github.com/Syslifters/sysreptor), [docs](https://docs.sysreptor.com/). Public pentest report corpus (not OT-specific) — [juliocesarfort/public-pentesting-reports](https://github.com/juliocesarfort/public-pentesting-reports)
- Training and certification pages (all resolve): [SANS ICS410](https://www.sans.org/cyber-security-courses/ics-scada-cyber-security-essentials/) / [GICSP](https://www.giac.org/certifications/global-industrial-cyber-security-professional-gicsp/); [ICS515](https://www.sans.org/cyber-security-courses/ics-visibility-detection-response/) / [GRID](https://www.giac.org/certifications/response-industrial-defense-grid/); [ICS612](https://www.sans.org/cyber-security-courses/ics-cyber-security-in-depth/); [ISA/IEC 62443 certificate program](https://www.isa.org/certification/certificate-programs/isa-iec-62443-cybersecurity-certificate-program); BSI-CS 123 qualification recommendations — [ACS BSI-CS 123E](https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_123E.html)

### Inferences
- An entry per incident is unnecessary. One "incident case studies" entry linking the six ATT&CK pages plus AA22-103A would cover consequence modelling for reporting (High Consequence Events) at low cost.
- The reporting template gap is better filled by building an OT findings template on SysReptor than by waiting for public OT reports, which are rarely published.

### Gaps
- No public, sanitised OT/ICS pentest report or OT-specific report template was found.
- The Pospíšil papers were not read in full.

## 6. Gaps the earlier work left open

### Takeaway
"selmux" resolves to the Labshock OT lab, which is mirrored under two GitHub owners. "OIDA" has no public trace, and its provenance has to come from the user. PTES and the dual-use regulation could not be verified from here.

### Cited Findings
- `selmux/labshock` and `zakharb/labshock` both resolve with the title "OT Security Lab for ICS networks". `selmux/ICS-Security` redirects to "selmux/Alhasawi-ICS-OT-Security-projetcs". A search summary says Labshock's "Pentest Fury" component is restricted to personal, non-commercial use, which is not confirmed in the repo. — [selmux/labshock](https://github.com/selmux/labshock); [zakharb/labshock](https://github.com/zakharb/labshock)
- PTES (`pentest-standard.org`) timed out over HTTP and HTTPS on 2026-11-10. — [PTES](http://www.pentest-standard.org/index.php/Main_Page) (no)
- EU dual-use Regulation 2021/821: EUR-Lex returned HTTP 202 (bot challenge), so the content was not read. — [EUR-Lex 32021R0821](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32021R0821) (no)

### Gaps
- OIDA could not be identified, so the user must supply its repository URL. The licence status of Labshock "Pentest Fury" for commercial engagements needs checking against the repo's LICENSE.
- GDPR (personal data in packet captures, operator logs and HMI screenshots) was not researched. No source is verified.
- The NVD developer pages remain unretrieved, which is low impact since CVE.org/cvelistV5 and CIRCL are already entries. IEC 62443 normative text remains paywalled.

## Gap register (prioritized)

| # | Gap | OWASP OT items | Severity | Best sources (URL) | Verified |
|---|---|---|---|---|---|
| 1 | No vendor advisories/CSAF for the reference device (KB has 0 advisories) | 2, 3, 10 | high | [VDE-2026-050 CSAF](https://phoenixcontact.csaf-tp.certvde.com/.well-known/csaf/white/2026/vde-2026-050.json) (2026-05-27); [VDE-2025-053 CSAF](https://phoenixcontact.csaf-tp.certvde.com/.well-known/csaf/white/2025/vde-2025-053.json) (2025-07-08); [CERT@VDE Phoenix list](https://certvde.com/en/advisories/vendor/phoenixcontact/) (VDE-2025-056, -2026-084, -2026-121) | yes |
| 2 | Change notes newer than en_51 | 2, 3 | high | [Change notes en_52](https://www.plcnext-community.net/robohelp/security/assets/docs/ah_en_axc_f_2152_change_notes_108427_en_52.pdf) (Phoenix Contact, 2026-01-29, free, primary) | yes |
| 3 | IEC 62443-4-2 certificate for the device | 9, 10 | high | [TÜV Rheinland 968/CSP 1037.00/25](https://www.plcnext-community.net/robohelp/security/assets/docs/968_CSP_1037_00_25_RL_2025-07-03%202.pdf) (2025); [TÜV SÜD IITS2 029429 0027 Rev.03](https://security.plcnext.help/assets/docs/IITS2%20029429%200027%20Rev.%2003.pdf) | yes (PDF fetched) / excerpt |
| 4 | Core engine OIDA has no source; selmux mapped | 1, 4, 9 | high | [selmux/labshock](https://github.com/selmux/labshock); OIDA: user must supply | yes / no |
| 5 | Safety/SIS and German operator duty for safety-relevant MSR | 4, 9 | high | TRBS 1115-1 via [activemind](https://www.activemind.legal/de/guides/trbs-1115-teil-1/) (BAuA 403); [HSE cyber security / OG86](https://www.hse.gov.uk/eci/cyber-security.htm) (2017, OLD) | excerpt / yes |
| 6 | Peer-reviewed scan-fragility evidence behind passive-first rule | 4, 1 | high | [Pospíšil, VUT](https://dspace.vut.cz/items/4ca50ea0-14b7-4237-a0b8-14d2f36464ad) (2021, OLD); [SpaCCS 2020, Springer](https://link.springer.com/chapter/10.1007/978-3-030-68884-4_46) (paywalled) | excerpt |
| 7 | BSI ICS set missing (Top 10, test recommendations, components, internet-exposed OT 2026) | 1, 2, 5, 7, 9, 10 | high | [BSI Compendium test recommendations](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/ICS/ICS-Security-Compendium-supplier.html); [BSI CS 154E (2026)](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/ICS/Operational-Technology_CS_154E.html); [BSI-CS 005 Top 10 2022 v1.5](https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_005.pdf) | yes (titles) |
| 8 | Protocol security specs: OPC UA, PROFINET | 9, 7 | medium-high | [BSI OPC UA analysis 2021/22](https://bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/Studies/OPCUA/OPCUA_2022_EN.pdf); [PI PROFINET security](https://profibus.com/security) (guideline members-only) | yes / excerpt for class details |
| 9 | PLCnext security docs beyond checklist and ports | 5, 7, 10 | medium-high | [PLCnext Info Center Security](https://www.plcnext.help/te/Security/Security.htm) (rev. 103, 2026-11-09) | yes |
| 10 | PLCnext remoting / ProConOS (41100/TCP) protocol | 1, 9 | medium-high | none public found; bench observation required | no |
| 11 | Other protocol specs (Modbus/TCP Security, CIP Security, IEC 62351, BACnet/SC, DNP3) | 9 | medium | [modbus.org specs](https://modbus.org/modbus-specifications); [ODVA CIP Security](https://www.odva.org/technology-standards/distinct-cip-services/cip-security/); [IEC 62351:2026](https://webstore.iec.ch/en/publication/6912) (paywalled) | excerpt / yes / yes |
| 12 | Incident case studies | 4, 6, 7 | medium | [CISA AA22-103A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-103a) (2022); ATT&CK [S1009](https://attack.mitre.org/software/S1009/), [S1072](https://attack.mitre.org/software/S1072/), [S1045](https://attack.mitre.org/software/S1045/) | yes |
| 13 | Remote access / jump hosts | 5, 7 | medium | [BSI-CS 108E remote maintenance](https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_108E.html) | yes |
| 14 | Reporting templates / sample OT reports | 2, 4 | medium | [SysReptor](https://github.com/Syslifters/sysreptor); [public-pentesting-reports](https://github.com/juliocesarfort/public-pentesting-reports) (not OT) | yes; OT samples not found |
| 15 | Peer-reviewed OT pentest platform research | 9 | medium | [LINICS, IEEE S&P 2026 / arXiv 2605.22590](https://arxiv.org/abs/2605.22590) | yes |
| 16 | Detection expectations (KRITIS/NIS2) | 6 | medium | [BSI OH SzA](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/KRITIS/oh-sza.html); [BSI KRITIS Konkretisierung](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/KRITIS/Konkretisierung_Anforderungen_Massnahmen_KRITIS.html) | yes |
| 17 | Component selection / buyer requirements | 3, 9 | medium | [CISA Secure by Demand OT](https://www.cisa.gov/resources-tools/resources/secure-demand-priority-considerations-operational-technology-owners-and-operators-when-selecting); [BSI-CS 067E](https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_067E.pdf) | yes |
| 18 | Container/app runtime on PLC | 3, 10 | medium | VDE-2026-050 (row 1); [NIST SP 800-190](https://csrc.nist.gov/pubs/sp/800/190/final) (2017, OLD) | yes |
| 19 | Training/certification paths | 8 | low | [ICS410/GICSP](https://www.giac.org/certifications/global-industrial-cyber-security-professional-gicsp/); [ISA/IEC 62443 certificates](https://www.isa.org/certification/certificate-programs/isa-iec-62443-cybersecurity-certificate-program); [BSI-CS 123E](https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_123E.html) | yes |
| 20 | VDE/DKE/VDI guidance | 1, 7 | low | [VDI/VDE 2182-1](https://www.vdi.de/richtlinien/details/vdivde-2182-blatt-1-informationssicherheit-in-der-industriellen-automatisierung-allgemeines-vorgehensmodell) (paywalled); [DKE Cybersecurity](https://www.dke.de/de/arbeitsfelder/industry/cybersecurity) | yes |
| 21 | Export control | 8 | low | [EU 2021/821](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32021R0821) | no (bot challenge) |
| 22 | PTES methodology | 4 | low | [pentest-standard.org](http://www.pentest-standard.org/index.php/Main_Page) | no (timeout) |
| 23 | GDPR for captures/logs; historians, EWS, wireless, JTAG/UART, MQTT, 61850 | 1, 5, 10 | medium | no source verified in this pass | no |
| 24 | ZVEI/VDMA, ENISA ICS-specific | 3, 8 | low | [ENISA ETL 2025](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025) (generic); ZVEI/VDMA URLs 404 | yes / no |
