---
title: "Operational Technology (OT) Security: Theory, Techniques, Testing, and Tools"
url: "https://github.com/paulveillard/cybersecurity-OT"
type: other
trust: secondary
accessed: 2026-11-09
published: 2025-02-09
owasp_ot: [1,2,8]
version: "commit c71a85b, 2025-02-09"
license: "MIT"
---

## Summary
A large personal link list covering ICS challenges, OSINT, CERT portals, protocols, PCAPs, papers, emulators, lab tutorials, hardware and news.
It has real gems in protocol research and datasets, but curation is uneven.
It has not changed since 2025-02-09 by commit history, and it marks several of its own links as down.
Only GitHub links were health-checked; repository metadata came from the web pages because the API was rate-limited.

## Key facts
- Sections include ICS_challenge, ICS_OSINT, ICS_CERT, ICS_Protocol, PCAP/dataset collection, papers and conferences, tools and PLC emulators, lab setup tutorials, hardware, training, books and news.
- Vendor CERT links are listed for Siemens, ABB and Schneider, plus Dragos advisories.
- Notable research entries: S7CommPlus (Black Hat EU 2017), AMNESIA:33, Claroty OPC UA attack surface and Evil PLC, web-based PLC malware (NDSS 2024), PLC vulnerability survey (MDPI 2023), and the SANS ICS Cyber Kill Chain paper.
- Lab tooling listed: FUXA (last commit 2026-11-08), HoneyPLC (2023-05-16), OpenPLC Docker images, NetToPLCSim, Rapid SCADA, GRFICSv2 tutorials, ControlThings tools, ICSpector (`microsoft/ics-forensics-tools`, 2024-11-12).
- Dataset entries include `gymgit/s7-pcaps` (2016-06-10), the Electra dataset and OPC UA datasets.
- Self-marked "[Down for the moment]": Principles of Information Security PDF, CCE Phase 1-4 reference, GreHack 2015 paper, Redfox PLC Hacking.
- One "Biero OT/ICS Resource list" entry points to a Rick Astley YouTube video and is a joke entry by its own description.
- Some entries link to apparent unofficial copies of paid material: a PDFDrive-labelled textbook, a Google Drive copy of a book, and a downturk.net "free e-learning" page.
- Requirements section lists NIST SP 800-82r3, NIST CSF 2.0, DoD Control Systems SRG, BSI OPC UA Security Analysis, CWE View 1424 (weaknesses addressed by ISA/IEC 62443), an IACS STAR scoring calculator, and EBIOS RM.
- OSINT section lists internet-wide search engines (Shodan, Censys, FOFA, ZoomEye) and honeypot detection; news section lists Telegram channels.

## Verbatim
None needed.

## Relevance
- Curated keep/stale judgement is in the research notes.
- Inference: exclude the apparent unofficial copies from project references on licensing grounds; whether they are infringing was not determined.
- Inference: internet-wide OSINT against third-party assets is outside an authorised single-site scope unless the Rules of Engagement include it.
