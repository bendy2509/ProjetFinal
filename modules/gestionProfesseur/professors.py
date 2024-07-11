""" """
from modules.contraintes.contraintes import afficher_affiches, clear_screen, pause_system
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

    def get_all_professors(self):
        """ """
        # clear_screen()
        all_professor = self.read_records(table="professors")

        if all_professor:
            data = []
            for prof in all_professor:
                data.append(
                    {"CODE": prof[0], "NOM": prof[1],"PRENOM": prof[2], "SEXE": prof[3], "EMAIL": prof[4], "TELEPHONE": prof[5], "CODE_COURS": prof[6]}
                )
            afficher_affiches(data=data, valeur_vide="...")
            
        else:
            print("\t" * 4 + "Pas de professeurs dans la base !")
        pause_system()

    def __str__(self):
        """ """
        return f"Codep : {self._codep}, Nom : {self._nom}, Prenom : {self._prenom}, sexe : {self._sexe}, Email : {self._email}, Telephone : {self._telephone}"
