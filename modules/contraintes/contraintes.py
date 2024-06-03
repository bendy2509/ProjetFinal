"""
Module définissant les contraintes pour les interactions utilisateur et les opérations du système.

Fonctions :
    - clear_screen : Efface l'écran de la console.
    - pause_system : Met le système en pause.
    - get_int_user : Demande à l'utilisateur une valeur entière valide.
    - check_building_name : Vérifie si le nom du bâtiment est valide.
    - validRoomFloor : Valide l'étage d'une salle.
    - validRoomNumber : Valide le numéro de la salle en fonction de l'étage.
    - is_valid_room_type : Vérifie si le type de salle est valide.
    - authenticate_admin : Authentifie un administrateur.
"""

import os
import re

def clear_screen():
    """Efface l'écran de la console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_system():
    """Met le système en pause en attendant une action de l'utilisateur."""
    os.system('pause' if os.name == 'nt' else input("\t" * 5 + "Appuyez sur Entrée pour continuer..."))

def is_valid_email(email):
    """
    Vérifie si l'email est valide.
    """
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    """
    Vérifie si le numéro de téléphone est valide selon les formats spécifiés.
    """
    patterns = [
        r"^\+509\d{4}-\d{2}-\d{2}$",
        r"^\+509\d{8}$",
        r"^\d{4}-\d{4}$",
        r"^\d{4}-\d{2}-\d{2}$",
        r"^\(509\)\d{4}-\d{4}$",
        r"^\(509\)\d{8}$",
    ]
    return any(re.match(pattern, phone) for pattern in patterns)

def is_valid_password(password):
    """
    Vérifie si le mot de passe est valide (au moins 8 caractères, une majuscule, une minuscule et un chiffre).
    """
    return len(password) >= 8 and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"[0-9]", password)

def get_validated_input(prompt, validation_func, error_message):
    """
    Demande une entrée utilisateur et valide cette entrée.
    """
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print(error_message)

def get_int_user(prompt):
    """
    Demande à l'utilisateur une valeur entière jusqu'à ce qu'une valeur valide soit entrée.

    :param prompt: Message à afficher pour demander l'entrée de l'utilisateur.
    :return: La valeur entière entrée par l'utilisateur.
    """
    while True:
        try:
            value = int(input("\t" * 5 + prompt))
            return value
        except ValueError:
            clear_screen()
            print("\t" * 5 + "Veuillez entrer un nombre entier valide.")
            pause_system()
            clear_screen()

def check_building_name(name):
    """
    Vérifie si le nom du bâtiment est valide.

    :param name: Nom du bâtiment à vérifier.
    :return: True si le nom est valide, False sinon.
    """
    valid_names = ["A", "B", "C", "D"]
    if name in valid_names:
        return True
    else:
        clear_screen()
        print("\t" * 5 + "Mauvais choix. Veuillez entrer A, B, C, D")
        pause_system()
        clear_screen()
        return False

def validRoomFloor(floor):
    """
    Valide l'étage d'une salle.

    :param floor: Numéro de l'étage à vérifier.
    :return: True si l'étage est valide (1, 2 ou 3), False sinon.
    """
    if 1 <= floor <= 3:
        return True
    clear_screen()
    print("\t" * 5 + "Mauvais choix. Veuillez entrer 1, 2 ou 3 pour l'étage.")
    pause_system()
    clear_screen()
    return False

def validRoomNumber(room_number, floor_number):
    """
    Valide le numéro de la salle en fonction de l'étage.

    :param room_number: Numéro de la salle à vérifier.
    :param floor_number: Numéro de l'étage associé.
    :return: True si le numéro de la salle est valide pour l'étage, False sinon.
    """
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
    print("\t" * 5 + "Vous devez choisir entre :")
    print("\t" * 5 + "Étage 1 : 101 à 106")
    print("\t" * 5 + "Étage 2 : 201 à 206")
    print("\t" * 5 + "Étage 3 : 301 à 306")
    pause_system()
    return False

def is_valid_room_type(room_type):
    """
    Vérifie si le type de salle est valide.

    :param room_type: Type de salle à vérifier.
    :return: True si le type de salle est valide, False sinon.
    """
    valid_room_types = ["salle de cours", "salle virtuelle", "labo"]
    if room_type.lower() not in valid_room_types:
        clear_screen()
        print("\t" * 5 + "Vous devez choisir entre 'salle de cours', 'salle virtuelle', 'labo'")
        pause_system()
        return False
    return True

def authenticate_admin(admin_manager):
    """
    Authentifie un administrateur en demandant les informations d'authentification.

    :param admin_manager: Instance de AdminManager pour vérifier les informations d'authentification.
    :return: True si l'authentification réussit, False sinon.
    """
    clear_screen()
    print("\t" * 5 + "Vous devez vous identifier !")
    admin_email = input("Email administrateur: ")
    admin_password = input("\t" * 5 + "Mot de passe : ")
    return admin_manager.authenticate_administrator(admin_email, admin_password)

def validate_phone_number(number):
    """Fonction test numero telephone"""
    if len(number) == 14 and number.startswith("(509)") and number[9] == "-":
        if number[5] in ["2", "3", "4", "5"]:
            return True
        else:
            clear_screen()
            print("Le chiffre après (509) doit être 2, 3, 4 ou 5. Veuillez réessayer...\n")
            pause_system()
            return False
    else:
        clear_screen()
        print("Format de numéro de téléphone invalide. Veuillez réessayer...\n")
        pause_system()
        return False

def is_valid_sexe(sexe):
    """Fonction test sexe"""
    list_valid = ["f", "F", "m", "M"]
    if sexe not in list_valid:
        os.system("cls")
        print("\nLe sexe doit etre f/F ou m/M. Veuillez réessayer...\n")
        return False
    return True

def is_empty(text):
    """Test champ vide"""
    if not text.strip():
        clear_screen()
        print("Ce champ ne peut etre vide. Veuillez réessayer...")
        pause_system()
        return False
    return True