"""   """


from modules.gestionProfesseur.professors import( 
    is_exist_record, Coordinates, modify_professor, Professor
)
from modules.database.database import Database
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionBatiment.buildings_manager import Building, BuildingManager
from modules.contraintes.contraintes import (
    clear_screen, pause_system, afficher_affiches
)


def menuProfessors():
    """ """
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
    print("|        Menu Gestion Professeur                  |")
    print("|                                                 |")
    print("===================================================")
    print("|  1. Enregistrez un Professeur (Admin)           |")
    print("|  2. Listez les professeurs                      |")
    print("|  3. Recherchez un professeur                    |")
    print("|  4. Modifiez infos d'un Professeur (Admin)      |")
    print("|  5. Suprimez un Professeur (Admin)              |")
    print("|  0. Tournez au menu principal                   |")
    print("===================================================")

def menuChoice():
    """ """
    while True:
        clear_screen()
        menuProfessors()
        try :
            admin_choice = int(input("\tFaites votre choix : "))
            if 0 <= admin_choice <= 5:
                return admin_choice

            clear_screen()
            print()
            print("\tVeillez Saisir un entier compris entre [0, 5]")
            pause_system()

        except ValueError:
            clear_screen()
            print()
            print("\t"  + f"Erreur: Veillez Saisir un entier compris entre [0, 5] ")
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
                print("\n")          
                print("\t" * 5,"Accès reservé aux Administrateurs.")
                pause_system()
  
        elif menuchoice == 2:
            print("\n")
            print("\t" * 4, "=-===========Les professeurs du systeme===========-=")
            professor.get_all_professors()

        elif menuchoice == 3:
            clear_screen()
            isExist = is_exist_record()
            if isExist :
                print()
                code = coordinates.validate_input(" le code  du Professeur")
                
                coordinates_find = data.read_records("professors", condition="code=?", params=(code,))
                if len(coordinates_find) > 0:
                    clear_screen()
                    data = []
                    data.append(
                        {"CODE": coordinates_find[0][0], "NOM": coordinates_find[0][1],"PRENOM": coordinates_find[0][2], "SEXE": coordinates_find[0][3], "EMAIL": coordinates_find[0][4], "TELEPHONE": coordinates_find[0][5], "CODE_COURS": coordinates_find[0][6]}
                    )
                    print("\n" * 2)
                    print("\t" * 4, f"=-===========L'information du professeur avec code ' {code} ' :===========-=")
                    afficher_affiches(data=data, valeur_vide="...")
                    pause_system()
                else:
                    clear_screen()
                    print()
                    print("\t", f"Pas de professeurs trouve avec le code ' {code} ' dans la base !")
                    pause_system()
            else:
                clear_screen()
                print()
                print("\t", "Pas de professeurs dans la base !")
                pause_system()

        elif menuchoice == 4:
            if is_authenticated:
                clear_screen()
                isExist = is_exist_record()
                if isExist :
                    print("\n\t=-=========== Session de modification des Professeurs.===========-=\n")

                    print()
                    modify_professor()

                else:
                    clear_screen()
                    print()
                    print("\t", "Pas de professeurs dans la base !")
                    pause_system()
                
            else:
                clear_screen()
                print()          
                print("\t","Accès reservé aux Administrateurs.")
                pause_system()

        elif menuchoice == 5:
            if is_authenticated:
                isExist = is_exist_record()
                if isExist:

                    print("\t" * 4, "=-===========Les professeurs du systeme===========-=")
                    professor.get_all_professors()
                    code = input("le code du Professeur :  ")
                    coordinates_find = data.read_records("professors", condition="code=?", params=(code,))

                    if len(coordinates_find) > 0:
                        data.delete_record(table="professors", condition="code=?", params=(code,))
                        print("\n")
                        print("\t" * 4, "=-===========Les professeurs du systeme après suppression===========-=")
                        professor.get_all_professors()
                        data.delete_record(table="cours", condition="teacher_code=?", params=(code,))
 
                    else:
                        clear_screen()
                        print("\t", f"Pas de professeurs trouve avec le code '{code} ' dans la base !")
                        pause_system()

                else:
                    clear_screen()
                    print("\t", "Pas de professeurs dans la base !")
                    pause_system()

            else:
                clear_screen()            
                print("\t","Accès reservé aux Administrateurs.")
                pause_system()

        else:
            clear_screen()
            break
