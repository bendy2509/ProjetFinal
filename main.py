import sys
import os

# Ajouter le chemin du projet au sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.database.database import Database
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionBatiment.buildingsManager import Building, BuildingManager, Room
from modules.gestionBatiment.gestionBatiment import menuGestionBatiment
from modules.contraintes.contraintes import clear_screen, cursor_position, get_int_user


db_file = "database.db"
database = Database(db_file)
manager = BuildingManager(db_file)
admin_manager = AdministratorManager(db_file)
#admin_manager.add_administrator("Bendy", "SERVILUS", "Pistère", "4170 5257", "bendyservilus@gmail.com", "Servilus_2509")


def main():
    x = 1
    y = 50

    while True:
        clear_screen()
        cursor_position(x,y+3)
        print("Menu Principal:")
        cursor_position(x+2,y)
        print("1. Menu gestion Batiment")

        cursor_position(x+5,50)
        choice = get_int_user("Choisissez une option: ", x+6, y)

        if choice == 1:
            menuGestionBatiment(db_file)



if __name__ == "__main__":
    main()
