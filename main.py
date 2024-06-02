import sys
import os

# Ajouter le chemin du projet au sys.path
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.administrateur.gestionAdministrateur import menu_gestion_administrateurs
from modules.gestionSalle.gestionSalle import menuGestionSalle
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionBatiment.gestionBatiment import menuGestionBatiment
from modules.contraintes.contraintes import clear_screen, pause_system
from modules.gestionProfesseur.menuProfessors import menuGestionProfesseur

def main_menu(db_file, invite=True):
    while True:
        clear_screen()
        print("===================================================")
        print("|      ____   _    _   ____    _                  |")
        print("|     / ___| | |  | | / ___|  | |                 |")
        print("|    | |     | |__| | | |     | |                 |")
        print("|    | |     |  __  | | |     | |                 |")
        print("|    | |___  | |  | | | |___  | |____             |")
        print("|    |_____| |_|  |_|  \\____| |______|            |")
        print("|                                                 |")
        print("|                      DSI-CHCL                   |")
        print("===================================================")
        print("|                                                 |")
        print("|                 Menu Principal                  |")
        print("|                                                 |")
        print("===================================================")
        print("|  1. Gestion des Bâtiments                       |")
        print("|  2. Gestion des Salles                          |")
        print("|  3. Gestion des Professeurs                     |")
        print("|  4. Gestion des Administrateurs                 |")
        print("|  5. Quitter                                     |")
        print("===================================================")

        choice = input("Choisissez une option (1-5) : ")

        if choice == '1':
            menuGestionBatiment(db_file, invite)
        elif choice == '2':
            menuGestionSalle(db_file, invite)
        elif choice == '3':
            menuGestionProfesseur(db_file)
        elif choice == '4':
            if invite:
                menu_gestion_administrateurs(db_file)
            else:
                print("Accès interdit !! Veuillez connecter en tant qu'Administrateur.")
        elif choice == '5':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 5.")
            pause_system()

def initial_menu(db_file):
    admin_manager = AdministratorManager(db_file)

    while True:
        clear_screen()
        print("===================================================")
        print("|      ____   _    _   ____    _                  |")
        print("|     / ___| | |  | | / ___|  | |                 |")
        print("|    | |     | |__| | | |     | |                 |")
        print("|    | |     |  __  | | |     | |                 |")
        print("|    | |___  | |  | | | |___  | |____             |")
        print("|    |_____| |_|  |_|  \\____| |______|            |")
        print("|                                                 |")
        print("|                      DSI-CHCL                   |")
        print("===================================================")
        print("|                                                 |")
        print("|                 Menu de configuration           |")
        print("|                                                 |")
        print("===================================================")
        print("|  1. Connecter en tant qu'Administrateur         |")
        print("|  2. Créer un compte Administrateur              |")
        print("|  3. Connecter en tant qu'invité                 |")
        print("|  4. Quitter                                     |")
        print("===================================================")

        choice = input("Choisissez une option (1-4) : ")

        if choice == '1':
            email = input("Email : ")
            password = input("Mot de passe : ")
            if admin_manager.authenticate_administrator(email, password):
                print("Connexion réussie.")
                pause_system()
                main_menu(db_file)
            else:
                print("Échec de la connexion. Vérifiez vos identifiants.")
                pause_system()
        elif choice == '2':
            first_name = input("Prénom : ")
            last_name = input("Nom : ")
            address = input("Adresse : ")
            phone = input("Téléphone : ")
            email = input("Email : ")
            password = input("Mot de passe : ")
            admin_manager.add_administrator(first_name, last_name, address, phone, email, password)
            pause_system()
        elif choice == '3':
            print("Connecté en tant qu'invité.")
            pause_system()
            main_menu(db_file, False)
        elif choice == '4':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 4.")
            pause_system()

if __name__ == "__main__":
    DB_FILE = "database.db"
    initial_menu(DB_FILE)