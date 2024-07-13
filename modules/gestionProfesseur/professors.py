"""
Module de gestion des coordonnées des professeurs et
des interactions avec la base de données. Fournit des
fonctions pour valider et mettre à jour les détails des
professeurs tels que le nom, le sexe, l'adresse e-mail,
le numéro de téléphone et le code de cours, assurant l'intégrité des données.
Inclut des méthodes pour générer des codes uniques pour les professeurs
et vérifier l'unicité des adresses e-mail et
des affectations de cours dans la base de données.

Classes :
    Coordinates : Gère les coordonnées des professeurs et les fonctions de validation.

Fonctions :
    clear_screen : Efface l'écran de la console.
    prompt_and_validate : Invite l'utilisateur à entrer des données
    et les valide selon les fonctions de validation fournies.

Utilisation :
    Ce module est utilisé dans des applications où
    la gestion précise et la validation des données
    des professeurs sont essentielles, assurant un
    enregistrement précis et l'unicité des informations.
"""


import os
import re
import random

from modules.contraintes.contraintes import afficher_affiches, clear_screen, pause_system
from modules.database.database import Database

class Coordinates:
    """Class to manage professor's coordinates including validation.
    Validates and manages attributes such as name, gender, email, phone,
    and course code, ensuring uniqueness and proper format. 
    Includes methods for generating unique professor codes and updating records.
    """
    global database
    DB_FILE = "database.db"
    database = Database(DB_FILE)

    def __init__(self, code=None, last_name=None, first_name=None,
                 gender=None, email=None, phone=None, course_code=None):
        self.code = code
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.email = email
        self.phone = phone
        self.course_code = course_code

    @staticmethod
    def clear_screen():
        """Clears the console screen."""
        os.system("cls" if os.name == "nt" else "clear")
        print()

    @staticmethod
    def validate_unique_phone(phone):
        """Checks if the given phone is already assigned to another professor.
        Ensures the phone is unique among all professors' records.
        """
        all_professors = database.read_records("professors")
        return not any(professor[5] == phone for professor in all_professors)

    @staticmethod
    def validate_unique_email(email):
        """Checks if the given email is already assigned to another professor.
        Ensures the email is unique among all professors' records.
        """
        all_professors = database.read_records("professors")
        return not any(professor[4] == email for professor in all_professors)

    @staticmethod
    def prompt_and_validate(prompt, validation_func, error_message):
        """Prompts the user for input and validates it.
        Displays a prompt, validates the input using a given function, and
        shows an error message if validation fails. Returns None if 'quit' is entered.
        """
        while True:
            print()
            value = input(prompt + " ou tapez 'quit' pour quitter : ").strip()
            if value.lower() == 'quit':
                return None
            if validation_func(value):
                return value
            print("\t" + error_message)

    @staticmethod
    def validate_name(field):
        """Validates if the field contains at least one alphabet character."""
        def is_valid_name(value):
            return value[:1].isalpha()

        return Coordinates.prompt_and_validate(
            f"Entrez le {field} : ",
            is_valid_name,
            f"Erreur : Le {field} devrait commencer par une lettre."
        )

    @staticmethod
    def validate_gender():
        """Prompts the user to choose a gender ('F' or 'M')."""
        def is_valid_gender(gender):
            return gender.lower() in ("f", "m")

        return Coordinates.prompt_and_validate(
            "Le sexe (F ou M) : ",
            is_valid_gender,
            "Veuillez choisir correctement le sexe ['F' ou 'M']"
        )

    @staticmethod
    def validate_phone(phone):
        expression = (
            r"^((\+)|(011))?[\s-]?((509)|(\(509\)))?[\s-]?"
            r"([2-9]{1}[0-9]{7}|(3[1-9]|4[0-4]|4[6-9]|5[5])[\s-]?"
            r"([0-9]{2})[\s-]?([0-9]{2})[\s-]?[0-9]{2})$"
        )
        return re.fullmatch(expression, phone) is not None

    @staticmethod
    def validate_course_code(course_code):
        cours_existe = database.read_records(
            table="cours",
            condition="code_cours=?",
            params=(course_code,)
        )
        if not cours_existe:
            return False

        course_assigned = database.read_records(table="professors")
        for items in course_assigned:
            if items[6] == course_code:
                return False

        return True

    @staticmethod
    def validate_email(email):
        """Checks if the given email is already assigned to another professor.

        Ensures the email is unique among all professors' records.
        """
        regex = (
            r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+'
            r'(\.[a-zA-Z]{2,})?$'
        )
        return re.match(regex, email) is not None

    @staticmethod
    def generate_code(last_name, first_name, gender):
        """Generates a unique code for the professor based on last name, first name, and gender."""
        random_number = random.randint(100, 1000)
        return last_name[:3] + first_name[:2] + gender + str(random_number)

    @staticmethod
    def return_coordinates():
        """Obtains and validates all coordinates for a professor.

        Prompts the user to enter details such as name, gender, email, phone,
        and course code, ensuring each is valid and unique. Returns a dictionary
        with the validated data or None if 'quit' is entered.
        """

        print("\n\t=-=========== Session d'enregistrement des Professeurs.===========-=\n")

        last_name = Coordinates.validate_name("nom")
        if last_name is None:
            return None

        first_name = Coordinates.validate_name("prénom")
        if first_name is None:
            return None

        gender = Coordinates.validate_gender()
        if gender is None:
            return None

        email = Coordinates.prompt_and_validate(
            "Entrez l'adresse email : ",
            Coordinates.validate_email,
            "Veuillez entrer une adresse email correcte."
        )
        if email is None:
            return None

        phone = Coordinates.prompt_and_validate(
            "Veuillez entrer votre numéro de téléphone : ",
            Coordinates.validate_phone,
            "Veuillez entrer un format de numéro correct."
        )
        if phone is None:
            return None

        course_code = Coordinates.prompt_and_validate(
            "Entrez le code du cours : ",
            Coordinates.validate_course_code,
            "Erreur : Code cours non trouvé ou déjà assigné à un professeur."
        )
        if course_code is None:
            return None

        code = Coordinates.generate_code(last_name, first_name, gender)

        return {
            "code": code,
            "nom": last_name,
            "prenom": first_name,
            "sexe": gender,
            "email": email,
            "telephone": phone,
            "codeCours": course_code
        }


