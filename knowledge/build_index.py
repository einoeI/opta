#!/usr/bin/env python3
"""Rebuild knowledge-base/INDEX.md and data/knowledge-base.csv from each
entry's YAML frontmatter (the frontmatter is the single source of truth).

Usage:
    python3 build_index.py            # validate entries, rewrite INDEX.md + CSV
    python3 build_index.py --check    # exit 1 if they are out of date (CI/pre-commit)
    python3 build_index.py --selftest
"""
import csv
import hashlib
import io
import pathlib
import re
import sys
import tempfile
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent
KB = ROOT / "knowledge-base"
INDEX = KB / "INDEX.md"
CSV_OUT = ROOT / "data" / "knowledge-base.csv"
REQUIRED = ("title", "url", "type", "trust", "accessed", "published", "owasp_ot")
OPTIONAL = ("local_file", "status", "reason", "version", "license", "superseded_by")
CSV_FIELDS = ("entry", "folder", "title", "url", "local_file", "extract", "sha256", "type", "trust",
              "accessed", "published", "owasp_ot", "status", "reason", "version",
              "license", "superseded_by")
TYPES = {"standard", "vendor-doc", "tool", "advisory", "paper", "blog", "dataset", "other"}
TRUST = {"primary", "secondary"}
STATUS = {"retrieved", "unretrieved", "metadata-only", "draft"}
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
PUBLISHED = re.compile(r"\d{4}(-\d{2}(-\d{2})?)?|unknown")
OWASP = re.compile(r"\[\s*(\d+\s*(,\s*\d+\s*)*)?\]")


def frontmatter(text):
    """Top-level `key: value` pairs of a frontmatter block (flat values only)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("no frontmatter")
    meta = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return meta
        key, sep, value = line.partition(":")
        if sep and key and not key[0].isspace():
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            meta[key.strip()] = value
    raise ValueError("unterminated frontmatter")


def validate(m):
    """Return a list of problems with one entry's metadata (empty = valid)."""
    errs = ["missing " + k for k in REQUIRED if not m.get(k)]
    if errs:
        return errs
    if m["type"] not in TYPES:
        errs.append("type %r not in %s" % (m["type"], sorted(TYPES)))
    if m["trust"] not in TRUST:
        errs.append("trust %r not in %s" % (m["trust"], sorted(TRUST)))
    if not DATE.fullmatch(m["accessed"]):
        errs.append("accessed must be YYYY-MM-DD")
    if not PUBLISHED.fullmatch(m["published"]):
        errs.append("published must be YYYY[-MM[-DD]] or unknown")
    if not OWASP.fullmatch(m["owasp_ot"]) or not all(
            1 <= int(n) <= 10 for n in re.findall(r"\d+", m["owasp_ot"])):
        errs.append("owasp_ot must be a list of 1-10, e.g. [1, 7]")
    if m.get("status") and m["status"] not in STATUS:
        errs.append("status %r not in %s" % (m["status"], sorted(STATUS)))
    if m.get("local_file") and not (ROOT / m["local_file"]).is_file():
        errs.append("local_file not found: " + m["local_file"])
    return errs


def owasp_items(m):
    return re.findall(r"\d+", m["owasp_ot"])


def extract_of(m, root=ROOT):
    """Repo-relative path of local_file's full-text extract (extract_pdf.py), or ""."""
    if not m.get("local_file"):
        return ""
    p = pathlib.PurePosixPath(m["local_file"])
    ext = p.with_name(p.stem + ".extracted.md")
    return ext.as_posix() if (root / ext).is_file() else ""


def files_cell(m, extract):
    """Markdown links (relative to knowledge-base/INDEX.md) to web, original and extract."""
    links = []
    if m["url"].startswith("http"):
        links.append("[web](%s)" % m["url"].replace(" ", "%20").replace(")", "%29"))
    if m.get("local_file"):
        links.append("[%s](../%s)" % (pathlib.PurePosixPath(m["local_file"]).suffix.lstrip(".") or "file",
                                     urllib.parse.quote(m["local_file"])))
    if extract:
        links.append("[text](../%s)" % urllib.parse.quote(extract))
    return " · ".join(links) or "-"


def csv_row(path, m):
    """Flat record for one entry; paths are relative to the repo root."""
    r = {k: m.get(k, "") for k in CSV_FIELDS}
    r["entry"] = path.relative_to(ROOT).as_posix()
    r["folder"] = path.parent.relative_to(KB).as_posix()
    r["owasp_ot"] = ";".join(owasp_items(m))
    r["status"] = m.get("status") or "retrieved"
    r["extract"] = extract_of(m)
    local = ROOT / r["local_file"] if r["local_file"] else None
    if local and local.is_file():
        r["sha256"] = hashlib.sha256(local.read_bytes()).hexdigest()
    return r


def cell(value):
    return value.replace("|", "\\|")


