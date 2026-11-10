import pytest
import yaml

from otpa import OtpaError
from otpa.engagement import load, validate


def test_valid(ws, engagement):
    validate(engagement, ws)


@pytest.mark.parametrize("change, msg", [
    ({"environment": "live"}, "aggressive"),
    ({"mode": "runtime"}, "runtime"),
    ({"mode": "fast"}, "mode"),
    ({"extra": 1}, "unknown"),
    ({"targets": []}, "target"),
    ({"date": "10.11.2026"}, "date"),
    ({"name": "My Test"}, "name"),
])
def test_invalid(ws, engagement, change, msg):
    with pytest.raises(OtpaError, match=msg):
        validate(engagement | change, ws)


@pytest.mark.parametrize("change, msg", [
    ({"purdue_level": 6}, "purdue_level"),
    ({"device": "acme/x/1"}, "device"),
    ({"zone": ""}, "zone"),
])
def test_invalid_target(ws, engagement, change, msg):
    engagement["targets"][0] |= change
    with pytest.raises(OtpaError, match=msg):
        validate(engagement, ws)


def test_duplicate_target(ws, engagement):
    engagement["targets"] *= 2
    with pytest.raises(OtpaError, match="duplicate"):
        validate(engagement, ws)


def test_load_validates(ws, engagement, tmp_path):
    engagement["environment"] = "live"
    (tmp_path / "engagement.yaml").write_text(yaml.safe_dump(engagement))
    with pytest.raises(OtpaError, match="aggressive"):
        load(tmp_path, ws)
