#!/usr/bin/env python3
"""Extract a PDF's text into a Markdown file next to it (<name>.extracted.md),
with <!-- page N --> markers so every passage can be cited by page.

Backends (chosen with --backend, default auto = best installed):
  docling  best result, least cleanup: headings, lists, tables, links, correct
           order on multi-column pages, OCR of text in images. Heavy (~2 GB with
           models, ~5-10 s per page on CPU). Install: pip install -r requirements-docling.txt
  pypdf    light, always available (requirements.txt): plain text per page, no
           headings or tables, page headers/footers and hyphenation left in.

The extract is a working copy for reading, grep and drafting entries; it is
not a knowledge-base entry and follows the same sharing rules as its PDF.

Usage:
    python3 extract_pdf.py sources/bsi-germany/*.pdf
    python3 extract_pdf.py --backend pypdf --force file.pdf
    python3 extract_pdf.py --selftest
"""
import argparse
import datetime
import pathlib
import re
import sys
import tempfile

MARK = "\n\n@@PAGEBREAK@@\n\n"
CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")  # e.g. NUL from PDF fonts; breaks grep


def clean(text):
    return CONTROL.sub("", text)


def output_path(pdf):
    return pdf.with_name(pdf.stem + ".extracted.md")


def number_pages(md, mark=MARK):
    """Replace page-break placeholders with numbered <!-- page N --> markers."""
    parts = md.split(mark.strip())
    return "".join("<!-- page %d -->\n\n%s\n\n" % (i, p.strip()) for i, p in enumerate(parts, 1))


def with_docling(pdf):
    from docling.document_converter import DocumentConverter  # optional dependency
    doc = DocumentConverter().convert(str(pdf)).document
    return number_pages(doc.export_to_markdown(page_break_placeholder=MARK.strip()))


def with_pypdf(pdf):
    from pypdf import PdfReader
    reader = PdfReader(str(pdf))
    return "".join("<!-- page %d -->\n\n%s\n\n" % (i, (pg.extract_text() or "").strip())
                   for i, pg in enumerate(reader.pages, 1))


def extract(pdf, backend="auto"):
    """Return (markdown, backend_used). auto prefers docling, falls back to pypdf."""
    if backend in ("auto", "docling"):
        try:
            return clean(with_docling(pdf)), "docling"
        except ImportError:
            if backend == "docling":
                raise SystemExit("docling not installed: pip install -r requirements-docling.txt")
    return clean(with_pypdf(pdf)), "pypdf"


def extract_to_file(pdf, backend="auto", force=False):
    pdf = pathlib.Path(pdf)
    out = output_path(pdf)
    if out.exists() and not force:
        return out, "exists"
    md, used = extract(pdf, backend)
    head = ("<!-- Extracted from %s by extract_pdf.py (%s) on %s. Working copy: check "
            "against the PDF before quoting. -->\n\n" % (pdf.name, used, datetime.date.today()))
    out.write_text(head + md, encoding="utf-8")
    return out, used


def selftest():
    assert number_pages("a" + MARK + "b" + MARK + "") == \
        "<!-- page 1 -->\n\na\n\n<!-- page 2 -->\n\nb\n\n<!-- page 3 -->\n\n\n\n"
    assert clean("a\x00b\tc\nd\x0c") == "ab\tc\nd"
    from pypdf import PdfWriter
    with tempfile.TemporaryDirectory() as tmp:
        pdf = pathlib.Path(tmp) / "t.pdf"
        w = PdfWriter()
        w.add_blank_page(100, 100)
        w.add_blank_page(100, 100)
        w.write(str(pdf))
        out, used = extract_to_file(pdf, backend="pypdf")
        text = out.read_text()
        assert out.name == "t.extracted.md" and used == "pypdf"
        assert "<!-- page 2 -->" in text and "<!-- page 3 -->" not in text, text
        assert extract_to_file(pdf, backend="pypdf") == (out, "exists")
    print("selftest ok")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("pdfs", nargs="*")
    p.add_argument("--backend", choices=("auto", "docling", "pypdf"), default="auto")
    p.add_argument("--force", action="store_true", help="overwrite existing .extracted.md")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args()
    if a.selftest:
        return selftest()
    for pdf in a.pdfs:
        out, how = extract_to_file(pdf, a.backend, a.force)
        print("%-8s %s" % (how, out))


if __name__ == "__main__":
    main()