def is_exist_record():
    """function to verify exist record"""
    DB_FILE = "database.db"
    database = Database(DB_FILE)
    isExist = database.read_records("professors")
    if len(isExist) == 0:
        return None

    return isExist

def modify_professor():
    """Function to modify professors"""
    global database
    DB_FILE = "database.db"
    database = Database(DB_FILE)
    code = input("le code du Professeur :  ")
    coordinates_find = database.read_records("professors", condition="code=?", params=(code,))

    if len(coordinates_find) > 0:
        print("\n")
        print("\t" * 4, f"=-===========L'information du professeur avec code ' {code} ' :===========-=")

        data_list = [
            {
                "CODE": coordinates_find[0][0], "NOM": coordinates_find[0][1],
                "PRENOM": coordinates_find[0][2], "SEXE": coordinates_find[0][3], 
                "EMAIL": coordinates_find[0][4], "TELEPHONE": coordinates_find[0][5],
                "CODE_COURS": coordinates_find[0][6]
            }
        ]
        afficher_affiches(data=data_list, valeur_vide="...")

        print("\n")
        # Validation et modification des coordonnées du professeur
        last_name = Coordinates.validate_name("nom")
        if last_name is None:
            last_name = coordinates_find[0][1]

        first_name = Coordinates.validate_name("prénom")
        if first_name is None:
            first_name = coordinates_find[0][2]

        gender = Coordinates.validate_gender()
        if gender is None:
            gender = coordinates_find[0][3]

        email = Coordinates.prompt_and_validate(
            "Entrez l'adresse email : ",
            lambda e: Coordinates.validate_email(e) and (e == coordinates_find[0][4] or Coordinates.validate_unique_email(e)),
            "Adresse email incorrecte ou l'adresse est déjà assignée à un autre professeur."
        )
        if email is None:
            email = coordinates_find[0][4]

        phone = Coordinates.prompt_and_validate(
            "Veuillez entrer votre numéro de téléphone : ",
            lambda p: Coordinates.validate_phone(p) and (p == coordinates_find[0][5] or Coordinates.validate_unique_phone(p)),
            "Le numéro incorrect ou le numéro est déjà assigné à un autre professeur."
        )
        if phone is None:
            phone = coordinates_find[0][5]

        course_code = Coordinates.prompt_and_validate(
            "Entrez le code du cours : ",
            Coordinates.validate_course_code,
            "Erreur : Code cours non trouvé ou déjà assigné à un professeur."
        )
        if course_code is None:
            course_code = coordinates_find[0][6]

        params = {
            "code": code,
            "nom": last_name,
            "prenom": first_name,
            "sexe": gender,
            "email": email,
            "telephone": phone,
            "codeCours": course_code
        }
        database.update_record(table="professors", values=params, condition="code=?", condition_params=(code,))

    else:
        print("\n")
        print("\t", f"Pas de professeurs trouvés avec le code '{code}' dans la base !")
        pause_system()

class Professor(Database):
    """Classe de gestion des professeurs héritant de la classe Database"""

    def __init__(self, database_name):
        """Fonction Init """
        super().__init__(database_name)

    def add_professor(self):
        """ Ajoute un professeur dans la base de données."""
        coordinates = Coordinates()

        parameters = coordinates.return_coordinates()
        if parameters:
            self.create_record(table="professors",values=parameters)

    def get_all_professors(self):
        """ """
        print()
        all_professor = self.read_records(table="professors")

        if all_professor:
            data = []
            for prof in all_professor:
                data.append(
                    {"CODE": prof[0], "NOM": prof[1],"PRENOM": prof[2],
                      "SEXE": prof[3], "EMAIL": prof[4], "TELEPHONE": prof[5],
                      "CODE_COURS": prof[6]
                    }
                )
            afficher_affiches(data=data, valeur_vide="...")


        else:
            print("\t" + "Pas de professeurs dans la base !")
        pause_system()
