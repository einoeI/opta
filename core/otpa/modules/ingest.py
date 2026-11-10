"""otpa ingest: store nmap XML / OIDA NDJSON (--json-log) in evidence/scans/, then rebuild
from all stored scans: ports.csv, oida.csv (OIDA security findings) and the engagement's
cves.csv (device CVEs per target with reachability, Observed, and decisions applied).

Reachability per component, from catalog/components.csv:
  yes      an open port matches (nmap product contains the component name, or the
           port's service is one of the component's services; OIDA rows use the module name)
  no       the component has services, every transport of its ports was scanned 1-65535
           (nmap scaninfo), and nothing matches
  unknown  everything else (libraries without a service, partial scans, unknown components)
Observed: nmap reports the component's product with the same version as the CVE row."""
import json
import pathlib
import re
import shutil
import xml.etree.ElementTree as ET

from otpa import OtpaError, manifest
from otpa import engagement as E
from otpa.modules import decide
from otpa.modules.components import catalog_lookup, load_catalog, read_csv, write_csv
from otpa.modules.vulns import COLUMNS as CVE_COLUMNS

PORT_COLUMNS = ["target", "address", "port", "transport", "state", "service", "product", "version",
                "tunnel", "source"]
OIDA_COLUMNS = ["target", "address", "port", "module", "title", "category", "details"]


def register(sub):
    p = sub.add_parser("ingest", help="read nmap XML / OIDA --json-log output into an engagement")
    p.add_argument("engagement", type=pathlib.Path, help="engagement folder")
    p.add_argument("files", nargs="*", type=pathlib.Path,
                   help="nmap -oX files and OIDA --json-log files; none = rebuild from stored scans")
    p.set_defaults(run=run)


def kind(text):
    if "<nmaprun" in text[:2000]:
        return "nmap"
    try:
        first = json.loads(text.lstrip().splitlines()[0])
        if isinstance(first, dict) and "module" in first and "host" in first:
            return "oida"
    except (ValueError, IndexError):
        pass
    return None


def parse_nmap(text):
    """(ports, complete) with ports = [{address, port, transport, state, service, product, version,
    tunnel}] and complete = {(address, transport)} for hosts scanned on all 65535 ports."""
    root = ET.fromstring(text)
    full = {s.get("protocol") for s in root.iter("scaninfo") if s.get("numservices") == "65535"}
    ports, complete = [], set()
    for host in root.iter("host"):
        if host.find("status") is not None and host.find("status").get("state") != "up":
            continue
        addr = next((a.get("addr") for a in host.iter("address") if a.get("addrtype") in ("ipv4", "ipv6")), None)
        complete |= {(addr, t) for t in full}
        for p in host.iter("port"):
            svc = p.find("service")
            svc = svc.attrib if svc is not None else {}
            ports.append({"address": addr, "port": int(p.get("portid")), "transport": p.get("protocol"),
                          "state": p.find("state").get("state"), "service": svc.get("name", ""),
                          "product": svc.get("product", ""), "version": svc.get("version", ""),
                          "tunnel": svc.get("tunnel", "")})
    return ports, complete


def parse_oida(text):
    """Security findings only: they prove the port answered. Info lines do not."""
    out = []
    for line in text.splitlines():
        if not line.strip():
            continue
        e = json.loads(line)
        if e.get("event_type") == "security" and e.get("port"):
            data = e.get("data") or {}
            out.append({"address": e["host"], "port": int(e["port"]), "module": e["module"],
                        "title": data.get("finding", e.get("message", "")),
                        "category": data.get("category", ""), "details": data.get("details", "")})
    return out


def build_ports(scans, targets):
    """ports rows, oida rows, complete set; only addresses that are engagement targets."""
    rows, complete, findings = {}, set(), []
    texts = [p.read_text(encoding="utf-8") for p in scans]
    for text in sorted(texts, key=lambda t: kind(t) != "nmap"):  # nmap first: it knows the transport
        if kind(text) == "nmap":
            ports, full = parse_nmap(text)
            complete |= full
            for p in ports:
                if p["address"] not in targets:
                    continue
                key = (p["address"], p["port"], p["transport"])
                row = rows.setdefault(key, {**p, "source": set()})
                if p["state"] == "open":  # ponytail: open in any scan wins; no time ordering
                    row["state"] = "open"
                for k in ("service", "product", "version", "tunnel"):
                    row[k] = row[k] or p[k]
                row["source"].add("nmap")
        else:
            for f in parse_oida(text):
                if f["address"] not in targets:
                    continue
                findings.append(f)
                key = next((k for k in rows if k[:2] == (f["address"], f["port"])), (f["address"], f["port"], ""))
                row = rows.setdefault(key, {"address": f["address"], "port": f["port"], "transport": "",
                                            "state": "open", "service": f["module"], "product": "",
                                            "version": "", "tunnel": "", "source": set()})
                row["source"].add(f"oida:{f['module']}")
    ports = [{**r, "target": targets[r["address"]], "source": ";".join(sorted(r["source"]))}
             for _, r in sorted(rows.items(), key=lambda kv: (targets[kv[0][0]], kv[0][1], kv[0][2]))]
    oida = sorted({tuple({**f, "target": targets[f["address"]]}[c] for c in OIDA_COLUMNS) for f in findings})
    return ports, [dict(zip(OIDA_COLUMNS, o)) for o in oida], complete


