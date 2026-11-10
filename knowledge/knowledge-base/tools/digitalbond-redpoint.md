---
title: "Digital Bond Redpoint (ICS NSE scripts)"
url: "https://github.com/digitalbond/Redpoint"
type: tool
trust: primary
accessed: 2026-11-10
published: unknown
owasp_ot: [1, 9]
license: "Same as Nmap (per script headers)"
version: "last commit 2016-03-08 (unmaintained)"
---

# Digital Bond Redpoint

## Summary
Collection of 13 Nmap NSE scripts by Stephen Hilt (Digital Bond) for identifying and enumerating ICS devices. Several were later merged into Nmap (s7-info, enip-info, bacnet-info, fox-info, omron-info, pcworx-info). The repository has not changed since 2016-03-08. Script files were downloaded and their port rules and categories read on 2026-11-10; the data is in `catalog/ot-ports.csv`.

## Key facts
- Scripts: BACnet-discover-enumerate, atg-info, codesys-v2-discover, cspv4-info, dnp3-info, enip-enumerate, fox-info, modicon-info, omrontcp-info, omronudp-info, pcworx-info, proconos-info, s7-enumerate.
- Ports and categories: `proconos-info` TCP 20547 (discovery, version); `pcworx-info` TCP 1962 (discovery, version); `dnp3-info` TCP 20000 (discovery, intrusive); `modicon-info` TCP 502 (discovery, intrusive); `s7-enumerate` TCP 102 (discovery, intrusive); `enip-enumerate` TCP 44818 (discovery, intrusive); `cspv4-info` TCP 2222 (discovery, intrusive); `BACnet-discover-enumerate` UDP 47808 (discovery, intrusive); `fox-info` TCP 1911 (discovery, intrusive); `omrontcp-info`/`omronudp-info` 9600 (discovery, version); `atg-info` TCP 10001 (discovery).
- `codesys-v2-discover` has a port rule matching any TCP port and states no default port (category discovery, safe).
- ProConOS (20547) and PC WORX (1962) are Phoenix Contact / KW-Software runtimes relevant to older Phoenix Contact controllers.

## Verbatim
- `portrule = shortport.portnumber(20547, "tcp")` (proconos-info.nse)

## Relevance
Still the only source for some ICS probes (ProConOS, DNP3, CSPv4, ATG), but unmaintained for ten years and several scripts are `intrusive`. Treat as testbed-first; prefer the Nmap-shipped versions where they exist. Corrects the handoff prompt's assumption that Redpoint is a current tool.
