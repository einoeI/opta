# data/

Machine-readable tables for scripts and tools. Plain CSV (UTF-8, comma-separated, header row), readable with Python's `csv` module, pandas, Excel or `grep`.

| File | Maintained how | What it is |
|---|---|---|
| `knowledge-base.csv` | **Generated** by `python3 build_index.py`. Do not edit; change the entry's frontmatter instead. | One row per knowledge-base entry: metadata, links, file hash. |

`ot-ports.csv` moved to `catalog/` (see `catalog/README.md`).

## knowledge-base.csv

One row per Markdown entry under `knowledge-base/`. All paths are relative to the repo root.

| Column | Meaning |
|---|---|
| `entry` | Path of the Markdown entry, e.g. `knowledge-base/owasp/owasp-ot-top-10-2025.md`. |
| `folder` | Topic folder of the entry (`owasp`, `nist`, `bsi-germany`, ...). |
| `title` | Source title. |
| `url` | Canonical online location of the source. |
| `local_file` | Path of the local copy under `sources/`, if one is kept; empty for web-only sources. |
| `extract` | Path of the full-text extract `<local_file stem>.extracted.md` made by `extract_pdf.py`, if it exists (derived, not in the frontmatter). Searchable text with `<!-- page N -->` markers; quote from the original. |
| `sha256` | SHA-256 of `local_file`, computed at build time; use it to check a copy is unchanged or to cite a source without redistributing it. |
| `type` | `standard`, `vendor-doc`, `tool`, `advisory`, `paper`, `blog`, `dataset` or `other`. |
| `trust` | `primary` (official, vendor, standard) or `secondary` (blog, forum). |
| `accessed` | Date the source was downloaded or read. |
| `published` | The source's own date, or `unknown`. |
| `owasp_ot` | OWASP OT Top 10 (2025) items it informs, separated by `;` (e.g. `1;7`). |
| `status` | `retrieved` (default when the field is empty), `unretrieved`, `metadata-only`, or `draft` (created by `new_entry.py`, not yet filled in). |
| `reason` | Why it was not retrieved, when applicable. |
| `version` | Edition, revision or release of a versioned source. |
| `license` | Licence, if stated. |
| `superseded_by` | Newer edition replacing this one, if any. |

Example: `python3 -c "import csv; print([r['entry'] for r in csv.DictReader(open('data/knowledge-base.csv')) if '7' in r['owasp_ot'].split(';') and r['trust']=='primary'])"`
