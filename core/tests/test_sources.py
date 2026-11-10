import json
import pathlib

import pytest

from otpa import sources

SNAP = pathlib.Path(__file__).parent / "fixtures/device/snapshots/2026-11-10"
FW = "2022.0.8 LTS"


@pytest.mark.parametrize("expr, result", [
    ("<2022.0.8 LTS", False), ("2022.0.8 LTS", True), ("<2025.0.2", True),
    ("vers:intdot/>=2021.0|<2023", True), ("<=2022.0.8", True), (">2022.0.8", False),
    ("n/a", None),
])
def test_in_range(expr, result):
    assert sources.in_range(FW, expr) is result


def test_csaf_status():
    adv = json.loads((SNAP / "csaf/VDE-2025-053.json").read_text())
    assert sources.csaf_status(adv, "AXC F 2152", "2404267", FW) == {
        "CVE-2024-12705": ("Version-candidate", "2025.0.2")}
    adv = json.loads((SNAP / "csaf/VDE-2022-046.json").read_text())
    assert sources.csaf_status(adv, "AXC F 2152", "2404267", FW)["CVE-2022-29824"][0] == "Not-affected"
    assert sources.csaf_status(adv, "RFC 9999", "0", FW) == {}


def test_cve_record_status():
    rows = json.loads((SNAP / "circl-search/phoenixcontact__axc_f_2152_firmware.json").read_text())["results"]
    recs = {cid: rec for rows in rows.values() for cid, rec in rows}
    assert sources.cve_record_status(recs["cve-2023-46144"], "AXC F 2152", "2404267", FW) == (True, "")
    assert sources.cve_record_status(recs["cve-2021-34570"], "AXC F 2152", "2404267", FW) == (False, "2021.0.5 LTS")
    assert sources.cve_record_status(recs["cve-2019-10997"], "AXC F 2152", "2404267", FW) == (None, "")


def test_nvd_cvss_all_versions():
    assert sources.nvd_cvss(json.loads((SNAP / "nvd/CVE-2021-3672.json").read_text())) == [
        ("2.0", 6.8, "AV:N/AC:M/Au:N/C:P/I:P/A:P"),
        ("3.1", 5.6, "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L")]


def test_osv_vulns():
    assert sources.osv_vulns(json.loads((SNAP / "osv/jinja2@2.4.1.json").read_text()))[1] == (
        "CVE-2019-10906", "GHSA-462w-v97r-4m45", "2.10.1")


def test_snapshot_saved_with_hash(tmp_path):
    p = sources.save_snapshot(tmp_path, "nvd", "CVE-1", "https://x", b"{}", "2026-11-10")
    assert p == tmp_path / "snapshots/2026-11-10/nvd/CVE-1.json"
    sources.save_snapshot(tmp_path, "nvd", "CVE-1", "https://x", b"[]", "2026-11-11")
    assert sources.latest_snapshots(tmp_path, "nvd") == {"CVE-1": tmp_path / "snapshots/2026-11-11/nvd/CVE-1.json"}
    index = (tmp_path / "snapshots/index.csv").read_text().splitlines()
    assert index[0] == "date,source,key,url,sha256" and len(index) == 3
    assert index[1].endswith("44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a")


def test_csaf_scores():
    adv = json.loads((SNAP / "csaf/VDE-2025-053.json").read_text())
    assert sources.csaf_scores(adv) == {"CVE-2024-12705": [
        ("3.1", 7.5, "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H")]}
