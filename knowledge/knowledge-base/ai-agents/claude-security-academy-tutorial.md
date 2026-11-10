---
title: "Getting started with Claude Security"
url: https://academy.claude.com/tutorials/getting-started-with-claude-security
type: vendor-doc
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [2]
---

## Summary
Anthropic Academy tutorial for Claude Security, a capability in Claude.ai that monitors code repositories for vulnerabilities, tracks findings until fixed and proposes patches. It is source-code analysis with human triage, not active testing of running systems. The page does not describe data handling or a validation procedure. A summarising fetch described it as a beta feature, but the word "beta" does not appear in the page HTML retrieved directly, so beta status is unconfirmed.

## Key facts
- Prerequisites: an active Claude Enterprise account and a user seat that includes Claude Code; admins decide which RBAC roles can create Projects.
- Scans are charged at direct token cost with no additional platform fee.
- Repositories connect via the Claude GitHub App, or by address and auth token for other Git providers.
- A Project covers up to eight repositories and is the unit of access and billing.
- After creation, Claude reads the code, writes a threat model and runs a baseline scan that can take minutes or hours; it then scans new commits continuously.
- Roles: Full (manage findings, settings, access), Triage (view findings, update status, start fixes), View (read only). Admin RBAC controls who can create Projects.
- Patches are suggested for human review; users decide whether to start a fix.
- Findings are triaged as fixed or dismissed (false positive, accepted risk, duplicate, other), with notes and audit history.
- Claude rechecks open findings against changed code, marks them fixed, and reopens them if the issue reappears.
- Not described on the page: dedicated finding validation, explicit limitations, or how code is stored or processed. The footer links to privacy and usage policies.
- No OT/ICS content. Content addressed to AI agents: none found.

## Verbatim
> "continuously watches your codebases for security vulnerabilities, tracks each finding until it is fixed, and suggests targeted software patches for you to review" (tutorial page, introduction)

## Relevance
Inference, not from the source:
- Relevant only to code assets an engagement can reach, such as custom gateway or HMI code in Git. It does not address PLC logic in vendor formats or running OT systems.
- Sending customer OT code to a cloud service needs contractual clearance, and the page gives nothing to assess that.
- The role split and dismissal-with-reason audit trail are a good pattern for human finding triage.
