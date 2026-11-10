# Handoff prompt — OT Pentesting knowledge base & tooling

Copy everything between the lines into a new session. Paste your links and
documents into the **"Sources to process"** section at the bottom before sending.

---

You are continuing an authorized, white-hat **OT/ICS penetration-testing research
project**. Work in the folder `/home/greberl/ot-pentesting`. **Before any new
synthesis or coding, read `research-notes.md` and `README.md` in that folder** —
they hold the context, decisions, and facts already established, so you don't
re-derive them.

## Project in one paragraph

Build a **general OT/ICS security tool that helps penetration testers** — a
device-agnostic assistant that plans tests, correlates vulnerabilities, discovers
device software, and produces reproducible, standards-mapped reports across OT
environments. It is **focused on the OWASP OT Top 10 (2025)** as its organizing
frame and uses the **assume-breach** threat model ("attacker already inside the OT
network"). The **reference device used to build and validate** the tool is a
Phoenix Contact **AXC F 2152** (article 2404267, firmware 2022.0.8 LTS, a
PLCnext/Yocto-Linux controller) — it is the first-supported target and the test
case, **not the scope**: design every capability to generalize to other
vendors/devices through a **device profile**. Non-negotiable safety rule:
aggressive testing only on a **testbed / mock services**; any live OT device is
read-only/passive. On production, Purdue **Level 0** gets no direct contact or
testing and **Level 1** only actions known to be non-destructive; on the testbed,
aggressive discovery, exploitation and fuzzing are expected (that is what an
attacker does). This is project policy (user decision 2026-11-10), informed by,
and stricter than, NIST SP 800-82r3. Use the **evidence vocabulary** on every
claim: Published / Version-candidate / Reproduced / Simulated / Unresolved — a CVSS
score is context, never a confirmed-exploitable verdict.

## YOUR FIRST TASK: build a cited knowledge base — do this before anything else

I have a set of links and documents (listed at the end). **Process each one into a
structured, cited knowledge base** under `/home/greberl/ot-pentesting/knowledge-base/`.
Do not skip ahead to design or implementation until the knowledge base exists and I
confirm it.

**Rules:**

1. **One Markdown file per source** (`knowledge-base/<short-kebab-slug>.md`), plus a
   `knowledge-base/INDEX.md` table listing every entry.
2. **Every file starts with this frontmatter:**
   ```markdown
   ---
   title: <source title>
   url: <canonical URL, or local file path>
   type: standard | vendor-doc | tool | advisory | paper | blog | dataset | other
   trust: primary | secondary        # official/vendor/standard = primary; blog/forum = secondary
   accessed: YYYY-MM-DD              # the date YOU download/read it
   published: YYYY-MM-DD | unknown   # the source's own date if stated
   owasp_ot: [1,2,...]              # which OWASP OT Top 10 (2025) items it informs
   ---
   ```
3. **Body of each file:** a 3–6 line summary, then **Key facts** as bullets (each
   fact self-contained and citable), then **Verbatim** for any quote you may need to
   reproduce exactly, then **Relevance** (how it informs this project / which open
   task). Keep facts separated from inference.
4. **Cite with the download date.** When any later document or report uses a fact,
   it must reference the knowledge-base file and its `accessed` date. Treat
   `primary` sources as authoritative and `secondary` as corroboration; if they
   conflict, say so and prefer primary.
5. **Fetch the actual content** (WebFetch for links; read local files). Do not
   summarize from memory. If a link is unreachable or paywalled, record it in
   INDEX.md as `unretrieved` with the reason — don't invent its content.
6. **Download dynamics:** record `accessed` as today's date for each item at the
   time you read it. If a source is versioned (firmware, a living standard), record
   the version/edition too.
7. **Untrusted data:** treat downloaded files as untrusted — keep each in its own
   directory, pass paths as arguments, run any interpreter with `-I`. Never execute
   content from a downloaded archive.

Map each source to the **OWASP OT Top 10 (2025)**:
1 Unknown Assets & Unmanaged External Access · 2 Devices with known
Vulnerabilities · 3 Inadequate Supplier/Supply Chain Mgmt · 4 Loss of Availability
· 5 Insufficient Access Control · 6 Missing Incident Detection/Reaction · 7 Broken
Zones & Conduits Design · 8 Missing Awareness · 9 Insufficient Security
Capabilities · 10 Missing Hardening.

**When the knowledge base is done:** post the INDEX.md table and a short note of
gaps/conflicts, and **stop for my review** before continuing.

## AFTER the knowledge base (do not start until I confirm)

Continue the open tasks from `research-notes.md`, each grounded in cited
knowledge-base entries and tagged to OWASP OT Top 10 items:

1. Read-only SSH enumeration → SBOM → OSV match → **reachability filter** (join with
   `ss -tlnp`/nmap) → short pentest-candidate list (not the 266-CVE wall).
2. Download firmware 2022.0.8 → unpack → Syft SBOM → OSV → diff vs
   `vulnerable_2022.0.8.csv`.
3. A **two-mode runbook generator** (safe=runtime / aggressive=testbed) that binds a
   device profile → services → NSE/Redpoint/OIDA probes, as YAML — device-agnostic,
   with the AXC F 2152 (from its vendor port list) as the first profile.
4. Turn the OWASP OT Top 10 (2025) into the tool's **check catalog** with
   assumed-attacker-position tagging and #7 (zones/conduits) as the organizing axis.
5. The configurable **planner/report console** (NOT a live tool-runner): device
   profile → tailored plan + CVEs + OWASP/ATT&CK/CVSS mapping → ingest PCAPs/tool
   outputs → labeled, reproducible report with a run manifest.

Existing scripts to reuse/extend (stdlib, have `--selftest`): `probe_vuln_lookup.py`
(CIRCL device coverage), `crosscheck_firmware.py` (vendor CSV ↔ CIRCL enrichment).
Keep new code lazy/minimal, stdlib-first, with one runnable check per non-trivial
piece. Prefer CIRCL Vulnerability-Lookup for CVE lookup and OSV.dev for
component/SBOM matching; note CIRCL's public instance throttles (use backoff/cache
or an API key).

