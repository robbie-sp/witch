from waitch.models import Witch
from sqlmodel import SQLModel, create_engine, Session


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print(f"Database is stored at: {engine.url.database}")


def populate_db():
    witches = [
        Witch(name="Hermione Granger", type="good"),
        Witch(name="Bellatrix Lestrange", type="evil"),
        Witch(name="Samantha Stephens", type="good"),
    ]
    with Session(engine) as session:
        for witch in witches:
            session.add(witch)

        session.commit()


def print_details():
    """print details of where db is stored on the machine."""
