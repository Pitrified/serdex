from serdex.db.mysqlalchemy import MySQLAlchemy
from serdex.metadata.explore import get_column_names, get_table_names


def sample_connection() -> MySQLAlchemy:
    """Do a sample connection."""
    host = "localhost"
    username = "api_access"
    database = "sakila"
    alchemist = MySQLAlchemy(host, username, database)
    return alchemist


def sample_read_tables() -> None:
    """Read a sample dataframe."""
    alchemist = sample_connection()
    tables = get_table_names(alchemist)
    print(tables)

    alchemist.close()


def sample_read_columns() -> None:
    """Read a sample dataframe."""
    alchemist = sample_connection()
    columns = get_column_names(alchemist, "film")
    print(columns)

    alchemist.close()


if __name__ == "__main__":
    # sample_connection()
    # sample_read_tables()
    sample_read_columns()
