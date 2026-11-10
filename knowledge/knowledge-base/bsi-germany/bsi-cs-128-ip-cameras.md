---
title: "Security of IP-based surveillance cameras (BSI-CS 128)"
url: "https://www.allianz-fuer-cybersicherheit.de/"
type: standard
trust: primary
accessed: 2026-11-10
published: 2016-11-08
owasp_ot: [1, 5, 10]
version: "BSI-CS 128, Version 1.10 of 08/11/2016"
local_file: "sources/bsi-germany/BSI-CS_IPBasedSurveillanve.pdf"
---

# BSI-CS 128: Security of IP-based surveillance cameras

## Summary
Five-page BSI recommendation (category "IT in the company", not ICS-specific) on selecting, installing and operating IP surveillance cameras securely. Motivated by incidents (Carbanak camera spying 2013, Insecam 2014, Mirai 2016). Read from the user's local PDF; the canonical BSI/Allianz für Cybersicherheit page for this document was not confirmed.

## Key facts
- Procurement: avoid cloud-concept cameras; prefer wired over Wi-Fi in critical areas; minimal services/ports or ability to disable them; encrypted protocols (TLS/SSH); role/rights concept; manufacturer must state the end of service (EOS) for patches, distinct from end of life (p.1-2).
- Installation: embedded web servers should not be exposed to the Internet; strong passwords or certificate authentication; disable unneeded services, especially Telnet and SNMPv1/v2; block camera-initiated Internet connections except whitelisted targets; never allow Telnet (23) from outside; avoid port forwarding (p.2).
- Operate cameras in a separate physical network or VLAN (p.3).

## Verbatim
- "In general, the following applies: Embedded web servers, such as in the case of surveillance cameras, are typically not suitable to be made fully accessible via the Internet." (p.2)

## Relevance
Peripheral to OT pentesting: IP cameras and similar IoT devices often sit on plant networks and are a common unmanaged asset (OWASP OT #1) and weak-credential entry point (#5, #10). Useful as a hardening checklist for non-PLC network devices found during discovery. Dated 2016.
