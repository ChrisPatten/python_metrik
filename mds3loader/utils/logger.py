"""Logging utilities for the mds3loader package."""

from __future__ import annotations

import logging

import structlog


class CloudWatchHandler(logging.Handler):
    """Stub for an AWS CloudWatch log handler."""

    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        """Send log record to CloudWatch."""  # TODO: implement
        pass


def configure_logging(level: str = "INFO") -> structlog.BoundLogger:
    """Configure structlog with JSON output and CloudWatch handler."""

    logging.basicConfig(
        level=level,
        handlers=[logging.StreamHandler(), CloudWatchHandler()],
        format="%(message)s",
    )

    wrapper = structlog.make_filtering_bound_logger(getattr(logging, level))
    structlog.configure(
        wrapper_class=wrapper,
        processors=[structlog.processors.JSONRenderer()],
    )
    return structlog.get_logger()


def get_logger(level: str = "INFO") -> structlog.BoundLogger:
    """Return a configured structlog logger."""

    return configure_logging(level)
