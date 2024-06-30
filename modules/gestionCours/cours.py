# cours.py
from modules.contraintes.contraintes import clear_screen, pause_system, saisir_annee, saisir_heure, saisir_nom_cours, saisir_session
from modules.database.database import Database

class Cours:
    """Gestion des cours"""
    def __init__(self, nom, debut, fin, session, annee, code_cours):
        """Fonction init"""
        self.nom = nom
        self.debut = debut
        self.fin = fin
        self.session = session
        self.annee = annee
        self.code_cours = code_cours

class Course_Manager:
    """Gestion des fonctions liées aux cours."""

    def __init__(self, db_file):
        """Initialise un gestionnaire de cours avec un gestionnaire de base de données."""
        self.db_manager = Database(db_file)

    def enregistrer_cours(self):
        """Enregistre un nouveau cours dans la base de données."""
        clear_screen()
        print("\n", "*" * 10 , "Enregistrer Cours" , "*" * 10 ,"\n")
        pause_system()
        
        nom = saisir_nom_cours()
        if nom is None:
            return
        
        debut = saisir_heure("Heure de début (ex : 2) : ")
        if debut is None:
            return
        
        fin = saisir_heure("Heure de fin (ex : 2) : ")
        if fin is None:
            return
        
        session = saisir_session()
        if session is None:
            return
        
        annee = saisir_annee()
        if annee is None:
            return
        code_cours = self._generer_code_cours(nom, session, annee)

        self.db_manager.create_record(
            "cours",
            {
                "code_cours": code_cours,
                "nom": nom,
                "debut": debut,
                "fin": fin,
                "session": session,
                "annee": annee
            }
        )
        print("Cours enregistré avec succès.")

    def _generer_code_cours(self, nom, session, annee):
        """Génère un code de cours unique à partir du nom, de la session et de l'année."""
        return f"{nom}-session{session}-{annee}".upper()
    
    def afficher_cours(self):
        """Affiche la liste des cours enregistrés."""
        clear_screen()
        print("\n", "*" * 10 , "Liste des Cours" , "*" * 10 ,"\n")
        
        cours = self.db_manager.read_records("cours")

        if not cours:
            print("Aucun cours trouvé.")
        else:
            for cour in cours:
                print(cour)
        pause_system()