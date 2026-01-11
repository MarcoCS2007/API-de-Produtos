import sqlite3

class Database:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls) 
            cls._instance._inicializado = False
        return cls._instance 

    def __init__(self, database_path: str = "exemple.db"):    
        if not self._inicializado:
            self._database_path = database_path
            self._connect = None
            self._inicializado = True

    def connect(self):
        if self._connect is None:
            self._connect = sqlite3.connect(self._database_path, isolation_level=None)
            self._connect.row_factory = sqlite3.Row
            self._connect.execute("PRAGMA foreign_keys = ON")
        return self._connect
    
    def close(self):
        if self._connect:
            self._connect.close()
            self._connect = None

    def cursor(self):
        if self._connect is None:
            self.connect()
        return self._connect.cursor()
    
    def create_tables(self):
        cur = self.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL,
            categoria TEXT NOT NULL
        );
        """)