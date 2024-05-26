# database.py
import sqlite3
from contextlib import closing

from modules.contraintes.contraintes import clear_screen, cursor_position, pause_system

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.create_connection()
        self.create_tables()

    def create_connection(self):
        """Crée une connexion à la base de données SQLite spécifiée par db_file."""
        try:
            conn = sqlite3.connect(self.db_file)
            print(f"Connected to database: {self.db_file}")
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_tables(self):
        """Crée les tables dans la base de données SQLite si elles n'existent pas."""
        with closing(self.conn.cursor()) as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS buildings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    floors INTEGER DEFAULT 3
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rooms (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    building_id INTEGER,
                    floor INTEGER,
                    number TEXT,
                    type TEXT,
                    capacity INTEGER DEFAULT 60,
                    disponibility TEXT DEFAULT 'disponible',
                    FOREIGN KEY (building_id) REFERENCES buildings(id)
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS administrators (
                    id INTEGER PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    address TEXT,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
            ''')
            self.conn.commit()
            print("Tables created successfully")

    def execute_query(self, query, params=None):
        """Exécute une requête SQL avec des paramètres facultatifs."""
        with closing(self.conn.cursor()) as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor.fetchall()

    def create_record(self, table, values):
        """Insère une nouvelle ligne dans la table spécifiée avec les valeurs données."""
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['?' for _ in values])
        query = f"INSERT OR IGNORE INTO {table} ({columns}) VALUES ({placeholders})"
        affected_rows = self.execute_query(query, list(values.values()))
        if affected_rows == 0:
            clear_screen()
            cursor_position(5,50)
            print("Les données que vous essayez d'insérer existent déjà dans la base de données.")

    def read_records(self, table, columns=None, condition=None, params=None):
        """Récupère des lignes de la table spécifiée en fonction des colonnes et de la condition données."""
        if columns:
            columns = ', '.join(columns)
        else:
            columns = '*'
        query = f"SELECT {columns} FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        if params:
            return self.execute_query(query, params)
        else:
            return self.execute_query(query)

    def update_record(self, table, values, condition):
        """Met à jour des lignes dans la table spécifiée en fonction de la condition donnée."""
        set_values = ', '.join([f"{column} = ?" for column in values.keys()])
        query = f"UPDATE {table} SET {set_values} WHERE {condition}"
        self.execute_query(query, list(values.values()))

    def delete_record(self, table, condition):
        """Supprime des lignes de la table spécifiée en fonction de la condition donnée."""
        query = f"DELETE FROM {table} WHERE {condition}"
        self.execute_query(query)

    def __del__(self):
        """Ferme la connexion à la base de données lors de la destruction de l'objet."""
        clear_screen()
        if self.conn:
            self.conn.close()
            print(f"Déconnection à la base de donnée: {self.db_file}")
            pause_system()
