"""otpa components: add to devices/<d>/components.csv from an SBOM (CycloneDX or SPDX JSON),
the curated picker (catalog/components.csv) or free text (flagged unmapped)."""
import csv
import json
import pathlib
import shutil

from otpa import OtpaError, manifest
from otpa.engagement import device_dir

CATALOG = pathlib.Path(__file__).resolve().parents[3] / "catalog" / "components.csv"
COLUMNS = ["name", "version", "cpe", "purl", "service", "ports", "origin", "mapped"]


def register(sub):
    p = sub.add_parser("components", help="add components to a device")
    p.add_argument("device", help="path under workspace/devices, e.g. phoenix-contact/axc-f-2152/2022.0.8")
    p.add_argument("--sbom", action="append", default=[], type=pathlib.Path, help="CycloneDX or SPDX JSON")
    p.add_argument("--pick", action="append", default=[], metavar="NAME@VERSION",
                   help="component from catalog/components.csv (name or alias)")
    p.add_argument("--free", action="append", default=[], metavar="TEXT@VERSION",
                   help="anything else; stored as unmapped")
    p.set_defaults(run=run)


def read_csv(path):
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, columns):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, columns, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def load_catalog():
    return read_csv(CATALOG)


def catalog_lookup(catalog, name="", cpe=""):
    """Catalog row matching the CPE vendor:product, or the name/an alias (case-insensitive)."""
    name = name.casefold()
    for row in catalog:
        if cpe and row["cpe"] == cpe:
            return row
        if name and name in [row["name"].casefold()] + row["aliases"].casefold().split(";"):
            return row
    return None


def _cpe_short(cpe23):
    parts = cpe23.split(":")
    return f"{parts[3]}:{parts[4]}" if len(parts) > 4 else ""


def parse_sbom(doc):
    """[{name, version, cpe (vendor:product), purl}] from CycloneDX or SPDX JSON.
    ponytail: top-level components only; nested CycloneDX components are skipped."""
    if doc.get("bomFormat") == "CycloneDX":
        return [{"name": c["name"], "version": c.get("version", ""), "cpe": _cpe_short(c.get("cpe", "")),
                 "purl": c.get("purl", "")} for c in doc.get("components", [])]
    if "spdxVersion" in doc:
        out = []
        for p in doc.get("packages", []):
            refs = {r["referenceType"]: r["referenceLocator"] for r in p.get("externalRefs", [])}
            out.append({"name": p["name"], "version": p.get("versionInfo", ""),
                        "cpe": _cpe_short(refs.get("cpe23Type", "")), "purl": refs.get("purl", "")})
        return out
    raise OtpaError("SBOM is neither CycloneDX nor SPDX JSON")


def _split(spec):
    name, _, version = spec.rpartition("@")
    return (name, version) if name else (version, "")


def _row(name, version, cpe, purl, cat, origin):
    return {"name": name, "version": version, "cpe": cpe or (cat or {}).get("cpe", ""), "purl": purl,
            "service": (cat or {}).get("service", ""), "ports": (cat or {}).get("ports", ""),
            "origin": origin, "mapped": "yes" if cpe or purl or cat else "no"}


def run(args, argv):
    dev = device_dir(args.workspace, args.device)
    catalog = load_catalog()
    new = []
    for path in args.sbom:
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            raise OtpaError(f"{path}: {e}")
        target = dev / "sbom" / path.name
        if target.exists() and target.read_bytes() != path.read_bytes():
            raise OtpaError(f"{target} exists with other content; rename the SBOM")
        for c in parse_sbom(doc):
            cat = catalog_lookup(catalog, c["name"], c["cpe"])
            new.append(_row(c["name"], c["version"], c["cpe"], c["purl"], cat, "sbom"))
    for spec in args.pick:
        name, version = _split(spec)
        cat = catalog_lookup(catalog, name)
        if not cat:
            raise OtpaError(f"{name} is not in {CATALOG}; use --free or add it to the catalog")
        new.append(_row(cat["name"], version, "", cat["purl"], cat, "picker"))
    for spec in args.free:
        new.append(_row(*_split(spec), "", "", None, "free"))
    if not new:
        raise OtpaError("nothing to add: give --sbom, --pick or --free")

    out = dev / "components.csv"
    with manifest.record(dev, argv) as entry:
        for path in args.sbom:
            (dev / "sbom").mkdir(exist_ok=True)
            shutil.copyfile(path, dev / "sbom" / path.name)
        rows = {(r["name"].casefold(), r["version"]): r for r in read_csv(out) + new}
        write_csv(out, [rows[k] for k in sorted(rows)], COLUMNS)
        entry["inputs"] = [dev / "sbom" / p.name for p in args.sbom]
        entry["outputs"] = [out]
    print(f"{out}: {len(rows)} components")
