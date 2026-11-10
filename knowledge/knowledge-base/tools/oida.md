---
title: "OIDA – OT/ICS Dynamic Assessment Framework"
url: "https://github.com/f0rw4rd/oida"
type: tool
trust: primary
accessed: 2026-11-10
published: unknown
owasp_ot: [1, 4, 5, 6, 9]
license: "AGPL-3.0"
version: "PyPI package oida-ics; no GitHub release listed; 739 commits as of 2026-11-10"
---

# OIDA (OT/ICS Dynamic Assessment Framework)

## Summary
Open-source CLI to scan, discover, fuzz and assess OT/ICS protocols ("Scan. Fuzz. Assess. Responsibly in OT."), described as covering 29 protocols across ICS/SCADA, energy, building automation, healthcare, manufacturing and Layer 2/fieldbus. Defaults are read-only; writes and state changes need an explicit `--confirm`. It ships Docker mock services ("shooting range") for rehearsal without hardware. The project site lists Limes Security as a partner. Per the user (2026-11-10), the author is a pentester from Limes Security (an OT security consultancy); the user has used the tool and recommends it as a concise, high-coverage tool for OT pentesters. Facts below are from the GitHub README and getoida.dev, fetched 2026-11-10.

## Key facts
- Install: `pip install 'oida-ics[all]'`; protocol stacks are optional extras, a bare install has none; the README says it "runs from a single binary, so it works air-gapped" (README).
- Protocols named in the README: Modbus, OPC UA, Siemens S7, DNP3, IEC 60870-5-104, BACnet, EtherNet/IP, PROFINET, HL7, DICOM, MQTT, SNMP, "and many more"; getoida.dev counts 29 (ICS/SCADA 8, energy 5 incl. MMS, building 5 incl. KNX, healthcare 4, manufacturing 2 incl. MTConnect, Layer 2/fieldbus 5 incl. PROFINET and GOOSE).
- Features (getoida.dev): protocol scanning with JSON/CSV export; passive and active asset discovery including from PCAP; security checks for default credentials, auth bypass, writable registers and missing IEC 62351 protections; boofuzz-based fuzzers with crash detection and radamsa; Docker shooting range.
- Discovery example: `oida discovery eth0` (README).
- Safety model: read-only default, `--confirm` for writes; warning that "The tool can crash devices, trigger physical actuator writes, and extract credentials."; the site says "Authorized testing only" and recommends rehearsing against the Docker range before production.
- Licence AGPL-3.0; support via QuellSec is mentioned in the README; author shown only as GitHub user f0rw4rd.

## Verbatim
- "Defaults are read-only. Writes and state changes need an explicit `--confirm`." (README)
- "Passive discovery and near-passive protocols like PROFINET DCP let you map your network without disrupting it." (getoida.dev)

## Relevance
The project's intended active testing engine for the testbed/aggressive mode, and a source of passive discovery for the live/safe mode (OWASP OT #1, #9; #5 for credential/auth checks; #4 for fuzzing on the testbed only; #6 by generating events to test detection). Its JSON/CSV output is what the planner/report console should ingest. A gap-audit pass on 2026-11-10 wrongly reported no public trace of OIDA; the repo and site are reachable. Release dates and which protocols are mature were not verified; record the OIDA version in every run manifest.
