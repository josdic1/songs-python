
CREATE TABLE songs (
    id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    UNIQUE(title, name)
)

CREATE TABLE tags (
    id INTEGER PRIMARY KEY,
    title TEXT
)

CREATE TABLE song_tags (
    id INTEGER PRIMARY KEY,
    song_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY (song_id) REFERENCES songs (id),
    FOREIGN KEY (tag_id) REFERENCES tags (id),
)