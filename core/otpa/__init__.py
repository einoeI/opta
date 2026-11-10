"""otpa – OT Pentesting Assistant. See DESIGN.md."""
__version__ = "0.1.0"


class OtpaError(Exception):
    """A user-facing error: printed without traceback, exit code 2."""
