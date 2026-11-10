import hashlib

import pytest
import yaml

from otpa import __version__, manifest


def test_entry_appended_with_hashes(tmp_path):
    (tmp_path / "out.txt").write_text("x")
    for _ in range(2):
        with manifest.record(tmp_path, ["otpa", "x"]) as e:
            e["outputs"] = [tmp_path / "out.txt"]
    entries = yaml.safe_load((tmp_path / "manifest.yaml").read_text())
    assert len(entries) == 2
    e = entries[0]
    assert e["command"] == "otpa x"
    assert e["otpa_version"] == __version__
    assert e["git_commit"]
    assert e["start"] <= e["end"]
    assert e["outputs"] == [{"path": "out.txt", "sha256": hashlib.sha256(b"x").hexdigest()}]


def test_error_recorded(tmp_path):
    with pytest.raises(ValueError):
        with manifest.record(tmp_path, ["otpa", "x"]):
            raise ValueError("no")
    assert yaml.safe_load((tmp_path / "manifest.yaml").read_text())[0]["error"] == "no"


def test_abort_recorded(tmp_path):
    with pytest.raises(KeyboardInterrupt):
        with manifest.record(tmp_path, ["otpa", "x"]):
            raise KeyboardInterrupt
    assert yaml.safe_load((tmp_path / "manifest.yaml").read_text())[0]["error"] == "KeyboardInterrupt"
