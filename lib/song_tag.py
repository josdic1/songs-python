import sqlite3
from lib import CONN, CURSOR

class SongTag:
    def __init__(self, song_id, tag_id):
        self.song_id = song_id
        self.tag_id = tag_id
        self.id = None
    
    def __repr__(self):
        return f"Song Tag: {self.song_id} | {self.tag_id}"
    
    @property
    def song_id(self):
        return self._song_id
    
    @song_id.setter
    def song_id(self, value):
        if isinstance (value, int) and value > 0:
            self._song_id = value
        else:
            raise ValueError("song_id is invalid")

    @property
    def tag_id(self):
        return self._tag_id
    
    @tag_id.setter
    def tag_id(self, value):
        if isinstance (value, int) and value > 0:
            self._tag_id = value
        else:
            raise ValueError("tag_id is invalid")
        
    
    @classmethod
    def _from_db_row(cls, row):
        song_tag = cls(row[1], row[2])
        song_tag.id = row[0]
        return song_tag
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM song_tags WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls._from_db_row(row)
        else:
            return None
        
    @classmethod
    def find_by_song_and_tag_ids(cls, song_id, tag_id):
        CURSOR.execute("SELECT * FROM song_tags WHERE song_id = ? AND tag_id = ?", (song_id, tag_id,))
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM song_tags")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def add_new(cls, song_id, tag_id):
        exisitng = cls.find_by_song_and_tag_ids(song_id, tag_id)
        if exisitng:
            return exisitng
        song_tag = cls(song_id, tag_id)
        song_tag.save()
        return song_tag

    
    def save(self):
        try:
            CURSOR.execute("INSERT INTO song_tags (song_id, tag_id) VALUES (?,?)", (self._song_id, self._tag_id,))
            self.id = CURSOR.lastrowid
            CONN.commit()
        except sqlite3.IntegrityError:
            print("song_tag already exists. Use add_new() or choose a different song_tag.")



