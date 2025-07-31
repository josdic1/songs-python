import sqlite3
from lib import CONN, CURSOR

class Song:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.id = None
    
    def __repr__(self):
        return f"Song: {self.title} | {self.genre}"
    

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance (value, str) and value.strip():
            self._title = value
        else:
            raise ValueError ("title invalid")
    

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, value):
        if isinstance (value, str) and value.strip():
            self._genre = value
        else:
            raise ValueError ("genre invalid")
    

    @classmethod
    def _from_db_row(cls, row):
        song = cls(row[1], row[2])
        song.id = row[0]
        return song
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM songs WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            cls._from_db_row(row)
        else:
            return None
        
    @classmethod
    def find_by_title(cls, title):
        CURSOR.execute("SELECT * FROM songs WHERE title = ?", (title,))
        row = CURSOR.fetchone()
        if row:
            return cls._from_db_row(row)
        else:
            return None
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM songs")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def add_new(cls, title, genre):
        existing = cls.find_by_title(title)
        if existing:
            return existing
        song = cls(title, genre)
        song.save()
        return song
    
    def add_tag(self, tag_id):
        from lib.song_tag import SongTag
        SongTag.add_new(self.id, tag_id)

    def get_tags(self):
        pass
        
    
    def update(self):
        CURSOR.execute("UPDATE songs SET title = ?, genre = ? WHERE id = ?",(self._title, self._genre, self.id,))
        CONN.commit()
    
    def delete(self):
        CURSOR.execute("DELETE FROM songs WHERE id = ?", (self.id,))

    def save(self):
        try:
            CURSOR.execute("INSERT INTO songs (title, genre) VALUES (?,?)", (self._title, self._genre))
            self.id = CURSOR.lastrowid
            CONN.commit()
        except sqlite3.IntegrityError:
            print("Title already exists. Use add_new() or choose a different title.")
 
    
    


        
    
