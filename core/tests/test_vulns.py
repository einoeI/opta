import json
import pathlib
import shutil

from otpa.cli import main
from otpa.modules import vulns

HERE = pathlib.Path(__file__).parent
DEVICE = "phoenix-contact/axc-f-2152/2022.0.8"


def setup_device(ws):
    dev = ws / "devices" / DEVICE
    shutil.copytree(HERE / "fixtures/device", dev)
    return dev


def test_cves_golden(tmp_path):
    dev = setup_device(tmp_path)
    assert main(["--workspace", str(tmp_path), "cves", DEVICE]) == 0
    assert (dev / "cves.csv").read_bytes() == (HERE / "golden/cves.csv").read_bytes()


def test_update_saves_snapshots(tmp_path, monkeypatch):
    dev = setup_device(tmp_path)
    shutil.rmtree(dev / "snapshots")
    feed = {"feed": {"entry": [{"id": "VDE-2025-053", "content": {"src": "https://example.test/a.json"}}]}}
    adv = (HERE / "fixtures/device/snapshots/2026-11-10/csaf/VDE-2025-053.json").read_bytes()
    calls = []

    def fake_get(url, data=None, headers=None):
        calls.append(url)
        if url.endswith("feed.json"):
            return json.dumps(feed).encode()
        if url.endswith("a.json"):
            return adv
        if "circl" in url:  # 150 results -> 2 pages of 100
            return json.dumps({"results": {}, "total_count": 150}).encode()
        return b"{}"
    monkeypatch.setattr(vulns.sources, "http_get", fake_get)
    monkeypatch.setattr(vulns.time, "sleep", lambda s: None)
    assert main(["--workspace", str(tmp_path), "update", DEVICE]) == 0
    assert not [c for c in calls if "nvd" in c], "NVD only with --cvss"
    assert main(["--workspace", str(tmp_path), "update", DEVICE, "--cvss"]) == 0
    snaps = {p.relative_to(dev / "snapshots").as_posix().split("/", 1)[1]
             for p in (dev / "snapshots").rglob("*.json")}
    assert snaps == {"circl-search/phoenixcontact__axc_f_2152_firmware__p1.json",
                     "circl-search/phoenixcontact__axc_f_2152_firmware__p2.json", "csaf-feed/feed.json",
                     "csaf/VDE-2025-053.json", "osv/jinja2@2.4.1.json",
                     # NVD for every CVE known after the other sources: CSAF + change-notes + override
                     "nvd/CVE-2019-10997.json",
                     "nvd/CVE-2024-12705.json", "nvd/CVE-2021-3672.json", "nvd/CVE-2022-29824.json"}
    calls.clear()
    assert main(["--workspace", str(tmp_path), "update", DEVICE, "--cvss"]) == 0
    assert not [c for c in calls if "nvd" in c], "NVD snapshots are not fetched twice"


def test_bad_override_refused(tmp_path):
    dev = setup_device(tmp_path)
    (dev / "overrides.csv").write_text("cve,label,fixed_in,reason,source_url\nCVE-2019-10997,Reproduced,,,\n")
    assert main(["--workspace", str(tmp_path), "cves", DEVICE]) == 2
