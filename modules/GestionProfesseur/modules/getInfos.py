"""
"""

import re
import os
import random

class Coordonnes:
    """_summary_""" 
    def __init__(self, code = None, nom = None, prenom = None,  sexe = None, email = None, telephone = None, code_cours = None) -> None:
        """ """
        self._code = code
        self._nom = nom
        self._prenom = prenom
        self._sexe = sexe
        self._email = email
        self._telephone = telephone
        self._code_cours = "Anglais"
    
    @staticmethod
    def clear_screen():
        """ """
        os.system("cls" if os.name == "nt" else "clear" )
        print()

    @staticmethod
    def saisirCoordonnes(coord):
        """ saisirNom _summary_ """
        Coordonnes.clear_screen()
        nom = input("\t" * 5 + f'Veuillez entrer le {coord}  :  ')
        while nom == '':
            Coordonnes.clear_screen()
            print("Nous evitons la saisie des coordonnes vides.")
            nom = input("\t" * 5 + f'Veuillez retaper le {coord} : ')
        return nom

    @staticmethod
    def valideCoordonnes(coord):
        """ Vérifier si le coordonne est valide (contient  lettres aux trois premiers caracteres. )"""
        while True:
            nom =Coordonnes.saisirCoordonnes(coord)
            try:
                if all(nom_part.isalpha() for nom_part in nom[:1]):
                    return nom
                raise ValueError(f"Le {coord} devrait avoir au moins une lettre au commencement.")
            except ValueError as err:
                print()
                print("\t" * 5, f'Erreur : {err}')

    @staticmethod
    def valideSexe():
        """ valideSexe _summary_"""
        print()
        print("\t" * 5 + "Veillez faire choix du sexe  ['F' ou 'M'] ")
        sexe = input("\t" * 5 + " Le sexe : ")
        while not  sexe.lower() in ("f", "m"):
            print()
            print("\t" * 5 +  "Veillez bien choisir le sexe ['F' ou 'M']")
            sexe = input("\t" * 5 + " Le sexe : ")
        return sexe.upper()   

    @staticmethod
    def setPhone():
        """ """
        while True:
            try:
                print()
                phone = int(input("\t" * 5 + "Entrer le téléphone :  "))
                return str(phone)
            except ValueError:
                print()
                print("\t" * 5 + "Veiller entrer un numero correct contient uniquement des chifres")

    @staticmethod
    def validePhone():
        """Valide un numero telephone en utilisant une expression régulière."""
        numero = Coordonnes.setPhone()
        expression = r"^((\+)|(011))?[\s-]?((509)|(\(509\)))?[\s-]?(3[1-9]|4[0-4]|4[6-9]|5[5])[\s-]?([0-9]{2})[\s-]?([0-9]{2})[\s-]?[0-9]{2}$"
        match = re.fullmatch(expression, numero)
        while not bool(match):
            print("\t" * 5, "Veillez entrer un format de numéro correct.")
            numero = Coordonnes.setPhone()
            expression = r"^((\+)|(011))?[\s-]?((509)|(\(509\)))?[\s-]?(3[1-9]|4[0-4]|4[6-9]|5[5])[\s-]?([0-9]{2})[\s-]?([0-9]{2})[\s-]?[0-9]{2}$"
            match = re.fullmatch(expression, numero)
        return numero

    @staticmethod
    def valide_email():
        """ Valide une adresse email en utilisant une expression régulière."""
        print()
        email = input("\t" * 5 + "Entrer l'adresse Email :  ")
        # Définition de l'expression régulière pour valider l'email
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$'
        # Utilisation de re.match pour vérifier si l'email correspond à la regex
        while not re.match(regex, email):
            print()
            print("\t" * 5, "Veillez entrer une adresse email correcte.")
            email = input("\t" * 5 + "Entrer l'adresse email :")
        return email

    @staticmethod
    def codes(nom, prenom, sexe):
        """" """
        aleatoire = random.randint(100, 1000)
        code = nom[:3] + prenom[:2] + sexe + str(aleatoire)
        return code

    def getCoords(self):
        """ getCoords _summary_"""
        self._nom = Coordonnes.valideCoordonnes("nom")
        self._prenom = Coordonnes.valideCoordonnes("prenom")
        self._sexe = Coordonnes.valideSexe()
        self._email = Coordonnes.valide_email()
        self._phone = Coordonnes. validePhone()
        self._code = Coordonnes.codes(self._nom, self._prenom, self._sexe)
        return (self._code, self._nom, self._prenom, self._sexe, self._email, self._phone, self._code_cours)
