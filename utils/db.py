import sqlite3
from datetime import datetime


DB_PATH = "data/posts.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_post(content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO posts (content, created_at)
        VALUES (?, ?)
    """, (content, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()


def get_all_posts():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, content, created_at 
        FROM posts 
        ORDER BY id DESC 
        LIMIT 10
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows
    
def delete_post(post_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))

    conn.commit()
    conn.close()
