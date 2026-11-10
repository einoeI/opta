---
title: "PHOENIXCONTACT/tools"
url: "https://github.com/PHOENIXCONTACT/tools"
type: tool
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [3]
version: "main @ f11debdc3b3d (2026-09-18)"
license: "Apache-2.0"
---

## Summary
GitHub Actions, reusable workflows and helper scripts used by Phoenix Contact's MORYX team to maintain quality for its .NET repositories. It contains a CI-time SBOM workflow, `sbom-generation-tool.yml`, which the README does not mention. That workflow builds CycloneDX SBOMs from .NET and npm project sources. It does not analyze firmware, filesystem images or PLCnext device software.

## Key facts
- Repository description: "This repo contains GitHub Actions, Workflows and other tools that the MORYX team uses to maintain quality".
- Latest main commit f11debdc3b3d, 2026-09-18; 3 stars; not archived; license Apache-2.0.
- `.github/workflows/` holds build, documentation, integrationtest, publish, reportgenerator, sbom-generation and unittest tool workflows; `.github/scripts/` holds `generate-product-sboms.sh`, `merge-sboms.sh`, `bom-metadata-template.xml`. A `feature/sbom-generation-tool` branch also exists.
- `sbom-generation-tool.yml` is a `workflow_call` reusable workflow with inputs REPOSITORY_NAME, dotnet_sdk_version and node_version (default 22).
- It installs the `CycloneDX` .NET global tool, `@cyclonedx/cyclonedx-npm`, and the latest `cyclonedx-cli` release binary.
- `generate-product-sboms.sh` walks .csproj files, skipping projects that are neither packable nor deployable; it runs `dotnet-CycloneDX` per project and `cyclonedx-npm` where a `package-lock.json` exists, labelling the root component `pkg:git` (application) or `pkg:nuget` (library).
- `bom-metadata-template.xml` uses the CycloneDX 1.6 namespace.
- `merge-sboms.sh` combines per-product BOMs with `cyclonedx merge --hierarchical` into `bom-all-products.json`, adds VCS and build-system external references with jq, and sets `metadata.lifecycles` to `build`.
- The workflow validates every SBOM with `cyclonedx validate --fail-on-errors` at the document's own spec version, uploads them as an artifact, and attaches `bom-all-products.json` to `v*` tag releases.
- The workflow checks out `phoenixcontact/tools` at `ref: main` and downloads `releases/latest` of cyclonedx-cli without pinning (observed in the YAML).

## Verbatim
- `dotnet-CycloneDX "$project" -F Json -ipr -o "$output_dir" -fn "bom-dotnet.json" --set-version "$product_version"` (abridged from the script)
- `cyclonedx merge --input-files "${product_boms[@]}" --input-format json --output-format json --output-file "$output_path/bom-all-products-raw.json" --hierarchical`

## Relevance
Answers whether it can replace part of the pipeline: not for firmware. Inference: it needs a source checkout and a .NET solution, so it cannot run on a vendor firmware image. Reusable patterns are the cyclonedx-cli validate gate and hierarchical merge. Nothing here links it to PLCnext controller firmware (OWASP OT #3).
