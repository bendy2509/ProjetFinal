import hashlib

from modules.contraintes.contraintes import clear_screen, pause_system
from modules.database.database import Database


class AdministratorManager:
    def __init__(self, DB_FILE):
        """
        Initialise une instance de AdministratorManager.

        :param DB_FILE: Le chemin du fichier de base de données SQLite.
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
        try:
            self.db.create_record(
                table="administrators",
                values={
                    "first_name": first_name,
                    "last_name": last_name,
                    "address": address,
                    "phone": phone,
                    "email": email,
                    "password": hashed_password
                },
            )
            print(f"Administrateur {first_name} {last_name} ajouté avec succès.")
        except Exception:
            print(f"Erreur lors de l'ajout de l'administrateur")

    def authenticate_administrator(self, email, password):
        """
        Authentifie un administrateur par email et mot de passe.

        :param email: Adresse email de l'administrateur.
        :param password: Mot de passe de l'administrateur.
        :return: True si l'authentification réussit, False sinon.
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            results = self.db.read_records(
                table="administrators", 
                condition="email=? AND password=?", 
                params=(email, hashed_password)
            )
            if results:
                return True
            else:
                print("Identifiants incorrects.")
                return False
        except:
            print(f"Erreur lors de l'authentification")
            pause_system()
            return False

    def list_administrators(self):
        """
        Liste tous les administrateurs dans la base de données.
        """
        clear_screen()
        try:
            administrators = self.db.read_records(table="administrators")
            if administrators:
                print("\t"*5, "Liste des administrateurs :\n")
                print("\t" * 2, "{:<15}{:<15}{:<15}{:<15}{:<30}".format("NOM","PRENOM","ADRESSE","TELEPHONE","EMAIL"))
                print()
                for admin in administrators:
                    print("\t" * 2, "{:<15}{:<15}{:<15}{:<15}{:<30}".format(admin[2],admin[1],
                    admin[3],admin[4],admin[5]))
            else:
                print("Aucun administrateur trouvé.")
        except:
            print(f"Erreur lors de la récupération des administrateurs.")
        finally:
            pause_system()

    def delete_administrator(self, email):
        """
        Supprime un administrateur de la base de données.

        :param email: Adresse email de l'administrateur à supprimer.
        """
        try:
            self.db.delete_record(table="administrators", condition="email=?", params=(email,))
            print(f"Administrateur avec l'email {email} supprimé avec succès.")
        except Exception as e:
            print(f"Erreur lors de la suppression de l'administrateur : {e}")
