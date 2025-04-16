from sqlmodel import create_engine
from sqlalchemy.engine.base import Engine
from pathlib import Path

# SQLITE_FILE_NAME = "database.db"
# SQLITE_URL = f"sqlite:///{SQLITE_FILE_NAME}"


SQLITE_FILE_NAME = "witch_database.db"
DB_LOCATION = Path("c:\\users\\spaul\\projects\\witch")

string_url = "sqlite:///" + str(Path(__name__) / SQLITE_FILE_NAME)
# bytes_url = rf"{string_url}"


def db_url(db_file_name: str, db_location: Path) -> str:
    """Generates a SQLite URL for the database."""
    return f"sqlite:///{db_location}/{db_file_name}"


def get_engine() -> Engine:
    return create_engine(
        db_url(db_file_name=SQLITE_FILE_NAME, db_location=DB_LOCATION), echo=True
    )
