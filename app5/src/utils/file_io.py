from __future__ import annotations

from pathlib import Path


def ensure_dir(path: Path | str) -> None:
    """Create a directory if it does not already exist."""
    Path(path).mkdir(parents=True, exist_ok=True)
