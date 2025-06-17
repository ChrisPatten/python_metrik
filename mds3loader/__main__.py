"""Entry point for ``python -m mds3loader``."""

from .cli import app

if __name__ == "__main__":
    raise SystemExit(app())
