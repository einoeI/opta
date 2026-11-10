# Obsidian and knowledge graphs for sharing the OT pentesting knowledge base

Research date: 2026-11-10. Pricing, licence and maintenance were checked today on primary pages unless marked otherwise. **Cited Findings are evidence-backed. Inferences are judgment.** "Local check" means I read files in `/home/greberl/ot-pentesting/` directly; nothing outside this notes file was modified.

**Verdict in one line:** the earlier recommendation holds, with two corrections. Obsidian stays an optional personal reader, never the shared channel. A knowledge graph is overkill. But "skip graphs until something queries the links" understated how small the useful step is: a ~30-line stdlib script that writes cross-reference tables (OWASP OT item x source, later ATT&CK for ICS technique x source) into Markdown gives most of the value now. Second correction: the corpus currently has **zero links between entries**, so backlinks and graph views (Obsidian, Quartz, Foam) would show 68 unconnected dots. Their value depends on content that does not exist yet (playbooks citing sources).

## Q1. Obsidian for a team: licence, Sync/Publish terms, residency, offline, sharing in practice

### Takeaway
Obsidian is free for commercial use and works fully offline on local files, so letting individuals open a Git clone in it costs nothing and needs no decision. As a *team sharing channel* it is weak: Sync caps shared vaults at 20 people, each needing a paid subscription, with no read-only role. The Git plugin works on desktop and is officially "very unstable" on mobile. Non-users and other teams get nothing from it.

