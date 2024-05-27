"""Definition des contraintes
    get_int_user :
                  Pour les choix entier des utilisateurs
    
    clear_screen : 
                  Pour effacer l'ecran

"""
import os

def clear_screen():
    """Efface l'écran de la console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_system():
    """ Pour mettre le système sur pause."""
    os.system('pause' if os.name == 'nt' else 'read -p "Appuyez sur Entrée pour continuer..."')

def get_int_user(prompt):
    """Demande à l'utilisateur une valeur entière jusqu'à ce qu'une valeur valide soit entrée."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            clear_screen()
            print("Veuillez entrer un nombre entier valide.")
            pause_system()
            clear_screen()

def check_building_name(name):
    """Vérifie si le nom du bâtiment est valide"""
    valid_names = ["A", "B", "C", "D"]
    if name in valid_names:
        return True
    else:
        clear_screen()
        print("Mauvais choix. Veuillez choisir entrer A, B, C, D")
        pause_system()
        clear_screen()
        return False

def validRoomFloor(floor):
    """Pour valider l'étage d'une salle."""
    if 1 <= floor <= 3:
        return True
    clear_screen()
    print("Mauvais choix. Veuiller entrer 1, 2 ou 3 pour l'étage.")
    pause_system()
    clear_screen()
    return False

def validRoomNumber(room_number, floor_number, ):
    """Tenir à ce que les salles soient dans la bonne étage avec le bon numéro."""
    room_ = {
        "floor_1": [n for n in range(101, 107)],
        "floor_2": [n for n in range(201, 207)],
        "floor_3": [n for n in range(301, 307)],
    }
    if floor_number == 1 and room_number in room_["floor_1"]:
        return True
    elif floor_number == 2 and room_number in room_["floor_2"]:
        return True
    elif floor_number == 3 and room_number in room_["floor_3"]:
        return True
    clear_screen()
    print("Vous devez choisir entrer :")
    print("Etage 1 : 101 à 106")
    print("Etage 2 : 201 à 206")
    print("Etage 3 : 301 à 306")
    pause_system()
    return False

def is_valid_room_type(room_type):
    clear_screen()
    """Vérifie si le type de salle est valide."""
    valid_room_types = ["salle de cours", "salle virtuelle", "labo"]
    if room_type not in valid_room_types:
        print("Vous devez choisir entre 'salle de cours, salle virtuelle, labo'")
        pause_system()
    return room_type.lower() in valid_room_types

def authenticate_admin(admin_manager):
    """Demande les informations d'authentification et vérifie l'authenticité de l'administrateur."""
    print("Vous devez vous identifier !")
    admin_email = input("Email administrateur: ")
    admin_password = input("Mot de passe : ")
    return admin_manager.authenticate_administrator(admin_email, admin_password)
