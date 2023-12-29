"""Test MySQLAlchemy class."""

from serdex.db.mysqlalchemy import MySQLAlchemy


def sample_connection() -> MySQLAlchemy:
    """Do a sample connection."""
    host = "localhost"
    username = "api_access"
    database = "sakila"
    alchemist = MySQLAlchemy(host, username, database)
    return alchemist


def sample_read_df() -> None:
    """Read a sample dataframe."""
    alchemist = sample_connection()

    query = "SELECT * FROM film;"
    df = alchemist.read_df(query)
    print(df.head())

    alchemist.close()


if __name__ == "__main__":
    # sample_connection()
    sample_read_df()
