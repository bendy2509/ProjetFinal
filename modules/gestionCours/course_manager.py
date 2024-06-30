# menuCours.py
from modules.database.database import Database
from modules.gestionCours.cours import Course_Manager
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
    
    return input("\t" * 5 + "   Faites votre choix : ")
    
def menu_gestion_cours(db_file, invite):
    db = Database(db_file)
    course_Manager = Course_Manager(db_file)
    
    while True:
        choice = menu_cours()
        if choice == '1':
            if invite:
                course_Manager.enregistrer_cours()
            else:
                print("Accès refusé. Authentification requise.")
                pause_system()

        elif choice == '2':
            course_Manager.afficher_cours()

        elif choice == '0':
            break
        else:
            print("Erreur: Veuillez saisir un entier compris entre [0, 4]")
            pause_system()
