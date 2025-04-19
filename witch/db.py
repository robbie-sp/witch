"""Database utilities for the Witch project.

This module provides functions and configurations for setting up and managing
the database connection using SQLAlchemy and environment variables.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import URL
from sqlalchemy.engine.base import Engine
from sqlmodel import create_engine

load_dotenv()  # take environment variables


def get_config() -> dict[str, any]:
    """Load configuration from environment variables."""
    return {
        "db_echo": os.getenv("DB_ECHO", "False").lower() in ("true", "1", "yes"),
        "sqlite_path": os.getenv("SQLITE_PATH", "witch.db"),
        "db_driver": os.getenv("DB_DRIVER", "sqlite"),
        "db_password": os.getenv("DB_PASSWORD", "password"),
        "db_username": os.getenv("DB_USERNAME", "postgres"),
        "db_database": os.getenv("DB_DATABASE", None),
        "db_host": os.getenv("DB_HOST", "localhost"),
    }


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
    if config["db_driver"] == "sqlite":
        return create_engine(
            f"sqlite:///{config["sqlite_path"]}",
            echo=config["db_echo"],
        )
    if config["db_driver"] == "postgresql":
        return create_engine(
            create_url_object(config),
            echo=config["db_echo"],
        )

    msg = f"Unsupported driver: {config['db_driver']}. Supported drivers are: sqlite, postgresql."
    raise UnsupportedDriverError(msg)


class UnsupportedDriverError(Exception):
    """Exception raised for unsupported database drivers."""

    def __init__(self, message: str) -> None:
        """Initialize the UnsupportedDriverError with a message.

        Parameters
        ----------
        message : str
            The error message describing the unsupported driver.

        """
        super().__init__(message)


def create_url_object(config: dict[str, str]) -> URL:
    """Create a URL object for PostgreSQL connection."""
    return URL.create(
        config["db_driver"],
        username=config["db_username"],
        password=config["db_password"],
        host=config["db_host"],
        database=config["db_database"],
    )
