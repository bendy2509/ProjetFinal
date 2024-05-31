import sys
import os

# Ajouter le chemin du projet au sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.gestionSalle.gestionSalle import menuGestionSalle
from modules.database.database import Database
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionBatiment.buildingsManager import BuildingManager
from modules.gestionBatiment.gestionBatiment import menuGestionBatiment
from modules.contraintes.contraintes import clear_screen, get_int_user, pause_system
from gestionProfesseur.menuProfessors import menuGestionProfesseur



def main():
    DB_FILE = "database.db"
    # database = Database(DB_FILE)
    # manager = BuildingManager(DB_FILE)
    # admin_manager = AdministratorManager(DB_FILE)
    # admin_manager.add_administrator("Bendy", "SERVILUS", "Pistère", "4170 5257", "bendyservilus@gmail.com", "Servilus_2509")

    while True:
        clear_screen()
        print("Menu Principal:")
        print("1. Menu gestion Bâtiment")
        print("2. Menu gestion Salle")
        print("3. Menu gestion Professeur")
        print("4. Quitter")

        choice = input("Choisissez une option (****) : ")

        if choice == '1':
            menuGestionBatiment(DB_FILE)
        elif choice == '2':
            menuGestionSalle(DB_FILE)
        elif choice == '3':
            menuGestionProfesseur(DB_FILE)
        elif choice == '4':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 4.")
            pause_system()


if __name__ == "__main__":
    main()
