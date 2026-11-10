---
title: "anchore/syft"
url: "https://github.com/anchore/syft"
type: tool
trust: primary
accessed: 2026-11-09
published: 2026-11-09
owasp_ot: [2,3]
version: "v1.57.1 (2026-11-09); main @ a0c0d3890a9d"
license: "Apache-2.0"
---

## Summary
CLI and Go library generating SBOMs from container images, filesystems and archives, across many packaging ecosystems. Outputs include CycloneDX, SPDX and Syft JSON. Its dpkg cataloger reads opkg metadata as well as dpkg. No SquashFS or RAUC target type was found in its docs, so firmware must be extracted first.

## Key facts
- Scan targets include container images, OCI/docker archives and layouts, directories, files, archives and Singularity SIF.
- `dpkg-db-cataloger` patterns: `lib/dpkg/status`, `lib/dpkg/status.d/*`, `lib/opkg/info/*.control`, `lib/opkg/status`.
- Output formats include CycloneDX, SPDX and Syft JSON, with SBOM format conversion.
- Can create signed SBOM attestations using in-toto.
- `--from containers-storage` reads Podman/Buildah local stores on Linux.
- Docs page for scan targets contains no "squash" match (grep, 2026-11-09).

## Verbatim
- "A CLI tool and Go library for generating a Software Bill of Materials (SBOM) from container images and filesystems."

## Relevance
Supports the `research-notes.md` §7-8 plan (Syft on an unpacked rootfs). Yocto-style `opkg` metadata is covered by path pattern. Inference: `dpkg`/`opkg` entries on PLCnext will carry no upstream distro, limiting ecosystem-based matching (OWASP OT #2, #3).
