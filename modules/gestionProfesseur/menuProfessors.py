"""Menu Gestion Professeur """


from modules.gestionProfesseur.professors import( 
    is_exist_record, Coordinates, modify_professor, Professor
)
from modules.database.database import Database
from modules.administrateur.administrateur import AdministratorManager
from modules.contraintes.contraintes import (
    pause_system, afficher_affiches,
    header_design, pause_system
)



def menuProfessors():
    """Menu professeur """
    print("\n")
    header_design()
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
    """Menu Choix d'option de l'utilisateur """
    while True:
        print("\n")
        menuProfessors()
        try :
            admin_choice = int(input("\tFaites votre choix : "))
            if 0 <= admin_choice <= 5:
                return admin_choice

            print()
            print("Veillez Saisir un entier compris entre [0, 5]")
            pause_system()

        except ValueError:
            print()          
            print("Erreur: Veillez Saisir un entier compris entre [0, 5] ")
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
                print("Accès reservé aux Administrateurs.")
                pause_system()

        elif menuchoice == 2:
            print("\n")
            print("\t" * 4, "=-===========Les professeurs du systeme===========-=")
            professor.get_all_professors()

        elif menuchoice == 3:
            print("\n")
            is_exist = is_exist_record()
            if is_exist :
                print()
                first_name = input(" le prenom  du Professeur :  ")

                coordinates_find = data.read_records("professors", \
                                                     condition="prenom=?", \
                                                        params=(first_name,))
                if len(coordinates_find) > 0:
                    print("\n")
                    data = []
                    data.append(
                        {"CODE": coordinates_find[0][0], "NOM": coordinates_find[0][1],\
                         "PRENOM": coordinates_find[0][2], "SEXE": coordinates_find[0][3], \
                            "EMAIL": coordinates_find[0][4], "TELEPHONE": coordinates_find[0][5], \
                                "CODE_COURS": coordinates_find[0][6]}
                    )
                    print("\n" * 2)
                    print("\t" * 4, f"=-===========L'information du professeur avec code ' {first_name} ' :===========-=")
                    afficher_affiches(data=data, valeur_vide="...")
                    pause_system()
                else:
                    print()
                    print(f"Pas de professeurs trouve avec le code ' {first_name} ' dans la base !")
                    pause_system()
            else:
                print()
                print("Pas de professeurs dans la base !")
                pause_system()

        elif menuchoice == 4:
            if is_authenticated:
                print("\n")
                is_exist = is_exist_record()
                if is_exist :
                    print("\n\t=-=========== Session de modification des Professeurs.===========-=\n")

                    print()
                    modify_professor()

                else:
                    print()
                    print("Pas de professeurs dans la base !")
                    pause_system()

            else:
                print()
                print("Accès reservé aux Administrateurs.")
                pause_system()

        elif menuchoice == 5:
            if is_authenticated:
                is_exist = is_exist_record()
                if is_exist:

                    print("\t" * 4, "=-===========La session de suppresion===========-=")
                    print("\n")
                    print("\t" * 4, "=-===========Les professeurs du systeme===========-=")
                    professor.get_all_professors()
                    code = input("le code du Professeur :  ")
                    coordinates_find = data.read_records("professors", condition="code=?", params=(code,))

                    if len(coordinates_find) > 0:
                        data.delete_record(table="professors", \
                                           condition="code=?", \
                                            params=(code,))
                        print("\n")
                        print("\t" * 4, "=-===========Les professeurs du systeme après suppression===========-=")
                        professor.get_all_professors()
                        data.delete_record(table="cours", \
                                           condition="teacher_code=?", \
                                            params=(code,))

                    else:
                        print()
                        print(f"Pas de professeurs trouve avec le code '{code} ' dans la base !")
                        pause_system()

                else:
                    print()
                    print("Pas de professeurs dans la base !")
                    pause_system()

            else:
                print()
                print("Accès reservé aux Administrateurs.")
                pause_system()

        else:
            print("\n")
            break
