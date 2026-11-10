---
title: "IANA Service Name and Transport Protocol Port Number Registry"
url: "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv"
type: dataset
trust: primary
accessed: 2026-11-10
published: unknown
owasp_ot: [1]
version: "CSV downloaded 2026-11-10 (1,158,903 bytes, 14,545 records)"
local_file: "sources/frameworks/iana-service-names-port-numbers.csv"
---

# IANA Service Name and Port Number Registry

## Summary
The authoritative registry of assigned TCP/UDP/SCTP/DCCP port numbers and service names, available as machine-readable CSV. Used on 2026-11-10 to verify the standard ICS ports in `catalog/ot-ports.csv`. Several common ICS ports are either registered to unrelated services or not registered at all, so a port number alone does not identify an OT protocol.

## Key facts
- Registered ICS/OT services: 102 iso-tsap (S7comm, IEC 61850 MMS); 502 mbap (Modbus); 802 mbap-s (Modbus Security); 1089-1091 Foundation Fieldbus HSE; 2221 ethernet-ip-s (EtherNet/IP over TLS); 2222 EtherNet-IP-1 (implicit I/O); 44818 EtherNet-IP-2 (explicit messaging); 2404 iec-104; 2455 wago-io-system; 4840 opcua-tcp / opcua-udp; 4843 opcua-tls; 5094 hart-ip; 20000 dnp; 34962-34964 PROFINET RT unicast, RT multicast, context manager; 47808 bacnet; 1883/8883 MQTT; 319/320 PTP; 5683/5684 CoAP.
- Registered to unrelated services despite ICS use: 1911 (mtp; Niagara Fox), 1962 (biap-mp; PC WORX), 9600 (micromuse-ncpw; Omron FINS), 10001 (scp-config; tank gauges).
- Not in the registry: 4911 (Niagara Fox TLS), 17725, 20547 (ProConOS), 41100 (PLCnext remoting).

## Verbatim
- Registry CSV columns: "Service Name,Port Number,Transport Protocol,Description,Assignee,Contact,Registration Date,Modification Date,Reference,Service Code,Unauthorized Use Reported,Assignment Notes"

## Relevance
Primary basis for the generic rows of `catalog/ot-ports.csv` (OWASP OT #1 asset/service discovery). Shows why passive protocol identification (e.g. Zeek ICSNPP, Wireshark dissectors) matters more than port-number guessing.
