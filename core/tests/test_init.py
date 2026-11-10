import pathlib

import pytest
import yaml

from otpa.cli import main
from conftest import DEVICE

GOLDEN = pathlib.Path(__file__).parent / "golden" / "engagement.yaml"
FLAGS = ["init", "axc-testbed", "--date", "2026-11-10", "--tester", "Leonie Greber",
         "--environment", "testbed", "--mode", "aggressive", "--attacker-position", "control",
         "--target", f"name=plc1,address=192.168.1.10,zone=cell-1,purdue=1,device={DEVICE}"]


def test_init_golden(ws):
    assert main(["--workspace", str(ws)] + FLAGS) == 0
    eng = ws / "engagements" / "2026-11-10-axc-testbed"
    assert (eng / "engagement.yaml").read_bytes() == GOLDEN.read_bytes()
    [entry] = yaml.safe_load((eng / "manifest.yaml").read_text())
    assert entry["outputs"][0]["path"] == "engagement.yaml"


def test_init_refuses_aggressive_on_live(ws, capsys):
    flags = [f if f != "testbed" else "live" for f in FLAGS]
    assert main(["--workspace", str(ws)] + flags) == 2
    assert "aggressive" in capsys.readouterr().err
    assert not (ws / "engagements").exists()


def test_init_refuses_existing(ws):
    main(["--workspace", str(ws)] + FLAGS)
    assert main(["--workspace", str(ws)] + FLAGS) == 2


def test_init_asks_missing(ws, monkeypatch):
    answers = iter(["Leonie Greber", "lab", "testbed",  # "lab" is not a choice: asked again
                    "safe", "control",
                    "plc1", "192.168.1.10", "cell-1", "", "1", DEVICE, ""])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    assert main(["--workspace", str(ws), "init", "axc-testbed", "--date", "2026-11-10"]) == 0
    eng = yaml.safe_load((ws / "engagements/2026-11-10-axc-testbed/engagement.yaml").read_text())
    assert eng["mode"] == "safe"
    assert eng["targets"][0]["conduit"] is None


@pytest.mark.parametrize("exc", [EOFError, KeyboardInterrupt])
def test_init_abort_writes_nothing(ws, monkeypatch, capsys, exc):
    answers = iter(["Leonie Greber", "testbed", "safe", "control", "plc1"])

    def fake_input(_):
        try:
            return next(answers)
        except StopIteration:
            raise exc
    monkeypatch.setattr("builtins.input", fake_input)
    assert main(["--workspace", str(ws), "init", "axc-testbed"]) == 130
    assert "aborted" in capsys.readouterr().err
    assert not (ws / "engagements").exists()
