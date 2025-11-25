import sqlite3
from contextlib import contextmanager
from lead_gen_pro.config import DB_PATH
from pathlib import Path

DB_PATH.parent.mkdir(exist_ok=True, parents=True)


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS leads (
            id TEXT PRIMARY KEY,
            name TEXT,
            source TEXT,
            url TEXT,
            location TEXT,
            score REAL,
            created_at TEXT,
            details TEXT
        )"""
        )


@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()
