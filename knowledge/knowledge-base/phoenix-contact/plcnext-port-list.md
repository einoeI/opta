---
title: "Port list (PLCnext Security)"
url: "https://security.plcnext.help/se/Appendix/Port_list.htm"
type: vendor-doc
trust: primary
accessed: 2026-11-09
published: 2026-08-17
owasp_ot: [1,7,9,10]
version: "Revision 024 at security.plcnext.help; Revision 022 (2026-04-20) at the plcnext-community.net mirror"
---

## Summary
Vendor port list for PLCnext devices, in two tables: ports under "PLCnext Security Profile standard" and further ports opened when components are switched on ("activatable"). The requested URL (plcnext-community.net/robohelp/security/se/Appendix/Port_list.htm) serves Revision 022. The same page on security.plcnext.help is Revision 024. The two differ only in the revision/date line. The page states no firmware applicability and lists no direction or default-state columns.

## Key facts
Full table, identical on both copies:

**PLCnext Security Profile standard**

| Description | Protocol | Port |
|---|---|---|
| Common remoting, e.g. via PLCnext Engineer | TCP | 41100 |
| HTTPS, Proficloud, eHMI (web server for eHMI and WBM) | TCP | 443 |

**PLCnext Security Profile activatable** ("When components are switched on, further ports are enabled:")

| Description | Protocol | Port |
|---|---|---|
| NTP (Network Time Protocol) | UDP | 123 |
| Common remoting, e.g. via PLCnext Engineer | TCP | 41100 |
| SSH connections, e.g. for secure shell connection or SFTP connection | TCP | 22 |
| HTTPS, Proficloud, eHMI (web server for eHMI and WBM) | TCP | 443 |
| OPC UA | TCP | 4840 |
| MATLAB/Simulink in External Mode | TCP | 17725 |
| SNMP (Simple Network Management Protocol) | UDP | 161 |
| PROFINET unicast/multicast ports | UDP | 34962-34964 |
| PROFINET device ports | UDP | 49152-65535 |
| Syslog | TLS | 6514 |

- Modbus TCP and port 502 do not appear on either copy.
- The table lists the protocol for Syslog as "TLS" rather than TCP.
- The page carries no firmware version, so its applicability to 2022.0.8 is not stated.

## Verbatim
- "When components are switched on, further ports are enabled:"
- Footer: "Published/reviewed: 2026-08-17 • Revision 024" (security.plcnext.help); "Published/reviewed: 2026-04-20 • Revision 022" (plcnext-community.net).

## Update 2026-11-10
- The user's link https://www.plcnext-community.net/security/port_list/ embeds the same page in an iframe (`/robohelp/security/se/Appendix/Port_list.htm`). Both copies were re-parsed on 2026-11-10 and the table is unchanged; the revision line no longer renders in the static HTML.
- The table is now machine-readable in `catalog/ot-ports.csv` (scope `plcnext`, state `standard`/`activatable`), queryable with `python3 ot_ports.py --scope plcnext`.
- The change notes explain the missing Modbus port: the firmware only adds a Modbus TCP *client* (2024.6.0, off by default), not a server (knowledge-base/phoenix-contact/axc-f-2152-change-notes-en51.md).

## Relevance
Primary input for the AXC F 2152 device profile and reachability filter (OWASP OT #1, #9). Contradicts `research-notes.md` "Exposed services (per vendor port list)", which includes Modbus TCP 502. Inference: only 41100/TCP and 443/TCP are the standard-profile baseline; SSH 22 is activatable, so on-device enumeration cannot be assumed available. Actual exposure on 2022.0.8 must be confirmed by `ss -tlnp`/nmap and labelled accordingly.
