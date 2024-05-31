"""   """
import sys
import os

from modules.contraintes.contraintes import clear_screen
from modules.gestionProfesseur.getInfosProfessors import Coordinates
from modules.gestionProfesseur.professors import *
from modules.database.database import Database

def menuProfessors():
    """ """
    print("\t" * 3, "*" * 68)
    print()
    print("\t" * 4 + "*" + "\t" + "1. Listez les professeurs.", "\t" * 3 + "*")
    print("\t" * 4 + "*" + "\t" + "2. Recherchez un professeur.", "\t" * 3 + "*")
    print("\t" * 4 + "*" + "\t" + "3. Enregistrez un Professeur (Admin).", "\t" * 2  + "*")
    print("\t" * 4 + "*" + "\t" + "4. Modifiez infos d'un Professeur (Admin).", "\t"   + "*")
    print("\t" * 4 + "*" + "\t" + "5. Suprimez un Professeur (Admin).", "\t" * 2  + "*")
    print("\t" * 4 + "*" + "\t" + "0. Tournez au menu principal.", "\t" * 3 + "*")
    print()
    print("\t" * 3, "*" * 68)

def menuChoice():
    """ """
    while True:
        clear_screen()
        menuProfessors()
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

        elif menuchoice == 2:
            clear_screen()
            isExist = data.read_records("professors")
            if len(isExist) == 0:
                print("\t" * 4, "Pas de professeurs dans la base !")
                pause_system()

            code = coordinates.validate_input(" le code  du Professeur")
            coordinates_find = data.read_records("professors", condition="code=?", params=(code,))
            if len(coordinates_find) > 0:
                # clear_screen()
                print("\n" * 2)
                print("\t" * 4, f"L'information du professeur avec code {code} : ")
                professor.format_coords(coordonates=coordinates_find)

                pause_system()

            else:
                clear_screen()
                print("\t" * 4, f"Pas de professeurs trouve avec le code '{code} ' dans la base !")
                pause_system()
 

        elif menuchoice == 3:
            professor.add_professor()

        elif menuchoice == 4:
            clear_screen()
            isExist = data.read_records("professors")
            if len(isExist) == 0:
                print("\t" * 4, "Pas de professeurs dans la base !")
                pause_system()
                continue

            code = Coordinates.validate_name("le code du Professeur")
            coordinates_find = data.read_records("professors", condition="code=?", params=(code,))
            if len(coordinates_find) > 0:
                clear_screen()
                print("\n")
                print("\t" * 4, f"L'information du professeur avec code {code} : ")
                professor.format_coords(coordonates=coordinates_find)
                print()
                print("\t" * 4, " SOS !!  Il est recommandé de ré-entrer tous les champs en entrant les mêmes infos si nécessaire : ")
                pause_system()
                params = Coordinates().get_coordinates()
                data.update_record(table="professors", values=params, condition="code = ?")
            else:
                clear_screen()
                print("\t" * 4, f"Pas de professeurs trouvés avec le code '{code}' dans la base !")
                pause_system()
            pause_system()
    
        elif menuchoice == 5:
            isExist = data.read_records("professors")
            if len(isExist) == 0:
                print("Pas de professeurs dans la base !")
                pause_system()

            professor.get_all_professors()
            code = Coordinates.validate_input("le code du professeur")
            coordinates_find = data.read_records("professors", condition="code=?", params=(code,))
            if len(coordinates_find) > 0:
                data.delete_record(table="professors", condition="code=?", params=(code,))
                print("\n")
                professor.get_all_professors()

            else:
                clear_screen()
                print("\t" * 4, f"Pas de professeurs trouve avec le code '{code} ' dans la base !")
                pause_system()

        else:
            clear_screen()
            break
            
        

