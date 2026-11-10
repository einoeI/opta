---
title: "BloodHound Community Edition (SpecterOps/BloodHound)"
url: "https://github.com/SpecterOps/BloodHound"
type: tool
trust: primary
accessed: 2026-11-09
published: 2026-11-06
owasp_ot: [5,7]
version: "CE v9.9.2 (2026-11-06); main @ 405bbc44734e (2026-11-09)"
license: "Apache-2.0"
---

## Summary
Monolithic web application (React frontend with Sigma.js, Go REST API, PostgreSQL and Neo4j) that uses graph theory to reveal relationships across identity and access management systems. It is maintained by SpecterOps. It is an identity attack-path tool and is unrelated to firmware or SBOM analysis.

## Key facts
- The link given in lowercase resolves to the canonical name SpecterOps/BloodHound.
- 3,542 stars; repo description "Six Degrees of Domain Admin".
- Powered by OpenGraph, per the README, for modelling relationships in identity systems.
- Community Edition via the published quickstart and Docker Compose example.

## Verbatim
- "BloodHound leverages graph theory to reveal hidden and often unintended relationships across identity and access management systems."

## Relevance
Out of scope for the SBOM toolchain. Inference: applicable to AD-integrated IT/OT boundaries and to access-path review (OWASP OT #5, #7), relevant here because the vendor checklist includes an optional Active Directory/LDAP connection.
