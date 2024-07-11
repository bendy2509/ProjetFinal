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

from datetime import datetime
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
    expression = r"^((\+)|(011))?[\s-]?((509)|(\(509\)))?[\s-]?(3[1-9]|4[0-4]|4[6-9]|5[5])[\s-]?([0-9]{2})[\s-]?([0-9]{2})[\s-]?[0-9]{2}$"
    if not re.fullmatch(expression, phone):
        return False
    return True

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
    print("\t" * 4 + "Vous devez vous identifier !")
    admin_email = input("\t" * 5 + "Email administrateur: ")
    admin_password = input("\t" * 5 + "Mot de passe : ")
    return admin_manager.authenticate_administrator(admin_email, admin_password)

def is_valid_sexe(sexe):
    """Fonction test sexe"""
    list_valid = ["f", "F", "m", "M"]
    if sexe not in list_valid:
        clear_screen()
        print("\nLe sexe doit etre f/F ou m/M. Veuillez réessayer...\n")
        pause_system()
        return False
    return True

def saisir_nom_cours():
    """Saisit et valide le nom du cours."""
    while True:
        nom = input("Entrer le nom du cours (q pour quitter): ").strip()
        if nom == 'q':
            return None
        if nom and len(nom) >= 3:
            return nom.capitalize()
        print("Erreur : Le nom du cours ne peut pas être vide et doit contenir au moins 3 caractères.")

def saisir_faculte():
    while True:
        fac = input("Entrer la faculté pour laquelle vous enregistrez le cours (q pour quitter): ").strip()
        if fac == 'q':
            return None
        if fac and len(fac) >= 3:
            return fac.capitalize()
        print("Erreur : Le nom de la fac ne peut pas être vide et doit contenir au moins 3 caractères.")

def saisir_duration(message):
    """Saisit et valide une duration (entier entre 0 et 23)."""
    while True:
        try:
            duration = input(message).strip()
            if duration == 'q':
                return None
            duration = int(duration)
            if 1 <= duration <= 5:
                return duration
            print("Erreur : La durée doit être comprise entre 1 et 5.")
        except ValueError:
            print("Erreur : Veuillez entrer une valeur entière pour la durée.")

def saisir_debut(message):
    """Saisit et valide le début (entier entre 8 et 16)."""
    while True:
        try:
            duration = input(message).strip()
            if duration == 'q':
                return None
            duration = int(duration)

            if 8 <= duration <= 16:
                return duration
            
            print("Erreur : Le début doit être comprise entre 8h et 16h.")
        except ValueError:
            print("Erreur : Veuillez entrer une valeur entière pour le début.")

def saisir_session():
    """Saisit et valide la session (1 ou 2)."""
    while True:
        try:
            session = input("Session (1 ou 2, taper q pour quitter) : ").strip()
            if session == 'q':
                return None
            session = int(session)
            if session in [1, 2]:
                return session
            print("Erreur : La session doit être 1 ou 2.")
        except ValueError:
            print("Erreur : Veuillez entrer une valeur entière pour la session.")

def saisir_annee():
    """Saisit et valide l'année académique (entre 2000 et l'année actuelle)."""
    while True:
        try:
            annee = input("Année académique (q pour quitter): ").strip()
            if annee == 'q':
                return None
            annee = int(annee)
            current_year = datetime.now().year
            if annee >= current_year:
                return annee
            print(f"Erreur : L'année académique doit être plus grande ou égale à {current_year}.")
        except ValueError:
            print("Erreur : Veuillez entrer une valeur entière pour l'année académique.")

def saisir_jour():
    jours_valides = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    
    while True:
        jour = input("Jour (lundi, mardi, etc.) : ").strip().lower()
        if jour in jours_valides:
            return jour.lower()
        elif jour == 'q':
            return None
        else:
            print("Entrée invalide. Veuillez entrer un jour valide (lundi, mardi, etc.).")

def afficher_ligne(donnees, longueurs_colonnes, valeurs_vide=None):
    """
    Affiche une ligne des données formatée.
    
    :param donnees: Liste des valeurs à afficher.
    :param longueurs_colonnes: Liste des longueurs des colonnes pour l'alignement.
    :param valeurs_vide: Valeur à utiliser si une valeur est vide (optionnel).
    """
    valeurs_formatees = []
    for i, valeur in enumerate(donnees):
        if not valeur and valeurs_vide:
            valeur = valeurs_vide
        valeurs_formatees.append(f"{str(valeur):<{longueurs_colonnes[i]}}")
    print("\t" * 3, "| " + " | ".join(valeurs_formatees) + " |")

def afficher_affiches(data, valeur_vide="...."):
    """
    Affiche les informations dans le dictionnaire sous forme de tableau formaté.
    
    :param data: Liste de dictionnaires contenant les données.
    :param valeur_vide: Valeur à utiliser si une valeur est vide.
    """
    if not data:
        print("Aucune donnée à afficher.")
        return

    # Extraire les clés pour les utiliser comme en-têtes de colonnes
    headers = list(data[0].keys())
    
    # Calculer la largeur de chaque colonne pour un affichage aligné
    col_widths = [max(len(str(row[key])) for row in data) for key in headers]
    col_widths = [max(width, len(header)) for width, header in zip(col_widths, headers)]

    # Afficher l'en-tête du tableau
    header_row = "| " + " | ".join(f"{header:<{col_widths[i]}}" for i, header in enumerate(headers)) + " |"
    separator = "-" * len(header_row)
    
    print("\n")
    print("\t" * 3, separator)
    print("\t" * 3, header_row)
    print("\t" * 3, separator)
    
    # Afficher chaque ligne de données
    for row in data:
        afficher_ligne(list(row.values()), col_widths, valeur_vide)
        print("\t" * 3, separator)
