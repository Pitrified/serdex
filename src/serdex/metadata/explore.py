import pandas as pd
from serdex.db.mysqlalchemy import MySQLAlchemy
from serdex.metadata.queries import show_tables


def get_table_names(msa: MySQLAlchemy) -> pd.DataFrame:
    """Get the table names."""
    table_names = msa.read_df(show_tables)
    # change the first column name to table_name
    cols = table_names.columns.tolist()
    cols[0] = "table_name"
    table_names.columns = cols
    return table_names
