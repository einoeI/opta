---
title: "anthropics/skills: Public repository for Agent Skills"
url: https://github.com/anthropics/skills/tree/main
type: vendor-doc
trust: primary
accessed: 2026-11-09
published: 2025-09-22
owasp_ot: [3]
version: "commit 2c5958ecac7c (2026-11-06)"
license: "No root license detected by GitHub API; README states many skills, including docx/pdf/pptx/xlsx, are Apache 2.0"
---

## Summary
Anthropic's public repository of example Agent Skills, the reference for the SKILL.md format. A skill is a folder with a SKILL.md holding YAML frontmatter and instructions, optionally with scripts, references and assets. The README labels the skills as demonstrations. The format specification has moved to agentskills.io. There are no security-testing or OT skills in the listing. Read only; nothing cloned or executed.

## Key facts
- Repo metadata (GitHub API, 2026-11-09): 190,567 stars, 22,416 forks, 1,504 open issues, created 2025-09-22, last commit 2026-11-06.
- Layout: `.claude-plugin/`, `skills/`, `spec/`, `template/`, `THIRD_PARTY_NOTICES.md` (repo page).
- `skills/` folders seen in the listing (19, listing may be incomplete): academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx.
- README template frontmatter: `name` (unique, lowercase with hyphens) and `description` (what it does and when to use it).
- Licensing: "Many skills in this repo are open source (Apache 2.0)", and the document skills are also stated as Apache 2.0 (README).
- `spec/agent-skills-spec.md` now only points to https://agentskills.io/specification (accessed 2026-11-09).
- Spec, directory: SKILL.md required; `scripts/`, `references/`, `assets/` optional (agentskills.io/specification).
- Spec, frontmatter: `name` max 64 chars, lowercase alphanumerics and hyphens, no leading/trailing or consecutive hyphens, must match the directory; `description` max 1024 chars; optional `license`, `compatibility` (max 500), `metadata`, and `allowed-tools` (agentskills.io/specification).
- `allowed-tools` is a space-separated list of pre-approved tools, marked experimental, with support varying by implementation (agentskills.io/specification).
- Progressive disclosure: about 100 tokens of metadata at startup; full SKILL.md on activation (under 5000 tokens recommended); resources on demand. Keep SKILL.md under 500 lines and references one level deep (agentskills.io/specification).
- Validation: the `skills-ref validate` tool checks frontmatter and naming conventions (agentskills.io/specification).
- The spec has no permission manifest, signature, or hash field; these exist only in OWASP's proposed format (compare `owasp-agentic-skills-top-10`).
- Content addressed to AI agents: none beyond normal documentation.

## Verbatim
> "These skills are provided for demonstration and educational purposes only." (README, Disclaimer)

> "Always test skills thoroughly in your own environment before relying on them for critical tasks." (README, Disclaimer)

## Relevance
Inference, not from the source:
- Use the format, not the content. OT skills should follow the folder layout and progressive disclosure.
- `allowed-tools` pre-approves tools rather than restricting them, and is experimental, so it cannot be the OT permission boundary.
- `metadata` is the natural place to carry a risk tier and content hash until the format has first-class fields.
- Default skills do not include any network-attack capability to inherit, which is appropriate for a controlled library.