def _names_match(name, product):
    return bool(name) and re.search(rf"\b{re.escape(name.casefold())}\b", product.casefold()) is not None


def reachability(component, ports, complete, address, catalog):
    """(reachable, matching open ports) for one component on one target."""
    cat = catalog_lookup(catalog, component)
    name = cat["name"] if cat else component
    services = set(filter(None, cat["service"].split(";"))) if cat else set()
    open_ports = [p for p in ports if p["address"] == address and p["state"] == "open"]
    hits = [p for p in open_ports if _names_match(name, p["product"])
            or p["service"] in services or (p["tunnel"] == "ssl" and "ssl" in services)]
    if hits:
        return "yes", hits
    transports = {p.split("/")[1] for p in cat["ports"].split(";") if "/" in p} if cat else set()
    if services and transports and all((address, t) in complete for t in transports):
        return "no", []
    return "unknown", []


def run(args, argv):
    eng_dir = args.engagement
    eng = E.load(eng_dir, args.workspace)
    scans_dir = eng_dir / "evidence" / "scans"
    for f in args.files:
        try:
            text = f.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            raise OtpaError(f"{f}: {e}")
        if not kind(text):
            raise OtpaError(f"{f}: neither nmap XML (-oX) nor OIDA --json-log NDJSON")
        dest = scans_dir / f.name
        if dest.exists() and dest.read_bytes() != f.read_bytes():
            raise OtpaError(f"{dest} exists with other content; rename the file")
    decisions = decide.load(eng_dir)
    catalog = load_catalog()

    with manifest.record(eng_dir, argv) as entry:
        scans_dir.mkdir(parents=True, exist_ok=True)
        for f in args.files:
            shutil.copyfile(f, scans_dir / f.name)
        scans = sorted(scans_dir.iterdir())
        targets = {t["address"]: t["name"] for t in eng["targets"]}
        ports, oida, complete = build_ports(scans, targets)
        write_csv(eng_dir / "ports.csv", ports, PORT_COLUMNS)
        write_csv(eng_dir / "oida.csv", oida, OIDA_COLUMNS)

        rows, missing = [], []
        for t in eng["targets"]:
            device_cves = E.device_dir(args.workspace, t["device"]) / "cves.csv"
            if not device_cves.exists():
                missing.append(t["name"])
                continue
            cache = {}
            target_rows = []
            for r in read_csv(device_cves):
                if r["component"] not in cache:
                    cache[r["component"]] = reachability(r["component"], ports, complete, t["address"], catalog)
                reachable, hits = cache[r["component"]]
                r = r | {"reachable": reachable}
                seen = [p for p in hits if r["version"] and p["version"] == r["version"]
                        and _names_match(r["component"], p["product"])]
                if seen and r["label"] == "Version-candidate":
                    p = seen[0]
                    why = f"nmap: {p['product']} {p['version']} on {p['port']}/{p['transport']}"
                    r = r | {"label": "Observed", "note": "; ".join(filter(None, [r["note"], why]))}
                target_rows.append(r)
            rows += [{"target": t["name"], **r} for r in decide.apply(target_rows, decisions, t["name"])]
        write_csv(eng_dir / "cves.csv", rows, ["target"] + CVE_COLUMNS)
        entry["inputs"] = scans + ([eng_dir / "decisions.yaml"] if (eng_dir / "decisions.yaml").exists() else [])
        entry["outputs"] = [eng_dir / n for n in ("ports.csv", "oida.csv", "cves.csv")]

    reach = {}
    for r in {(r["target"], r["cve"]): r for r in rows}.values():
        reach[r["reachable"]] = reach.get(r["reachable"], 0) + 1
    print(f"{eng_dir}: {len(scans)} scans, {len(ports)} ports, {len(oida)} OIDA findings, "
          f"CVEs reachable yes/no/unknown: {reach.get('yes', 0)}/{reach.get('no', 0)}/{reach.get('unknown', 0)}")
    if missing:
        print(f"no cves.csv yet for: {', '.join(missing)} (run otpa cves <device>)")
