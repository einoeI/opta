---
title: "CERT@VDE RSS/Atom feeds and CSAF endpoints"
url: "https://certvde.com/de/service/rss-feeds/"
type: dataset
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [2,3]
---

## Summary
Index of CERT@VDE news, bulletin and advisory feeds, per-vendor advisory feeds, the CSAF aggregator and CSAF trusted provider metadata URLs. It is the discovery point for automation vendors coordinated through CERT@VDE, Phoenix Contact among them. Coverage differs between the feed list, trusted providers and aggregator.

## Key facts
- General feeds: `/de/blog/feeds/{rss,atom}/`, `/de/bulletins/feeds/{rss,atom}/`, `/de/advisories/feeds/{rss,atom}/`.
- Per-vendor feeds: `/de/advisories/vendor/<slug>/feeds/{rss,atom}/`; 41 vendor slugs, including `phoenixcontact`, `wago`, `beckhoff`, `codesys`, `festo`, `pilz`.
- CSAF aggregator: `https://aggregator.certvde.com/.well-known/csaf-aggregator/aggregator.json`; its `csaf_providers` array held 25 entries, last_updated 2026-11-09.
- CSAF trusted providers: 46 distinct hosts of the form `https://<slug>.csaf-tp.certvde.com/.well-known/csaf/provider-metadata.json`.
- The page does not mention TLP or license terms.
- Phoenix Contact provider metadata (fetched directly): role `csaf_trusted_provider`, publisher Phoenix Contact GmbH & Co. KG, contact psirt@phoenixcontact.com, ROLIE feed `csaf-feed-tlp-white.json`.
- That Phoenix Contact TLP:WHITE feed held 115 entries, oldest published 2017-03-07, latest updated 2026-11-04.

## Verbatim
None retained.

## Relevance
Air-gap or direct fallback when CIRCL is unavailable, and confirms the 115-advisory count in `research-notes.md` §5. Phoenix Contact is the publisher; CERT@VDE hosts the provider (OWASP OT #2, #3). Inference: for complete coverage use the 46 per-provider URLs, not the 25-provider aggregator.
