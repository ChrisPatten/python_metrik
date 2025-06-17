"""Command line interface for mds3loader."""

from __future__ import annotations

import typer

from pathlib import Path
import json
from dataclasses import asdict

from .config import load_settings
from .utils.logger import get_logger
from .loader.schema_inference import infer_schema
from .metadata.generator import generate_metadata
from .loader.copy_builder import build_copy_statement

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


@app.command("infer-schema")
def infer_schema_cmd(csv_file: Path) -> None:
    """Print inferred schema as JSON."""

    schema = infer_schema(csv_file)
    typer.echo(json.dumps([asdict(c) for c in schema], indent=2))


@app.command("gen-metadata")
def gen_metadata_cmd(
    csv_file: Path, out_dir: Path = typer.Option(Path("."), "--out-dir")
) -> None:
    """Generate metadata JSON file."""

    schema = infer_schema(csv_file)
    metadata_path = generate_metadata(csv_file, schema, out_dir)
    typer.echo(str(metadata_path))


@app.command("build-copy")
def build_copy_cmd(
    metadata_file: Path,
    stage: str = typer.Option(..., "--stage"),
    table: str = typer.Option(..., "--table"),
) -> None:
    """Create Snowflake COPY INTO statement."""

    sql = build_copy_statement(metadata_file, stage, table)
    typer.echo(sql)


@app.command("poc-run")
def poc_run(data: Path, out: Path, table: str) -> int:
    """Run the full POC pipeline."""

    csv_file = data / "sample_people.csv"
    schema = infer_schema(csv_file)
    typer.echo("Schema Inference \u2713")
    metadata_file = generate_metadata(csv_file, schema, out)
    typer.echo("Metadata \u2713")
    build_copy_statement(metadata_file, "@LOCAL_POC_STAGE", table)
    typer.echo("COPY SQL \u2713")
    return SUCCESS


if __name__ == "__main__":
    raise SystemExit(app())
