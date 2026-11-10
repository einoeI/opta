# OT Pentesting — Research Notes

**Project:** Authorized, white-hat OT/ICS penetration-testing research + a hands-on
presentation. Implementation to be focused on the **OWASP OT Top 10 (2025)**.
**Primary target:** Phoenix Contact **AXC F 2152** (article 2404267, firmware
**2022.0.8 LTS**), a PLCnext controller running Yocto Linux (OSADL real-time).
**Research dates:** 2026-11-03 → 2026-11-09. Web sources accessed **2026-11-09**
unless noted. All sources are listed in the "Sources" section with access dates.

> **Evidence discipline (carried from the parent project).** Label every claim:
> **Published** (a primary advisory/paper says it) · **Version-candidate** (the
> version matches an affected range, but exploitability is unestablished) ·
> **Reproduced** (a defined test produced the effect) · **Simulated** (effect
> staged, vuln not exercised) · **Unresolved**. A CVSS score is *context*, never
> a confirmed-exploitable verdict. Distinguish *observed* from *inferred*.

---

## 1. LLMs on constrained hardware (Raspberry Pi 3 B)

- **Do not host an LLM on a Pi 3 B.** 1 GB RAM is the wall. Only sub-2B quantized
  models fit, and they are too weak for trustworthy pentest reasoning or report
  writing (they hallucinate register addresses / advisories — the exact failure
  the evidence discipline exists to prevent). Keep the Pi as a **target**.
- **Training/fine-tuning on the Pi: impossible** (inference only). More
  importantly, **fine-tuning is the wrong tool** for OT methodology + report
  style: expensive, needs curated data, goes stale, and bakes in un-auditable
  knowledge. Use **prompting + skills + RAG** over your own docs instead.
- If offline/air-gapped inference is required, use a **Pi 5 16 GB or a mini-PC**
  (runs 7–8B quantized at ~5–10 tok/s), not a Pi 3. Otherwise use the Claude API.

## 2. Existing tools / repos landscape

| Project | What it is | Role for us |
|---|---|---|
| **selmux/ot-security-agent-skills** | Passive OT **forensics/IR** as AI agent skills (Modbus, BACnet, S7, IEC-104). PCAP in → JSON findings → timeline. Never touches live devices. | Pattern to copy (SKILL.md structure, safety sections); defensive analysis layer. |
| **OIDA (f0rw4rd)** | Active **dynamic assessment** CLI, "NetExec for ICS", 29 protocols; scan/discover/fuzz; read-only default, writes behind `--confirm`; Docker "shooting range" mock services. AGPL-3.0. | The **active testing engine** to orchestrate — testbed/mock only. |
| **Anthropic-Cybersecurity-Skills (mukul975)** | ~753 skills w/ ATT&CK mappings, incl. OT/SCADA. Apache-2.0. | Mine for structure; OT depth unverified. |
| **Pentest-agent benchmarks** | AutoPenBench (33 Dockerized tasks, milestone scoring), PentestEval (stage-level), AutoPentest-Bench (reproducible targets), Cybench (40 CTFs), CyberGym (best agent reproduced only **11.9%** of real vulns), SEC-bench (~$0.87/instance). | Benchmark patterns: containerized targets, milestone/stage scoring. Reality check: LLM pentest agents are weak on realistic targets. |
| **hslatman/awesome-industrial-control-system-security** | Canonical curated ICS list (scanners, Conpot, GRASSMARLIN, 4SICS PCAPs). | Source of tools to wrap, not reinvent. |

**Key conclusion:** selmux (passive) and OIDA (active) are **complementary**, and
**neither** provides the middle layer we care about: AI skills + standards
mapping + reproducible reports. That middle layer is the contribution.

## 3. The configurable interface idea — feasibility

**Verdict: build the planner/report console; do NOT build a live tool-runner in v1.**

- **Build (A):** pick a device profile → tailored test plan + applicable CVEs +
  OWASP-OT/ATT&CK/CVSS mapping → ingest PCAPs + tool outputs → **labeled,
  reproducible report**. This is the gap nobody fills; it's safe and small.
- **Don't build (B):** a UI button that *executes* OIDA/fuzzers at a device. OIDA
  can crash devices / trigger actuator writes; one-click live testing violates
  NIST SP 800-82 and risks the real PLC. Operators run dangerous tools
  **out-of-band** (testbed/mock) and **upload the JSON**.
