import sqlite3

# Функции для работы с базой данных

def create_db():
    conn = sqlite3.connect("casino_db.sqlite")
    cursor = conn.cursor()

    # Создание таблицы пользователей
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            balance REAL DEFAULT 0
        )
    """)

    # Создание таблицы ставок
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bets (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            game_id TEXT,
            bet_amount REAL,
            result TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def get_user_balance(user_id):
    conn = sqlite3.connect("casino_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else 0

def update_user_balance(user_id, new_balance):
    conn = sqlite3.connect("casino_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user_id))
    conn.commit()
    conn.close()

def add_bet(user_id, game_id, bet_amount, result):
    conn = sqlite3.connect("casino_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bets (user_id, game_id, bet_amount, result) VALUES (?, ?, ?, ?)", (user_id, game_id, bet_amount, result))
    conn.commit()
    conn.close()
