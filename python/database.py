import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = "data.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                temperatura REAL NOT NULL,
                humidade REAL NOT NULL
            )
        """)
        conn.commit()

def insert_record(timestamp: datetime, temperatura: float, humidade: float):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """INSERT INTO registros (timestamp, temperatura, humidade) VALUES (?, ?, ?)""",
            (timestamp, temperatura, humidade)
        )
        conn.commit()

def load_dataframe():
    import pandas as pd
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(
            "SELECT timestamp, temperatura, humidade FROM registros ORDER BY id ASC",
            conn
        )
    return df