---
title: "Monitoring and Anomaly Detection in Production Networks (BSI-CS 134E)"
url: "https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Industrielle-Steuerungs-und-Automatisierungssysteme/Download/download.html"
type: standard
trust: primary
accessed: 2026-11-10
published: 2019-10-14
owasp_ot: [1, 6]
version: "BSI-CS 134E, Version 1.00 of 14/10/2019"
local_file: "sources/bsi-germany/BSI-CS_MonitoringAndAnomalyDetection.pdf"
---

# BSI-CS 134: Monitoring and Anomaly Detection in Production Networks

## Summary
Seven-page BSI recommendation explaining monitoring and anomaly detection for production networks and listing required features of anomaly-detection systems by category. Anomaly detection learns the normal state in a training phase from passive taps or mirror ports, then flags deviations. Read from the user's local PDF.

## Key facts
- Anomalies include (p.3): a new device, DHCP requests, packets from unknown devices, communication between devices that never talked before, new or unusual protocols, events at unusual times, public IP addresses, address or port scans, changes in network quality; in logs: unusual errors, unsupported or first-time function calls, malformed packets, unknown function codes; in process data: out-of-range values, changed frequency, cycle time or variance.
- Detection works by passive sensors (ideally taps; alternatively switch port mirroring) collecting data over a training phase; every first-time event is an anomaly, so false positives must be tuned (p.3-4).
- Required system features (ch. 6, p.4-5): device, protocol and link overview; detection of new devices, new device pairs, new ports, new protocols, connections to insecure networks, missing encryption; detection of invalid or never-before-used ICS function codes and access to unusual addresses; process-value deviation detection; export for forensics; role model; integration into alarm systems.

## Verbatim
- "Generally noteworthy events such as address or port scans" (listed as an anomaly, p.3)
- "To identify anomalies, the normal state of a system – in this case, a production network – must first be known." (p.3)

## Relevance
Defines what a mature OT site should detect, so it doubles as a test checklist for OWASP OT #6 (missing incident detection): on a testbed, each listed anomaly (new device, port scan, unknown Modbus function code, write to an unusual register) can be generated and the detection result recorded. It also means active discovery on a monitored live network will raise alarms and must be announced under the rules of engagement.
