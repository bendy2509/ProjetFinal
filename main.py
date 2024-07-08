# import os

# Ajouter le chemin du projet au sys.path
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

""" 
Importation des modules 

"""
from modules.gestion_horaire.gestion_horaire import menu_gestion_horaires
from modules.database.database import Database
from modules.administrateur.gestionAdministrateur import menu_gestion_administrateurs
from modules.gestionSalle.gestionSalle import menuGestionSalle
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionBatiment.gestion_batiment import menu_gestion_batiment
from modules.gestionProfesseur.menuProfessors import menuGestionProfesseur
from modules.gestionCours.course_manager import menu_gestion_cours
from modules.contraintes.contraintes import (
    authenticate_admin,
    clear_screen, 
    get_validated_input,is_valid_email,
    is_valid_password,
    is_valid_phone, pause_system
)

def create_account(admin_manager):
    clear_screen()
    first_name = input("Prénom : ")
    last_name = input("Nom : ")
    address = input("Adresse : ")
    phone = get_validated_input("Téléphone : ", is_valid_phone, "Numéro de téléphone invalide. Veuillez réessayer.")
    email = get_validated_input("Email : ", is_valid_email, "Email invalide. Veuillez réessayer.")
    password = get_validated_input("Mot de passe : ", is_valid_password, "Mot de passe invalide. Il doit contenir au moins 8 caractères, une majuscule, une minuscule et un chiffre.")
    admin_manager.add_administrator(first_name, last_name, address, phone, email, password)

    return


def display_main_menu():
    """
    Affiche le menu principal
    
    """
    clear_screen()
    print("===================================================")
    print("|      ____   _    _   ____    _                  |")
    print("|     / ___| | |  | | / ___|  | |                 |")
    print("|    | |     | |__| | | |     | |                 |")
    print("|    | |     |  __  | | |     | |                 |")
    print("|    | |___  | |  | | | |___  | |____             |")
    print("|    |_____| |_|  |_|  \\____| |______|            |")
    print("|                                                 |")
    print("|                      DSI-CHCL                   |")
    print("===================================================")
    print("|                                                 |")
    print("|                 Menu Principal                  |")
    print("|                                                 |")
    print("===================================================")
    print("|  1. Gestion des cours                           |")
    print("|  2. Gestion des Salles                          |")
    print("|  3. Gestion des Bâtiments                       |")
    print("|  4. Gestion des Professeurs                     |")
    print("|  5. Gestion des Administrateurs                 |")
    print("|  6. Pour tester avant (Pas encore terminé)      |")
    print("|  0. Retour au menu de configuration             |")
    print("===================================================")

def handle_main_menu_choice(choice, db_file, invite):
    """Gère les choix du menu principal."""
    if choice == '1':
        menu_gestion_cours(db_file, invite)
    elif choice == '2':
        menuGestionSalle(db_file, invite)
    if choice == '3':
        menu_gestion_batiment(db_file, invite)
    elif choice == '4':
        menuGestionProfesseur(db_file)
    elif choice == '5':
        if invite:
            menu_gestion_administrateurs(db_file)
        else:
            print("Accès interdit !! Veuillez connecter en tant qu'Administrateur.")
            pause_system()
    elif choice == '6':
        menu_gestion_horaires(db_file, invite)
    elif choice == '0':
        print("Au revoir!")
        return False
    else:
        print("Choix invalide. Veuillez saisir un nombre entre 1 et 6.")
        pause_system()
    return True

def main_menu(db_file, invite=True):
    """Affiche le menu principal et gère la navigation."""
    while True:
        display_main_menu()
        choice = input("Choisissez une option (1-5) : ")
        if not handle_main_menu_choice(choice, db_file, invite):
            break

def display_initial_menu():
    """Affiche le menu de démarrage."""
    clear_screen()
    print("===================================================")
    print("|      ____   _    _   ____    _                  |")
    print("|     / ___| | |  | | / ___|  | |                 |")
    print("|    | |     | |__| | | |     | |                 |")
    print("|    | |     |  __  | | |     | |                 |")
    print("|    | |___  | |  | | | |___  | |____             |")
    print("|    |_____| |_|  |_|  \\____| |______|           |")
    print("|                                                 |")
    print("|                      DSI-CHCL                   |")
    print("===================================================")
    print("|                                                 |")
    print("|                 Menu de configuration           |")
    print("|                                                 |")
    print("===================================================")
    print("|  1. Connecter en tant qu'Administrateur         |")
    print("|  2. Créer un compte Administrateur              |")
    print("|  3. Connecter en tant qu'invité                 |")
    print("|  4. Quitter                                     |")
    print("===================================================")

def handle_initial_menu_choice(choice, db_file, admin_manager):
    database = Database(db_file)
    clear_screen()
    """Gère les choix du menu de démarrage."""
    if choice == '1':
        email = input("Email : ")
        password = input("Mot de passe : ")
        if admin_manager.authenticate_administrator(email, password):
            print("Connexion réussie.")
            pause_system()
            main_menu(db_file, True)
        else:
            print("Échec de la connexion. Vérifiez vos identifiants.")
            pause_system()
    elif choice == '2':
        administrators = database.read_records("administrators")
        if len(administrators) == 0:
            create_account(admin_manager)
        else:
            if authenticate_admin(admin_manager):
                print("Authentification réussie...")
                pause_system()
                create_account(admin_manager)
                
            print("Authentification échouée. Vous ne pouvez pas créer de compte.")
    elif choice == '3':
        print("Connecté en tant qu'invité.")
        pause_system()
        main_menu(db_file, True)
    elif choice == '4':
        print("Au revoir!")
        return False
    else:
        print("Choix invalide. Veuillez saisir un nombre entre 1 et 4.")
        pause_system()
    return True

def initial_menu(db_file):
    """Affiche le menu de démarrage et gère la navigation."""
    admin_manager = AdministratorManager(db_file)
    while True:
        display_initial_menu()
        choice = input("Choisissez une option (1-4) : ")
        if not handle_initial_menu_choice(choice, db_file, admin_manager):
            break

if __name__ == "__main__":
    DB_FILE = "database.db"
    initial_menu(DB_FILE)
