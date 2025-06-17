from mds3loader.config import load_settings


def test_load_settings_env(monkeypatch):
    monkeypatch.setenv("MDS3_LOG_LEVEL", "DEBUG")
    settings = load_settings()
    assert settings.log_level == "DEBUG"


def test_load_settings_override():
    settings = load_settings(log_level="WARNING")
    assert settings.log_level == "WARNING"
