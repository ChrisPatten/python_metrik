from pathlib import Path

from mds3loader.loader.copy_builder import build_copy_statement


def test_copy_sql_parameters(tmp_path: Path):
    meta = tmp_path / "file.csv.metadata"
    meta.write_text("{}")
    sql = build_copy_statement(meta, "@STAGE", "DB.TBL")
    expected = (
        "COPY INTO DB.TBL\n"
        "FROM @STAGE/file.csv\n"
        "FILE_FORMAT = (type = 'CSV' field_optionally_enclosed_by='\"')\n"
        "ON_ERROR = 'continue';\n"
    )
    assert sql == expected
    assert (tmp_path / "file.csv.copy.sql").read_text() == expected
