# otpa – OT Pentesting Assistant: design (v1)

Agreed on 2026-11-10. Change this file when a decision changes.

## What it is

An offline CLI that helps an OT pentester plan tests, find the CVEs that matter
for a device, keep the evidence and write the report. In v1 it does not run
active tools: it prints the exact command, logs it in the manifest and ingests
the output. It works without an LLM; AI skills come later and only call `otpa`.

## Rules

- **Deterministic.** Same inputs give byte-identical outputs (CSV, plan,
  findings, report body). Inputs are: API snapshots, uploaded files,
  `decisions.yaml`, catalog files and the tool version. A golden-file test
  proves it. The manifest has timestamps and is not part of the comparison.
- **Live APIs only on update.** Each live call saves the raw response as a
  dated snapshot with SHA-256. All processing reads snapshots only.
- **Mode gate.** `aggressive` only with `environment: testbed`. Purdue L0
  targets get no active checks. `runtime` exists as a name and refuses to run.
  In `safe`, the gate decides which commands are printed at all.
- **Test-first.** pytest, red → green → refactor. One small test per module,
  plus golden files for the whole pipeline.
- **Skills (later)** call `otpa` commands and interpret the output. They never
  compute facts. AI prose goes to separate files (`report.ai.md`).
- **OIDA** is called as a subprocess, never imported (AGPL).

## Layout

```
core/        otpa package: cli, modules/ (one file per step, found by folder scan), tests/
catalog/     owasp-ot-top10.yaml, components.csv, ot-ports.csv, attck-ics.csv
knowledge/   knowledge-base/, sources/, data/, notes/, build_index.py, new_entry.py, extract_pdf.py
vendor/      third-party repos (ot-security-agent-skills as git submodule)
workspace/   gitignored
  devices/<vendor>/<model>/<fw>/   device.yaml, sbom/, components.csv, snapshots/, cves.csv
  engagements/<date>-<name>/       engagement.yaml, plan.yaml, decisions.yaml, evidence/,
                                   ports.csv, oida.csv, cves.csv, manifest.yaml, report.md
                                   (raw scans in evidence/scans/)
pyproject.toml     all pip deps; uv.lock pins them. docling is the optional extra `docling`.
```

`skills/` is created when the first skill is written. `otpa doctor` checks
non-pip tools (nmap, pandoc, syft) and prints their versions.

## Data

**engagement.yaml** (written by `otpa init`, asks with fixed choices, or flags):
environment `live|testbed`, mode `forensics|safe|aggressive|runtime`,
attacker position, per target zone/conduit and Purdue level, device pointer,
tester. Validated on every load; invalid combinations stop with an error.

**device.yaml**: vendor, model, article no., firmware, OS type, protocols,
vendor port list, which evidence sources exist (vendor SBOM/VEX, firmware
obtainable, SSH, change-notes), `circl_products` (vendor/product spellings for
the CIRCL device search, merged) and `csaf_feed` (vendor ROLIE feed URL).
Commands on a device (`components`, `update`, `cves`) log to a `manifest.yaml`
in the device folder.

**Components**: from SBOM (CycloneDX or SPDX JSON, original kept in `sbom/`),
the curated picker (`catalog/components.csv`: name, CPE vendor:product, purl,
service, default ports) or free text (stored, flagged `unmapped`, keyword
search only; v1 lists them as not looked up).

**Vulnerability sources**: CIRCL Vulnerability-Lookup for the device, OSV.dev
for components (includes GHSA), CSAF from the vendor feed (CERT@VDE for Phoenix
Contact), optional change-notes CSV. CVSS: the vendor's score from CSAF by default;
NVD only on request (`otpa update --cvss`, slow without an API key). No standalone VEX
upload in v1.

