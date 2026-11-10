# otpa – OT Pentesting Assistant

Offline CLI for OT/ICS penetration testers: test planning from the OWASP OT Top 10
(2025), CVE correlation for a device filtered by what is reachable, evidence
handling and a reproducible report. Works without an LLM. Authorized testing only.

First device profile: **Phoenix Contact AXC F 2152** (article 2404267, firmware
2022.0.8 LTS), a PLCnext/Yocto-Linux controller.

Design and decisions: **`DESIGN.md`**. Status: layout done (step 1), the `otpa`
package itself is not written yet.

## Layout

| Folder | What is in it |
|---|---|
| `core/` | The `otpa` package (from step 2). `core/legacy/` holds the research scripts that become modules: `probe_vuln_lookup.py` (CIRCL + CERT@VDE coverage check), `crosscheck_firmware.py` (change-notes CVEs vs CIRCL, CVSS enrichment), `ot_ports.py` (port lookup). Each has `--selftest`. |
| `catalog/` | Hand-maintained data the tool reads: `ot-ports.csv` (see `catalog/README.md`). |
| `knowledge/` | Knowledge base: `knowledge-base/` (one cited entry per source, start at `INDEX.md`), `sources/` (local PDFs, check licences before sharing), `data/` (generated CSV), `notes/` (research notes, reports, handoff prompt), and the scripts `build_index.py`, `new_entry.py`, `extract_pdf.py`. |
| `vendor/` | Third-party repos. `ot-security-agent-skills` (selmux, PCAP forensics for Modbus/BACnet/S7/IEC-104) as git submodule. |
| `workspace/` | Device and engagement data. Gitignored. `devices/phoenix-contact/axc-f-2152/2022.0.8/` holds `device.yaml`, the vendor change-notes CVE list, the enriched CSV and the CIRCL snapshot. |

## Setup

```
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-docling.txt --extra-index-url https://download.pytorch.org/whl/cpu   # optional
git submodule update --init
```

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
