#!/usr/bin/env python3
"""Create a draft knowledge-base entry for a source, ready for a human to finish.

Copies the file into sources/<folder>/ (if it is not already under sources/),
then writes knowledge-base/<folder>/<slug>.md with every editable frontmatter
field and an empty body template. For PDFs it pre-fills title, page count,
PDF dates and the PDF's own outline (needs `pypdf`; without it the entry is
still created, just with less pre-filled). Afterwards run build_index.py.

Usage:
    python3 new_entry.py path/to/file.pdf --folder bsi-germany [--slug x] [--url URL] [--extract]
    python3 new_entry.py --folder tools --slug some-tool --url https://...   (web-only)
    python3 new_entry.py --selftest
"""
import argparse
import datetime
import pathlib
import re
import shutil
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent

TEMPLATE = """---
title: "{title}"
url: "{url}"
type: other
trust: secondary
accessed: {today}
published: unknown
owasp_ot: []
local_file: "{local_file}"
status: draft
reason:
version:
license:
superseded_by:
---

# {title}

<!-- Draft created by new_entry.py on {today}. To finish:
  - frontmatter: set type (standard | vendor-doc | tool | advisory | paper | blog | dataset | other),
    trust (primary = official/vendor/standard, secondary = blog/forum), published, owasp_ot,
    the canonical url; then delete the `status: draft` line (or set it to retrieved).
  - body: fill the four sections below; keep facts (with page numbers) apart from inference.
  - then run: python3 build_index.py
-->

## Summary
TODO: 3-6 lines: what the source is, who published it, why it matters.

## Key facts
- TODO: one self-contained, citable fact per bullet, with page or section (p.N).

## Verbatim
- TODO: exact quotes you may need to reproduce, with page.

## Relevance
TODO: which project step / OWASP OT Top 10 item it informs; conflicts with other entries.
{auto}"""


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:60] or "entry"


def pdf_info(path):
    """(title, auto-section text) from a PDF; degrades gracefully without pypdf."""
    try:
        from pypdf import PdfReader
    except ImportError:
        return None, "\n## Auto-extracted (delete when done)\n- pypdf not installed: no metadata read.\n"
    reader = PdfReader(str(path))
    meta = reader.metadata or {}

    def pdf_date(key):
        m = re.match(r"D:(\d{4})(\d{2})(\d{2})", str(meta.get(key) or ""))
        return "-".join(m.groups()) if m else "unknown"

    lines = ["", "## Auto-extracted (delete when done)",
             "- Pages: %d" % len(reader.pages),
             "- PDF created: %s; modified: %s (file dates, not necessarily the publication date)"
             % (pdf_date("/CreationDate"), pdf_date("/ModDate")),
             "- PDF title / author: %s / %s" % (meta.get("/Title") or "-", meta.get("/Author") or "-"),
             "", "PDF outline (bookmarks), for navigation:"]

    def walk(items, depth):
        for it in items:
            if len(lines) > 80:
                return
            if isinstance(it, list):
                if depth < 2:
                    walk(it, depth + 1)
                continue
            try:
                page = reader.get_destination_page_number(it) + 1
            except Exception:
                page = "?"
            lines.append("%s- %s (p.%s)" % ("  " * depth, it.title, page))

    try:
        walk(reader.outline, 0)
    except Exception:
        pass
    if lines[-1].endswith("navigation:"):
        lines.append("- (no outline in this PDF)")
    title = str(meta.get("/Title") or "").strip() or None
    return title, "\n".join(lines) + "\n"


