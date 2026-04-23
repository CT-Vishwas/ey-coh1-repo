from __future__ import annotations

import pandas as pd


def load_csv(source) -> pd.DataFrame:
    """Load CSV data from a file-like object or path."""
    return pd.read_csv(source)


def describe_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return a numeric summary of the provided DataFrame."""
    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        return pd.DataFrame(columns=["count", "mean", "std", "min", "25%", "50%", "75%", "max"])
    return numeric_df.describe().transpose()


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize whitespace and remove duplicate rows."""
    cleaned = df.copy()
    for column in cleaned.select_dtypes(include=["object"]).columns:
        cleaned[column] = cleaned[column].str.strip()
    return cleaned.drop_duplicates().reset_index(drop=True)


def filter_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Return a DataFrame with only the selected columns."""
    return df[columns].copy() if columns else df.copy()

# function to give list of unique values in a column, for dropdown options
def get_unique_values(df: pd.DataFrame, column: str) -> list[str]:
    """Return a sorted list of unique values from a specified column."""
    if column in df.columns:
        return sorted(df[column].dropna().unique().tolist())
    return []