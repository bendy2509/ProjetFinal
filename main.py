import sys
import os

# Ajouter le chemin du projet au sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.administrateur.gestionAdministrateur import menu_gestion_administrateurs
from modules.gestionSalle.gestionSalle import menuGestionSalle
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionBatiment.gestionBatiment import menuGestionBatiment
from modules.contraintes.contraintes import authenticate_admin, clear_screen, pause_system
from modules.gestionProfesseur.menuProfessors import menuGestionProfesseur

def main():
    DB_FILE = "database.db"
    # database = Database(DB_FILE)
    # manager = BuildingManager(DB_FILE)
    admin_manager = AdministratorManager(DB_FILE)
    # admin_manager.add_administrator("Bendy", "SERVILUS", "Pistère", "4170 5257", "bendyservilus@gmail.com", "Servilus_2509")

    while True:
        clear_screen()
        print("\t" * 4 + "===================================================")
        print("\t" * 4 + "|      ____   _    _   ____    _                  |")
        print("\t" * 4 + "|     / ___| | |  | | / ___|  | |                 |")
        print("\t" * 4 + "|    | |     | |__| | | |     | |                 |")
        print("\t" * 4 + "|    | |     |  __  | | |     | |                 |")
        print("\t" * 4 + "|    | |___  | |  | | | |___  | |____             |")
        print("\t" * 4 + "|    |_____| |_|  |_|  \____| |______|            |")
        print("\t" * 4 + "|                                                 |")
        print("\t" * 4 + "===================================================")
        print("\t" * 4 + "|                                                 |")
        print("\t" * 4 + "|                 Menu Principal                  |")
        print("\t" * 4 + "|                                                 |")
        print("\t" * 4 + "===================================================")
        print("\t" * 4 + "|  1. Menu gestion Bâtiment                       |")
        print("\t" * 4 + "|  2. Menu gestion Salle                          |")
        print("\t" * 4 + "|  3. Menu gestion Professeur                     |")
        print("\t" * 4 + "|  4. Menu gestion administrateur                 |")
        print("\t" * 4 + "|  5. Quitter                                     |")
        print("\t" * 4 + "===================================================")

        choice = input("\t" * 4 + "Choisissez une option (****) : ")

        if choice == '1':
            menuGestionBatiment(DB_FILE)
        elif choice == '2':
            menuGestionSalle(DB_FILE)
        elif choice == '3':
            menuGestionProfesseur(DB_FILE)
        elif choice == '4':
            if authenticate_admin(admin_manager):
                menu_gestion_administrateurs(DB_FILE)
            else:
                print("\t" * 4 + "Accès non autorisé.")
            pause_system()

        elif choice == '5':
            print("\t" * 4 + "Au revoir!")
            break
        else:
            print("\t" * 4 + "Choix invalide. Veuillez saisir un nombre entre 1 et 4.")
            pause_system()


if __name__ == "__main__":
    main()
