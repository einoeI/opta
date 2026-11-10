import json

import pytest

from conftest import DEVICE
from otpa.cli import main
from otpa import OtpaError
from otpa.modules.components import parse_sbom

CDX = {"bomFormat": "CycloneDX", "components": [
    {"name": "openssl", "version": "1.1.1n", "cpe": "cpe:2.3:a:openssl:openssl:1.1.1n:*:*:*:*:*:*:*"},
    {"name": "jinja2", "version": "2.4.1", "purl": "pkg:pypi/jinja2@2.4.1"}]}
SPDX = {"spdxVersion": "SPDX-2.3", "packages": [{"name": "zlib", "versionInfo": "1.2.11", "externalRefs": [
    {"referenceType": "cpe23Type", "referenceLocator": "cpe:2.3:a:zlib:zlib:1.2.11:*:*:*:*:*:*:*"}]}]}


def test_parse_sbom():
    assert parse_sbom(CDX)[0] == {"name": "openssl", "version": "1.1.1n", "cpe": "openssl:openssl", "purl": ""}
    assert parse_sbom(CDX)[1]["purl"] == "pkg:pypi/jinja2@2.4.1"
    assert parse_sbom(SPDX) == [{"name": "zlib", "version": "1.2.11", "cpe": "zlib:zlib", "purl": ""}]
    with pytest.raises(OtpaError):
        parse_sbom({"foo": 1})


def test_components_csv(ws, tmp_path):
    sbom = tmp_path / "bom.json"
    sbom.write_text(json.dumps(CDX))
    base = ["--workspace", str(ws), "components", DEVICE]
    assert main(base + ["--sbom", str(sbom), "--pick", "OpenSSH@8.9p1", "--free", "codesys runtime@3.5"]) == 0
    assert main(base + ["--pick", "openssh@9.0p1"]) == 0
    dev = ws / "devices" / DEVICE
    assert (dev / "sbom/bom.json").read_text() == sbom.read_text()
    assert (dev / "components.csv").read_text() == (
        "name,version,cpe,purl,service,ports,origin,mapped\n"
        "codesys runtime,3.5,,,,,free,no\n"
        "jinja2,2.4.1,,pkg:pypi/jinja2@2.4.1,,,sbom,yes\n"
        "openssh,8.9p1,openbsd:openssh,,ssh,22/tcp,picker,yes\n"
        "openssh,9.0p1,openbsd:openssh,,ssh,22/tcp,picker,yes\n"
        "openssl,1.1.1n,openssl:openssl,,https;ssl,443/tcp,sbom,yes\n")


def test_pick_unknown(ws):
    assert main(["--workspace", str(ws), "components", DEVICE, "--pick", "nosuch@1"]) == 2
