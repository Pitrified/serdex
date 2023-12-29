import pandas as pd
from serdex.db.mysqlalchemy import MySQLAlchemy
from serdex.metadata.queries import show_tables, show_columns_tmpl


def get_table_names(msa: MySQLAlchemy) -> pd.DataFrame:
    """Get the table names."""
    table_names = msa.read_df(show_tables)
    # change the first column name to table_name
    cols = table_names.columns.tolist()
    cols[0] = "table_name"
    table_names.columns = cols
    return table_names


def get_column_names(msa: MySQLAlchemy, table_name: str) -> pd.DataFrame:
    """Get the column names."""
    table_name = msa.sanitize_input(table_name)
    show_columns = show_columns_tmpl.format(table_name=table_name)
    column_names = msa.read_df(show_columns)
    return column_names


def get_data_sample(
    msa: MySQLAlchemy,
    table_name: str,
    column_name: str | None = None,
    sample_size: int = 5,
) -> pd.DataFrame:
    """Get a sample of the data."""
    table_name_ = msa.sanitize_input(table_name)
    if column_name:
        column_name = msa.sanitize_input(column_name)
        query_col = f"{column_name}"
    else:
        query_col = "*"
    if not isinstance(sample_size, int):
        raise TypeError("sample_size must be an integer")
    query = f"SELECT {query_col} FROM {table_name_} LIMIT {sample_size};"
    data_sample = msa.read_df(query)
    return data_sample
