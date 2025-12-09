# etl/pipeline.py
from __future__ import annotations

from .ingest import ingest
from .materialize import materialize
from .transform import transform


def run_etl() -> None:
    """Minimal ETL pipeline placeholder."""
    data = ingest()
    transformed = transform(data)
    materialize(transformed)


if __name__ == "__main__":
    run_etl()
