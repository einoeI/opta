import shutil

import pytest
import yaml

from conftest import DEVICE
from otpa.cli import main
from otpa import OtpaError
from otpa.modules import decide
from test_init import FLAGS
from test_vulns import HERE


@pytest.fixture
def eng(ws):
    shutil.copy(HERE / "golden/cves.csv", ws / "devices" / DEVICE / "cves.csv")
    main(["--workspace", str(ws)] + FLAGS)
    eng = ws / "engagements/2026-11-10-axc-testbed"
    (eng / "evidence").mkdir()
    (eng / "evidence/poc.txt").write_text("crash")
    return eng


def run(ws, eng, *args):
    return main(["--workspace", str(ws), "decide", str(eng), "plc1", *args])


def test_decide_and_apply(ws, eng):
    assert run(ws, eng, "CVE-2023-46144", "Reproduced", "--evidence", "evidence/poc.txt") == 0
    assert run(ws, eng, "CVE-2021-3672", "False-positive", "--reason", "c-ares not used") == 0
    assert run(ws, eng, "CVE-2021-3672", "Not-affected", "--reason", "backported") == 0  # replaces
    decisions = decide.load(eng)
    assert [(d["cve"], d["label"]) for d in decisions] == [
        ("CVE-2021-3672", "Not-affected"), ("CVE-2023-46144", "Reproduced")]
    assert len(decisions[1]["sha256"]) == 64
    rows = decide.apply([{"cve": "CVE-2021-3672", "label": "Version-candidate", "note": ""}], decisions, "plc1")
    assert rows == [{"cve": "CVE-2021-3672", "label": "Not-affected", "note": "tester: backported"}]


@pytest.mark.parametrize("args", [
    ["CVE-2023-46144", "Reproduced"],                         # no evidence
    ["CVE-2023-46144", "Reproduced", "--evidence", "nope"],   # missing file
    ["CVE-2023-46144", "False-positive"],                     # no reason
    ["CVE-2023-46144", "Observed", "--reason", "x"],          # tool label
    ["CVE-1999-0001", "Not-affected", "--reason", "x"],       # not in cves.csv
])
def test_decide_refuses(ws, eng, args):
    assert run(ws, eng, *args) == 2
    assert not (eng / "decisions.yaml").exists()


def test_changed_evidence_fails_load(ws, eng):
    run(ws, eng, "CVE-2023-46144", "Reproduced", "--evidence", "evidence/poc.txt")
    (eng / "evidence/poc.txt").write_text("edited")
    with pytest.raises(OtpaError, match="changed"):
        decide.load(eng)
