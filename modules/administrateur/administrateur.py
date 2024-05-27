# administrateur.py

import hashlib
from modules.contraintes.contraintes import pause_system
from modules.database.database import Database

class AdministratorManager:
    def __init__(self, DB_FILE):
        self.db = Database(DB_FILE)

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
            pause_system()
        return False