Which source decides a CVE's label: `overrides.csv` in the device folder
(hand-written: cve, label, fixed_in, reason, source_url; for facts the tool
cannot parse, e.g. a range only in the CVE description), then vendor data (change-notes, CSAF matched by
article no. and firmware range) over OSV over the version range in the CVE
record from the CIRCL device search. Within the deciding source, affected wins.
A CVE record without a usable range stays Version-candidate with a note.

**cves.csv** (canonical, sorted by CVE id): cve, component, version, source,
cvss_version, score, vector, cvss_source (`nvd` or `csaf:<advisory>`), reachable, label, vendor_fixed_in, note. One row
per CVE and CVSS version, so all CVSS versions are stored; the report shows 3.1 first, 4.0 next to it, and always
names the version.

**Evidence labels**

| Label | Set by |
|---|---|
| Version-candidate | tool: version match |
| Observed | tool: ingested output confirms (banner, OIDA check) |
| Reproduced | tester, evidence file required |
| Not-affected | tool from vendor data, or tester with reason |
| False-positive | tester, reason required |

Tester decisions live in the engagement's `decisions.yaml`, one per target and
CVE (`otpa decide`), and are re-applied on every run. Evidence must be a file
inside the engagement folder; its SHA-256 is stored and checked on every load.
The device's `cves.csv` holds tool labels only; `reachable` stays `unknown`
there until step 4 joins it with an engagement's scans.

**Reachability** (`otpa ingest`): component → service via
`catalog/components.csv` and nmap product name. `yes` = an open port matches
(product contains the component name, or the port's service is one of the
component's services); `no` = the component has services, every transport of
its ports was scanned 1-65535 and nothing matches; `unknown` = no mapping or no
complete scan. `unknown` never counts as `no`. OIDA input is its `--json-log`
NDJSON; only `security` events count (they prove the port answered) and go to
`oida.csv`. The engagement's `cves.csv` = each target's device CVEs with
reachability, `Observed` (nmap shows the same product and version), and the
decisions applied. Out-of-scope hosts in a scan are ignored.

**Finding** (one schema for every module): id, title, module, owasp_ot,
attck_ics, zone_required, cvss_version, vector, score, evidence_label,
evidence (paths + SHA-256), affected, kb_refs.

**OWASP catalog** (`catalog/owasp-ot-top10.yaml`): per check id, owasp_ot,
title, zone_required, modes, purdue_max, either `module` or `manual: true` with
a question, attck_ics, kb_refs. Manual checks get pass/fail/n.a. + note.

**plan.yaml**: catalog filtered by scope and device, sorted by OWASP item then
check id, excluded checks listed with the reason.

**manifest.yaml** (one per engagement, one entry per command): command line,
otpa version + git commit, external tool versions, input/output files with
SHA-256, snapshot ids, approvals/refusals, start/end time.

**Report**: overview page (by zone, by OWASP item, reachable components with
CVE count, max CVSS, label), one finding per reachable component with its CVEs,
appendix with non-reachable CVEs, CSV and manifest. Markdown; pandoc with a
`reference.docx` for Word when installed. Zones/conduits (#7) are the axis.

## v1 build order

1. git init; move existing files into the layout; AXC F 2152 / 2022.0.8 as first device. **(done)**
2. `otpa init` + engagement.yaml + manifest. **(done)**
3. Components (SBOM / picker / free text) → CIRCL + OSV + CSAF (+ change-notes CSV) → cves.csv + decisions.yaml. **(done)**
4. Ingest nmap XML and OIDA output → ports.csv → reachability. **(done)**
5. `otpa plan` with the OWASP catalog (automated + manual checks).
6. Overview report.
7. Run end-to-end on the AXC F 2152 testbed before adding anything.

## Later (v2+)

UI (Flask or NiceGUI, decided then; holds no logic). Running nmap/OIDA from
the tool with plan approval + per-write confirm. Offline NVD CPE dictionary.
Forensics wrapper over `vendor/ot-security-agent-skills`. Standalone VEX
upload. AI skills. Runtime mode. Licence (internal for now).
