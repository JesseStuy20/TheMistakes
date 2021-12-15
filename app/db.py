from flask import g
import sqlite3

DB_FILE="datum.db"

create_users = '''CREATE TABLE IF NOT EXISTS USERS(
                USERNAME TEXT UNIQUE,
                PASSWORD TEXT,
                POINTS INTEGER,
                WINS INTEGER,
                LOSSES INTEGER,
                PROFILE_PICTURE TEXT,
                PROFILE_BACKGROUND TEXT,
                CARD_COLOR TEXT,
                INVENTORY TEXT)'''

create_market = '''CREATE TABLE IF NOT EXISTS market (
                NAME TEXT,
                IMAGE_URL TEXT,
                PRICE INTEGER)''' # create market table

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB_FILE)
        g.db.row_factory = sqlite3.Row
    return g.db

def init_db(): 
    d = get_db()
    c = d.cursor()
    c.execute(create_users)
    c.execute(create_market)
    d.commit()