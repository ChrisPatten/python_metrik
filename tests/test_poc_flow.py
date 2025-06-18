from pathlib import Path
import json

from mds3loader.loader.schema_inference import infer_schema
from mds3loader.metadata.generator import generate_metadata
from mds3loader.loader.copy_builder import build_copy_statement


def test_full_poc_flow(tmp_path: Path):
    data_dir = Path("poc/data")
    out_dir = tmp_path
    csv_file = data_dir / "sample_people.csv"

    schema = infer_schema(csv_file)
    meta_file = generate_metadata(csv_file, schema, out_dir)
    sql = build_copy_statement(meta_file, "@LOCAL_POC_STAGE", "RAW.PEOPLE")

    assert meta_file.exists()
    metadata = json.loads(meta_file.read_text())
    assert len(metadata["schema_definition"]) == 5
    assert "@LOCAL_POC_STAGE" in sql
    assert "RAW.PEOPLE" in sql