def make_entry(root, folder, src=None, slug=None, url=""):
    if not re.fullmatch(r"[a-z0-9-]+", folder):
        raise ValueError("folder must be lowercase-kebab, e.g. bsi-germany")
    title, auto, local = None, "", ""
    if src:
        src = pathlib.Path(src).resolve()
        if not src.is_file():
            raise ValueError("no such file: %s" % src)
        sources = (root / "sources").resolve()
        dest = src if sources in src.parents else sources / folder / src.name
        if dest != src:
            if dest.exists():
                raise ValueError("already exists: %s" % dest.relative_to(root))
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
        local = dest.relative_to(root.resolve()).as_posix()
        if src.suffix.lower() == ".pdf":
            title, auto = pdf_info(dest)
    slug = slug or slugify(pathlib.Path(src).stem if src else "")
    entry = root / "knowledge-base" / folder / ("%s.md" % slug)
    if entry.exists():
        raise ValueError("entry already exists: %s" % entry.relative_to(root))
    entry.parent.mkdir(parents=True, exist_ok=True)
    title = (title or (pathlib.Path(src).stem if src else slug)).replace('"', "'")
    entry.write_text(TEMPLATE.format(title=title, url=url or "TODO", today=datetime.date.today(),
                                     local_file=local, auto=auto), encoding="utf-8")
    return entry


def selftest():
    sys.path.insert(0, str(ROOT))
    from build_index import frontmatter, validate
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        pdf = tmp / "My Report (v2).pdf"
        try:
            from pypdf import PdfWriter
            w = PdfWriter()
            w.add_blank_page(100, 100)
            w.add_metadata({"/Title": "Test Report", "/CreationDate": "D:20160128095115"})
            w.add_outline_item("Chapter 1", 0)
            w.write(str(pdf))
        except ImportError:
            pdf.write_bytes(b"%PDF-1.4\n")
        e = make_entry(tmp, "papers", pdf, url="https://example.org/r.pdf")
        text = e.read_text(encoding="utf-8")
        m = frontmatter(text)
        assert e.name == "my-report-v2.md" and (tmp / "sources/papers/My Report (v2).pdf").is_file()
        assert m["status"] == "draft" and m["local_file"] == "sources/papers/My Report (v2).pdf", m
        assert m["url"] == "https://example.org/r.pdf"
        assert [k for k in ("title", "type", "trust", "accessed", "published", "owasp_ot")
                if not m.get(k)] == []
        if "Chapter 1" in text:  # pypdf available
            assert m["title"] == "Test Report" and "2016-01-28" in text
        web = make_entry(tmp, "tools", slug="some-tool", url="https://example.org")
        assert frontmatter(web.read_text())["local_file"] == ""
        for bad in (lambda: make_entry(tmp, "tools", slug="some-tool"),
                    lambda: make_entry(tmp, "Bad Folder", slug="x")):
            try:
                bad()
            except ValueError:
                continue
            raise AssertionError("expected ValueError")
    m = frontmatter(TEMPLATE.format(title="t", url="u", today="2026-11-10", local_file="", auto=""))
    assert validate(m) == [], validate(m)
    print("selftest ok")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("file", nargs="?", help="source file to add (PDF, CSV, ...); omit for web-only")
    p.add_argument("--folder", help="topic folder, e.g. bsi-germany, tools, papers")
    p.add_argument("--slug", help="entry file name without .md (default: from file name)")
    p.add_argument("--url", default="", help="canonical URL of the source")
    p.add_argument("--extract", action="store_true",
                   help="also write <pdf>.extracted.md via extract_pdf.py (docling if installed)")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args()
    if a.selftest:
        return selftest()
    if not a.folder or not (a.file or a.slug):
        p.error("need --folder and either a file or --slug")
    try:
        entry = make_entry(ROOT, a.folder, a.file, a.slug, a.url)
    except ValueError as e:
        sys.exit("error: %s" % e)
    print("created %s - fill it in, then run: python3 build_index.py" % entry.relative_to(ROOT))
    if a.extract and a.file and a.file.lower().endswith(".pdf"):
        from build_index import frontmatter
        from extract_pdf import extract_to_file
        local = ROOT / frontmatter(entry.read_text(encoding="utf-8"))["local_file"]
        out, how = extract_to_file(local)
        print("extracted (%s) %s" % (how, out.relative_to(ROOT)))


if __name__ == "__main__":
    main()
