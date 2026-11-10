# otpa – OT Pentesting Assistant

Offline CLI for OT/ICS penetration testers: test planning from the OWASP OT Top 10
(2025), CVE correlation for a device filtered by what is reachable, evidence
handling and a reproducible report. Works without an LLM. Authorized testing only.

First device profile: **Phoenix Contact AXC F 2152** (article 2404267, firmware
2022.0.8 LTS), a PLCnext/Yocto-Linux controller.

Design and decisions: **`DESIGN.md`**. Status: steps 1-5 done; the report (step 6) is next. How to use it: see below.

## Layout

| Folder | What is in it |
|---|---|
| `core/` | The `otpa` package (`core/otpa/`, commands in `core/otpa/modules/`) and its tests (`core/tests/`). `core/legacy/` holds the research scripts that become modules: `probe_vuln_lookup.py` (CIRCL + CERT@VDE coverage check), `crosscheck_firmware.py` (change-notes CVEs vs CIRCL, CVSS enrichment), `ot_ports.py` (port lookup). Each has `--selftest`. |
| `catalog/` | Hand-maintained data the tool reads: `owasp-ot-top10.yaml` (checks), `components.csv`, `ot-ports.csv` (see `catalog/README.md`). |
| `knowledge/` | Knowledge base: `knowledge-base/` (one cited entry per source, start at `INDEX.md`), `sources/` (local PDFs, check licences before sharing), `data/` (generated CSV), `notes/` (research notes, reports, handoff prompt), and the scripts `build_index.py`, `new_entry.py`, `extract_pdf.py`. |
| `vendor/` | Third-party repos. `ot-security-agent-skills` (selmux, PCAP forensics for Modbus/BACnet/S7/IEC-104) as git submodule. |
| `workspace/` | Device and engagement data. Gitignored. `devices/<vendor>/<model>/<fw>/` holds `device.yaml`, `components.csv`, `overrides.csv`, `snapshots/` and `cves.csv`; `engagements/<date>-<name>/` holds one engagement. |

## Setup

