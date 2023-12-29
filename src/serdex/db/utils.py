"""Utils for db functions."""

import pandas as pd


def uncapitalize_column_names(df: pd.DataFrame) -> None:
    """Uncapitalize the column names inplace."""
    df.columns = df.columns.str.lower()
