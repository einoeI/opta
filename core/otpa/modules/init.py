"""otpa init: create workspace/engagements/<date>-<name>/ with engagement.yaml.
Missing values are asked for, with fixed choices where the schema has them."""
import datetime

from otpa import engagement as E
from otpa import manifest

TARGET_FLAG_KEYS = {"name", "address", "zone", "conduit", "purdue", "device"}


def register(sub):
    p = sub.add_parser("init", help="create an engagement")
    p.add_argument("name", help="short slug, e.g. axc-testbed")
    p.add_argument("--date", default=datetime.date.today().isoformat(), help="default: today")
    p.add_argument("--tester")
    p.add_argument("--environment", choices=E.ENVIRONMENTS)
    p.add_argument("--mode", choices=E.MODES)
    p.add_argument("--attacker-position", choices=E.POSITIONS)
    p.add_argument("--target", action="append", default=[],
                   metavar="name=..,address=..,zone=..,[conduit=..,]purdue=..,device=..",
                   help="repeat per target; device is a path under workspace/devices")
    p.set_defaults(run=run)


def ask(question, choices=None):
    hint = f" [{'/'.join(choices)}]" if choices else ""
    while True:
        answer = input(f"{question}{hint}: ").strip()
        if choices is None or answer in choices:
            return answer


def parse_target(text):
    try:
        d = dict(kv.split("=", 1) for kv in text.split(","))
    except ValueError:
        raise E.OtpaError(f"--target {text}: use key=value pairs separated by ','")
    if set(d) - TARGET_FLAG_KEYS:
        raise E.OtpaError(f"--target: unknown keys {sorted(set(d) - TARGET_FLAG_KEYS)}")
    purdue = d.get("purdue")
    return {"name": d.get("name"), "address": d.get("address"), "zone": d.get("zone"),
            "conduit": d.get("conduit") or None,
            "purdue_level": int(purdue) if purdue and purdue.isdigit() else purdue,
            "device": d.get("device")}


def ask_targets(workspace):
    devices = sorted(str(p.parent.relative_to(workspace / "devices"))
                     for p in (workspace / "devices").glob("*/*/*/device.yaml"))
    if not devices:
        raise E.OtpaError(f"no device profiles under {workspace / 'devices'}")
    targets = []
    while name := ask("target name (empty to finish)"):
        targets.append({"name": name, "address": ask("address"), "zone": ask("zone"),
                        "conduit": ask("conduit (empty for none)") or None,
                        "purdue_level": int(ask("Purdue level", tuple("012345"))),
                        "device": ask("device", devices)})
    return targets


def run(args, argv):
    ws = args.workspace
    eng = {"name": args.name, "date": args.date,
           "tester": args.tester or ask("tester"),
           "environment": args.environment or ask("environment", E.ENVIRONMENTS),
           "mode": args.mode or ask("mode", E.MODES),
           "attacker_position": args.attacker_position or ask("attacker position", E.POSITIONS),
           "targets": [parse_target(t) for t in args.target] or ask_targets(ws)}
    E.validate(eng, ws)
    eng_dir = ws / "engagements" / f"{args.date}-{args.name}"
    if eng_dir.exists():
        raise E.OtpaError(f"{eng_dir} already exists")
    with manifest.record(eng_dir, argv) as entry:
        eng_dir.mkdir(parents=True)
        (eng_dir / "engagement.yaml").write_text(E.dump(eng), encoding="utf-8")
        entry["outputs"] = [eng_dir / "engagement.yaml"]
    print(eng_dir)
