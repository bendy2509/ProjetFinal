""" """
import sqlite3
import hashlib

from modules.contraintes.contraintes import clear_screen, pause_system
from modules.gestionProfesseur.getInfos import Coordinates
from modules.database.database import Database

class Professor(Database):
    """Classe de gestion des professeurs héritant de la classe Database"""

    def __init__(self, database_name):
        """ """
        super().__init__(database_name)

    def add_professor(self,coordinates):
        """ Ajoute un professeur dans la base de données."""
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
        
        

    def search_professor(self, code):
        """Recherche un professeur par code"""
        try:
            cursor = self.connexion.cursor()
            cursor.execute("SELECT * FROM professors WHERE code = ?", (code,))
            professor_find = cursor.fetchall()
            if professor_find:
                return professor_find
            else:
                print("\t" * 5, f"Professeur avec code '{code}' introuvable.")
                return None
        except sqlite3.OperationalError as e:
            print("\t" * 5, "Erreur lors de la recherche du professeur or :", e)
            return None

    def delete_professor(self, codep):
        """ """
        query = "DELETE FROM professors WHERE code = ?"
        parameters = (codep,)
        self.execute_query(query, "delete", parameters)

    def updateProfessor(self, codep):
        """ Modifies the cordonates of a professor if they exist. """
        cursor = self.connexion.cursor()
        cursor.execute("SELECT * FROM professors WHERE code = ?", (codep,))
        professor = cursor.fetchone()

        if professor:
            newCoordonates = Coordinates.get_coordinates()
            cursor.execute("UPDATE professors SET code = ?, nom = ?, prenom = ?, sexe = ?, email = ?, telephone = ?, codeCours = ? WHERE codep = ?", 
                           (newCoordonates._code, newCoordonates._nom, newCoordonates._prenom, newCoordonates._sexe,
                            newCoordonates._email, newCoordonates._telephone, newCoordonates._code_cours ))
            cursor.commit()
            print(f"Cordonnees du professeur avec code : '{codep}' modifiees avec succes !professeur avec code : '{codep}' modifiees avec succes !")        

        else:
            print("\t" * 5 + f"Aucun professeur trouve avec le codep : '{codep}' !")

    def __str__(self):
        """ """
        return f"Codep : {self._codep}, Nom : {self._nom}, Prenom : {self._prenom}, sexe : {self._sexe}, Email : {self._email}, Telephone : {self._telephone}"
