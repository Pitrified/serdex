import os

import pandas as pd
from sqlalchemy import create_engine

from serdex.db.utils import uncapitalize_column_names


class MySQLAlchemy:
    def __init__(self, host, username, database) -> None:
        """Setup a simple mysql connector."""
        self.host = host
        self.username = username
        self.database = database
        self.create_engine()

    def get_password(self) -> str:
        """Get the password."""
        return os.environ["MYSQL_PASSWORD"]

    def build_uri(self) -> str:
        """Build the connection uri."""
        engine_uri = (
            f"mysql+pymysql://"
            f"{self.username}"
            f":{self.get_password()}"
            f"@{self.host}"
            f"/{self.database}"
        )
        return engine_uri

    def create_engine(self) -> None:
        """Create the engine."""
        engine_uri = self.build_uri()
        self.engine = create_engine(engine_uri)

    def close(self) -> None:
        """Dispose of the engine."""
        self.engine.dispose()

    def read_df(self, query: str, uncapitalize: bool = True) -> pd.DataFrame:
        """Read a dataframe."""
        df = pd.read_sql(query, self.engine)
        if uncapitalize:
            uncapitalize_column_names(df)
        return df
