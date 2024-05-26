# administrateur.py

import hashlib
from modules.contraintes.contraintes import pause_system
from modules.database.database import Database

class AdministratorManager:
    def __init__(self, db_file):
        self.db = Database(db_file)

    def add_administrator(self, first_name, last_name, address, phone, email, password):
        """Ajoute un administrateur à la base de données."""
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        query = """
            INSERT INTO administrators (first_name, last_name, address, phone, email, password)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (first_name, last_name, address, phone, email, hashed_password)
        self.db.execute_query(query, params)

    def authenticate_administrator(self, email, password):
        """Authentifie un administrateur par email et mot de passe."""
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            results = self.db.read_records(
                table="administrators", 
                condition="email=? AND password=?", 
                params=(email, hashed_password)
            )
            return len(results) > 0
        except Exception as e:
            print(f"Erreur lors de l'authentification : {e}")
        return False
       
    def __del__(self):
        """Ferme la connexion à la base de données lors de la destruction de l'objet."""
        if self.db.conn:
            self.db.conn.close()
            print(f"Disconnected from database: {self.db.db_file}")

