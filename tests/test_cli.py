from typer.testing import CliRunner

from mds3loader.cli import SUCCESS, app


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.output


def test_run_command():
    runner = CliRunner()
    result = runner.invoke(app, ["run"])
    assert result.exit_code == 0
    assert SUCCESS == 0
