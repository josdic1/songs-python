import sqlite3
from lib import CONN, CURSOR

class Tag:
    def __init__(self, title):
        self.title = title
        self.id = None
    
    def __repr__(self):
        return f"Tag: {self.title} "
    

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance (value, str) and value.strip():
            self._title = value
        else:
            raise ValueError ("tag invalid")
    

    @classmethod
    def _from_db_row(cls, row):
        tag = cls(row[1])
        tag.id = row[0]
        return tag
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM tags WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            cls._from_db_row(row)
        else:
            return None
        
    @classmethod
    def find_by_title(cls, title):
        CURSOR.execute("SELECT * FROM tags WHERE title = ?", (title,))
        row = CURSOR.fetchone()
        if row:
            cls._from_db_row(row)
        else:
            return None
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM songs")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def add_new(cls, title):
        existing = cls.find_by_title(title)
        if existing:
            return existing
        tag = cls(title)
        tag.save()
        return tag
    
    def update(self):
        CURSOR.execute("UPDATE tags SET title = ? WHERE id = ?",(self._title, self.id,))
        CONN.commit()
    
    def delete(self):
        CURSOR.execute("DELETE FROM tags WHERE id = ?", (self.id,))

    def save(self):
        try:
            CURSOR.execute("INSERT INTO tags (title) VALUES (?)", (self._title,))
            self.id = CURSOR.lastrowid
            CONN.commit()
        except sqlite3.IntegrityError:
            print("Tag already exists. Use add_new() or choose a different tag.")
 
    
    


        
    
