"""otpa plan: the OWASP OT catalog filtered by engagement, target and device -> plan.yaml,
plus the exact commands to run (printed, never run). otpa check: record pass/fail/n.a.

A check is excluded, first reason wins, when:
  the engagement mode is not in its modes; it is active and the target is Purdue L0;
  the target's Purdue level is above purdue_max; the device has none of its protocols;
  it needs a position inside the target's zone and the attacker position is not control/field."""
import csv
import pathlib
import re
import string

import yaml

from otpa import OtpaError, manifest
from otpa import engagement as E

ROOT = pathlib.Path(__file__).resolve().parents[3]
CATALOG = ROOT / "catalog" / "owasp-ot-top10.yaml"
KB = ROOT / "knowledge" / "knowledge-base"
PORTS = ROOT / "catalog" / "ot-ports.csv"
CHECK_MODES = ("forensics", "safe", "aggressive")
INSIDE = ("control", "field")
RESULTS = ("pass", "fail", "n.a.")


def register(sub):
    p = sub.add_parser("plan", help="build plan.yaml and print the commands for an engagement")
    p.add_argument("engagement", type=pathlib.Path)
    p.set_defaults(run=run)
    p = sub.add_parser("check", help="record the result of a planned check")
    p.add_argument("engagement", type=pathlib.Path)
    p.add_argument("target")
    p.add_argument("check", help="check id, e.g. OT05-01")
    p.add_argument("result", help=" | ".join(RESULTS))
    p.add_argument("--note", help="required: what you saw or why")
    p.set_defaults(run=run_check)


def load_catalog(path):
    cat = yaml.safe_load(path.read_text(encoding="utf-8"))
    if sorted(cat.get("items", {})) != list(range(1, 11)):
        raise OtpaError(f"{path}: items must be 1-10")
    seen = set()
    for c in cat.get("checks", []):
        cid = c.get("id", "?")
        bad = lambda msg: OtpaError(f"{path} {cid}: {msg}")
        if not re.fullmatch(r"OT(\d\d)-\d\d", cid) or int(cid[2:4]) != c.get("owasp_ot") or cid in seen:
            raise bad("id must be OTnn-nn, unique, nn = owasp_ot")
        seen.add(cid)
        for key in ("title", "modes", "purdue_max", "kb_refs", "attck_ics"):
            if key not in c:
                raise bad(f"missing {key}")
        if not set(c["modes"]) <= set(CHECK_MODES) or not c["modes"]:
            raise bad(f"modes must be from {CHECK_MODES}")
        if bool(c.get("module")) == bool(c.get("manual")) or (c.get("manual") and not c.get("question")):
            raise bad("needs either module or manual: true with a question")
        if not set(c.get("commands", {})) <= set(c["modes"]) | {"all"}:
            raise bad("commands keys must be its modes or 'all'")
        if not all(re.fullmatch(r"T\d{4}", t) for t in c["attck_ics"]):
            raise bad("attck_ics ids look like T0846")
        for ref in c["kb_refs"]:
            if not (KB / ref).is_file():
                raise bad(f"kb_ref {ref} not in knowledge/knowledge-base")
    return cat


