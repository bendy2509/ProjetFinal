
from modules.contraintes.contraintes import clear_screen, pause_system
from modules.administrateur.administrateur import AdministratorManager

def menuAdmin():
    clear_screen()
    print("===================================================")
    print("|      ____   _    _   ____    _                  |")
    print("|     / ___| | |  | | / ___|  | |                 |")
    print("|    | |     | |__| | | |     | |                 |")
    print("|    | |     |  __  | | |     | |                 |")
    print("|    | |___  | |  | | | |___  | |____             |")
    print("|    |_____| |_|  |_|  \____| |______|            |")
    print("|                                                 |")
    print("===================================================")
    print("|                                                 |")
    print("|           Menu Gestion Administrateurs          |")
    print("|                                                 |")
    print("===================================================")
    print("|                                                 |")
    print("|  1. Lister les administrateurs                  |")
    print("|  2. Ajouter un administrateur                   |")
    print("|  3. Supprimer un administrateur                 |")
    print("|  4. Retourner au menu principal                 |")
    print("|                                                 |")
    print("===================================================")
    choice = input("Choisissez une option: ")
    return choice

def menu_gestion_administrateurs(DB_FILE):
    admin_manager = AdministratorManager(DB_FILE)

    while True:
        clear_screen()
        choice = menuAdmin()

        if choice == '1':
            admin_manager.list_administrators()
        elif choice == '2':
            # Demander les informations nécessaires pour ajouter un administrateur
            first_name = input("Prénom : ")
            last_name = input("Nom : ")
            email = input("Email : ")
            password = input("Mot de passe : ")
            admin_manager.add_administrator(first_name, last_name, email, password)
            pause_system()
        elif choice == '3':
            email = input("Entrez l'email de l'administrateur à supprimer : ")
            admin_manager.delete_administrator(email)
            pause_system()
        elif choice == '4':
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 4. Réessayez !!")
            pause_system()
