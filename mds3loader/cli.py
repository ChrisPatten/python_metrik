"""Command line interface for mds3loader."""

from __future__ import annotations

import typer

from .config import load_settings
from .utils.logger import get_logger

SUCCESS = 0
CONFIG_ERROR = 2
RUNTIME_ERROR = 3

app = typer.Typer(add_completion=False)
logger = get_logger()


@app.callback()
def main(
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose output",
    )
) -> None:
    """Configure logging based on CLI options."""

    level = "DEBUG" if verbose else "INFO"
    global logger
    logger = get_logger(level)


@app.command()
def run(log_level: str = typer.Option(None, help="Override log level")) -> int:
    """Placeholder command that does nothing."""

    try:
        if log_level:
            settings = load_settings(log_level=log_level)
        else:
            settings = load_settings()
        logger.info("running", level=settings.log_level)
        return SUCCESS
    except ValueError as exc:
        typer.echo(str(exc), err=True)
        return CONFIG_ERROR
    except Exception as exc:  # pragma: no cover - unexpected
        logger.exception("runtime error", exc_info=exc)
        return RUNTIME_ERROR


if __name__ == "__main__":
    raise SystemExit(app())