def vendor_tcp_ports(scope):
    if not scope:
        return None
    ports = set()
    with open(PORTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["scope"] == scope and "tcp" in r["transport"]:
                ports.update(range(int(r["port"]), int(r["port_end"] or r["port"]) + 1))
    return ",".join(map(str, sorted(ports))) or None


class _Fill(dict):
    def __missing__(self, key):
        return f"<{key}>"  # placeholders the tester fills in, e.g. <interface>, <capture>


def render(cmd, values):
    return string.Formatter().vformat(cmd, (), _Fill({k: v for k, v in values.items() if v}))


def exclusion(c, eng, target, device):
    if eng["mode"] not in c["modes"]:
        return f"not in mode {eng['mode']}"
    if c.get("active") and target["purdue_level"] == 0:
        return "Purdue L0: no active checks"
    if target["purdue_level"] > c["purdue_max"]:
        return f"only for Purdue level <= {c['purdue_max']}"
    if c.get("protocols") and not set(c["protocols"]) & set(device.get("protocols") or []):
        return f"device has none of: {', '.join(c['protocols'])}"
    if c.get("zone_required") and eng["attacker_position"] not in INSIDE:
        return f"needs a position inside the target's zone (control or field), not {eng['attacker_position']}"
    return None


def build(eng, eng_dir, workspace, cat):
    targets = []
    for t in sorted(eng["targets"], key=lambda t: t["name"]):
        dev_dir = E.device_dir(workspace, t["device"])
        device = yaml.safe_load((dev_dir / "device.yaml").read_text(encoding="utf-8")) or {}
        values = {"address": t["address"], "target": t["name"], "device": t["device"],
                  "engagement": str(eng_dir), "vendor_tcp_ports": vendor_tcp_ports(device.get("vendor_port_scope"))}
        checks, excluded = [], []
        for c in sorted(cat["checks"], key=lambda c: (c["owasp_ot"], c["id"])):
            reason = exclusion(c, eng, t, device)
            if reason:
                excluded.append({"id": c["id"], "title": c["title"], "reason": reason})
                continue
            entry = {"id": c["id"], "owasp_ot": c["owasp_ot"], "owasp_title": cat["items"][c["owasp_ot"]],
                     "title": c["title"]}
            entry |= {"kind": "manual", "question": c["question"]} if c.get("manual") else \
                {"kind": "automated", "module": c["module"]}
            cmds = c.get("commands", {})
            entry["commands"] = [render(x, values) for x in cmds.get(eng["mode"], cmds.get("all", []))]
            entry |= {"attck_ics": list(c["attck_ics"]), "kb_refs": list(c["kb_refs"])}
            checks.append(entry)
        targets.append({"target": t["name"], "address": t["address"], "purdue_level": t["purdue_level"],
                        "device": t["device"], "checks": checks, "excluded": excluded})
    return {"engagement": eng_dir.name, "environment": eng["environment"], "mode": eng["mode"],
            "attacker_position": eng["attacker_position"], "catalog": cat.get("source", ""), "targets": targets}


def load_results(eng_dir):
    path = eng_dir / "checks.yaml"
    return (yaml.safe_load(path.read_text(encoding="utf-8")) or []) if path.exists() else []


def run(args, argv):
    eng_dir = args.engagement
    eng = E.load(eng_dir, args.workspace)
    cat = load_catalog(CATALOG)
    plan = build(eng, eng_dir, args.workspace, cat)
    out = eng_dir / "plan.yaml"
    commands = [cmd for t in plan["targets"] for c in t["checks"] for cmd in c["commands"]]
    with manifest.record(eng_dir, argv) as entry:
        (eng_dir / "evidence" / "scans").mkdir(parents=True, exist_ok=True)  # where the printed commands write
        out.write_text(yaml.safe_dump(plan, sort_keys=False, allow_unicode=True, width=200), encoding="utf-8")
        entry["inputs"] = [CATALOG, eng_dir / "engagement.yaml"]
        entry["outputs"] = [out]
        entry["printed_commands"] = commands
    results = {(r["target"], r["check"]): r["result"] for r in load_results(eng_dir)}
    print(f"{out}  (mode {eng['mode']}, environment {eng['environment']})")
    for t in plan["targets"]:
        print(f"\n== {t['target']} {t['address']} (Purdue L{t['purdue_level']}): "
              f"{len(t['checks'])} checks, {len(t['excluded'])} excluded")
        for c in t["checks"]:
            status = results.get((t["target"], c["id"]), "open")
            print(f"  [{status:>4}] {c['id']} {c['title']}")
            for cmd in c["commands"]:
                print(f"         $ {cmd}")
            if c["kind"] == "manual":
                print(f"         ? {c['question']}")
    print(f"\nCommands are printed, not run. They write to {eng_dir}/evidence/scans/; afterwards run: "
          f"otpa ingest {eng_dir}")


def run_check(args, argv):
    eng_dir = args.engagement
    E.load(eng_dir, args.workspace)
    plan_file = eng_dir / "plan.yaml"
    if not plan_file.exists():
        raise OtpaError(f"{plan_file} missing: run otpa plan first")
    plan = yaml.safe_load(plan_file.read_text(encoding="utf-8"))
    target = next((t for t in plan["targets"] if t["target"] == args.target), None)
    if not target or args.check not in {c["id"] for c in target["checks"]}:
        raise OtpaError(f"{args.check} is not a planned check for {args.target} (see plan.yaml)")
    if args.result not in RESULTS:
        raise OtpaError(f"result must be one of {', '.join(RESULTS)}")
    if not args.note:
        raise OtpaError("--note is required")
    results = [r for r in load_results(eng_dir) if (r["target"], r["check"]) != (args.target, args.check)]
    results.append({"target": args.target, "check": args.check, "result": args.result, "note": args.note})
    results.sort(key=lambda r: (r["target"], r["check"]))
    out = eng_dir / "checks.yaml"
    with manifest.record(eng_dir, argv) as entry:
        out.write_text(yaml.safe_dump(results, sort_keys=False, allow_unicode=True), encoding="utf-8")
        entry["outputs"] = [out]
    print(f"{out}: {args.target} {args.check} -> {args.result}")
