---
title: "0x727/BypassPro (README_EN)"
url: https://github.com/0x727/BypassPro/blob/main/README_EN.md
type: tool
trust: primary
accessed: 2026-11-09
published: 2023-04-06
owasp_ot: [5]
version: "commit 4dca2c01d6cf (2026-10-30, 'Release BypassPro 5.1'); README describes 5.2 highlights"
license: Apache-2.0
---

## Summary
A Java Burp Suite extension that automates testing of web access controls (401/403 responses, unauthorised access) and of web application firewall and parser behaviour during authorised testing. It generates request variants and offers a manual workbench. It is not an LLM tool and has no OT/ICS scope. Described here at a functional level only; techniques and payloads are deliberately not recorded. Read only; nothing cloned or executed.

## Key facts
- Repo metadata (GitHub API, 2026-11-09): 1,332 stars, 66 forks, Apache-2.0, 0 open issues, not archived, created 2023-04-06, last commit 2026-10-30.
- Category: Burp Suite extension; Java 8 compatible, builds on JDK 8+ (README_EN).
- Function: automated request-variant generation for access-control and WAF testing, a manual request workbench, and YAML-based configuration (README_EN).
- It has a raw-socket sending mode that does not use Burp's upstream proxy settings, intended for labs, CTFs and authorised testing (README_EN, line 130).
- Origin: second-development fork of an earlier Burp extension, published with the original author's permission (README_EN).
- Disclaimer: learning, research and authorised testing only (README_EN, line 3).
- Version note: the last commit is titled 5.1 while the README has a 5.2 highlights section (README_EN).
- ICS/OT/SCADA: not mentioned (README_EN).
- Content addressed to AI agents: none found.

## Verbatim
> "all techniques, ideas, and tooling described here are provided only for security learning, research, and authorized testing." (README_EN, line 3)

## Relevance
Inference, not from the source:
- Marginal for OT: only conceivable against HTTP interfaces such as HMI or engineering web panels, and only on a lab or spare device.
- Automated variant generation means bursts of malformed requests, which is the wrong profile for embedded web servers of unknown robustness on production networks.
- The raw-socket mode escapes the proxy path, so a proxy-based scope or logging control would not see that traffic.
- Should not be packaged into a shared agent skill.
