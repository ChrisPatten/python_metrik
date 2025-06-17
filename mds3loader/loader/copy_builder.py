"""Snowflake COPY INTO statement builder."""

from __future__ import annotations

from pathlib import Path


def build_copy_statement(metadata_path: Path, stage: str, table: str) -> str:
    """Return COPY INTO SQL statement and write it beside the metadata file."""

    file_name = metadata_path.stem
    statement = (
        f"COPY INTO {table}\n"
        f"FROM {stage}/{file_name}\n"
        "FILE_FORMAT = (type = 'CSV' field_optionally_enclosed_by='\"')\n"
        "ON_ERROR = 'continue';\n"
    )
    output_path = metadata_path.parent / f"{file_name}.copy.sql"
    output_path.write_text(statement, encoding="utf-8")
    return statement
