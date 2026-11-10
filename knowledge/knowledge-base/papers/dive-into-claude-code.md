---
title: "Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems"
url: https://arxiv.org/abs/2604.14228
type: paper
trust: secondary
accessed: 2026-11-09
published: 2026-10-10
owasp_ot: [3, 5, 9]
version: "arXiv:2604.14228v3 (10 Oct 2026); analyses Claude Code v2.1.88 source snapshot"
local_file: "sources/papers/2604.14228v3.pdf"
---

## Summary
Liu et al. (MBZUAI/UCL) analyse Claude Code's TypeScript source at v2.1.88 and compare it with OpenClaw and Hermes Agent. The core is a simple model-tools loop; most code surrounds it with a seven-mode permission system, layered safety checks, context compaction, and four extension mechanisms. The paper quantifies approval fatigue and documents where defence-in-depth has failed. It is a third-party preprint, so behaviour may differ in later versions. Not about pentesting; it is the main source here on harness and permission design.

## Key facts
- Design ratio: an estimated 1.6% of the codebase is AI decision logic, 98.4% operational infrastructure (§3, p.6; §12.7, pp.38-39).
- Seven independent safety layers: tool pre-filtering, deny-first rules, permission-mode constraints, auto-mode ML classifier, shell sandboxing, not restoring permissions on resume, hook interception (§3.5, pp.9-10).
- Deny-first: a deny rule always beats an allow rule, even a more specific allow (§5.1, p.14).
- Pre-filtering removes blanket-denied tools from the model's view at tool-pool assembly (§5.2, p.14).
- Modes: plan, default, acceptEdits, auto (feature-gated), dontAsk, bypassPermissions, and internal bubble for subagent escalation (§5.1, p.13).
- dontAsk auto-denies anything that would otherwise prompt; bypassPermissions still keeps safety-critical checks and bypass-immune rules (§5.1, p.13).
- Approval fatigue: users approve about 93% of prompts (§5, p.13; §12.3, p.35). Auto-approve rates rise from about 20% below 50 sessions to over 40% by 750 sessions (§12.3, p.35).
- Sandboxing reduced permission prompts by an estimated 84% (§12.3, p.35).
- Denial as routing signal: on a block, the model receives the reason and attempts a safer alternative next iteration, so enforcement shapes behaviour rather than halting it (§5.2, p.14).
- PreToolUse hooks can deny, ask or modify input; a hook allow does not bypass later rule denies or safety checks (§5.2-5.3, pp.14-15). Of 27 hook events, five take part directly in the permission flow (§5.3, p.15).
- Authorisation and isolation are separate axes: a command can be approved yet still sandboxed (§5.4, p.15).
- Layered failure: commands with more than 50 subcommands fell back to one generic approval instead of per-subcommand deny checks, because of UI freezes (§5.4, p.15; §12.3, p.35).
- Sandbox gap: independent research reports a parser-differential in network confinement for v2.0.24-v2.1.89, no CVE assigned (§5.4 footnote 3, p.15; source grade "Tier C").
- Pre-trust window: CVE-2025-59536 (CVSS 8.7) and CVE-2026-21852 (CVSS 5.3) ran code during project initialisation before trust acceptance; patched (§12.3 footnote 5, p.35).
- Extension context cost: hooks zero, skills low until invoked, plugins medium, MCP high once schemas load (Table 2, p.18).
- Skills: a SKILL.md with YAML frontmatter, 15+ parsed fields including allowed tools, model overrides, fork execution context; skills can define hooks that register on invocation (§6.1, p.17).
- Plugins accept ten component types and are the main third-party distribution vehicle (§6.1, p.17).
- Subagents run in isolated context, return only a summary, and write separate transcripts for audit (§8.1-8.3, pp.21-23).
- Session-scoped permissions are not stored in the transcript, so a resumed process must be re-granted them (§9.2, p.24).
- Transcripts are append-only JSONL, favouring auditability over query power (§12.7, p.38).
- Silent failure: one cited industry estimate says 78% of AI failures are invisible (§12.6, p.37; secondary citation of a Bessemer report).
- Stated structural limit: any LLM agent that uses the model for its own safety evaluation shares failure modes across layers (§12.3, p.35).

## Verbatim
> "users approve approximately 93% of permission prompts, indicating that approval fatigue renders interactive confirmation behaviorally unreliable as a sole safety mechanism." (§5, p.13)

> "The relevant evaluation criterion is not whether any individual layer can be bypassed, but how many independent layers must fail simultaneously and whether they share failure modes." (§12.3, p.35)

## Relevance
Inference, not from the source:
- Human approval alone cannot be the OT safety control. Approvals must be rare and high-signal, with deterministic denial for dangerous classes.
- In OT, a denial should be a hard stop for the class of action. A denial that invites a "safer alternative" could lead an agent to route around a block.
- Tool pre-filtering, so write-capable OT tools do not exist in the agent's pool, is stronger than relying on approval.
- The compound-command fallback argues for single-purpose tool wrappers rather than raw shell near OT networks.
- Not restoring grants on resume is a useful property for per-window authorisation.
- The paper analyses one version; re-check behaviour against the deployed version before relying on any specific control.
