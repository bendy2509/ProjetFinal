#import os

# Ajouter le chemin du projet au sys.path
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
""" 
Importation des modules 

"""
from modules.gestion_horaire.gestion_horaire import menu_gestion_horaires
from modules.administrateur.gestionAdministrateur \
    import create_account, menu_gestion_administrateurs
from modules.gestionSalle.gestionSalle import menuGestionSalle
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionBatiment.gestion_batiment import menu_gestion_batiment
from modules.gestionProfesseur.menuProfessors import menuGestionProfesseur
from modules.gestionCours.menu_gestion_cours import menu_gestion_cours
from modules.contraintes.contraintes import (
    clear_screen, header_design, pause_system
)

def display_main_menu():
    """
    Affiche le menu principal
    
    """
    clear_screen()
    header_design()
    print("===================================================")
    print("|                                                 |")
    print("|                 Menu Principal                  |")
    print("|                                                 |")
    print("===================================================")
    print("|  1. Gestion des Bâtiments                       |")
    print("|  2. Gestion des Salles                          |")
    print("|  3. Gestion des cours                           |")
    print("|  4. Gestion des Professeurs                     |")
    print("|  5. Gestion des Administrateurs                 |")
    print("|  6. Gestion des horaires                        |")
    print("|  0. Retour au menu de configuration             |")
    print("===================================================")

def main_menu(db_file, invite=True):
    """Affiche le menu principal et gère la navigation."""
    while True:
        display_main_menu()
        choice = input("Choisissez une option (0-6) : ")
        if choice == '1':
            menu_gestion_batiment(db_file, invite)
        elif choice == '2':
            menuGestionSalle(db_file, invite)
        elif choice == '3':
            menu_gestion_cours(db_file, invite)
        elif choice == '4':
            menuGestionProfesseur(db_file, invite)
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
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 6.")
            pause_system()

def display_initial_menu():
    """Affiche le menu de démarrage."""
    clear_screen()
    header_design()
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
    """Gère les choix du menu de démarrage."""
    if choice == '1':
        email = input("Entrer l'email de l'administrateur : ")
        password = input("Entrer le mot de passe de l'administrateur : ")
        
        if admin_manager.authenticate_administrator(email, password):
            print("Connexion réussie.")
            pause_system()
            main_menu(db_file, True)
        else:
            print("Échec de la connexion. Vérifiez vos identifiants.")
            pause_system()
    elif choice == '2':
        create_account(admin_manager, db_file)
    elif choice == '3':
        print("Connecté en tant qu'invité.")
        pause_system()
        main_menu(db_file, False)
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
