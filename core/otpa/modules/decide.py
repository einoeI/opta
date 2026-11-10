"""otpa decide: record a tester decision for one CVE on one target in decisions.yaml.
Decisions are validated on every load (evidence must still exist with the same SHA-256)
and re-applied with apply() wherever CVE rows are shown for an engagement."""
import hashlib
import pathlib

import yaml

from otpa import OtpaError, manifest
from otpa import engagement as E
from otpa.modules.components import read_csv

LABELS = ("Reproduced", "Not-affected", "False-positive")
KEYS = ("target", "cve", "label", "reason", "evidence", "sha256")


def register(sub):
    p = sub.add_parser("decide", help="record a tester decision for a CVE on a target")
    p.add_argument("engagement", type=pathlib.Path, help="engagement folder")
    p.add_argument("target")
    p.add_argument("cve")
    p.add_argument("label", help=" | ".join(LABELS))
    p.add_argument("--reason", help="required for Not-affected and False-positive")
    p.add_argument("--evidence", type=pathlib.Path,
                   help="file inside the engagement folder; required for Reproduced")
    p.set_defaults(run=run)


def _sha256(path):
    with open(path, "rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def validate(decisions, eng_dir):
    if not isinstance(decisions, list):
        raise OtpaError("decisions.yaml must be a list")
    for d in decisions:
        what = f"decision {d.get('target')} {d.get('cve')}"
        if not isinstance(d, dict) or set(d) - set(KEYS) or not all(d.get(k) for k in KEYS[:3]):
            raise OtpaError(f"{what}: needs target, cve, label; allowed keys {', '.join(KEYS)}")
        if d["label"] not in LABELS:
            raise OtpaError(f"{what}: label must be one of {', '.join(LABELS)} (other labels are set by the tool)")
        if d["label"] != "Reproduced" and not d.get("reason"):
            raise OtpaError(f"{what}: {d['label']} needs a reason")
        if d["label"] == "Reproduced" and not d.get("evidence"):
            raise OtpaError(f"{what}: Reproduced needs an evidence file")
        if d.get("evidence"):
            path = eng_dir / d["evidence"]
            if not path.is_file():
                raise OtpaError(f"{what}: evidence {d['evidence']} not found")
            if d.get("sha256") and _sha256(path) != d["sha256"]:
                raise OtpaError(f"{what}: evidence {d['evidence']} changed since the decision")


def load(eng_dir):
    path = eng_dir / "decisions.yaml"
    decisions = yaml.safe_load(path.read_text(encoding="utf-8")) or [] if path.exists() else []
    validate(decisions, eng_dir)
    return decisions


def apply(rows, decisions, target):
    """Rows (dicts with cve, label, note) with this target's decisions applied."""
    by_cve = {d["cve"]: d for d in decisions if d["target"] == target}
    out = []
    for r in rows:
        d = by_cve.get(r["cve"])
        if d:
            why = f"tester: {d['reason']}" if d.get("reason") else f"tester: evidence {d['evidence']}"
            r = r | {"label": d["label"], "note": "; ".join(filter(None, [r["note"], why]))}
        out.append(r)
    return out


def run(args, argv):
    eng_dir = args.engagement
    eng = E.load(eng_dir, args.workspace)
    target = next((t for t in eng["targets"] if t["name"] == args.target), None)
    if not target:
        raise OtpaError(f"no target {args.target} in {eng_dir / 'engagement.yaml'}")
    cves_csv = E.device_dir(args.workspace, target["device"]) / "cves.csv"
    if not cves_csv.exists():
        raise OtpaError(f"{cves_csv} missing: run otpa cves {target['device']} first")
    cve = args.cve.upper()
    if cve not in {r["cve"] for r in read_csv(cves_csv)}:
        raise OtpaError(f"{cve} is not in {cves_csv}")

    d = {"target": args.target, "cve": cve, "label": args.label}
    if args.reason:
        d["reason"] = args.reason
    if args.evidence:
        ev = args.evidence.resolve() if args.evidence.is_absolute() else (eng_dir / args.evidence).resolve()
        if not ev.is_relative_to(eng_dir.resolve()):
            raise OtpaError("evidence must be inside the engagement folder (put it in evidence/)")
        d["evidence"] = ev.relative_to(eng_dir.resolve()).as_posix()
        if ev.is_file():
            d["sha256"] = _sha256(ev)
    validate([d], eng_dir)

    decisions = [x for x in load(eng_dir) if (x["target"], x["cve"]) != (d["target"], cve)] + [d]
    decisions.sort(key=lambda x: (x["target"], x["cve"]))
    out = eng_dir / "decisions.yaml"
    with manifest.record(eng_dir, argv) as entry:
        out.write_text(yaml.safe_dump(decisions, sort_keys=False, allow_unicode=True), encoding="utf-8")
        entry["inputs"] = [eng_dir / d["evidence"]] if args.evidence else []
        entry["outputs"] = [out]
    print(f"{out}: {cve} on {args.target} -> {args.label}")