- **Implementation (lazy):** Flask (reuse existing HMI pattern) + stdlib +
  Jinja2. Device profiles & mappings as flat JSON/YAML. No DB, no live execution
  in v1. Report = Markdown → PDF only if asked.
- **Reproducibility is designed in:** every run writes a manifest (tool versions,
  target image hash, inputs, timestamps); findings carry the evidence label +
  evidence hashes; same inputs → byte-identical report except timestamp.
- **YAGNI flag:** for one tester on one testbed, a config-file + CLI does ~90%.
  The UI earns its place only because the goal is a *presentation* demo.

## 4. CVE / CPE and the vulnerability databases

- **CVE ↔ CPE are linked:** a CVE record's `configurations → cpeMatch` lists the
  affected CPEs with version ranges (`versionStartIncluding` etc.). That linkage
  is how "which CVEs affect product X version Y" works.
- **NVD API 2.0:** `cves/2.0?cpeName=` (exact) or `?virtualMatchString=` +
  `versionStart/End/Type` (range); `cpes/2.0?keywordSearch=` to find the CPE.
  Rate limit 5 req/30s (50 with free key).
- **The NVD CPE enrichment crisis (2024–2026):** NVD supplied CPEs for only
  ~41% of 2024 CVEs; NVD-authored CPE fell 93%→56%; old backlog is "Deferred."
  **CPE is the one field nobody else backfilled.** Without a CPE, a CPE-based
  query **silently misses** the CVE — worse for OT. ⇒ **Do not make NVD CPE the
  spine.**
- **For OT, prioritize:** (1) **CISA ICS CSAF** (machine-readable, OT-focused),
  (2) the **vendor PSIRT** — for Phoenix Contact this is **CERT@VDE**
  (`phoenixcontact.csaf-tp.certvde.com`), (3) **NVD** only as CVSS/cross-ref.

## 5. CIRCL Vulnerability-Lookup as the aggregation spine — VERIFIED

- **vulnerability-lookup (CIRCL)** aggregates ~**69 sources** (NVD, cvelistV5,
  GHSA, OSV, **~45 CSAF feeds** incl. CISA/Siemens/Schneider/ABB), does
  **cross-source correlation**, and backfills missing CPEs via **CISA ADP
  Vulnrichment**. Public API at `vulnerability.circl.lu`. AGPL-3.0.
- **Use it as the single spine** instead of hand-gluing NVD+CISA+vendor.
- **Verified for our device** (via `probe_vuln_lookup.py`, 2026-11-09):
  search `phoenix contact / axc f 2152 (2404267)` → **4 CVEs**
  (CVE-2020-12517/12518/12519/12521, PLCnext/PROFINET), **all assigned by
  CERT@VDE**, cross-sourced from cvelistV5+NVD. CERT@VDE feed itself reachable
  (115 TLP:WHITE advisories) — but not needed online, since its data flows into
  CIRCL. Keep it only as an air-gap fallback.
- **API shapes learned:** `/api/browse/` (vendors), `/api/browse/<vendor>`
  (products), `/api/search/<vendor>/<product>` (results keyed by source, each a
  list of `[cve_id, record]`), `/api/vulnerability/<id>`. **Product-string choice
  matters:** `axc f 2152 (2404267)`→4, `phoenixcontact/axc_f_2152_firmware`→10.
  Query **several vendor/product aliases and union** or you under-report.
- **Caveat:** the public instance **throttles aggressively** (429s). Use backoff
  + caching, or an API key / self-host for volume.

## 6. Firmware component CVEs = an SBOM/SCA problem (the core insight)

- A **device-level CPE/advisory search finds component CVEs = 0.** Component CVEs
  (glibc, curl, openssl, vim…) never carry the PLC's CPE.
- **Cross-check done** (`crosscheck_firmware.py`, 2026-11-09): the vendor
  change-notes list `vulnerable_2022.0.8.csv` = **266 component CVEs** affecting
  2022.0.8 (everything fixed in 2022.6.0+). Results:
  - **263/266 (98%)** enriched with CVSS by CIRCL (the 3 gaps were throttle
    casualties, not genuinely missing).
  - **19 CRITICAL, 101 HIGH.** Top: glibc 23218/23219, zlib 37434, curl/git RCE
    class, strongswan, openssl, glib, rsync (all CVSS 9.8).
  - **0 caught by a device-level search** — proves the gap with real numbers.
- **The vendor change-notes list is ground truth** for "what's unpatched on this
  firmware." CIRCL/OSV's role is **enrichment (CVSS), not discovery.**

