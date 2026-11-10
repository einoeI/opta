---
title: "GRFICSv3: Open Source OT Security Lab"
url: "https://github.com/Fortiphyd/GRFICSv3"
type: tool
trust: primary
accessed: 2026-11-09
published: 2026-10-20
owasp_ot: [5,6,7,8,9]
version: "main at 8d611b7, 2026-10-20"
license: "GPL-3.0"
---

## Summary
A containerized OT/ICS cyber-physical lab from Fortiphyd Logic that simulates an industrial chemical plant with a 3D visualization.
It bundles a soft PLC, HMI, engineering workstation, router/firewall, Kali, MITRE Caldera with an OT plugin, and optional Wazuh and Zeek.
It is actively developed and suited to attack-workflow and detection exercises.
Nothing was cloned or run; facts come from the README, repository page, commit list and `docker-compose.yml`.

## Key facts
- Repository page on the access date: 293 stars, 52 forks, 286 commits, no archive notice. Top-level folders: attacker, caldera, docs, images, packaging, plc, router, scadalts, simulation, wazuh, workstation, zeek.
- Newest commits are dated 2026-10-20, including 8d611b7, "Merge pull request #68 from Fortiphyd/fix/macvlan-vlan-isolation".
- Compose services: simulation, plc, ews, hmi, kali, router, caldera, plus wazuh and zeek under the `siem` profile.
- The PLC is OpenPLC (`192.168.95.2:8080`); the HMI image is ScadaLTS-based; the router/firewall has a management UI on both zones.
- Networks: `b-ics-net` 192.168.95.0/24 on macvlan parent `eth0.95`; `c-dmz-net` 192.168.90.0/24 on macvlan parent `eth0.90`. The compose file tells the user to replace `eth0` with the host's actual NIC.
- Built-in tools: Kali, Caldera with OT plugin, custom firewall and Suricata interface, optional Wazuh SIEM (adds about 3-4 GB).
- Zeek sees mirrored traffic in both zones and forwards selected events, such as Modbus write commands, to Wazuh. The mirror needs a real Linux kernel (native Linux or Docker Engine inside WSL2, not Docker Desktop's VM) and must be re-enabled after every restart.
- Reset: `docker compose down --volumes` wipes firewall rules, PLC programs and HMI configuration; everything re-initialises from image defaults.
- Default lab credentials are published in the README, such as `openplc : openplc` and `kali : kali`.
- It includes a virtual walk-through for physical-security findings, with a Vulnerabilities Found tracker.
- Prerequisites: Docker and Docker Compose for prebuilt images; Git and Git LFS for source builds. Fortiphyd sells commercial sector-specific simulations and hosted ranges separately.

## Verbatim
- "**GRFICSv3** is a fully containerized OT / ICS cyber-physical security lab that simulates a industrial chemical plant."

## Relevance
- Inference: a suitable aggressive-mode testbed for Modbus and OpenPLC attack workflows, Caldera OT emulation and detection validation.
- Inference: not a fidelity testbed for the project's first device profile (AXC F 2152). It contains an OpenPLC soft PLC, so vendor firmware, services and CVEs are not represented.
- Inference: because the networks attach to a host NIC through macvlan VLAN sub-interfaces, run it on a dedicated or disconnected NIC and never on a host attached to an OT LAN.
- Gap: the README does not mention a safety instrumented system or list protocols beyond Modbus; check the `docs` folder and images before relying on either.
