# menuCours.py
from modules.database.database import Database
from modules.gestionCours.cours import Manager
from modules.contraintes.contraintes import clear_screen, pause_system, authenticate_admin

def menu_cours():
    clear_screen()
    print("\t" * 4 + "===================================================")
    print("\t" * 4 + "|      ____   _    _   ____    _                  |")
    print("\t" * 4 + "|     / ___| | |  | | / ___|  | |                 |")
    print("\t" * 4 + "|    | |     | |__| | | |     | |                 |")
    print("\t" * 4 + "|    | |     |  __  | | |     | |                 |")
    print("\t" * 4 + "|    | |___  | |  | | | |___  | |____             |")
    print("\t" * 4 + "|    |_____| |_|  |_|  \\____| |______|           |")
    print("\t" * 4 + "|                                                 |")
    print("\t" * 4 + "===================================================")
    print("\t" * 4 + "|                                                 |")
    print("\t" * 4 + "|                Menu Gestion Cours               |")
    print("\t" * 4 + "|                                                 |")
    print("\t" * 4 + "===================================================")
    print("\t" * 4 + "|  1. Enregistrer un cours (Admin)                |")
    print("\t" * 4 + "|  2. Lister les cours                            |")
    print("\t" * 4 + "|  3. Modifier un cours (Admin)                   |")
    print("\t" * 4 + "|  4. Rechercher un cours                         |")
    print("\t" * 4 + "|  0. Retour au menu principal                    |")
    print("\t" * 4 + "===================================================")

def menu_gestion_cours():
    db = Database("gestion_cours.db")
    manager = Manager(db)
    
    while True:
        clear_screen()
        menu_cours()
        try:
            admin_choice = int(input("\t" * 5 + "   Faites votre choix : "))
            if admin_choice == 1:
                if authenticate_admin():
                    manager.enregistrer_cours()
                else:
                    print("Authentification échouée.")
                    pause_system()
            elif admin_choice == 2:
                manager.afficher_cours()
                pause_system()
            elif admin_choice == 3:
                if authenticate_admin():
                    manager.modifier_cours()
                else:
                    print("Authentification échouée.")
                    pause_system()
            elif admin_choice == 4:
                manager.rechercher_cours()
                pause_system()
            elif admin_choice == 0:
                break
            else:
                print("Option invalide. Veuillez réessayer.")
                pause_system()
        except ValueError:
            clear_screen()
            print("\t" * 5 + "Erreur: Veuillez saisir un entier compris entre [0, 5]")
            pause_system()

if __name__ == "__main__":
    menu_gestion_cours()
