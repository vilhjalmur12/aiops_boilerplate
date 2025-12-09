from __future__ import annotations

from .pipeline import run_training


def main() -> None:
    """Entry point for training jobs.

    For now this just calls a no-op pipeline function.
    """
    run_training()


if __name__ == "__main__":
    main()
