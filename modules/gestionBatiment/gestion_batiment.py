"""Module de gestion des bâtiments pour le projet CHCL-DSI."""

from modules.gestionSalle.roomManager import Room
from modules.gestionBatiment.buildings_manager import Building, BuildingManager
from modules.contraintes.contraintes import (check_building_name, clear_screen,
    get_int_user, header_design, is_valid_room_type, pause_system,
    validRoomFloor, validRoomNumber
)


def menu_batiment():
    """Affiche le menu de gestion des bâtiments et renvoie le choix de l'utilisateur."""
    clear_screen()
    header_design()
    print("===================================================")
    print("|                                                 |")
    print("|                 Menu Gestion Bâtiment           |")
    print("|                                                 |")
    print("===================================================")
    print("|                                                 |")
    print("|  1. Enregistrer un bâtiment (admin)             |")
    print("|  2. Ajouter une salle à un bâtiment (admin)     |")
    print("|  3. Modifier le nom d'un bâtiment (admin)       |")
    print("|  4. Afficher les bâtiments                      |")
    print("|  5. Supprimer un bâtiment (admin)               |")
    print("|  0. Retour au menu principal                    |")
    print("|                                                 |")
    print("===================================================")
    choice = input("Choisissez une option: ")
    return choice

def to_add_building(manager):
    """Enregistre un nouveau bâtiment après vérification du nom."""
    while True:
        clear_screen()
        name = input("Nom du bâtiment (A, B, C ou D): ")
        if check_building_name(name):
            break
        print("Veuillez réessayer !!")
        pause_system()
    floors = 3
    building = Building(name, floors)
    manager.add_building(building)

def add_room_to_building(manager, invite):
    """Ajoute une salle à un bâtiment après authentification de l'administrateur."""
    if invite:
        building_name = input("Nom du bâtiment: ")
        room_floor = get_int_user("Entrer le numéro étage (1, 2 ou 3) : ")

        while not validRoomFloor(room_floor):
            room_floor = get_int_user("Entrer le numéro étage (1, 2 ou 3) : ")

        room_number = get_int_user("Numéro de la salle: ")
        while not validRoomNumber(room_number, room_floor):
            clear_screen()
            room_number = get_int_user("Numéro de la salle: ")
        room_number = f"{building_name}-{room_number}"

        room_type = input("Type de salle (salle de cours, salle virtuelle, labo): ")
        while not is_valid_room_type(room_type):
            clear_screen()
            room_type = input("Type de salle (salle de cours, salle virtuelle, labo): ")

        capacity = get_int_user("Nombre de places disponibles (taper 0 pour laisser par défaut soit 60): ")
        capacity = 60 if capacity == 0 else capacity
        room = Room(room_number, room_type, room_floor, "disponible", capacity)
        manager.add_room_to_building(building_name, room)
    else:
        print("Accès refusé. Veuillez connecter en tant qu'Administrateur.")
        pause_system()

def update_building_name(manager, invite):
    """Modifie le nom d'un bâtiment après authentification de l'administrateur."""
    if invite:
        old_name = input("Nom actuel du bâtiment: ")
        new_name = input("Nouveau nom du bâtiment: ")
        while not check_building_name(new_name):
            new_name = input("Nouveau nom du bâtiment: ")

        if check_building_name(new_name):
            manager.update_building_name(old_name, new_name)
        else:
            pause_system()
    else:
        print("Accès refusé. Veuillez connecter en tant qu'Administrateur.")
        pause_system()

def delete_building(manager, invite):
    """Supprime un bâtiment après authentification de l'administrateur."""
    if invite:
        name = input("Nom du bâtiment à supprimer: ")
        manager.delete_building(name)
    else:
        print("Accès refusé. Veuillez connecter en tant qu'Administrateur.")
        pause_system()

def menu_gestion_batiment(db_file, invite):
    """
    Fonction principale pour gérer le menu de gestion des bâtiments et
    effectuer les opérations en fonction du choix de l'utilisateur.
    """
    manager = BuildingManager(db_file)

    while True:
        choice = menu_batiment()
        clear_screen()
        if choice == '1':
            if invite:
                to_add_building(manager)
            else:
                print("Accès refusé. Veuillez connecter en tant qu'Administrateur.")
                pause_system()
        elif choice == '2':
            add_room_to_building(manager, invite)
        elif choice == '3':
            update_building_name(manager, invite)
        elif choice == '4':
            manager.list_buildings()
        elif choice == '5':
            delete_building(manager, invite)
        elif choice == '0':
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 6. Réessayez !!")
            pause_system()
