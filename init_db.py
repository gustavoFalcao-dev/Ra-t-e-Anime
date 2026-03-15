import os
import sqlite3


def databaseExists(path: str) -> bool:
    """Verifica se o arquivo do banco de dados já existe."""
    return os.path.exists(path)


def createDatabase(path: str) -> sqlite3.Connection:
    """Cria o banco de dados e as tabelas Anime e Discord."""
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Anime (
            anime_id                INTEGER PRIMARY KEY,
            anime_title             TEXT    NOT NULL,
            url_anime_main_picture  TEXT,
            alternative_title_en    TEXT,
            score                   REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Discord (
            id_user       INTEGER PRIMARY KEY AUTOINCREMENT,
            username      TEXT    NOT NULL,
            anime_id      INTEGER NOT NULL,
            score_pessoal REAL,
            FOREIGN KEY (anime_id) REFERENCES Anime(anime_id)
        )
    """)

    conn.commit()
    print(f"[OK] Banco de dados criado em: {path}")
    return conn


def connectDB(path: str) -> sqlite3.Connection:
    """Conecta a um banco de dados já existente."""
    conn = sqlite3.connect(path)
    print(f"[OK] Conectado ao banco existente: {path}")
    return conn
