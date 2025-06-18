"""Metadata generation utilities."""

from __future__ import annotations

import json
from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
from typing import List

from mds3loader.loader.schema_inference import Column


def generate_metadata(csv_path: Path, schema: List[Column], out_dir: Path) -> Path:
    """Write metadata JSON beside the source file and return the path."""

    out_dir.mkdir(parents=True, exist_ok=True)
    metadata_file = out_dir / f"{csv_path.name}.metadata"
    metadata = {
        "file_info": {"name": csv_path.name, "path": str(csv_path)},
        "ingest_metadata": {"records": sum(1 for _ in csv_path.open()) - 1},
        "schema_definition": [asdict(col) for col in schema],
        "checksum": sha256(csv_path.read_bytes()).hexdigest(),
    }
    metadata_file.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    return metadata_file
