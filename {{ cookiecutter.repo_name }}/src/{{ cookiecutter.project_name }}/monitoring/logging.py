from __future__ import annotations

import logging


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a basic logger.

    This will be extended with structured logging and config later.
    """
    return logging.getLogger(name)
