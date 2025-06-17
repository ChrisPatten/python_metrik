from pathlib import Path
import json

from mds3loader.loader.schema_inference import infer_schema
from mds3loader.metadata.generator import generate_metadata


def test_metadata_matches_schema(tmp_path: Path):
    csv_file = Path("poc/data/sample_people.csv")
    expected = json.loads(Path("poc/expected_schema.json").read_text())
    schema = infer_schema(csv_file)
    meta_file = generate_metadata(csv_file, schema, tmp_path)
    data = json.loads(meta_file.read_text())
    assert data["schema_definition"] == expected
