"""otpa command line. Commands are the files in otpa/modules/."""
import argparse
import importlib
import pathlib
import pkgutil
import sys

from otpa import OtpaError, __version__, modules

WORKSPACE = pathlib.Path(__file__).resolve().parents[2] / "workspace"


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(prog="otpa", description="OT Pentesting Assistant")
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("--workspace", type=pathlib.Path, default=WORKSPACE,
                        help="default: %(default)s")
    sub = parser.add_subparsers(required=True, metavar="command")
    for name in sorted(m.name for m in pkgutil.iter_modules(modules.__path__)):
        importlib.import_module(f"otpa.modules.{name}").register(sub)
    args = parser.parse_args(argv)
    try:
        return args.run(args, ["otpa", *argv]) or 0
    except OtpaError as e:
        print(f"otpa: {e}", file=sys.stderr)
        return 2
    except (KeyboardInterrupt, EOFError):
        # init asks everything before writing, so it leaves nothing behind. update keeps
        # the snapshots it already saved (they are complete responses) and logs the abort.
        print("\notpa: aborted", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
