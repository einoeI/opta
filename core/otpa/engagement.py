"""engagement.yaml: schema, validation (on every load) and deterministic dump."""
import datetime
import re

import yaml

from otpa import OtpaError

ENVIRONMENTS = ("live", "testbed")
MODES = ("forensics", "safe", "aggressive", "runtime")
POSITIONS = ("internet", "enterprise", "dmz", "operations", "control", "field")
KEYS = ("name", "date", "tester", "environment", "mode", "attacker_position", "targets")
TARGET_KEYS = ("name", "address", "zone", "conduit", "purdue_level", "device")


def _check(ok, msg):
    if not ok:
        raise OtpaError(msg)


def _text(value):
    return isinstance(value, str) and value.strip() != ""


def _keys(d, allowed, what):
    _check(isinstance(d, dict), f"{what} must be a mapping")
    _check(not set(d) - set(allowed), f"{what}: unknown keys {sorted(set(d) - set(allowed))}")
    _check(not set(allowed) - set(d), f"{what}: missing keys {sorted(set(allowed) - set(d))}")


def validate(eng, workspace):
    """Raise OtpaError on the first problem. workspace holds devices/."""
    _keys(eng, KEYS, "engagement")
    _check(isinstance(eng["name"], str) and re.fullmatch(r"[a-z0-9][a-z0-9-]*", eng["name"]),
           "name: use lowercase letters, digits and '-'")
    date = str(eng["date"])
    try:
        ok = datetime.date.fromisoformat(date).isoformat() == date
    except ValueError:
        ok = False
    _check(ok, "date must be YYYY-MM-DD")
    _check(_text(eng["tester"]), "tester must not be empty")
    for key, choices in (("environment", ENVIRONMENTS), ("mode", MODES),
                         ("attacker_position", POSITIONS)):
        _check(eng[key] in choices, f"{key} must be one of {', '.join(choices)}")
    _check(eng["mode"] != "runtime", "mode runtime is not available in v1")
    _check(eng["mode"] != "aggressive" or eng["environment"] == "testbed",
           "mode aggressive needs environment testbed")

    targets = eng["targets"]
    _check(isinstance(targets, list) and targets, "at least one target is required")
    names = set()
    for t in targets:
        _keys(t, TARGET_KEYS, "target")
        what = f"target {t['name']}"
        for key in ("name", "address", "zone"):
            _check(_text(t[key]), f"{what}: {key} must not be empty")
        _check(t["name"] not in names, f"{what}: duplicate name")
        names.add(t["name"])
        _check(t["conduit"] is None or _text(t["conduit"]), f"{what}: conduit must be text or null")
        _check(type(t["purdue_level"]) is int and 0 <= t["purdue_level"] <= 5,
               f"{what}: purdue_level must be 0-5")
        _check(_text(t["device"]) and (workspace / "devices" / t["device"] / "device.yaml").is_file(),
               f"{what}: device {t['device']} has no device.yaml under {workspace / 'devices'}")


def device_dir(workspace, pointer):
    path = workspace / "devices" / pointer
    _check((path / "device.yaml").is_file(), f"device {pointer} has no device.yaml under {workspace / 'devices'}")
    return path


def load(eng_dir, workspace):
    eng = yaml.safe_load((eng_dir / "engagement.yaml").read_text(encoding="utf-8"))
    validate(eng, workspace)
    return eng


def dump(eng):
    """Fixed key order, so the same engagement always gives the same bytes."""
    eng = {k: eng[k] for k in KEYS} | {"targets": [{k: t[k] for k in TARGET_KEYS} for t in eng["targets"]]}
    return yaml.safe_dump(eng, sort_keys=False, allow_unicode=True)