def row(name, m):
    status = m.get("status") or "retrieved"
    if m.get("reason"):
        status += ": " + m["reason"]
    if m.get("superseded_by"):
        status += "; superseded by " + m["superseded_by"]
    return "| [%s](%s) | %s | %s | %s | %s | %s | %s | %s |" % (
        cell(m["title"]), urllib.parse.quote(name), files_cell(m, extract_of(m)), m["type"],
        m["trust"], m["accessed"], m["published"], ",".join(owasp_items(m)) or "-", cell(status))


def render():
    """Validate all entries and return (index_text, csv_text, count)."""
    groups, bad, records = {}, [], []
    for path in sorted(KB.rglob("*.md")):
        if path.name == "INDEX.md":
            continue
        rel = path.relative_to(KB).as_posix()
        try:
            meta = frontmatter(path.read_text(encoding="utf-8"))
        except ValueError as e:
            bad.append("%s: %s" % (rel, e))
            continue
        errs = validate(meta)
        if errs:
            bad.append("%s: %s" % (rel, "; ".join(errs)))
            continue
        groups.setdefault(path.parent.relative_to(KB).as_posix(), []).append(row(rel, meta))
        records.append(csv_row(path, meta))
    if bad:
        sys.exit("Invalid entries:\n" + "\n".join(bad))
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=CSV_FIELDS, lineterminator="\n")
    w.writeheader()
    w.writerows(records)
    out = ["# Knowledge base index", "",
           "Generated by `build_index.py` - do not edit by hand. %d entries in %d folders."
           % (len(records), len(groups)), "",
           "**Source** opens the cited summary. **Files**: *web* = online original, "
           "*pdf/csv* = local copy in `sources/`, *text* = full-text extract with page markers "
           "(search it; quote from the original).", "",
           " · ".join("[%s](#%s) (%d)" % (g, g, len(r)) for g, r in groups.items())]
    for g, rows in groups.items():
        out += ["", "## %s" % g, "",
                "| Source (summary) | Files | Type | Trust | Accessed | Published | OWASP OT | Status |",
                "|---|---|---|---|---|---|---|---|"] + rows
    return "\n".join(out) + "\n", buf.getvalue(), len(records)


def build(check=False):
    index, table, n = render()
    targets = ((INDEX, index), (CSV_OUT, table))
    if check:
        stale = [p.relative_to(ROOT).as_posix() for p, text in targets
                 if not p.is_file() or p.read_text(encoding="utf-8") != text]
        if stale:
            sys.exit("Out of date: %s - run python3 build_index.py" % ", ".join(stale))
        print("ok: %d entries, index and CSV up to date" % n)
        return
    for p, text in targets:
        p.write_text(text, encoding="utf-8")
    print("wrote %d entries" % n)


def selftest():
    m = frontmatter('---\ntitle: "A: B"\nowasp_ot: [1, 2]\n  nested: x\n---\nbody: y\n')
    assert m == {"title": "A: B", "owasp_ot": "[1, 2]"}, m
    for broken in ("no block", "---\ntitle: x\n"):
        try:
            frontmatter(broken)
        except ValueError:
            continue
        raise AssertionError(broken)
    good = dict(title="a|b", url="u", type="tool", trust="primary", accessed="2026-11-10",
                published="unknown", owasp_ot="[]")
    assert validate(good) == [], validate(good)
    assert validate(dict(good, published="2013")) == []
    assert len(validate(dict(good, type="tol", trust="x", accessed="10.11.2026",
                             owasp_ot="[0, 11]", status="done"))) == 5
    assert validate(dict(good, url="")) == ["missing url"]
    r = row("a.md", dict(good, status="unretrieved", reason="403"))
    assert "a\\|b" in r and "| - |" in r and "unretrieved: 403" in r, r
    c = csv_row(KB / "x" / "a.md", dict(good, owasp_ot="[1, 7]", status=""))
    assert c["entry"] == "knowledge-base/x/a.md" and c["folder"] == "x", c
    assert c["owasp_ot"] == "1;7" and c["status"] == "retrieved" and c["sha256"] == "", c
    assert c["extract"] == ""
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        (root / "sources").mkdir()
        (root / "sources/A B.extracted.md").write_text("x")
        m = dict(good, url="https://x.org/a b", local_file="sources/A B.pdf")
        assert extract_of(m, root) == "sources/A B.extracted.md"
        assert extract_of(dict(m, local_file="sources/C.pdf"), root) == ""
    f = files_cell(dict(good, url="https://x.org/a b", local_file="sources/A B.pdf"),
                   "sources/A B.extracted.md")
    assert f == ("[web](https://x.org/a%20b) · [pdf](../sources/A%20B.pdf) · "
                 "[text](../sources/A%20B.extracted.md)"), f
    assert files_cell(dict(good, url="TODO"), "") == "-"
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        build(check="--check" in sys.argv)