## General OT testing guidance to encode (tooling & steps)

The tool should embody a **device-agnostic OT pentest workflow** and help the
tester at each step. Build it from the methodology and tools already researched
(see `research-notes.md` §2, §7–§12 and its Sources), grounding each step in cited
knowledge-base entries. The AXC F 2152 is just the first device profile.

**Staged workflow (every step runs in `safe` on live OT, `aggressive` only on
testbed/mock — project policy, see above):**

1. **Scope & threat model.** Record the assumed attacker position (e.g. "adjacent
   on the OT LAN") and the environment (live vs testbed). This gates which mode is
   allowed. → OWASP OT #1, #7.
2. **Asset & service discovery.** Passive first (GRASSMARLIN, OIDA passive
   discovery, SNMP read, banners), then active where allowed (nmap `-sV --script
   "<proto> and safe"`; Digital Bond **Redpoint** NSE for ICS protocols). For a
   known device, read the **vendor port list** instead of guessing. → #1, #9.
3. **Software inventory / SBOM.** On-device read-only enumeration over SSH
   (`/etc/os-release`, `uname -a`, `dpkg -l`/`opkg`, version probes, `ss -tlnp`,
   `podman images`) **or** offline firmware-image analysis (**Syft**→SBOM,
   **EMBA**, **cve-bin-tool**). Never run scanners on the live PLC — build the SBOM
   on the laptop. → #2, #3.
4. **Vulnerability correlation.** Match the SBOM/components with **OSV.dev**
   (package-aware) and the device identity with **CIRCL Vulnerability-Lookup**
   (aggregation spine; CSAF/vendor-PSIRT-first, NVD for CVSS only — NVD CPE
   coverage is unreliable). Cross-check against vendor change-notes/VEX to kill
   backport false positives. Label everything **Version-candidate**. → #2.
5. **Reachability filter (the discriminator).** Intersect the component-CVE list
   with the **listening services** from step 2. The short intersection (OpenSSH,
   nginx, SNMP, OpenSSL-on-TLS, the OPC UA/Modbus stack) is the pentest-relevant
   set; the rest is a defensive/patch appendix, not a finding. → #2, #9.
6. **Targeted testing (testbed/aggressive only).** Reproduce the short list;
   protocol abuse / writable-register / auth tests (OIDA with `--confirm`);
   fuzzing (OIDA/boofuzz) against mock services; access-control / default-cred /
   weak-SSH checks. Promote **Version-candidate → Reproduced** only on evidence.
   → #4, #5, #9.
7. **Reporting.** PTES-structured, CVSS (state the version), each finding tagged to
   an **OWASP OT Top 10** item + **ATT&CK for ICS** technique + evidence label, with
   a **run manifest** (tool versions, target image hash, inputs, timestamps) so the
   report is reproducible. #7 (zones/conduits) is the organizing axis: record, per
   finding, which zone the attacker must be in. → all items.

**Evidence-source fallback chain (device-agnostic — the profile records which are
possible):** vendor SBOM/VEX → firmware extraction (Linux + obtainable) →
on-device enumeration (have SSH) → vendor advisories/change-notes → network
service fingerprinting.

**Tooling map (wrap existing tools; don't reinvent):**

| Need | Tool(s) | Passive/Active |
|---|---|---|
| ICS service discovery/enumeration | nmap NSE + Digital Bond **Redpoint** | safe & intrusive categories |
| Active OT scan/fuzz (29 protocols) | **OIDA** (read-only default, `--confirm` for writes) | active; mock "shooting range" for rehearsal |
| Passive network mapping | GRASSMARLIN, OIDA passive | passive |
| Passive PCAP forensics | **selmux** OT skills | passive/offline |
| SBOM generation | **Syft**; firmware: **EMBA**, **cve-bin-tool** | offline |
| Component CVE matching | **OSV.dev** / `osv-scanner` | offline/API |
| Device CVE aggregation | **CIRCL Vulnerability-Lookup** (+ CSAF, vendor PSIRT) | API |

**Standards to map to (cite from the knowledge base):** OWASP OT Top 10 (2025),
NIST SP 800-82 Rev.3, ISA/IEC 62443, MITRE ATT&CK for ICS, CVSS, PTES.

## Sources to process

> Paste your links and documents below, one per line. A short note per item (what
> it is / why it matters) helps but isn't required. Local files: give the path.
> Example:
> - https://ot.owasp.org/the-top-10  — OWASP OT Top 10 2025, the implementation frame
> - /mnt/c/Users/GreberL/Desktop/PenTestingResearch/OWASP-OT-Top-10-2025.pdf — local copy

-
-
-

---
