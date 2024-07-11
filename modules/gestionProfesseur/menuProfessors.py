"""   """

from modules.gestionProfesseur.getInfosProfessors import Coordinates
from modules.gestionProfesseur.professors import *
from modules.database.database import Database
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionBatiment.buildings_manager import Building, BuildingManager
from modules.contraintes.contraintes import (
    authenticate_admin, clear_screen, pause_system
)


def menuProfessors():
    """ """
    clear_screen()
    print("\t" * 4 + "===================================================")
    print("\t" * 4 + "|      ____   _    _   ____    _                  |")
    print("\t" * 4 + "|     / ___| | |  | | / ___|  | |                 |")
    print("\t" * 4 + "|    | |     | |__| | | |     | |                 |")
    print("\t" * 4 + "|    | |     |  __  | | |     | |                 |")
    print("\t" * 4 + "|    | |___  | |  | | | |___  | |____             |")
    print("\t" * 4 + "|    |_____| |_|  |_|  \____| |______|            |")
    print("\t" * 4 + "|                                                 |")
    print("\t" * 4 + "===================================================")
    print("\t" * 4 + "|                                                 |")
    print("\t" * 4 + "|        Menu Gestion Professeur                  |")
    print("\t" * 4 + "|                                                 |")
    print("\t" * 4 + "===================================================")
    print("\t" * 4 + "|  1. Enregistrez un Professeur (Admin)           |")
    print("\t" * 4 + "|  2. Listez les professeurs                      |")
    print("\t" * 4 + "|  3. Recherchez un professeur                    |")
    print("\t" * 4 + "|  4. Modifiez infos d'un Professeur (Admin)      |")
    print("\t" * 4 + "|  5. Suprimez un Professeur (Admin)              |")
    print("\t" * 4 + "|  0. Tournez au menu principal                   |")
    print("\t" * 4 + "===================================================")

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

def is_exist_record():
    """function to verify exist record"""
    isExist = data.read_records("professors")
    if len(isExist) == 0:
        return False
    
    return True

def modify_professor():
    """function for modify professors"""

    code = Coordinates.validate_name("le code du Professeur")
    coordinates_find = data.read_records("professors", condition="code=?", params=(code,))
    if len(coordinates_find) > 0:
        clear_screen()
        print("\n")
        print("\t" * 4, f"L'information du professeur avec code {code} : ")
        
        data = []
        data.append(
            {"CODE": coordinates_find[0], "NOM": coordinates_find[1],"PRENOM": coordinates_find[2], "SEXE": coordinates_find[3], "EMAIL": coordinates_find[4], "TELEPHONE": coordinates_find[5], "CODE_COURS": coordinates_find[6]}
        )
        afficher_affiches(data=data, valeur_vide="...")
        print("\n", "\t" * 4, " SOS !!  Il est recommandé de ré-entrer tous les champs en entrant les mêmes infos si nécessaire : ")
        pause_system()
        params = Coordinates().get_coordinates()
        data.update_record(table="professors", values=params, condition="code=?", condition_params=(code,))

    else:
        clear_screen()
        print("\t" * 4, f"Pas de professeurs trouvés avec le code '{code}' dans la base !")
        pause_system()


def menuGestionProfesseur(DB_FILE, access):
    """Fonction principale pour démarrer le programme."""

    global professor, coordinates,data,admin_manager,is_authenticated
    professor = Professor(DB_FILE)
    coordinates = Coordinates()
    data = Database(DB_FILE)
    admin_manager = AdministratorManager(DB_FILE)
    is_authenticated = access

    while True:
        menuchoice = menuChoice()

        if menuchoice == 1:
            if is_authenticated:
                professor.add_professor()

            else:
                clear_screen()            
                print("\t" * 5,"Accès reservé aux Administrateurs.")
                pause_system()
  
        elif menuchoice == 2:
            professor.get_all_professors()

        elif menuchoice == 3:
            clear_screen()
            isExist = is_exist_record()
            if isExist :
                code = coordinates.validate_input(" le code  du Professeur")
                
                coordinates_find = data.read_records("professors", condition="code=?", params=(code,))
                if len(coordinates_find) > 0:
                    clear_screen()
                    print("\n" * 2)
                    print("\t" * 4, f"L'information du professeur avec code ' {code} ' : ")
                    data = []
                    data.append(
                        {"CODE": coordinates_find[0], "NOM": coordinates_find[1],"PRENOM": coordinates_find[2], "SEXE": coordinates_find[3], "EMAIL": coordinates_find[4], "TELEPHONE": coordinates_find[5], "CODE_COURS": coordinates_find[6]}
                    )
                    afficher_affiches(data=data, valeur_vide="...")
                    pause_system()
                else:
                    clear_screen()
                    print("\t" * 4, f"Pas de professeurs trouve avec le code ' {code} ' dans la base !")
                    pause_system()
            else:
                clear_screen()
                print("\t" * 4, "Pas de professeurs dans la base !")
                pause_system()

        elif menuchoice == 4:
            if is_authenticated:
                clear_screen()
                isExist = is_exist_record()
                if isExist :
                    modify_professor()

                else:
                    clear_screen()
                    print("\t" * 4, "Pas de professeurs dans la base !")
                    pause_system()
                
            else:
                clear_screen()            
                print("\t" * 5,"Accès reservé aux Administrateurs.")
                pause_system()

        elif menuchoice == 5:
            if is_authenticated:
                isExist = is_exist_record()
                if isExist:

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
                    print("\t" * 4, "Pas de professeurs dans la base !")
                    pause_system()

            else:
                clear_screen()            
                print("\t" * 5,"Accès reservé aux Administrateurs.")
                pause_system()

        else:
            clear_screen()
            break

