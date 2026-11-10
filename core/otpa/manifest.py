"""manifest.yaml: one entry per command, appended. Has timestamps, so not part of golden tests."""
import contextlib
import datetime
import hashlib
import pathlib
import shlex
import subprocess

import yaml

from otpa import __version__

REPO = pathlib.Path(__file__).resolve().parents[2]


def _now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def git_commit():
    try:
        return subprocess.run(["git", "-C", str(REPO), "describe", "--always", "--dirty", "--abbrev=40"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def file_entry(path, eng_dir):
    path = pathlib.Path(path)
    with open(path, "rb") as f:
        digest = hashlib.file_digest(f, "sha256").hexdigest()
    shown = path.relative_to(eng_dir) if path.is_relative_to(eng_dir) else path
    return {"path": str(shown), "sha256": digest}


@contextlib.contextmanager
def record(eng_dir, argv):
    """Yield the entry dict. Callers may set inputs/outputs (paths, hashed on success),
    tools, snapshots, approvals, refusals. Written only if eng_dir exists at the end."""
    eng_dir = pathlib.Path(eng_dir)
    entry = {"command": shlex.join(argv), "otpa_version": __version__,
             "git_commit": git_commit(), "start": _now()}
    try:
        yield entry
        for key in ("inputs", "outputs"):
            if key in entry:
                entry[key] = [file_entry(p, eng_dir) for p in entry[key]]
    except BaseException as e:  # incl. Ctrl-C: the entry says the command did not finish
        entry["error"] = str(e) or type(e).__name__
        raise
    finally:
        entry["end"] = _now()
        if eng_dir.is_dir():
            with open(eng_dir / "manifest.yaml", "a", encoding="utf-8") as f:
                f.write(yaml.safe_dump([entry], sort_keys=False, allow_unicode=True))
