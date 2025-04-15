import waitch.create_db as create_db


def main():
    create_db.create_db_and_tables()
    create_db.populate_db()


if __name__ == "__main__":
    main()
