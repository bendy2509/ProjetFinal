"""
"""

import re
import os
import random

from modules.database.database import Database
from modules.contraintes.contraintes import clear_screen, pause_system

class InvalidInputError(Exception):
    """Classe d'exception personnalisée pour les entrées invalides."""

    def __init__(self, message):
        """
        Initialise l'exception avec un message spécifique.

        :param message: Le message d'erreur à afficher.
        """
        super().__init__(message)

class Coordinates:
    """Class to manage professor's coordinates."""
    
    def __init__(self, code=None, last_name=None, first_name=None, gender=None, email=None, phone=None, course_code=None):
        self._code = code
        self._last_name = last_name
        self._first_name = first_name
        self._gender = gender
        self._email = email
        self._phone = phone
        self._course_code = course_code

    @property
    def code(self):
        return self._code

    @property
    def last_name(self):
        return self._last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def gender(self):
        return self._gender

    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone

    @property
    def course_code(self):
        return self.course_code

    @staticmethod
    def clear_screen():
        """Clears the console screen."""
        os.system("cls" if os.name == "nt" else "clear")
        print()

    @staticmethod
    def validate_input(field_name):
        """
        Valide l'entrée utilisateur pour un champ donné.

        :param field_name: Le nom du champ à valider.
        :return: La valeur validée du champ.
        :raises InvalidInputError: Si l'entrée est invalide.
        """
        while True:
            try:
                value = input("\t" * 5 + f"Entrez {field_name}: ")
                while value == "":
                    clear_screen()
                    print("\t" * 5 + f"Erreur : {field_name} ne doit pas être vide.")
                    pause_system()
                    clear_screen()
                    value = input("\t" * 5 + f"Entrez {field_name}: ")

                return value
            except InvalidInputError as e:
                print("\t" * 5 + f"Erreur : {field_name} ne doit pas être vide.")
                pause_system()

    @staticmethod
    def validate_name(field):
        """Validates if the field contains at least one alphabet character."""
        while True:
            value = Coordinates.validate_input(field)
            if value[:1].isalpha():
                return value
            print("\t" * 5 + f'Erreur : Le {field} devrait commencer par une lettre.')

    @staticmethod
    def validate_gender():
        """Prompts the user to choose a gender ('F' or 'M')."""
        print("\t" * 5 + "Veuillez faire le choix du sexe ['F' ou 'M']")
        gender = input("\t" * 5 + "Le sexe : ").strip().upper()
        while gender not in ("F", "M"):
            print("\t" * 5 + "Veuillez choisir correctement le sexe ['F' ou 'M']")
            gender = input("\t" * 5 + "Le sexe : ").strip().upper()
        return gender

    @staticmethod
    def prompt_for_phone():
        """Prompts the user to input a phone number and ensures it contains only digits."""
        while True:
            try:
                phone = input("\t" * 5 + "Entrez le téléphone : ").strip()
                if phone[:4] == "+509" or phone[:3] == "509" or phone[:5] == "(509)" or phone[:6] == "+(509)":
                    if phone[1:].isdigit() or phone[6:].isdigit() :
                        return phone
                int(phone)
                return phone
            except ValueError:
                print("\t" * 5 + "Veuillez entrer un numéro correct contenant uniquement des chiffres.")

    @staticmethod
    def validate_phone():
        """Validates a phone number using a regular expression."""
        expression = r"^((\+)|(011))?[\s-]?((509)|(\(509\)))?[\s-]?(3[1-9]|4[0-4]|4[6-9]|5[5])[\s-]?([0-9]{2})[\s-]?([0-9]{2})[\s-]?[0-9]{2}$"
        phone = Coordinates.prompt_for_phone()
        while not re.fullmatch(expression, phone):
            print("\t" * 5 + "Veuillez entrer un format de numéro correct.")
            phone = Coordinates.prompt_for_phone()
        return phone


    @staticmethod
    def validate_course_code(DB_FILE):
        """Valide le code du cours."""
        data = Database(DB_FILE)
        clear_screen()
        course_code = input("\t" * 5 + "Entrez le code du cours : ").strip()

        # Vérifier l'existence du cours
        cours_existe = data.read_records(
            table="cours",
            condition="code_cours=?",
            params=(course_code,)
        )
        if not cours_existe:
            print("\t" * 5 + "Erreur : Code cours non trouvé.")
            pause_system()
            return None

        course_assigned = data.read_records(table="professors")
        if course_assigned:

            for items in course_assigned:
                 if items[6] == course_code:
                    clear_screen()
                    print("\t" * 5, "Erreur : Un professeur est déjà assigné à ce cours.")
                    pause_system()
                    return None

        return course_code


    @staticmethod
    def validate_email():
        """Validates an email address using a regular expression."""
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        email = input("\t" * 5 + "Entrez l'adresse email : ").strip()
        while not re.match(regex, email):
            print("\t" * 5 + "Veuillez entrer une adresse email correcte.")
            email = input("\t" * 5 + "Entrez l'adresse email : ").strip()
        return email

    @staticmethod
    def generate_code(last_name, first_name, gender):
        """Generates a unique code for the professor based on last name, first name, and gender."""
        random_number = random.randint(100, 1000)
        return last_name[:3] + first_name[:2] + gender + str(random_number)

    def get_coordinates(self):
        """Obtient et valide toutes les coordonnées du professeur."""
        DB_FILE = "database.db"
        while True:
            isvalue = Coordinates.validate_course_code(DB_FILE)
            if isvalue:
                self._course_code = isvalue
                self._last_name = Coordinates.validate_name(field="nom")
                self._first_name = Coordinates.validate_name(field="prénom")
                self._gender = Coordinates.validate_gender()
                self._email = Coordinates.validate_email()
                self._phone = Coordinates.validate_phone()
                self._code = Coordinates.generate_code(last_name=self._last_name, first_name=self._first_name, gender=self._gender)

                return {
                    "code": self._code,
                    "nom": self._last_name,
                    "prenom": self._first_name,
                    "sexe": self._gender,
                    "email": self._email,
                    "telephone": self._phone,
                    "codeCours": self._course_code
                }

            Coordinates.clear_screen()
            print("\t" * 4, "Le cours doit exister et ne doit être attribué à aucun professeur pour pouvoir passer à l'étape suivante.")
            pause_system()