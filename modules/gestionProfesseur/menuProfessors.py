"""   """

from modules.gestionProfesseur.getInfosProfessors import Coordinates
from modules.gestionProfesseur.professors import *
from modules.database.database import Database
from modules.administrateur.administrateur import AdministratorManager
from modules.gestionBatiment.buildings_manager import Building, BuildingManager
from modules.contraintes.contraintes import (
    authenticate_admin, clear_screen, pause_system,is_valid_email
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

def is_exist_record():
    """function to verify exist record"""
    isExist = data.read_records("professors")
    if len(isExist) == 0:
        return None
    
    return isExist
    
def valide_coordinates_modify(code):
    """
    Valide et modifie les coordonnées d'un professeur.

    :param code: Code du professeur à modifier
    :return: Dictionnaire des coordonnées mises à jour
    """
    coordinates_find = data.read_records("professors", condition="code=?", params=(code,))

    def get_valid_name(field_name, current_value):
        """
        Valide que le nom/prénom commence par une lettre. Utilise la valeur actuelle si l'entrée est vide.

        :param field_name: Nom du champ (nom ou prénom)
        :param current_value: Valeur actuelle du champ
        :return: Nouvelle valeur validée du champ ou valeur actuelle si l'entrée est vide
        """
        while True:
            print("\n")
            value = input("\t" + f"Entrez le {field_name} : ").strip()
            if not value:
                return current_value
            if value[:1].isalpha():
                return value
            print("\t", f"{field_name.capitalize()} devrait commencer par une lettre.")
            pause_system()

    def get_unique_value(field_name, current_value, index):
        """
        Valide que le téléphone ou l'email est unique dans la base de données, sauf s'il est inchangé.

        :param field_name: Nom du champ (phone ou email)
        :param current_value: Valeur actuelle du champ
        :param index: Index du champ dans les enregistrements de la base de données
        :return: Nouvelle valeur validée du champ ou valeur actuelle si l'entrée est inchangée
        """
        while True:
            print("\n")
            value = getattr(Coordinates, f"validate_{field_name}")()
            if value == current_value:
                return value
            all_professors = data.read_records("professors")
            if any(items[index] == value for items in all_professors):
                print("\n")
                print("\t", f"Ce {field_name} est déjà attribué à un professeur.")
                pause_system()
            else:
                return value

    def get_valid_course_code():
        """
        Valide que le code du cours existe et n'est pas déjà attribué à un autre professeur.

        :return: Code du cours validé
        """
        while True:
            print("\n")
            course_code = input("\t" + "Entrez le code du cours ou taper 'quit' pour quiter la modification : ").strip()
            if course_code.lower() == 'quit':
                break

            if not data.read_records("cours", condition="code_cours=?", params=(course_code,)):
                print("\tCode cours non trouvé.")
                pause_system()
                continue
            if course_code != coordinates_find[0][6]:
                print("\n")
                if data.read_records("professors", condition="codeCours=?", params=(course_code,)):
                    print("\t", "Un professeur est déjà assigné à ce cours.")
                    pause_system()
                    continue
            return course_code

    # Validation et modification des coordonnées du professeur
    nom = get_valid_name("nom", coordinates_find[0][1])
    prenom = get_valid_name("prénom", coordinates_find[0][2])
    gender = Coordinates.validate_gender()
    phone = get_unique_value("phone", coordinates_find[0][5], 5)
    email = get_unique_value("email", coordinates_find[0][4], 4)
    course_code = get_valid_course_code()

    codeP = Coordinates.generate_code(last_name=nom, first_name=prenom, gender=gender)

    # Retourne les nouvelles coordonnées
    return {
        "code": codeP,
        "nom": nom,
        "prenom": prenom,
        "sexe": gender,
        "email": email,
        "telephone": phone,
        "codeCours": course_code
    }


def modify_professor():
    """function for modify professors"""
    DB_FILE = "database.db"
    dB = Database(DB_FILE)
    code = Coordinates.validate_name("le code du Professeur")
    coordinates_find =dB.read_records("professors", condition="code=?", params=(code,))
    if len(coordinates_find) > 0:
        clear_screen()
        print("\n")
        print("\t" * 4, f"L'information du professeur avec code \" {code} \" : ")
        
        data_list = []
        data_list.append(
            {"CODE": coordinates_find[0][0], "NOM": coordinates_find[0][1],"PRENOM": coordinates_find[0][2], "SEXE": coordinates_find[0][3], "EMAIL": coordinates_find[0][4], "TELEPHONE": coordinates_find[0][5], "CODE_COURS": coordinates_find[0][6]}
        )
        afficher_affiches(data=data_list, valeur_vide="...")
        print()
        print("\n", "\t", " SOS !!  seulement les champs contenant un * sont aubligatoire. : ")
        print()
        print("\tnom")
        print("\tprenom")
        print("\tsexe *")
        print("\tphone *")
        print("\temail *")
        print("\tcode cours *")
        print()
        pause_system()
        params = valide_coordinates_modify(code)
        dB.update_record(table="professors", values=params, condition="code=?", condition_params=(code,))


    else:
        clear_screen()
        print()
        print("\t", f"Pas de professeurs trouvés avec le code '{code}' dans la base !")
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
                print()          
                print("\t" * 5,"Accès reservé aux Administrateurs.")
                pause_system()
  
        elif menuchoice == 2:
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
                    print("\n" * 2)
                    print("\t" * 4, f"L'information du professeur avec code ' {code} ' : ")
                    data = []
                    data.append(
                        {"CODE": coordinates_find[0][0], "NOM": coordinates_find[0][1],"PRENOM": coordinates_find[0][2], "SEXE": coordinates_find[0][3], "EMAIL": coordinates_find[0][4], "TELEPHONE": coordinates_find[0][5], "CODE_COURS": coordinates_find[0][6]}
                    )
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

                    professor.get_all_professors()
                    code = Coordinates.validate_input("le code du professeur")
                    coordinates_find = data.read_records("professors", condition="code=?", params=(code,))
                    if len(coordinates_find) > 0:
                        data.delete_record(table="professors", condition="code=?", params=(code,))
                        print("\n")
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

