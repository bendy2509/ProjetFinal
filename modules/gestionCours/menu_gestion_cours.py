# menuCours.py
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
    print("\t" * 4 + "|    |_____| |_|  |_|  \\____| |______|            |")
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
    print("\t" * 4 + "|  5. Assigner un professeur à un cours (Admin)   |")
    print("\t" * 4 + "|  6. Filtrer par les cours ayant des proffesseurs|")
    print("\t" * 4 + "|  7. Filtrer par les cours qui n'ont pas de prof |")
    print("\t" * 4 + "|  0. Retour au menu principal                    |")
    print("\t" * 4 + "===================================================")
    
    return input("\t" * 5 + "   Faites votre choix : ")

def menu_ajouter_professeur_au_cours(course_manager):
    clear_screen()
    print("\n", "*" * 10 , "Ajouter Professeur au Cours" , "*" * 10 ,"\n")

    code_cours = input("Entrer le code du cours : ")
    code_professeur = input("Entrer le code du professeur : ")

    course_manager.ajouter_professeur_au_cours(code_cours, code_professeur)
    pause_system()

def menu_gestion_cours(db_file, invite):
    # db = Database(db_file)
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

        elif choice == '3':
            if invite:
                course_Manager.modifier_cours()
            else:
                print("Accès refusé. Authentification requise.")
                pause_system()

        elif choice == '4':
            course_Manager.rechercher_cours()
        elif choice == '5':
            if invite:
                menu_ajouter_professeur_au_cours(course_Manager)
            else:
                print("Accès refusé. Authentification requise.")
                pause_system()
        elif choice == '6':
            course_Manager.cours_assignes_ou_non(assigner=True)            

        elif choice == '7':
            course_Manager.cours_assignes_ou_non(assigner=False)

        elif choice == '0':
            break
        else:
            print("Erreur: Veuillez saisir un entier compris entre 0 et 7")
            pause_system()
