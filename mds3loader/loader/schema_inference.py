"""CSV schema inference utilities."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class Column:
    """Simple column representation."""

    name: str
    type: str
    nullable: bool


def _guess_type(value: str) -> str:
    """Return primitive type name for ``value``."""

    if value.lower() in {"true", "false"}:
        return "BOOLEAN"
    try:
        int(value)
        return "NUMBER"
    except ValueError:
        pass
    try:
        float(value)
        return "FLOAT"
    except ValueError:
        pass
    try:
        datetime.fromisoformat(value)
        return "DATE"
    except ValueError:
        pass
    return "STRING"


def infer_schema(path: Path) -> List[Column]:
    """Infer column types from ``path``."""

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        columns: Dict[str, Optional[str]] = {
            name: None for name in reader.fieldnames or []
        }
        nullables = {name: False for name in reader.fieldnames or []}
        for row in reader:
            for name, value in row.items():
                if value == "" or value is None:
                    nullables[name] = True
                    continue
                guessed = _guess_type(value)
                current = columns[name]
                if current is None:
                    columns[name] = guessed
                elif current == "NUMBER" and guessed == "FLOAT":
                    columns[name] = "FLOAT"
                elif current != guessed:
                    if current in {"NUMBER", "FLOAT"} and guessed in {
                        "NUMBER",
                        "FLOAT",
                    }:
                        columns[name] = "FLOAT"
                    else:
                        columns[name] = "STRING"
        result = [
            Column(
                name=name,
                type=columns.get(name, "STRING") or "STRING",
                nullable=nullables[name],
            )
            for name in reader.fieldnames or []
        ]
    return result
