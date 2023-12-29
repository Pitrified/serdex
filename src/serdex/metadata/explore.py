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
