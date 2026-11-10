import pathlib

import pytest
import yaml

from conftest import DEVICE
from otpa import OtpaError
from otpa.cli import main
from otpa.modules import plan

HERE = pathlib.Path(__file__).parent
FIXTURE = HERE / "fixtures/catalog.yaml"


def make_eng(ws, monkeypatch, environment="testbed", mode="aggressive", position="control"):
    monkeypatch.setattr(plan, "CATALOG", FIXTURE)
    (ws / "devices" / DEVICE / "device.yaml").write_text(
        "vendor: x\nprotocols: [opcua, ssh]\nvendor_port_scope: plcnext\n")
    assert main(["--workspace", str(ws), "init", "axc-testbed", "--date", "2026-11-10", "--tester", "T",
                 "--environment", environment, "--mode", mode, "--attacker-position", position,
                 "--target", f"name=plc1,address=192.168.1.10,zone=cell-1,purdue=1,device={DEVICE}",
                 "--target", f"name=plc0,address=192.168.1.5,zone=cell-1,purdue=0,device={DEVICE}"]) == 0
    return ws / "engagements/2026-11-10-axc-testbed"


def test_real_catalog_is_valid():
    cat = plan.load_catalog(plan.CATALOG)
    assert {c["owasp_ot"] for c in cat["checks"]} == set(range(1, 11)), "every OWASP item has a check"


def test_catalog_validation(tmp_path):
    bad = yaml.safe_load(FIXTURE.read_text())
    bad["checks"][0]["kb_refs"] = ["nope.md"]
    (tmp_path / "c.yaml").write_text(yaml.safe_dump(bad))
    with pytest.raises(OtpaError, match="nope.md"):
        plan.load_catalog(tmp_path / "c.yaml")


def test_plan_golden(ws, monkeypatch):
    eng = make_eng(ws, monkeypatch)
    assert main(["--workspace", str(ws), "plan", str(eng)]) == 0
    assert (eng / "plan.yaml").read_text() == (HERE / "golden/plan.yaml").read_text()


def test_plan_live_safe(ws, monkeypatch):
    eng = make_eng(ws, monkeypatch, "live", "safe", "dmz")
    assert main(["--workspace", str(ws), "plan", str(eng)]) == 0
    p = yaml.safe_load((eng / "plan.yaml").read_text())["targets"][1]
    reasons = {e["id"]: e["reason"] for e in p["excluded"]}
    assert reasons == {"OT04-01": "not in mode safe",
                       "OT07-01": "needs a position inside the target's zone (control or field), not dmz"}
    nmap = next(c for c in p["checks"] if c["id"] == "OT01-02")["commands"][0]
    assert nmap.startswith("nmap -sT -sV -p ") and "-p 22," in nmap and "-p-" not in nmap


def test_forensics_has_no_active_checks(ws, monkeypatch):
    eng = make_eng(ws, monkeypatch, "live", "forensics", "control")
    main(["--workspace", str(ws), "plan", str(eng)])
    p = yaml.safe_load((eng / "plan.yaml").read_text())
    assert all(not c["id"] in ("OT01-02", "OT09-01") for t in p["targets"] for c in t["checks"])


def test_manual_check_results(ws, monkeypatch):
    eng = make_eng(ws, monkeypatch)
    main(["--workspace", str(ws), "plan", str(eng)])
    run = lambda *a: main(["--workspace", str(ws), "check", str(eng), *a])
    assert run("plc1", "OT05-01", "fail", "--note", "no matrix exists") == 0
    assert run("plc1", "OT05-01", "pass", "--note", "found it") == 0  # replaces
    assert run("plc0", "OT04-01", "pass", "--note", "x") == 2  # excluded for plc0
    assert run("plc1", "OT05-01", "maybe", "--note", "x") == 2
    assert run("plc1", "OT05-01", "pass") == 2  # note required
    assert yaml.safe_load((eng / "checks.yaml").read_text()) == [
        {"target": "plc1", "check": "OT05-01", "result": "pass", "note": "found it"}]
