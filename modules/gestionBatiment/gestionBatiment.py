import sys
import os

# Ajouter le chemin du projet au sys.path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.gestionSalle.roomManager import Room
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionBatiment.buildingsManager import Building, BuildingManager
from modules.contraintes.contraintes import (
    authenticate_admin, check_building_name, clear_screen,
    get_int_user, is_valid_room_type, pause_system,
    validRoomFloor, validRoomNumber
)


def menuBatiment():
    clear_screen()
    print("Menu Gestion Batiment :")
    print("1. Enregistrer un bâtiment (admin)")
    print("2. Ajouter une salle à un bâtiment (admin)")
    print("3. Modifier le nom d'un bâtiment (admin)")
    print("4. Afficher les bâtiments")
    print("5. Supprimer un bâtiment (admin)")
    print("6. Retour au menu principal")
    choice = get_int_user("Choisissez une option: ")

    return choice


def to_add_building(manager):
    """Enregistre un nouveau bâtiment après vérification du nom."""
    while True:
        clear_screen()
        name = input("Nom du bâtiment (A, B, C ou D): ")
        if check_building_name(name):
            break
        else:
            print("Veuillez réessayer !!")
            pause_system()
    floors = 3
    building = Building(name, floors)
    manager.add_building(building)


def add_room_to_building(manager, admin_manager, ):
    """Ajoute une salle à un bâtiment après authentification de l'administrateur."""
    if authenticate_admin(admin_manager):
        building_name = input("Nom du bâtiment: ")
        room_floor = get_int_user("Entrer le numéro étage (1, 2 ou 3) : ")

        while not validRoomFloor(room_floor):
            room_floor = get_int_user("Entrer le numéro étage (1, 2 ou 3) : ")

        room_number = get_int_user("Numéro de la salle: ")
        while not validRoomNumber(room_number, room_floor):
            clear_screen()
            room_number = get_int_user("Numéro de la salle: ")
        room_type = input("Type de salle (salle de cours, salle virtuelle, labo): ")
        while not is_valid_room_type(room_type):
            clear_screen()
            room_type = input("Type de salle (salle de cours, salle virtuelle, labo): ")

        capacity = get_int_user("Nombre de places disponibles (taper 0 pour laisser par défaut soit 60): ")
        capacity = 60 if capacity == 0 else capacity
        room = Room(room_number, room_type, room_floor, capacity=capacity)
        manager.add_room_to_building(building_name, room)
    else:
        print("Authentification échouée. Accès refusé.")
        pause_system()


def menuGestionBatiment(DB_FILE):
    """
    Fonction principale pour gérer le menu de gestion des bâtiments et
    effectuer les opérations en fonction du choix de l'utilisateur.
    """
    manager = BuildingManager(DB_FILE)
    admin_manager = AdministratorManager(DB_FILE)

    while True:
        choice = menuBatiment()
        clear_screen()
        if choice == 1:
            if authenticate_admin(admin_manager):
                to_add_building(manager)
            else:
                print("Authentification échouée. Accès refusé.")
                pause_system()

        elif choice == 2:
            add_room_to_building(manager=manager, admin_manager=admin_manager)
        elif choice == 3:
            if authenticate_admin(admin_manager):
                old_name = input("Nom actuel du bâtiment: ")
                new_name = input("Nouveau nom du bâtiment: ")
                while not check_building_name(new_name):
                    new_name = input("Nouveau nom du bâtiment: ")

                if check_building_name(new_name):
                    manager.update_building_name(old_name, new_name)
                else:
                    pause_system()
            else:
                print("Authentification échouée. Accès refusé.")
                pause_system()

        elif choice == 4:
            manager.list_buildings()
        elif choice == 5:
            if authenticate_admin(admin_manager):
                name = input("Nom du bâtiment à supprimer: ")
                manager.delete_building(name)
            else:
                print("Authentification échouée. Accès refusé.")
                pause_system()

        elif choice == 6:
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 7. Réessayez !!")
            pause_system()


if __name__ == "__main__":
    menuGestionBatiment()
