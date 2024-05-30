"""   """
import sys
import os

from modules.contraintes.contraintes import clear_screen
from modules.gestionProfesseur.getInfos import Coordinates
from modules.gestionProfesseur.createData import *
from modules.database.database import Database
from modules.gestionProfesseur import menu

def menu():
    """ """
    print("\t" * 3, "*" * 68)
    print()
    print("\t" * 4 + "*" + "\t" + "1. Lister les professeurs.", "\t" * 3 + "*")
    print("\t" * 4 + "*" + "\t" + "2. Rechercher un professeur.", "\t" * 3 + "*")
    print("\t" * 4 + "*" + "\t" + "3. Enregistrer un Professeur (Admin)", "\t" * 2  + "*")
    print("\t" * 4 + "*" + "\t" + "4. Modifier infos d'un Professeur(Admin).", "\t"   + "*")
    print("\t" * 4 + "*" + "\t" + "5. Suprimer un Professeur(Admin).", "\t" * 2  + "*")
    print("\t" * 4 + "*" + "\t" + "0. Tourner au menu principal.", "\t" * 3 + "*")
    print()
    print("\t" * 3, "*" * 68)

def menuChoice():
    """ """
    while True:
        clear_screen()
        menu()
        try :
            admin_choice = int(input("\t" * 5 + "   Faites votre choix : "))
            if 0 <= admin_choice <= 5:
                return admin_choice

            clear_screen()
            print()
            print("\t" * 5 + "Veillez Saisir un entier compris entre [0, 5]")
            pause_system()

        except ValueError:
            clear_screen()
            print()
            print("\t" * 5 + f"Erreur: Veillez Saisir un entier compris entre [0, 5] ")
            pause_system()          


def menuGestionProfesseur(DB_FILE):
    """ """
    professor = Professor(DB_FILE)
    coordinates = Coordinates()
    data = Database(DB_FILE)

    while True:
        menuchoice = menuChoice()
        if menuchoice == 1:
            professor.get_all_professors()
            print()

        elif menuchoice == 2:
            clear_screen()
            isExist = data.read_records("professors")
            if len(isExist) > 0:
                code = coordinates.validate_input("code cours")
                isExist = data.read_records("professors",columns=['code'], condition="code=?", params=(code,))
                clear_screen()
                print("\n" * 2)
                print("\t" * 4, f"L'information du prefesseur avec code {code} : ")
                professor.format_coords(coordonates=isExist)
                print()
                pause_system()

            print("Pas de professeurs dans la base !")
            pause_system()
            
            pass

        elif menuchoice == 3:
            professor.add_professor(coordinates=coordinates)

        elif menuchoice == 4:
            pass

        elif menuchoice == 5:
            isExist = data.read_records("professors")
            if len(isExist) > 0:
                code = Coordinates.validate_input("code cours")
                professor.delete_professor(code)
                professor.get_all_professors()
                print()

            print("Pas de professeurs dans la base !")
            pause_system()

        else:
            break
            clear_screen()
            
        

