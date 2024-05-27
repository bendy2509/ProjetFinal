import sys
import os

# Ajouter le chemin du projet au sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.gestionSalle.gestionSalle import menuGestionSalle
from modules.database.database import Database
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionBatiment.buildingsManager import BuildingManager
from modules.gestionBatiment.gestionBatiment import menuGestionBatiment
from modules.contraintes.contraintes import clear_screen, get_int_user


DB_FILE = "database.db"
database = Database(DB_FILE)
manager = BuildingManager(DB_FILE)
admin_manager = AdministratorManager(DB_FILE)
#admin_manager.add_administrator("Bendy", "SERVILUS", "Pistère", "4170 5257", "bendyservilus@gmail.com", "Servilus_2409")


def main():
    x = 1
    y = 40

    while True:
        clear_screen()
        print("Menu Principal:")
        print("1. Menu gestion Batiment")
        print("2. Menu gestion Salle")

        choice = get_int_user("Choisissez une option: ")

        if choice == 1:
            menuGestionBatiment(DB_FILE)

        if choice == 2:
            menuGestionSalle(DB_FILE)



if __name__ == "__main__":
    main()
