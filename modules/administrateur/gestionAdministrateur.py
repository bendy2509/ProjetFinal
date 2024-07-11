
from modules.contraintes.contraintes import clear_screen, get_validated_input, is_valid_email, is_valid_password, is_valid_phone, pause_system
from modules.administrateur.administrateur import AdministratorManager

def create_account(admin_manager):
    """
    Crée un compte administrateur en demandant les informations nécessaires à l'utilisateur.
    """
    first_name = input("Prénom : ")
    last_name = input("Nom : ")
    address = input("Adresse : ")
    phone = get_validated_input("Téléphone : ", is_valid_phone, "Numéro de téléphone invalide. Veuillez réessayer.")
    email = get_validated_input("Email : ", is_valid_email, "Email invalide. Veuillez réessayer.")
    password = get_validated_input("Mot de passe : ", is_valid_password, "Mot de passe invalide. \
                                   Il doit contenir au moins 8 caractères, une majuscule, une minuscule et un chiffre.")
    
    admin_manager.add_administrator(first_name, last_name, address, phone, email, password)

def menuAdmin():
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
    print("|           Menu Gestion Administrateurs          |")
    print("|                                                 |")
    print("===================================================")
    print("|                                                 |")
    print("|  1. Ajouter un administrateur                   |")
    print("|  2. Lister les administrateurs                  |")
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
            create_account(admin_manager)
        elif choice == '2':
            admin_manager.list_administrators()
        elif choice == '3':
            email = input("Entrez l'email de l'administrateur à supprimer : ")
            admin_manager.delete_administrator(email)
            pause_system()
        elif choice == '4':
            break
        else:
            print("Choix invalide. Veuillez saisir un nombre entre 1 et 4. Réessayez !!")
            pause_system()
