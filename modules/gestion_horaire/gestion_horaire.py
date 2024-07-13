"""Gestion Horaire"""

from modules.gestion_horaire.schedule_manager import Schedule_Manager
from modules.contraintes.contraintes import clear_screen, \
    get_int_user, pause_system, saisir_duration


def menu_horaires():
    """Affichage Menu Horaire"""
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
    print("\t" * 4 + "|                 Menu Horaires                   |")
    print("\t" * 4 + "|                                                 |")
    print("\t" * 4 + "===================================================")
    print("\t" * 4 + "|  1. Enregistrer une horaire(Admin)                     |")
    print("\t" * 4 + "|  2. Afficher l'horaire d'une salle              |")
    print("\t" * 4 + "|  3. Vérifier la disponibilité d'une salle       |")
    print("\t" * 4 + "|  0. Retour au menu principal                    |")
    print("\t" * 4 + "===================================================")
    return input("\t" * 5 + "   Faites votre choix : ")

def menu_gestion_horaires(db_file, invite):
    """Menu Gestion Horaires"""
    horaire_manager = Schedule_Manager(db_file)
    clear_screen()
    while True:
        choice = menu_horaires()
        if choice == '1':
            if invite:
                horaire_manager.ajouter_horaire()
            else:
                print("Accès interdit.")
                pause_system()

        elif choice == '2':
            code_salle = input("Entrez le numéro de la salle : ")
            horaire_manager.afficher_horaire(code_salle)

        elif choice == '3':
            salle = input("Entrez le numéro de la salle : ")
            jour = input("Jour (lundi, mardi, etc.) : ").lower()
            debut = saisir_duration("Durée du cours : ")
            fin = get_int_user("Heure de fin : ")
            disponible = horaire_manager.verifier_disponibilite(salle, jour, debut, fin)
            if disponible:
                print(f"La salle {salle} est disponible le {jour} de {debut}h à {fin}h.")
            else:
                print(f"La salle {salle} n'est pas disponible le {jour} de {debut}h à {fin}h.")
            pause_system()

        elif choice == '0':
            break
        else:
            print("Erreur: Veuillez saisir un entier compris entre [0, 3]")
            pause_system()
