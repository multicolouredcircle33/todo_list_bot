import sqlite3
from pathlib import Path

DB_PATH = Path('data/tasks.db')

def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task_name TEXT NOT NULL,
            description TEXT NOT NULL,
            task_time TEXT NOT NULL,
            duration INTEGER NOT NULL,
            completed INTEGER DEFAULT 0
            )
    """)
    conn.commit()
    conn.close()

def save_task(user_id, task_name, description, task_time, duration):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO TASKS(user_id, task_name, description, task_time, duration)
    VALUES(?,?,?,?,?)
    """, (user_id, task_name, description, task_time, duration))
    task_id = cursor.lastrowid   # <-- get the auto generated ID
    conn.commit()
    conn.close()
    return task_id

def get_task(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, task_name, description, task_time, duration, completed
        FROM tasks
        WHERE user_id = ?
    """,(user_id,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT id, user_id, task_name, description, task_time, duration, completed
        FROM tasks
        WHERE completed = 0
                   ''')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def mark_completed(user_id, task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE tasks
        SET completed = 1
        WHERE user_id = ? AND id = ?
    ''', (user_id, task_id,))

    conn.commit()
    conn.close()

def delete_task(task_id, user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ? AND user_id = ?
    """, (task_id, user_id))

    conn.commit()
    conn.close()