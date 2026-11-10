---
title: "AXC F 2152 – Change Notes (Application note 108427_en_51)"
url: "https://www.phoenixcontact.com/en-pc/products/controller-axc-f-2152-2404267"
type: vendor-doc
trust: primary
accessed: 2026-11-10
published: 2025-08-13
owasp_ot: [2, 3, 5, 10]
version: "108427_en_51 (covers firmware 1.0.0 to 2025.6.0); en_52 exists (see knowledge-gaps notes)"
local_file: "sources/phoenix-contact/ah_en_axc_f_2152_change_notes_108427_en_51.pdf"
---

# AXC F 2152 Change Notes (en_51)

## Summary
Phoenix Contact's application note listing every change between firmware 1.0.0 and 2025.6.0 for the AXC F 2152 (item 2404267), 101 pages. Each firmware section lists known limitations, functional changes and "Security updates" (component name + CVE IDs, plus PSIRT items). It is the origin of the project's `vulnerable_2022.0.8.csv` (266 component CVEs fixed after 2022.0.8). The user supplied the PDF; the product page it is downloaded from returned HTTP 403 to automated fetches. A newer edition, en_52, exists and was not yet read.

## Key facts
- Current firmware per this edition: 2025.6.0; product revision VC 19 ships with 2024.0.8 LTS (p.1).
- Release branches: LTS lines (2019.0, 2020.0, 2021.0, 2022.0, 2023.0, 2024.0) plus feature releases; hotfixes of an LTS line only contain that branch's fixes (p.1, p.3).
- Firmware 2022.0.8 LTS is on the 2022.0 LTS branch; its own section (ch. 22, p.54-55) lists security updates for BusyBox, Curl (15 CVEs), Cyrus SASL, LIBEXPAT, LIBXML, OpenSSL (CVE-2022-0778), OpenVPN, Vim (~70 CVEs), ZLib (CVE-2018-25032), "HMI hardening against DoS attacks", IPv6 firewall rule fixes and the Unified Automation OPC UA SDK update to 1.7.7.
- 2022.0.8 note: OpenSSH was updated from 8.4p1 to 8.8p1; SHA1 and BusyBox are announced for removal in future releases (p.54).
- "Security Profile" was introduced in 2022.0.3 LTS (ch. 24): activating it via WBM requires a licence, reboots the PLC, deletes the project, resets nearly all configuration and deactivates potentially insecure services. So it can exist on 2022.0.8, and whether it is active changes the attack surface.
- Later Security Profile changes: 2024.0.9 LTS fixed `AllowTcpForwarding` from yes to no in the profile's sshd config; 2025.0.2 keeps the `admin` user when activating, lets services (Modbus client TCP, OPC UA client, Proficloud, software update, etc.) be toggled, and allows ICMP through the firewall (ch. 6, ch. 9).
- Modbus: the change notes mention only a "Modbus TCP client" (introduced in 2024.6.0, used with PLCnext Engineer 2024.6+, deactivated by factory default) and libmodbus updates. No Modbus TCP server is described, consistent with port 502 being absent from the vendor port list (knowledge-base/phoenix-contact/plcnext-port-list.md).
- 2024.0.9 LTS lists a "PxC PSIRT Report": bash scripts runnable by the `plcnext` group or `plcnext_firmware` user were vulnerable to environment-variable injection (ch. 9).
- Firmware updates restart the controller; plant availability is not guaranteed during the update (p.1).

## Verbatim
- "This document contains all changes made between firmware version 1.0.0 and the current firmware version of the AXC F 2152 controller (item no. 2404267). Current firmware version: 2025.6.0" (p.1)
- "When the "Security Profile" is activated, the PLC is rebooted and set into a secure state. This includes deleting the project, resetting nearly all configurations and deactivating potentially insecure system services." (ch. 24, 2022.0.3 LTS)
- "As factory default setting, the feature Modbus TCP client is deactivated." (ch. 8, 2024.6.0)

## Relevance
Ground truth for the reference device: the CVE list per firmware (OWASP OT #2), supplier patch cadence (#3), and hardening state via the Security Profile (#10, #5). For the device profile, record firmware version and whether the Security Profile is active. Keep Modbus/502 as "Unresolved" for the device (an app could add a server; not covered here). Re-read en_52 to extend the list beyond 2025.6.0.
