from modules.gestionBatiment.buildingsManager import BuildingManager
from modules.gestionBatiment.gestionBatiment import add_room_to_building
from modules.contraintes.contraintes import clear_screen, pause_system
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionSalle.roomManager import RoomManager

def update_room(room_manager, building_name, room_number):
    """
    Affiche une liste de choix pour mettre à jour les informations d'une salle.

    :param building_name: Nom du bâtiment.
    :param room_number: Numéro de la salle.
    """
    while True:
        clear_screen()
        print(f"Mise à jour de la salle {room_number} dans le bâtiment {building_name} :")
        print("1. Mettre à jour le numéro de la salle")
        print("2. Mettre à jour l'étage de la salle")
        print("3. Mettre à jour le type de la salle")
        print("4. Mettre à jour la capacité de la salle")
        print("5. Retourner au menu précédent")
        choice = input("Choisissez une option: ")

        if choice == '1':
            
            room_manager.update_room_number(building_name, room_number)
        elif choice == '2':
            room_manager.update_room_floor(building_name, room_number)
        elif choice == '3':
            room_manager.update_room_type(building_name, room_number)
        elif choice == '4':
            room_manager.update_room_capacity(building_name, room_number)
        elif choice == '5':
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 5. Réessayez !!")
            pause_system()

def menuGestionSalle(db_file):
    """
    Fonction principale pour gérer le menu de gestion des salles.
    """
    room_manager = RoomManager(db_file)
    manager = BuildingManager(db_file)
    admin_manager = AdministratorManager(db_file)

    while True:
        clear_screen()
        print("Menu Gestion Salle :")
        print("1. Lister les salles d'un bâtiment")
        print("2. Ajouter une salle dans un batiment")
        print("3. Mettre à jour les informations d'une salle")
        print("4. Supprimer une salle d'un bâtiment")
        print("5. Retourner au menu principal")
        choice = input("Choisissez une option: ")

        if choice == '1':
            building_name = input("Nom du bâtiment: ")
            room_manager.list_rooms(building_name)
            pause_system()
        elif choice == '2':
            add_room_to_building(manager=manager, admin_manager=admin_manager)

        elif choice == '3':
            building_name = input("Nom du bâtiment: ")
            room_number = input("Numéro de la salle: ")
            if building_name.strip() and room_number.strip():
                update_room(room_manager, building_name, room_number)
            else:
                print("Le nom du bâtiment et le numéro de la salle ne peuvent pas être vides.")
            

        elif choice == '4':
            building_name = input("Nom du bâtiment: ")
            room_number = input("Numéro de la salle: ")
            if building_name.strip() and room_number.strip():
                room_manager.delete_room_from_building(building_name, room_number)
            else:
                print("Le nom du bâtiment et le numéro de la salle ne peuvent pas être vides.")
        elif choice == '5':
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 4. Réessayez !!")
            pause_system()
