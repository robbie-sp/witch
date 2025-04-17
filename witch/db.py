"""Database utilities for the Witch project.

This module provides functions and configurations for setting up and managing
the database connection using SQLAlchemy and environment variables.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy.engine.base import Engine
from sqlmodel import create_engine

load_dotenv()  # take environment variables


def get_config() -> dict[str, any]:
    """Load configuration from environment variables."""
    return {
        "db_location": os.getenv("DB_LOCATION"),
        "db_file_name": os.getenv("DB_FILE_NAME"),
        "db_echo": os.getenv("DB_ECHO", "False").lower() in ("true", "1", "yes"),
    }


def db_url(db_file_name: str, db_location: Path) -> str:
    """Generate a SQLite URL for the database."""
    return f"sqlite:///{db_location}/{db_file_name}"


def get_engine(config: dict[str, any]) -> Engine:
    """Create and return a SQLAlchemy engine.

    Parameters
    ----------
    config : dict
        A dictionary containing database configuration, including
        'db_file_name', 'db_location', and 'db_echo'.

    Returns
    -------
    Engine
        A SQLAlchemy Engine instance for the database connection.

    """
    return create_engine(
        db_url(db_file_name=config["db_file_name"], db_location=config["db_location"]),
        echo=config["db_echo"],
    )
