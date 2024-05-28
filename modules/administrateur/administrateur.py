# administrateur.py

import hashlib
from modules.contraintes.contraintes import pause_system
from modules.database.database import Database

class AdministratorManager:
    def __init__(self, DB_FILE):
        """
        Initialise une instance d'AdministratorManager.

        :param DB_FILE: Le fichier de base de données SQLite.
        """
        self.db = Database(DB_FILE)

    def add_administrator(self, first_name, last_name, address, phone, email, password):
        """
        Ajoute un administrateur à la base de données.

        :param first_name: Prénom de l'administrateur.
        :param last_name: Nom de famille de l'administrateur.
        :param address: Adresse de l'administrateur.
        :param phone: Numéro de téléphone de l'administrateur.
        :param email: Adresse email de l'administrateur.
        :param password: Mot de passe de l'administrateur (en clair, sera haché).
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        query = """
            INSERT INTO administrators (first_name, last_name, address, phone, email, password)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (first_name, last_name, address, phone, email, hashed_password)
        self.db.execute_query(query, params)
        print(f"Administrateur {first_name} {last_name} ajouté avec succès.")

    def authenticate_administrator(self, email, password):
        """
        Authentifie un administrateur par email et mot de passe.

        :param email: Adresse email de l'administrateur.
        :param password: Mot de passe de l'administrateur.
        :return: True si l'authentification réussit, False sinon.
        """
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
