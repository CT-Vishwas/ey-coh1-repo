from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from src.data_processing import describe_data
from src.utils.file_io import ensure_dir


def build_report(df: pd.DataFrame) -> dict[str, object]:
    """Build a structured report payload from the DataFrame."""
    summary_df = describe_data(df)
    return {
        "record_count": len(df),
        "columns": df.columns.tolist(),
        "numeric_summary": summary_df.to_dict(orient="index"),
    }


def save_report(report: dict[str, object], output_dir: Path, *, file_name: str = "csv_report", format: str = "csv") -> Path:
    """Save a report to disk in CSV or JSON format."""
    ensure_dir(output_dir)
    output_file = output_dir / f"{file_name}.{format}"

    if format == "csv":
        summary = pd.DataFrame(report["numeric_summary"]).transpose()
        summary.insert(0, "column", summary.index)
        summary = summary.reset_index(drop=True)
        summary.to_csv(output_file, index=False)
    elif format == "json":
        output_file.write_text(json.dumps(report, indent=2), encoding="utf-8")
    else:
        raise ValueError("Unsupported report format. Use 'csv' or 'json'.")

    return output_file
