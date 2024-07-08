# database.py
import sqlite3
from contextlib import closing

from modules.contraintes.contraintes import clear_screen, pause_system

class Database:
    """
    Classe pour gérer les interactions avec une base de données SQLite.
    """

    def __init__(self, DB_FILE):
        """
        Initialise la connexion à la base de données et crée les tables si elles n'existent pas.

        :param DB_FILE: Chemin vers le fichier de base de données SQLite.
        """
        self.DB_FILE = DB_FILE
        self.conn = self.create_connection()
        self.create_tables()

    def create_connection(self):
        """
        Crée une connexion à la base de données SQLite spécifiée par DB_FILE.

        :return: Objet de connexion à la base de données.
        """
        try:
            conn = sqlite3.connect(self.DB_FILE)
            print(f"Connected to database: {self.DB_FILE}")
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_tables(self):
        """
        Crée les tables dans la base de données SQLite si elles n'existent pas.
        """
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
                    number TEXT PRIMARY KEY,
                    building_id INTEGER,
                    floor INTEGER,
                    type TEXT,
                    capacity INTEGER DEFAULT 60,
                    statut TEXT DEFAULT 'disponible',
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
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS professors(
                    code TEXT PRIMARY KEY,
                    nom TEXT ,
                    prenom TEXT ,
                    sexe TEXT,
                    email TEXT UNIQUE,
                    telephone TEXT UNIQUE,
                    codeCours TEXT UNIQUE
            )''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cours (
                    code_cours TEXT PRIMARY KEY,
                    nom TEXT,
                    teacher_code TEXT DEFAULT NULL,
                    duration INTEGER,
                    session INTEGER,
                    annee INTEGER,
                    FOREIGN KEY (teacher_code) REFERENCES professors(code)
                )
            ''')
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS schedules(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    room_number TEXT NOT NULL,
                    jour TEXT NOT NULL,
                    debut INTEGER NOT NULL,
                    fin INTEGER NOT NULL,
                    cours_id TEXT NOT NULL,
                    FOREIGN KEY (room_number) REFERENCES rooms(number),
                    FOREIGN KEY (cours_id) REFERENCES cours(code_cours)
                )
            """)
            self.conn.commit()
            print("Tables created successfully")

    def execute_query(self, query, params=None):
        """
        Exécute une requête SQL avec des paramètres facultatifs.

        :param query: La requête SQL à exécuter.
        :param params: Paramètres optionnels pour la requête SQL.
        :return: Résultat de la requête SQL.
        """
        with closing(self.conn.cursor()) as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor.fetchall()

    def create_record(self, table, values):
        """
        Insère une nouvelle ligne dans la table spécifiée avec les valeurs données.

        :param table: Nom de la table.
        :param values: Valeurs à insérer sous forme de paires clé-valeur.
        """
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['?' for _ in values])
        query = f"INSERT OR IGNORE INTO {table} ({columns}) VALUES ({placeholders})"
        affected_rows = self.execute_query(query, list(values.values()))
        clear_screen()
        print('\t' * 4 + "Request ok !")

        if affected_rows == 0:
            clear_screen()
            print("\t" * 4 + "Les données que vous essayez d'insérer existent déjà dans la base de données.")
            pause_system()

        pause_system()

    def read_records(self, table, columns=None, condition=None, params=None):
        """
        Récupère des lignes de la table spécifiée en fonction des colonnes et de la condition données.

        :param table: Nom de la table.
        :param columns: Colonnes à récupérer qui est une liste.
        :param condition: Condition pour la récupération des lignes.
        :param params: Paramètres pour la condition.
        :return: Résultat de la requête SQL.
        """
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

    def update_record(self, table, values, condition, condition_params=None):
        """
        Met à jour des lignes dans la table spécifiée en fonction de la condition donnée.

        :param table: Nom de la table où la mise à jour doit être effectuée.
        :param values: Dictionnaire de paires colonne-valeur à mettre à jour.
        :param condition: Condition SQL pour identifier les lignes à mettre à jour.
        :param condition_params: Paramètres optionnels pour la condition SQL.
        :return: Résultat de l'exécution de la requête SQL.
        """
        # Construire la clause SET de la requête SQL en joignant les paires colonne-valeur
        set_values = ', '.join([f"{column} = ?" for column in values.keys()])

        # Former la requête SQL complète
        query = f"UPDATE {table} SET {set_values} WHERE {condition}"

        # Préparer les paramètres pour l'exécution de la requête
        params = list(values.values())

        # Ajouter les paramètres de la condition à la liste des paramètres s'ils existent
        if condition_params:
            params.extend(condition_params)

        # Exécuter la requête avec les paramètres préparés
        return self.execute_query(query, params)

    def delete_record(self, table, condition, params=None):
        """
        Supprime des lignes de la table spécifiée en fonction de la condition donnée.

        :param table: Nom de la table.
        :param condition: Condition pour déterminer les lignes à supprimer.
        :param params: Paramètres pour la requête SQL, si nécessaire.
        """
        query = f"DELETE FROM {table} WHERE {condition}"
        if params:
            self.execute_query(query, params)
        else:
            self.execute_query(query)
        clear_screen()
        print('\t' * 4 + "Request ok !")

    def __del__(self):
        """
        Ferme la connexion à la base de données lors de la destruction de l'objet.
        """
        clear_screen()
        if self.conn:
            self.conn.close()
