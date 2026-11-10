import pathlib
import shutil

import yaml

from conftest import DEVICE
from otpa.cli import main
from test_init import FLAGS

HERE = pathlib.Path(__file__).parent
SCANS = HERE / "fixtures/scans"
DEVICE_CVES = """\
cve,component,version,source,cvss_version,score,vector,cvss_source,reachable,label,vendor_fixed_in,note
CVE-2023-1,openssh,8.9p1,osv,,,,,unknown,Version-candidate,,
CVE-2023-2,nginx,,change-notes,,,,,unknown,Version-candidate,,
CVE-2023-3,net-snmp,,change-notes,,,,,unknown,Version-candidate,,
CVE-2023-4,rsync,,change-notes,,,,,unknown,Version-candidate,,
CVE-2023-5,strongswan,,change-notes,,,,,unknown,Version-candidate,,
CVE-2023-6,glibc,,change-notes,,,,,unknown,Version-candidate,,
CVE-2023-7,openssh,8.9p1,osv,,,,,unknown,Not-affected,,vendor
"""


def setup(ws):
    (ws / "devices" / DEVICE / "cves.csv").write_text(DEVICE_CVES)
    main(["--workspace", str(ws)] + FLAGS)
    eng = ws / "engagements/2026-11-10-axc-testbed"
    (eng / "decisions.yaml").write_text(yaml.safe_dump(
        [{"target": "plc1", "cve": "CVE-2023-2", "label": "False-positive", "reason": "WBM disabled"}]))
    return eng


def ingest(ws, eng, *files):
    return main(["--workspace", str(ws), "ingest", str(eng), *map(str, files)])


def test_ingest_golden(ws):
    eng = setup(ws)
    assert ingest(ws, eng, SCANS / "nmap-tcp-full.xml", SCANS / "oida-plc1.ndjson") == 0
    assert (eng / "evidence/scans/nmap-tcp-full.xml").read_bytes() == (SCANS / "nmap-tcp-full.xml").read_bytes()
    for name, golden in [("ports.csv", "ports.csv"), ("oida.csv", "oida.csv"), ("cves.csv", "engagement-cves.csv")]:
        assert (eng / name).read_text() == (HERE / "golden" / golden).read_text(), name
    before = (eng / "cves.csv").read_bytes()
    assert ingest(ws, eng) == 0  # rebuild from stored scans only
    assert (eng / "cves.csv").read_bytes() == before


def test_without_full_scan_reachability_unknown(ws, tmp_path):
    eng = setup(ws)
    partial = tmp_path / "nmap-top.xml"
    partial.write_text((SCANS / "nmap-tcp-full.xml").read_text().replace(
        'numservices="65535" services="1-65535"', 'numservices="1000" services="1-1024"'))
    assert ingest(ws, eng, partial) == 0
    rsync = [l for l in (eng / "cves.csv").read_text().splitlines() if "rsync" in l][0]
    assert ",unknown," in rsync


def test_ingest_refuses(ws, tmp_path):
    eng = setup(ws)
    junk = tmp_path / "junk.txt"
    junk.write_text("hello")
    assert ingest(ws, eng, junk) == 2
    other = tmp_path / "nmap-tcp-full.xml"
    other.write_text((SCANS / "nmap-tcp-full.xml").read_text().replace("8.9p1", "9.0p1"))
    assert ingest(ws, eng, SCANS / "nmap-tcp-full.xml") == 0
    assert ingest(ws, eng, other) == 2  # same name, other content


def test_file_order_does_not_matter(ws, tmp_path):
    eng = setup(ws)
    early = tmp_path / "0-oida.ndjson"  # sorts before the nmap file
    early.write_bytes((SCANS / "oida-plc1.ndjson").read_bytes())
    assert ingest(ws, eng, early, SCANS / "nmap-tcp-full.xml") == 0
    assert (eng / "ports.csv").read_text() == (HERE / "golden/ports.csv").read_text()


def test_scans_written_into_engagement_are_picked_up(ws):
    eng = setup(ws)
    (eng / "evidence/scans").mkdir(parents=True)
    shutil.copy(SCANS / "nmap-tcp-full.xml", eng / "evidence/scans/nmap-plc1-full.xml")
    assert ingest(ws, eng) == 0  # no file arguments: reads what the printed commands wrote
    assert ingest(ws, eng, eng / "evidence/scans/nmap-plc1-full.xml") == 0  # same file: no copy error
    assert "OpenSSH" in (eng / "ports.csv").read_text()
