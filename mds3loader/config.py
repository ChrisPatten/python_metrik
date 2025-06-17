"""Configuration handling for mds3loader."""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration loaded from environment and CLI."""

    log_level: str = Field("INFO")

    model_config = {
        "env_prefix": "MDS3_",
    }


def load_settings(**kwargs: str) -> Settings:
    """Return Settings populated from environment variables and overrides."""

    return Settings(**kwargs)