### Cited Findings
- "Obsidian is free for all purposes, including personal, commercial, and non-profit use"; the Commercial License is optional; the page was last updated 2025-02-20 — [Obsidian license](https://obsidian.md/license).
- "Downloading Obsidian does not require an account"; data "is saved locally on your device and is not sent to our server"; Sync data is encrypted and inaccessible to staff; Publish data is hosted on Obsidian's servers — [Obsidian license](https://obsidian.md/license).
- Current prices on the pricing page: Sync $4 per user per month billed annually ($5 monthly), including end-to-end encryption, version history, and "Collaborate on shared vaults"; Publish $8 per site per month annually ($10 monthly); Commercial $50 per user per year (optional) — [Obsidian pricing](https://obsidian.md/pricing), fetched 2026-11-10.
  - Conflict: the 2023 announcement listed Sync at $8/month (10 GB) or $16/month (100 GB) billed yearly from January 2024 — [Obsidian blog, 2023-11-21](https://obsidian.md/blog/new-sync-plans/). The live pricing page is the more current source; the tier and storage split could not be reconciled from what I fetched.
- Sync shared vaults: maximum 20 collaborators; "All collaborators must have an active Sync subscription"; "Fine-grained permissions are not supported yet", everyone has the owner's permissions except inviting; simultaneous edits "will be merged"; for E2E-encrypted vaults collaborators enter the encryption password — [Obsidian help, Collaborate on a shared vault](https://obsidian.md/help/sync/collaborate).
- Conflicts across devices can be auto-merged or written as separate conflict files, a per-device setting — [Obsidian help, Sync settings](https://obsidian.md/help/sync/settings).
- Sync region: the 2023 update introduced choosing a sync server region — [Obsidian blog](https://obsidian.md/blog/new-sync-plans/). After selection, "your data center cannot be moved to a different server without re-uploading your data" — [Obsidian help, Set up Sync](https://obsidian.md/help/sync/setup). A search summary of Obsidian's help pages states the European option is Frankfurt, Germany, and that changing region means re-creating the vault and losing version history — [search result pointing to obsidian.md help](https://obsidian.md/de/help/sync/collaborate). **I did not open the page that names Frankfurt directly**; treat the location as likely but unverified.
- Obsidian Git plugin (maintained by Vinzent03 since March 2021): "The Git implementation on mobile is very unstable!"; no SSH on mobile, repo size limited by memory; offers in-editor conflict resolution; no team-workflow guidance — [obsidian-git README](https://raw.githubusercontent.com/Vinzent03/obsidian-git/master/README.md).

### Inferences
- **Offline and air-gap:** strong. Obsidian reads a local folder; no account needed. Fine for a laptop on a site visit.
- **Sync is the wrong channel for this content.** OT attack knowledge at TLP:AMBER would sit on a third-party US company's servers (E2E-encrypted, likely Frankfurt) outside the company's access control, with no read-only role, no review step, and a 20-person ceiling. Other pentest teams and AI agents cannot use it. It also duplicates the forge, creating the second store of truth the earlier notes warned against. Cost is minor (about $48 per user per year); governance is the problem.
- **Publish is excluded** for AMBER content: it hosts notes on Obsidian's public web servers. (Publish supports password protection per my prior knowledge, not verified today.)
- **Shared drive (SMB/OneDrive) vault:** not researched by primary source; Obsidian writes `.obsidian/` workspace files constantly, which in my experience causes churn and conflicts on shared folders. Judgment, not evidence.
- **What works:** each person who wants Obsidian opens their own Git clone as a vault, commits through Git (CLI, IDE, or the Git plugin on desktop), and the forge stays the review gate. Add `.obsidian/workspace*.json` to `.gitignore`; decide whether to commit a minimal `.obsidian/` (a shared `.base` file needs no plugin). Forbid community plugins in the shared config (judgment: community plugins run arbitrary code in the app, which matters on a pentester laptop holding client data).
- Plugin sprawl and merge conflicts on `.obsidian/` are the predictable failure modes; both vanish if `.obsidian/` is not committed or is limited to Bases files outside it.

### Gaps
- **No credible evidence found of security or pentest teams using Obsidian as a shared team KB** (only personal-use blog content surfaced; I did not cite any). The team-use assessment rests on documented product limits plus judgment.
- Frankfurt region, Publish password protection, and Obsidian's source availability (closed source) not confirmed from a primary page today.
- How Obsidian handles a value that does not match a property's type was not documented on the Properties page.

## Q2. What Obsidian concretely adds over Git + rendered Markdown for THIS corpus

### Takeaway
Only one thing is real today: Bases (core, no plugin) can turn the existing frontmatter into filterable tables, such as "primary sources for OWASP OT #7". Backlinks, graph view and Canvas add nothing yet, because no entry links to another. The frontmatter mostly works as-is but has two snags: `published: unknown` in 25 of 68 entries collides with Obsidian's vault-wide Date type, and `owasp_ot` is a YAML flow list of integers that Obsidian's list type does not document. No lock-in, as long as the team does not start writing wikilinks.

### Cited Findings
- Local check, frontmatter survey of all 68 entries:
  - All use `owasp_ot: [..]` YAML flow lists of integers, with mixed spacing (`[2,3]` and `[4, 9]`); 5 entries have `owasp_ot: []`.
  - `published:` is an ISO date in 43 entries and the string `unknown` in 25.
  - `accessed:` is an unquoted ISO date in all 68.
  - `trust:` is primary in 52 and secondary in 16.
  - `version` and `license` are quoted strings; `superseded_by` is a bare slug (for example `nist-sp-800-82r3` on `nist-sp-800-82r2.md`), not a link.
  - No entry contains a link to another entry; the only internal links are in `INDEX.md`. Five entries mention ATT&CK for ICS IDs (T0xxx) in body text; none has an `attack_ics` field.
- Obsidian property types are Text, List, Number, Checkbox, Date, Date & time, Tags, and a type applies to the property name "across your vault"; list values "can contain text, numbers, and Internal links"; flow syntax `[1,2,3]` is not mentioned — [Obsidian help, Properties](https://obsidian.md/help/properties).
- Bases files "must be valid YAML"; filters use formula syntax such as `authors.contains(this)` and date arithmetic such as `file.mtime > now() - "1 week"`; `file.links` includes links in frontmatter; `file.backlinks` is performance-heavy and does not refresh automatically — [Obsidian help, Bases syntax](https://obsidian.md/help/bases/syntax).

### Inferences
- **Queries that would work on the current frontmatter** (syntax pattern from the Bases docs; not executed in Obsidian):
  - `owasp_ot.contains(7) && trust == "primary"` gives all primary sources for OWASP OT #7. 12 entries, per the local script below. Integer-vs-string matching on flow lists is the thing to test first.
  - `superseded_by` (non-empty) gives the superseded entries.
  - "Past review date" needs the proposed `review_by:` field, which does not exist yet: `review_by < today()`.
- **`published: unknown` is a real snag.** If Obsidian types `published` as Date, the 25 `unknown` values become invalid for that type and drop out of date sorting and filtering. Fix (judgment): omit the field, or leave it empty, when the date is unknown, and record "unknown" in a note. That also suits any YAML tooling. Do this only if someone actually adopts Bases.
- **Editing in Obsidian's property UI may rewrite flow lists to block style.** This is my expectation, not documented. That would create noisy Git diffs. Mitigation: edit frontmatter as text, or let `build_index.py` or a check normalise it.
- **Lock-in:** the content is plain Markdown plus YAML. Lock-in only arises if people write `[[wikilinks]]` (Obsidian's default) or embed `.canvas` or `.base` files that other renderers ignore. Set "Use [[Wikilinks]]" to off, which makes Obsidian write relative Markdown links that GitLab, GitHub, MkDocs/Zensical and agents all understand. Treat `.base` files as optional views, not content.
- **Dataview vs Bases:** Bases is core and stores plain-YAML view files. Dataview is a community plugin with its own query language. Prefer Bases if anything. Not re-verified today: Dataview's maintenance status and the version that introduced Bases.
- **Graph view and backlinks:** with zero inter-entry links, the graph is the INDEX hub plus 68 isolated nodes. They become useful once `playbooks/` cite source entries with relative links, which is the layout the earlier notes proposed. Even then, a generated "Cited by" table (below) gives the same information to non-Obsidian readers.
- **Canvas:** a whiteboard for one person's thinking. No team value for a reference corpus.
- **Net:** nothing Obsidian adds is needed by the audiences other than the researcher. OT engineers and other teams need a browser link; agents need files and grep. For an individual, Obsidian is a pleasant reader, and the Bases tables are a convenience the script below also provides.

### Gaps
- Bases filtering on integer flow lists and on mistyped dates was not tested in a running Obsidian, since no Obsidian install is available here. These are the two things to check in 10 minutes before recommending a shared `.base` file.

## Q3. Alternatives at the same weight

### Takeaway
For the people who will not use Git, the right step up is still a static site from the same files. Quartz is the one option that adds backlinks and a graph to a site, and it is Obsidian-compatible. Zensical/MkDocs gives a plainer, more conventional docs site. Logseq is now the wrong bet, and Foam is a VS Code-only personal tool. Plain forge rendering remains enough today.

### Cited Findings
- Quartz is a static-site generator that "transforms Markdown content into fully functional websites", with wikilinks, transclusions, backlinks, graph view, full-text search and Obsidian compatibility; footer shows v5.1.0 — [Quartz](https://quartz.jzhao.xyz/). The licence was not shown on that page.
- Logseq split in 2026: a SQLite-based DB version and the Markdown file version. The 2026-05-16 update says "Logseq is splitting into two versions", the Markdown Mirror is one-way and opt-in per graph, and the two-way round-trip "is in active development on a feature branch and not yet shipped" — [Logseq forum, 2026-05-16](https://discuss.logseq.com/t/whats-new-with-logseq-db-may-16th-2026/35020).
  - Secondary sources (not verified) say the Markdown version, "Logseq OG", is maintenance-only and that DB build 2.0.2 (2026-10-07) is still beta — [issoh.co.jp](https://www.issoh.co.jp/md/tech/4954); [kompozy](https://kompozy.io/news/logseq-2-0-db-version-beta).
- Zensical (MIT, 0.1.0 on 2026-11-05, beta, reads `mkdocs.yml`, offline client-side search) and Material for MkDocs (maintenance mode) were verified yesterday — [earlier notes](../OT%20pentesting%20knowledge%20base/knowledge_storage.md). I did not re-check them today.

### Inferences
- **Logseq:** reject. It is outliner-first, its storage is moving to SQLite, and its Markdown round-trip is not shipped. That is the opposite of "Markdown in Git is the source of truth".
- **Foam:** a VS Code extension for wikilinks, backlinks and graph. I could not fetch its README today (404 at the path tried), so its status is **unverified**. It suits developers who already live in VS Code, not OT engineers. Optional, like Obsidian.
- **Quartz vs Zensical:** choose Quartz only if backlinks and graph matter to site readers, which they will not until playbooks exist. Otherwise Zensical with a vanilla `mkdocs.yml`, per the earlier notes. Quartz is a Node build; Zensical is Python.
- **Plain GitLab/GitHub rendering** shows frontmatter as a table at the top of the file (GitHub does; GitLab behaviour not verified today), renders relative links, and has search. For 68 entries plus a generated index and cross-reference tables, that is enough for the team and for agents.

### Gaps
- Quartz licence and maintenance cadence, Foam status, and GitLab's frontmatter rendering were not verified today.

## Q4. Knowledge graphs: when they pay off, what the schema would be, GraphRAG evidence

### Takeaway
A graph database (Neo4j, RDF/SPARQL, OpenCTI) or GraphRAG is overkill for 68 entries, about 234 KB of text and roughly 60,000 tokens, which fits in one LLM context. The domain does have a natural graph shape, so write the edges down as frontmatter IDs now (cheap, and portable to any graph later). Adopt a graph tool only when a recurring multi-hop question cannot be answered by grep plus generated tables.

### Cited Findings
- Microsoft GraphRAG README: "GraphRAG indexing can be an expensive operation"; out-of-the-box use "may not yield the best possible results" and prompt tuning is advised; the code "serves as a demonstration and is not an officially supported Microsoft offering"; "This project is largely in maintenance mode, and won't be accepting new PRs or implementing new features" — [microsoft/graphrag README](https://raw.githubusercontent.com/microsoft/graphrag/main/README.md).
- Xiang et al. (GraphRAG-Bench, ICLR 2026): "recent studies report that GraphRAG frequently underperforms vanilla RAG on many real-world tasks"; the paper investigates "the conditions when GraphRAG surpasses traditional RAG" — [arXiv 2506.05690](https://arxiv.org/abs/2506.05690). The detailed numbers were not in the abstract. A secondary summary says graphs roughly tie on simple fact retrieval and lead on complex reasoning and summarization — [search summary; Persistent blog](https://www.persistent.com/blogs/when-does-graphrag-outperform-traditional-rag/) (**unverified against the paper**).
- Han et al., "RAG vs. GraphRAG: A Systematic Evaluation and Key Insights": a unified-protocol comparison on QA and query-based summarization. It analyses failure modes and efficiency trade-offs; per the search summary, RAG and GraphRAG are complementary, each better on different tasks — [arXiv 2502.11371](https://arxiv.org/abs/2502.11371).
- A corpus under about 200,000 tokens can go directly in the prompt — [Anthropic, Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) (verified in the earlier round).
- Local check: all 68 entries total 234,403 bytes, about 60,000 tokens at 4 characters per token.
- ATT&CK is distributed as STIX objects joined by typed relationships, with an ICS domain, revoked/deprecated flags and versioned bundles; v20.1 was released 2026-11-05 — verified in the earlier round, [ATT&CK USAGE](https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/USAGE.md).

### Inferences
- **The GraphRAG evidence argues against it here.** It helps on multi-hop and global "summarise the whole corpus" questions over large corpora. It costs LLM indexing and latency, and Microsoft's reference implementation is now maintenance-only. A 60k-token corpus can simply be read whole by an agent, which beats any retrieval, graph or vector.
- **Domain schema, if ever needed** (judgment):
  - Nodes: Source, OWASP-OT item, ATT&CK-ICS technique, CWE, CAPEC, D3FEND countermeasure, Protocol (Modbus, OPC UA, PROFINET), Device or product family, Firmware version, CVE, Tool, Playbook, Finding template.
  - Edges: Source-COVERS->OWASP item; Source-SUPERSEDED_BY->Source; Playbook-CITES->Source; Playbook-TESTS->Technique; Technique-USES_PROTOCOL->Protocol; Device-SPEAKS->Protocol; Device-HAS_FIRMWARE->Firmware-AFFECTED_BY->CVE-HAS_WEAKNESS->CWE; Finding-MAPS_TO->{CWE, Technique, OWASP item}; Tool-IMPLEMENTS->Technique; Technique-MITIGATED_BY->D3FEND.
  - Of these, only COVERS and SUPERSEDED_BY have data today.
- **What would justify a graph tool:** (a) a recurring multi-hop query, such as "which techniques against protocols spoken by device X have no playbook and no primary source", asked often enough that hand-joining tables hurts; (b) importing external graphs (ATT&CK STIX, CVE to CWE to CAPEC) and joining them with the team's own entries at scale, such as thousands of CVEs across many device families; (c) a counterpart that requires STIX or OpenCTI exchange (already covered by the earlier STIX/MISP table). At that point, start with a SQLite or DuckDB file generated from frontmatter plus the ATT&CK JSON. Use Neo4j or OpenCTI only if the queries become path-shaped and the team will run the server.
- **OpenCTI** is a CTI platform (threat actors, indicators, reports) and is the wrong shape for methodology knowledge. I did not re-verify its docs today; this is judgment consistent with the earlier STIX verdict.
- **The earlier "skip knowledge graphs" was right in outcome.** Its stated trigger, "until something queries the links", is fine but should be made concrete: the trigger is a question that a generated cross-reference table cannot answer.

### Gaps
- I did not read the full results tables of either GraphRAG paper, so no specific corpus-size threshold can be cited. **I found no study of GraphRAG on corpora as small as 60k tokens**; the "read it whole" argument rests on context-window size, not on a benchmark.
- Neo4j, OpenCTI, D3FEND and CAPEC docs were not fetched this round.

## Q5. A lightweight middle path: generated cross-reference tables

### Takeaway
Yes, and it is the recommended next step. The existing `build_index.py` already parses this frontmatter, so extend it, or add about 30 lines of stdlib, to emit a `CROSSREF.md`: a table of OWASP OT items by source (primary and secondary counts, linked slugs), a list of superseded entries, and later ATT&CK for ICS technique by source and a "Cited by" table for playbooks. Everyone reads that in the forge or any Markdown viewer, Obsidian included, and agents read it as text. It is the graph, as tables.

### Cited Findings
- Local check, a 10-line stdlib prototype, run read-only in the knowledge-base folder, parsed `owasp_ot` and `trust` from all 68 entries without PyYAML and produced per-item counts:

  | OWASP OT item | Sources | Primary |
  |---|---|---|
  | 1 | 16 | 10 |
  | 2 | 39 | 31 |
  | 3 | 30 | 28 |
  | 4 | 17 | 12 |
  | 5 | 21 | 18 |
  | 6 | 16 | 12 |
  | 7 | 15 | 12 |
  | 8 | 17 | 10 |
  | 9 | 22 | 15 |
  | 10 | 16 | 13 |

  The table answers "all primary sources for OWASP OT #7" (12 entries) with no tool installed. It also shows the coverage skew, items 2 and 3 against item 7, which is a source-gap signal.
- Local check: `build_index.py` exists at the repo root and already generates `knowledge-base/INDEX.md`.
- Earlier notes already propose `attack_ics:`, `cwe:`, `review_by:` and a playbook `sources:` field, plus a stdlib `check_kb.py` — [earlier notes](../OT%20pentesting%20knowledge%20base/knowledge_storage.md).

### Inferences
- **Minimal setup, judgment:**
  1. Extend `build_index.py` to also write `knowledge-base/CROSSREF.md` with:
     - OWASP OT item x source: slugs as relative links, primary first;
     - a superseded list;
     - an "overdue review" list, once `review_by` exists;
     - a "Cited by" section per source, once playbooks with `sources:` exist (this is generated backlinks);
     - ATT&CK-ICS x source, once `attack_ics` is populated. The 5 entries that mention T-IDs in body text are the start.
  2. Keep relative Markdown links only; no wikilinks.
  3. Optionally, one committed `knowledge-base/sources.base` file for Obsidian users. It is a YAML view that other tools ignore. Add it only after the 10-minute test in Q2, and after fixing `published: unknown` if it breaks the Date type.
  4. Add a one-line README note: "Obsidian works: open the clone as a vault, turn off wikilinks, do not commit `.obsidian/`."
- **Next-step triggers:**
  - Static site (Zensical, or Quartz if a graph matters): when people outside the forge must read it.
  - SQLite or DuckDB generated from frontmatter plus ATT&CK STIX: when a question needs joins across three or more entity types, or external datasets are joined at scale.
  - Neo4j or OpenCTI: only if those queries are path-shaped, recurring, and someone will own the server.
  - GraphRAG: not before the corpus is far beyond one context window *and* plain retrieval demonstrably misses multi-hop answers.
- **Was the earlier round wrong?** No on the verdict. Two refinements:
  - "Obsidian as an optional reader" is right, but its graph and backlinks are currently empty, so do not sell Obsidian to the team on those features.
  - The "grep-generated backlinks" idea should become an explicit `CROSSREF.md` output now, since it already answers the queries the task lists, for every audience at once.
- **The earlier notes did not cover the frontmatter's fit with tools.** `published: unknown` (25 entries) is the one schema change worth making regardless of tool: an empty or absent value is friendlier to every YAML consumer than a sentinel string in a date field.

### Gaps
- No evidence base exists comparing generated tables with graph tools for small security KBs. The middle path is a judgment from size, audience and the cost evidence above.