Needs [uv](https://docs.astral.sh/uv/). Dependencies are in `pyproject.toml`, exact versions
in `uv.lock`, Python version in `.python-version`.

```
uv sync                    # .venv with otpa, its deps and pytest
uv sync --extra docling    # optional, ~2 GB: best PDF extraction, CPU-only PyTorch
git submodule update --init
```

Run everything through uv: `uv run otpa ...`, `uv run pytest`, `uv run python knowledge/build_index.py`.
After changing dependencies in `pyproject.toml`, run `uv lock` and commit `uv.lock`.

## How to use this version (steps 1-5)

What works: engagements, components, CVE sources, `cves.csv`, overrides, decisions, plan
with printed commands, manual check results, scan ingest with reachability. Not yet: the
report (step 6). otpa never runs nmap or OIDA itself; it prints the commands, you run them.

All commands below run from the repo root. Each command that writes something adds an entry
to `manifest.yaml` (engagement or device folder). Every command has `-h`.

### 0. Check the install

```
uv sync
uv run pytest -q           # all tests should pass
uv run otpa -h             # lists the commands
```

### 1. Device data and CVEs (once per device and firmware)

The AXC F 2152 / 2022.0.8 profile is already in `workspace/devices/`. For another device,
copy its folder and edit `device.yaml` (vendor, model, article_no, firmware, protocols,
`circl_products`, `csaf_feed`, change notes file).

```
D=phoenix-contact/axc-f-2152/2022.0.8
uv run otpa components $D --pick openssh@8.9p1          # optional: --sbom bom.json, --free "name@ver"
uv run otpa update $D                                   # network, ~1 min; add --cvss for NVD scores
uv run otpa cves $D                                     # offline -> cves.csv
```

Look at `workspace/devices/$D/cves.csv`: one row per CVE and CVSS version, with `label`,
`source`, `vendor_fixed_in`, `note`. Facts the tool cannot read go in `overrides.csv` in the
same folder (`cve,label,fixed_in,reason,source_url`); rerun `otpa cves $D` after editing it.

### 2. Create an engagement

```
uv run otpa init axc-lab
```

It asks for tester, environment (`live`/`testbed`), mode (`forensics`/`safe`/`aggressive`),
attacker position and targets. The same works with flags:

```
uv run otpa init axc-lab --tester "Name" --environment testbed --mode aggressive \
  --attacker-position control \
  --target name=plc1,address=192.168.1.10,zone=cell-1,purdue=1,device=$D
E=workspace/engagements/$(date +%F)-axc-lab
```

Things worth trying: `aggressive` with `live` is refused; Ctrl-C during the questions writes
nothing; a second target with `purdue=0` gets no active checks in the plan.

### 3. Plan

```
uv run otpa plan $E
```

Writes `$E/plan.yaml` and prints per target the checks from `catalog/owasp-ot-top10.yaml`
with their commands (`$`) or questions (`?`). Excluded checks are in `plan.yaml` with the
reason. Compare an engagement in `live`/`safe` with one in `testbed`/`aggressive`: the safe
plan has a slow vendor-port scan, the aggressive one a full `-p-` scan and testbed-only
checks. Placeholders like `<interface>` and `<capture>` are yours to fill in.

Record manual check results (note required):

```
uv run otpa check $E plc1 OT05-01 fail --note "no access matrix exists"
uv run otpa plan $E        # status column now shows fail
```

### 4. Scans and reachability

Run the printed commands yourself (they write into `$E/evidence/scans/`; always keep
OIDA's `--json-log`), then:

```
uv run otpa ingest $E                       # reads everything in evidence/scans/
uv run otpa ingest $E other-scan.xml        # or give files from elsewhere; they are copied in
```

Dry run without the PLC, with the sample scans from the tests (they assume target
192.168.1.10):

```
uv run otpa ingest $E core/tests/fixtures/scans/nmap-tcp-full.xml core/tests/fixtures/scans/oida-plc1.ndjson
```

Results in `$E`: `ports.csv` (ports per target), `oida.csv` (OIDA findings), `cves.csv`
(device CVEs per target with `reachable` yes/no/unknown, `Observed` where nmap shows the same
product and version, and your decisions). `reachable` is only `no` after a full `-p-` scan.

### 5. Decisions on CVEs

```
mkdir -p $E/evidence && cp proof.txt $E/evidence/
uv run otpa decide $E plc1 CVE-2022-37434 Reproduced --evidence evidence/proof.txt
uv run otpa decide $E plc1 CVE-2021-3672 Not-affected --reason "c-ares not used"
uv run otpa ingest $E      # re-applies decisions to cves.csv
```

`Reproduced` needs an evidence file inside the engagement; `Not-affected` and
`False-positive` need a reason. Editing the evidence file afterwards makes every later
command stop with "changed since the decision".

### Notes

- `otpa update` is the only command that uses the network. Responses are kept under
  `snapshots/<date>/` with SHA-256 in `snapshots/index.csv`, so `cves` gives the same output
  for the same snapshots.
- For `--cvss`: put `export NVD_API_KEY=...` in `~/.config/otpa/nvd.env` and source it from
  `~/.bashrc`; about 10x faster.
- To start over, delete the engagement folder. `workspace/` is not in git.

## PDF extraction: which tool and why

Compared on 2026-11-10 on 7 PDFs from `sources/` (OWASP OT Top 10, BSI Top 10, AXC F 2152
change notes, OSSTMM, a Medium article, two papers):

| Tool | Result | Verdict |
|---|---|---|
| **docling** (MIT) | Headings, lists, tables, links, joined hyphenation, correct order on two-column pages, OCR of text in images (recovered the urjasec port table that is only an image). ~2-3 min per 20-100 page PDF on CPU; ~2 GB with models. | **Best: least cleanup.** Optional backend. |
| **pypdf** (BSD) | Plain text per page in correct order; keeps page headers/footers and hyphenation; no headings/tables. ~1-5 s per PDF. | **Default**: light, always works. |
| pymupdf4llm (AGPL) | Good headings/tables, fast, but **mixed up the two columns** of the change notes (CVEs landed under the wrong component). | Rejected: silent errors + AGPL. |
| markitdown (MIT) | Thin wrapper over pdfminer: plain text, few tables, no headings. | No gain over pypdf. |
| pdfplumber (MIT) | Lost word spaces on papers ("Penetrationtesting,acrucial..."). | Rejected. |

`knowledge/extract_pdf.py` uses docling when installed, otherwise pypdf, and writes
`<pdf>.extracted.md` next to the PDF with `<!-- page N -->` markers for citing.
The extract is a working copy (grep, drafting); always check quotes against the PDF.

## Adding a source (no AI needed)

1. `python3 knowledge/new_entry.py path/to/file.pdf --folder <topic> --url <canonical URL> [--extract]`
   copies the file to `sources/<topic>/` and creates `knowledge-base/<topic>/<slug>.md`
   with every frontmatter field, a body template and the PDF's outline.
   For a web-only source: `python3 knowledge/new_entry.py --folder tools --slug name --url ...`.
2. Read the source and fill in the entry: frontmatter values, Summary, Key facts (with
   pages), Verbatim, Relevance. Remove `status: draft` when done.
3. `python3 knowledge/build_index.py` validates every entry (allowed types, trust, dates,
   OWASP items 1-10, existing `local_file`) and regenerates `knowledge-base/INDEX.md`
   and `data/knowledge-base.csv`. Never edit those two files by hand.
4. `python3 knowledge/build_index.py --check` exits 1 if the index/CSV are stale. Once the
   folder is in git, run it in a pre-commit hook or CI so nothing goes out of sync.

Field definitions: `knowledge/data/README.md`.

## Quick facts established

- The device-level CVE lookup finds **4** CVEs (CERT@VDE product advisories);
  the vendor change-notes list **266** component CVEs affecting 2022.0.8 — of
  which a device-level search catches **0**. Component CVEs are an **SBOM/SCA**
  problem, not a lookup problem.
- Use **CIRCL Vulnerability-Lookup** as the CVE aggregation spine (confirmed to
  cover this device via CERT@VDE). Use **OSV.dev** for SBOM/component matching.
- Firmware is downloadable from Phoenix Contact for **zero-touch** offline
  analysis (the device runs from internal flash, not the SD card).

See `knowledge/notes/research-notes.md` for the full picture and sources.
