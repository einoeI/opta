import pytest

DEVICE = "phoenix-contact/axc-f-2152/2022.0.8"


@pytest.fixture
def ws(tmp_path):
    """Workspace with one device profile."""
    d = tmp_path / "devices" / DEVICE
    d.mkdir(parents=True)
    (d / "device.yaml").write_text("vendor: Phoenix Contact\n")
    return tmp_path


@pytest.fixture
def engagement():
    return {
        "name": "axc-testbed",
        "date": "2026-11-10",
        "tester": "Leonie Greber",
        "environment": "testbed",
        "mode": "aggressive",
        "attacker_position": "control",
        "targets": [{"name": "plc1", "address": "192.168.1.10", "zone": "cell-1",
                     "conduit": None, "purdue_level": 1, "device": DEVICE}],
    }
