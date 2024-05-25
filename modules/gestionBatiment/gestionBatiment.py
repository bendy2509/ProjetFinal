import sys
import os

# Ajouter le chemin du projet au sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.administrateur.administrateur import AdministratorManager
from modules.gestionBatiment.buildingsManager import Building, BuildingManager, Room
from modules.contraintes.contraintes import (
    check_building_name, clear_screen, cursor_position,
    get_int_user, is_valid_room_type, pause_system,
    validRoomFloor, validRoomNumber
)


def menuBatiment(x, y):
    clear_screen()
    cursor_position(x, y+3)
    print("Menu Gestion Batiment :")
    cursor_position(x+2, y)
    print("1. Enregistrer un bâtiment")
    cursor_position(x+3, y)
    print("2. Ajouter une salle à un bâtiment")
    cursor_position(x+4, y)
    print("3. Modifier le nom d'un bâtiment")
    cursor_position(x+5, y)
    print("4. Modifier le nombre d'étages d'un bâtiment")
    cursor_position(x+6, y)
    print("5. Afficher les bâtiments")
    cursor_position(x+7, y)
    print("6. Supprimer un bâtiment")
    cursor_position(x+8, y)
    print("7. Quitter")
    cursor_position(x+9, y)
    choice = get_int_user("Choisissez une option: ", x+10, y)

    return choice


def to_add_building(manager, x, y):
    """Enregistre un nouveau bâtiment après vérification du nom."""

    while True:
        clear_screen()
        cursor_position(x, y)
        name = input("Nom du bâtiment (A, B, C ou D): ")
        if check_building_name(name):
            break
        else:
            cursor_position(x+2, y)
            print("Mauvais choix. Veuillez réessayer !!")
            pause_system()
    floors = 3
    building = Building(name, floors)
    manager.add_building(building)


def add_room_to_building(manager, admin_manager, x, y):
    """Ajoute une salle à un bâtiment après authentification de l'administrateur."""

    cursor_position(x, y)
    print("Vous devez vous identifier !")
    cursor_position(x+1, y)
    admin_email = input("Email administrateur: ")
    cursor_position(x+2, y)
    admin_password = input("Mot de passe : ")
    if admin_manager.authenticate_administrator(admin_email, admin_password):
        cursor_position(x+3, y)
        building_name = input("Nom du bâtiment: ")
        cursor_position(x+4, y)
        room_floor = get_int_user("Entrer le numéro étage (1, 2 ou 3) : ", x+1, y)

        while not validRoomFloor(room_floor):
            room_floor = get_int_user("Entrer le numéro étage (1, 2 ou 3) : ", x+1, y)

        room_number = get_int_user("Numéro de la salle: ", x+2, y)
        while not validRoomNumber(room_number, room_floor, x+3, y):
            clear_screen()
            room_number = get_int_user("Numéro de la salle: ", x+2, y)
        cursor_position(x+3, y)
        room_type = input("Type de salle (salle de cours, salle virtuelle, labo): ")
        while not is_valid_room_type(room_type):
            clear_screen()
            cursor_position(x+3, y)
            room_type = input("Type de salle (salle de cours, salle virtuelle, labo): ")

        capacity = get_int_user("Nombre de places disponibles (taper 0 pour laisser par défaut soit 60): ", x+4, y)
        capacity = 60 if capacity == 0 else capacity
        room = Room(room_number, room_type, room_floor, capacity=capacity)
        manager.add_room_to_building(building_name, room)
    else:
        print("Authentification échouée. Accès refusé.")
        pause_system()


def menuGestionBatiment(db_file):
    """
    Fonction principale pour gérer le menu de gestion des bâtiments et
    effectuer les opérations en fonction du choix de l'utilisateur.
    """
    manager = BuildingManager(db_file)
    admin_manager = AdministratorManager(db_file)

    x, y = 1, 50

    while True:
        choice = menuBatiment(x, y)
        clear_screen()
        if choice == 1:
            to_add_building(manager, x, y)
        elif choice == 2:
            add_room_to_building(manager=manager, admin_manager=admin_manager, x=x, y=y)
        elif choice == 3:
            old_name = input("Nom actuel du bâtiment: ")
            new_name = input("Nouveau nom du bâtiment: ")
            manager.update_building_name(old_name, new_name)
        elif choice == 4:
            name = input("Nom du bâtiment: ")
            new_floors = int(input("Nouveau nombre d'étages: "))
            manager.update_building_floors(name, new_floors)
        elif choice == 5:
            manager.list_buildings()
        elif choice == 6:
            name = input("Nom du bâtiment à supprimer: ")
            manager.delete_building(name)
        elif choice == 7:
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 7. Réessayez !!")
            pause_system()


if __name__ == "__main__":
    menuGestionBatiment()
