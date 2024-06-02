from modules.gestionBatiment.buildings_manager import BuildingManager
from modules.gestionBatiment.gestion_batiment import add_room_to_building
from modules.contraintes.contraintes import clear_screen, pause_system
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionSalle.roomManager import RoomManager

def menuSalle():
    clear_screen()
    print("===================================================")
    print("|      ____   _    _   ____    _                  |")
    print("|     / ___| | |  | | / ___|  | |                 |")
    print("|    | |     | |__| | | |     | |                 |")
    print("|    | |     |  __  | | |     | |                 |")
    print("|    | |___  | |  | | | |___  | |____             |")
    print("|    |_____| |_|  |_|  \\____| |______|            |")
    print("|                                                 |")
    print("===================================================")
    print("|                                                 |")
    print("|                 Menu Gestion Salle              |")
    print("|                                                 |")
    print("===================================================")
    print("|                                                 |")
    print("|  1. Lister les salles d'un bâtiment             |")
    print("|  2. Ajouter une salle dans un bâtiment (Admin)  |")
    print("|  3. Supprimer une salle d'un bâtiment (Admin)   |")
    print("|  4. Retourner au menu principal                 |")
    print("|                                                 |")
    print("===================================================")
    choice = input("Choisissez une option: ")
    return choice


def menuGestionSalle(db_file, invite):
    """
    Fonction principale pour gérer le menu de gestion des salles.
    """
    room_manager = RoomManager(db_file)
    manager = BuildingManager(db_file)
    admin_manager = AdministratorManager(db_file)

    while True:
        choice = menuSalle()

        if choice == '1':
            building_name = input("Nom du bâtiment: ")
            room_manager.list_rooms(building_name)
            pause_system()
        elif choice == '2':
            add_room_to_building(manager=manager, admin_manager=admin_manager, invite=invite)

        elif choice == '3':
            if invite:
                room_number = input("Numéro de la salle à supprimer : ")
                if building_name.strip() and room_number.strip():
                    room_manager.delete_room_from_building(room_number)
                else:
                    print("Le numéro de la salle ne peut pas être vide.")
            else:
                print("Accès refusé. Veuillez connecter en tant qu'Administrateur.")
                pause_system()

        elif choice == '4':
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 4. Réessayez !!")
            pause_system()
