---
title: "OWASP Dependency-Track"
url: "https://dependencytrack.org/"
type: tool
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [2,3]
version: "5.2.1 (latest in release feed); 4.14.6 also released; site advertises 5.2"
license: "Apache-2.0"
---

## Summary
Open source platform that ingests CycloneDX BOMs into a portfolio inventory and continuously re-analyzes them against vulnerability and policy data. Version 5 is a redesign, separating API server and frontend images and requiring PostgreSQL. Also covers https://owasp.org/projects/dependency-track?tab=download.

## Key facts
- OWASP Flagship project; Apache 2.0; Java.
- Ingests CycloneDX SBOMs through REST API, CI plugins or web UI; tracks libraries, containers, operating systems, firmware, hardware and services.
- Consumes and produces CycloneDX SBOM, HBOM, VEX and VDR (OWASP page).
- Vulnerability sources named by the project: NVD, GitHub Advisories, OSV, Snyk, plus Sonatype OSS Index (site) or Sonatype Guide (OWASP page), Trivy and VulnDB (OWASP page).
- Prioritizes with EPSS, and has an expression-based policy engine.
- v5: "bundled container image and executable WAR are discontinued" in favor of separate API server and frontend images (`dependencytrack/apiserver`, `dependencytrack/frontend`).
- Docker Compose quickstart; default sign-in credentials admin/admin on first run.
- The "20,000+ organizations" figure is the project's own claim.

## Verbatim
- "Ingest CycloneDX SBOMs and track libraries, containers, operating systems, firmware, and services across every version of every project in your portfolio."
- "The bundled container image and executable WAR are discontinued in favor of separate API server and frontend images."

## Relevance
Candidate persistence and re-matching layer for per-device SBOMs (`research-notes.md` §7, "build once, re-match later"). EMBA documents a Dependency-Track integration. Inference: not needed for a single-device pentest; adds value when tracking many profiles over time (OWASP OT #2).
