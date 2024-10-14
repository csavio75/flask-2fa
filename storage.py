import sqlite3


# Fonction pour se connecter à la base de données SQLite
def connect_db():
    conn = sqlite3.connect('users.db')
    return conn


# Fonction pour créer les tables nécessaires si elles n'existent pas
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