## 7. Discovering what's inside the device (non-fuzzing)

Three access levels, all discovery not fuzzing:

- **A. On-device enumeration (SSH/admin — best, ground truth).** PLCnext = Yocto
  Linux, `dpkg` present in newer FW, SSH as admin, uses **podman**. Read-only
  commands: `/etc/os-release`, `uname -a`, `dpkg -l`, version probes
  (`openssl version`, `busybox`, `python3 --version`…), `ss -tlnp` + `ps`
  (listening services → fuzz targets), `podman images`. **Non-intrusive — safe on
  production.** Build the SBOM on the laptop (don't run scanners on the PLC).
- **B. Firmware-image analysis (offline, totally safe).** Unpack the firmware →
  **EMBA** / **Syft+Grype** / **cve-bin-tool**. This is the automated version of
  what the vendor did to make the change-notes CSV.
- **C. Network/passive (limited access).** nmap `-sV`, SNMP sysDescr, banners,
  OIDA passive discovery. Gives *service* versions, not the full component list.

- **Matching DB for components: OSV.dev** (package/purl-aware; `POST /v1/query`,
  `/v1/querybatch`; `osv-scanner --sbom=…`). Better than NVD/CIRCL for packages.
- **Caveat — distro backports** cause version false positives (patched package
  keeps old version). Fix: cross-check generated SBOM ∩ OSV against the vendor
  change-notes/VEX. The two sources correct each other.
- **Curate per-device:** build the SBOM once, store it in the device profile,
  re-match later. The change-notes CSV is a partial, manual SBOM-delta.

## 8. Getting a firmware snapshot without touching the live system

- **Best: download the firmware from Phoenix Contact** (product page, item
  2404267, Firmware section) — **zero contact with the live PLC.** Format: older
  = RAUC `.raucb` (signed SquashFS), newer = `.tar.xz`. Signed ≠ encrypted; the
  2022.0.8 payload should unpack (`unsquashfs`/`binwalk`/`tar`). Get the **exact
  2022.0.8** file to match device + CSV.
- **Read-only live snapshot over SSH** (testbed-friendly): `tar`/`rsync` the
  rootfs read-only, or the enumeration from §7A. Reads only; diff against the
  stock image to find local modifications.
- **SD-card imaging: skip** — the AXC F 2152 runs from **internal flash/eMMC**;
  the SD card is optional expansion, off by default. Not a reliable OS source.

## 9. Do all vendors provide firmware? No — two axes

- **Obtainable?** public download (Phoenix Contact, WAGO, Siemens via SIOS,
  Rockwell) → account-gated → distributor/contract-only → not distributed.
- **Analyzable?** Linux PLC (PLCnext, WAGO, Beckhoff) = SBOM-friendly; proprietary
  RTOS (classic Siemens S7, VxWorks on Rockwell/Schneider) = binary/hard;
  **signed+encrypted** firmware = blocked for static analysis (increasingly common).
- **Trend your way:** EU **CRA** + CISA **SBOM** push vendors to publish SBOMs/VEX
  directly. **Design the tool for a fallback chain**, not firmware-always:
  vendor SBOM/VEX → firmware extraction → on-device enumeration → vendor
  advisories/change-notes → network fingerprinting. The device profile records
  *which are possible for this device*.

## 10. Does SBOM→CVE hunting even make sense for a pentest?

- **As a primary pentest activity: mostly no.** CVE ≠ exploitable ≠ reachable. A
  266-CVE wall is a **patch-management artifact**, not a finding. Real OT findings
  are usually **design/config**: unauthenticated protocols, writable registers,
  default creds, unauthenticated firmware update, exposed engineering access.
- **Where it does matter:** (1) **filter by reachability** — intersect SBOM CVEs
  with **listening services** (`ss -tlnp` + nmap) → a short, real list (OpenSSH,
  nginx, SNMP, OpenSSL-on-TLS, the OPC UA/Modbus stack). (2) Keep the full list as
  a **defensive/patch deliverable** (appendix). (3) It tells you **what to fuzz
  next**.
- Pipeline: `SBOM → OSV → full list (defensive)` and `∩ listening services →
  short list (pentest candidates to reproduce)`. Reachability is the discriminator.

## 11. Service/port lists already exist — tool curates, doesn't invent

- **Generic ICS:** nmap **NSE** + Digital Bond **Redpoint** scripts
  (`modicon-info`/502, `s7-enumerate`/102, `enip-enumerate`/44818, `dnp3-info`/
  20000, `BACnet-discover-enumerate`/47808, `pcworx-info`, `codesys`…).
- **Per-device (authoritative):** Phoenix Contact **security.plcnext.help** has an
  AXC F 2152 page, a **Port list** (services conditional on enabled components:
  WBM/HTTPS, SSH 22, OPC UA 4840, Modbus 502, SNMP 161, remote eng. 41100,
  PROFINET ranges, NTP 123), and a **Security checklist**.
- **Two-mode (aggressive testbed / safe runtime) is standard:** nmap **`safe` vs
  `intrusive`** script categories; passive-vs-active tooling (OIDA read-only
  default vs `--confirm`/fuzz); NIST SP 800-82 (aggressive only in
  replicated/simulated env; production read-only/passive).
- **The gap = the synthesis:** a per-device, mode-aware runbook binding
  {device profile → vendor port list → NSE/Redpoint/OIDA probes, split into
  `safe`/`aggressive`}. Inputs all exist; the binding doesn't. That's the tool's job.

## 12. OT threat model & OWASP OT Top 10 (2025) — the implementation frame

- **"Assume the attacker is already inside" is the standard OT model.** OT is
  rarely internet-facing; the realistic adversary pivots IT→OT, or comes via a
  compromised engineering workstation / insider / supply chain / remote
  maintenance. Endpoint security is weak by design; the model is **network
  segmentation (zones & conduits)**. Scope engagements from an **assumed attacker
  position** (e.g. "adjacent on the OT LAN").
- **A severe SSH/auth problem under "already inside" is a legitimate high finding**
  — often full device control. But **severity = reachability, not CVSS**: an SSH
  flaw reachable only from an isolated mgmt zone is lower risk than a writable
  Modbus port on the flat plant LAN. **Zones/conduits (#7) is the multiplier.**

### OWASP OT Top 10 — 2025 Edition (verbatim list, from the local PDF, p.86–89)

1. Unknown Assets and Unmanaged External Access
2. Devices with known Vulnerabilities/Issues
3. Inadequate Supplier/Supply Chain Management
4. Loss of Availability
5. Insufficient Access Control
6. Missing Incident Detection/Reaction Capabilities
7. Broken Zones and Conduits Design
8. Missing Awareness
9. Insufficient Security Capabilities
10. Missing Hardening

### How this session's threads map onto the Top 10

| Thread | OWASP OT Top 10 item(s) |
|---|---|
| SBOM → component CVEs (§6, §7) | **2** Devices with known Vulnerabilities |
| Service/port enumeration (§11) | **1** Unmanaged External Access, **9** Insufficient Security Capabilities |
| Reachability / can-I-cross-the-conduit | **7** Broken Zones and Conduits Design |
| SSH / default creds / weak auth (§12) | **5** Insufficient Access Control |
| Fuzzing / DoS / reboot (e.g. CVE-2020-12521) | **4** Loss of Availability |
| Safe-vs-aggressive mode (don't break prod) | respects **4** (availability is paramount) |
| Monitoring/detection during the test | **6** Missing Incident Detection/Reaction |
| Supply-chain / firmware provenance (§8, §9) | **3** Inadequate Supply Chain Management |

**Implementation stance:** make the assume-breach position an explicit scope
input; tag every check to one of the 10; treat **#7 as the organizing finding**
(record, per check, which zone the attacker must be in for it to work).

---

## Target device reference (AXC F 2152)

- Vendor: Phoenix Contact · Controller: AXC F 2152 · Article: **2404267**
- Firmware under test: **2022.0.8 LTS** (current line as of research: 2025.6.0)
- OS: Yocto Linux + OSADL real-time; `dpkg` present; SSH as admin; podman
- Exposed services (per vendor port list): WBM/HTTPS, SSH 22, OPC UA 4840,
  Modbus TCP 502, SNMP 161, remote engineering 41100, PROFINET, NTP 123
- Certs: IEC 62443-4-1 (dev process) and 62443-4-2 (product)
- PSIRT/advisories: **CERT@VDE** (`phoenixcontact.csaf-tp.certvde.com`)
- Device-level CVEs in CIRCL: CVE-2020-12517/12518/12519/12521 (PLCnext/PROFINET)
- Local docs held: `ah_en_axc_f_2152_change_notes_108427_en_51.pdf` (en_52 exists,
  newer), `vulnerable_2022.0.8.csv` (266 CVEs derived from the change notes)

---

## Open / next steps

- [ ] Read-only SSH enumeration → SBOM → OSV → **reachability filter** (join with
      `ss -tlnp`/nmap) script — produces the short pentest list, not the 266 wall.
- [ ] Download firmware 2022.0.8 → unpack → Syft SBOM → OSV → diff vs the CSV.
- [ ] Per-device **two-mode runbook** (safe/aggressive) for the AXC F 2152 from
      the vendor port list + NSE/Redpoint/OIDA mapping, as YAML.
- [ ] Turn the OWASP OT Top 10 (2025) into the tool's concrete **check catalog**
      with assumed-attacker-position tagging (pull per-risk detail pages from PDF).
- [ ] Add `--api-key`/env to the CIRCL scripts so throttling stops being an issue.
- [ ] Optionally join top criticals against **CISA KEV / EPSS** for exploited-first.

---

## Sources (accessed 2026-11-09 unless noted)

**Standards / methodology**
- OWASP OT Top 10 (2025): https://ot.owasp.org/the-top-10 · local PDF
  `OWASP-OT-Top-10-2025.pdf` (v2025.0.0, CC BY-SA 4.0)
- NIST SP 800-82 Rev. 3: https://csrc.nist.gov/pubs/sp/800/82/r3/final
- ISA/IEC 62443: https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards
- MITRE ATT&CK for ICS: https://attack.mitre.org/matrices/ics
- CISA SBOM: https://www.cisa.gov/sbom

**Tools / repos**
- selmux/ot-security-agent-skills: https://github.com/selmux/ot-security-agent-skills
- OIDA: https://github.com/f0rw4rd/oida · https://getoida.dev/
- Anthropic-Cybersecurity-Skills: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
- awesome-ICS: https://github.com/hslatman/awesome-industrial-control-system-security
- Digital Bond Redpoint: https://github.com/digitalbond/Redpoint
- nmap NSE categories: https://nmap.org/nsedoc/categories/
- EMBA: https://github.com/e-m-b-a/emba
- Intel cve-bin-tool: https://github.com/intel/cve-bin-tool
- Syft / Grype: https://github.com/anchore/syft · https://github.com/anchore/grype
- OSV.dev API: https://google.github.io/osv.dev/post-v1-query · osv-scanner: https://github.com/google/osv-scanner

**Vulnerability data**
- NVD API 2.0: https://nvd.nist.gov/developers/vulnerabilities
- NVD enrichment crisis: CSA research (labs.cloudsecurityalliance.org, Apr 2026),
  VulnCheck / Securin, Tom Alrich blog (2025)
- CISA CSAF repo: https://github.com/cisagov/CSAF
- CIRCL Vulnerability-Lookup: https://github.com/vulnerability-lookup/vulnerability-lookup ·
  API https://vulnerability.circl.lu/api
- CERT@VDE Phoenix Contact CSAF provider:
  https://phoenixcontact.csaf-tp.certvde.com/.well-known/csaf/provider-metadata.json

**Benchmarks (for the testing/benchmarking methodology)**
- AutoPenBench: https://arxiv.org/html/2410.03225v2
- PentestEval: https://www.alphaxiv.org/abs/2512.14233
- AutoPentest-Bench: https://www.ijcai.org/proceedings/2026/0725.pdf
- CyberGym: https://arxiv.org/abs/2506.02548
- SEC-bench: https://arxiv.org/abs/2506.11791

**Device (Phoenix Contact AXC F 2152 / PLCnext)**
- PLCnext OS: https://www.plcnext-community.net/robohelp/infocenter/te/Operating_System/Operating_system.htm
- PLCnext security docs: https://security.plcnext.help/se/PLCnext_Control/AXC_F_2152.htm ·
  Port list: https://www.plcnext-community.net/robohelp/security/se/Appendix/Port_list.htm ·
  Security checklist: https://security.plcnext.help/se/Security_checklist.htm
- Product page (item 2404267): https://www.phoenixcontact.com/en-in/products/controller-axc-f-2152-2404267
- Local: `ah_en_axc_f_2152_change_notes_108427_en_51.pdf`, `vulnerable_2022.0.8.csv`

> Note: some sources above were reached via web search summaries on 2026-11-09;
> primary/official pages (NIST, OWASP, vendor docs, tool repos) should be treated
> as authoritative, and secondary blogs as corroboration. Re-verify any fact a
> recommendation depends on against the primary source and record the date.
