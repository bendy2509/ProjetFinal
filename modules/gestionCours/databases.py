import sqlite3

class DBManager:
    """Gestionnaire de base de données"""
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Créer les tables nécessaires"""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cours (
                               code_cours TEXT PRIMARY KEY,
                               nom TEXT,
                               debut INTEGER,
                               fin INTEGER,
                               session INTEGER,
                               annee INTEGER)''')
        self.conn.commit()

    def execute_query(self, query, params=()):
        """Exécuter une requête"""
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor.fetchall()
