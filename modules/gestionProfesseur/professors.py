""" """
import sqlite3
import hashlib

from modules.contraintes.contraintes import clear_screen, pause_system
from modules.gestionProfesseur.getInfosProfessors import Coordinates
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

        if parameters:
            self.create_record(table="professors",values=parameters)

        else:
            clear_screen()
            print("\t" * 4, "Oups! Enregistrement echoue, une erreur s'est produite lors de votre saisie .")
            pause_system()

    def format_coords(self,coordonates):
        """ """
        print()
        print("\t", "=" * 130 )
        print("\t", "|", "\t", "{:<15}{:<15}{:<15}{:<10}{:<30}{:<15}{:<15}".format("CODE","NOM","PRENOM","SEXE","EMAIL","TELEPHONE", "CODE_COURS"),"\t", "|")
        print()
        for coordonate in coordonates:
            print("\t", "|", "\t", "{:<15}{:<15}{:<15}{:<10}{:<30}{:<15}{:<15}".format(coordonate[0],coordonate[1],
            coordonate[2],coordonate[3],coordonate[4],coordonate[5], coordonate[6]),"\t", "|")

        print()
        print("\t", "=" * 130 )

    def get_all_professors(self):
        """ """
        # clear_screen()
        all_professor = self.read_records(table="professors")

        if all_professor:
            self.format_coords(all_professor)
            return all_professor

        else:
            print("\t" * 4 + "Pas de professeurs dans la base !")
        pause_system()

    def __str__(self):
        """ """
        return f"Codep : {self._codep}, Nom : {self._nom}, Prenom : {self._prenom}, sexe : {self._sexe}, Email : {self._email}, Telephone : {self._telephone}"
