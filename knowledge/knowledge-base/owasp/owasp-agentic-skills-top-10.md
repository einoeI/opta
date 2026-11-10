---
title: "OWASP Agentic Skills Top 10 (AST10)"
url: https://owasp.github.io/www-project-agentic-skills-top-10/
type: standard
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [3, 5, 9]
version: "1.0 (2026 Edition); status New Project Proposal, active development; page says 'Last updated: March 2026'"
license: CC-BY-SA-4.0
---

## Summary
OWASP incubator project listing the ten main security risks of agentic AI skills across platforms, with severity, mitigations, an incident timeline and a proposed universal skill format. Its core claim is that skills are an under-protected execution layer between the model and MCP tools, mixing natural-language instructions with code. Project status is still a proposal, and incident statistics are drawn from vendor research rather than OWASP's own measurements. Facts below come from the index page and the ten per-risk pages (`ast01.html` to `ast10.html`).

## Key facts
- AST01 Malicious Skills (Critical): hidden payloads in skills or SKILL.md prose. Mitigation includes ed25519 signatures bound to revocable publisher identity, behavioural scanning, and isolation. A signature proves authorship, not safety (ast01).
- AST02 Supply Chain Compromise (Critical): weak registry provenance. Pin nested dependencies to sha256; treat repo config files as executable code; use an internal mirror or allowlist; provide revocation (ast02).
- AST03 Over-Privileged Skills (High): broader permissions than needed. Require a permission manifest, per-skill scoped credentials, runtime enforcement, domain-level network allowlists, an instruction hierarchy that never elevates tool output, and operator consent for persistent state changes (ast03).
- AST04 Insecure Metadata (High): manifests can impersonate or understate risk, and unsafe parsing can execute code at load. Use safe parsers, schema validation, and detection of zero-width or smuggled characters (ast04).
- AST05 Untrusted External Instructions (High): remote documents a skill references become instructions but are mutable. Pin content hashes, inline at publish time, allowlist domains, audit transitively (ast05).
- AST06 Weak Isolation (High): skills run with the host agent's full access. Container isolation by default, host mode as explicit opt-in, seccomp/AppArmor, per-skill process isolation (ast06).
- AST07 Update Drift (Medium): pin to content hashes, verify signatures, use a freeze mode in production, and require human approval for skill updates in enterprises (ast07).
- AST08 Poor Scanning (Medium): pattern-matching misses natural-language attacks. Combine pattern, semantic and sandbox analysis; scan the whole directory; treat scanner results as advisory and the scanner's own LLM as attackable (ast08).
- AST09 No Governance (Medium): central inventory, approval workflow, non-human identities with scoped credentials, audit logging of file, network, shell and memory actions, formal revocation (ast09).
- AST10 Cross-Platform Reuse (Medium): security metadata is lost when porting; re-validate on every port (ast10).
- Lethal Trifecta, attributed to Simon Willison / Palo Alto Networks: private data access + untrusted content exposure + external communication (index).
- Scale claims as reported on the page: Snyk ToxicSkills scanned 3,984 skills, 1,467 (36.82%) with flaws, 534 (13.4%) critical, 76+ malicious payloads (index).
- ClawHavoc: 1,184 malicious skills, per Antiy CERT (index).
- Trail of Bits, Jun 2026: every public skill scanner tested was bypassed in under an hour (index).
- Air Security, Jun 2026: a researcher-built malicious skill reached over 26,000 agents while cleared by every scanner; 17,822 of 142,836 live skills (12.4%) rest on an untrusted external instruction source (index).
- Air Security, Jul 2026: 925 skills serving about 134K agents sit on hijackable dependencies (index).
- Claude Code CVE-2025-59536 and CVE-2026-21852: repo config could run commands before the trust dialog; patched (index).
- Proposed Universal Skill Format fields: `permissions` (files read/write/deny_write, network allow/deny, shell, tools), `risk_tier` L0-L3 (L3 = destructive), `signature`, `content_hash`, `scan_status`, `requires` (index).
- Content addressed to AI agents: none found.

## Verbatim
> "A signature proves authorship, not safety" (ast01)

> "Enforce a human-in-the-loop approval step for any skill update in enterprise environments." (ast07)

## Relevance
Inference, not from the source:
- Directly applicable as the threat model for a shared OT pentest skill library; see the mapping in the research notes.
- Page reliability flags: the "Last updated: March 2026" footer predates its June and July 2026 entries; the version is 1.0 while the status remains a proposal, and its timeline schedules v1.0 release for Q4 2026.
- The page lists the Claude Code skill format as "skill.json / YAML + scripts/", which conflicts with SKILL.md described in `dive-into-claude-code` (§6.1) and `anthropics-skills`. Prefer the latter for format facts.
- Incident numbers come from third-party vendor research, cited by OWASP. Trace originals before quoting them.
