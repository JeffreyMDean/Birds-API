import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS birds;
        """
    )
    conn.execute(
        """
        CREATE TABLE birds (
          id INTEGER PRIMARY KEY NOT NULL,
          name TEXT,
          domain TEXT,
          kingdom TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    birds_seed_data = [
        (1, "Parrot", "Eukayota", "Animalia" ),
        (2, "Penguin", "Eukaryota", "Animalia"),
        (3, "Blue jay", "Eukaryota", "Animalia"),
    ]
    conn.executemany(
        """
        INSERT INTO birds (id, name, domain, kingdom)
        VALUES (?,?,?,?)
        """,
        birds_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()