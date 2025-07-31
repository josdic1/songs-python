import sqlite3

CONN = sqlite3.connect('songs.db')
CURSOR = CONN.cursor()