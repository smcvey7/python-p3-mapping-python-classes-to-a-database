"""Module allowing connection to server"""

from config import CONN, CURSOR

class Song:
    """Class representing a song"""

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        """Method to create new table"""

        sql = """
            CREATE TABLE IF NOT EXISTS songs(
            id INTEGER PRIMARY KEY,
            name TEXT,
            album TEXT
            )
        """
        CURSOR.execute(sql)

    def save(self):
        """Method to save new entry to db and update id once assigned"""

        sql = """
            INSERT INTO songs (name, album) VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs ").fetchone()[0]

    @classmethod
    def create(cls, name, album):
        """Method to create and save new record"""

        song = Song(name, album)
        song.save()
        return song
