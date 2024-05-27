

from modules.contraintes.contraintes import clear_screen, get_int_user, pause_system
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionSalle.roomManager import RoomManager


def menuGestionSalle(db_file):
    """
    Fonction principale pour gérer le menu de gestion des salles.
    """
    room_manager = RoomManager(db_file)
    #admin_manager = AdministratorManager(db_file)

    while True:
        clear_screen()
        print("Menu Gestion Salle :")
        print("1. Lister les salles d'un bâtiment")
        # print("2. Lister toutes les salles avec les bâtiments")
        print("3. Supprimer une salle d'un bâtiment")
        print("4. Retourner au menu principal")
        choice = get_int_user("Choisissez une option: ")

        if choice == 1:
            building_name = input("Nom du bâtiment: ")
            room_manager.list_rooms_of_building(building_name)
        # elif choice == 2:
        #     room_manager.list_all_rooms_with_buildings()
        elif choice == 3:
            building_name = input("Nom du bâtiment: ")
            room_number = input("Numéro de la salle: ")
            room_manager.delete_room_from_building(building_name, room_number)
        elif choice == 4:
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 4. Réessayez !!")
            pause_system()

if __name__ == "__main__":
    menuGestionSalle()
