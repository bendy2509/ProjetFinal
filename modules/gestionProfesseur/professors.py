""" """
import sqlite3
import hashlib

from modules.contraintes.contraintes import clear_screen, pause_system
from gestionProfesseur.getInfosProfessors import Coordinates
from modules.database.database import Database

class Professor(Database):
    """Classe de gestion des professeurs héritant de la classe Database"""

    def __init__(self, database_name):
        """ """
        super().__init__(database_name)

    def add_professor(self):
        """ Ajoute un professeur dans la base de données."""
        coordinates = Coordinates()
        clear_screen()
        parameters = coordinates.get_coordinates()
        self.create_record(table="professors",values=parameters)

    def format_coords(self,coordonates):
        """ """
        print()
        print("\t", "*" * 120 )
        print("\t" * 2, "{:<15}{:<15}{:<15}{:<10}{:<30}{:<15}{:<15}".format("CODE","NOM","PRENOM","SEXE","EMAIL","TELEPHONE", "CODE_COURS"))
        print()
        for coordonate in coordonates:
            print("\t" * 2, "{:<15}{:<15}{:<15}{:<10}{:<30}{:<15}{:<15}".format(coordonate[0],coordonate[1],
            coordonate[2],coordonate[3],coordonate[4],coordonate[5], coordonate[6]))

        print()
        print("\t", "*" * 120 )

    def get_all_professors(self):
        """ """
        clear_screen()
        all_professor = self.read_records(table="professors")

        if all_professor:
            self.format_coords(all_professor)

        else:
            print("Pas de professeurs dans la base !")
        pause_system()

    def __str__(self):
        """ """
        return f"Codep : {self._codep}, Nom : {self._nom}, Prenom : {self._prenom}, sexe : {self._sexe}, Email : {self._email}, Telephone : {self._telephone}"
