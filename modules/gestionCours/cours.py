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

    def modifier_cours(self):
        """Modifie un cours existant dans la base de données."""
        clear_screen()
        print("\n", "*" * 10 , "Modifier un Cours" , "*" * 10 ,"\n")
        pause_system()

        code_cours = input("Entrer le code du cours à modifier : ")
        cours = self.db_manager.read_records(table="cours", condition="code_cours=?", params=(code_cours,))
        if not cours:
            print("Erreur : Cours non trouvé.")
            pause_system()
            return

        print("Sélectionnez ce que vous voulez modifier : ")
        print("1. Nom du cours")
        print("2. Heure de début")
        print("3. Heure de fin")
        print("4. Session")
        print("5. Année académique")
        print("6. Modifier tout")
        print("0. Annuler")

        choix = input("Votre choix : ")

        if choix == '0':
            print("Modification annulée.")
            return

        nom = cours[0][1]
        debut = cours[0][2]
        fin = cours[0][3]
        session = cours[0][4]
        annee = cours[0][5]

        if choix == '1' or choix == '6':
            nom = saisir_nom_cours()
        if choix == '2' or choix == '6':
            debut = saisir_heure("Heure de début (ex : 2) : ")
        if choix == '3' or choix == '6':
            fin = saisir_heure("Heure de fin (ex : 2) : ")
        if choix == '4' or choix == '6':
            session = saisir_session()
        if choix == '5' or choix == '6':
            annee = saisir_annee()

        nouveau_code_cours = self._generer_code_cours(nom, session, annee)

        if nouveau_code_cours != code_cours and self._verifier_existence_cours(nouveau_code_cours):
            print("Erreur : Un autre cours avec ce nouveau code existe déjà.")
            pause_system()
            return

        self.db_manager.update_record(
            table="cours",
            values={
                "nom": nom,
                "debut": debut,
                "fin": fin,
                "session": session,
                "annee": annee,
                "code_cours": nouveau_code_cours
            },
            condition="code_cours=?",
            condition_params=(code_cours,)
        )
        print("Cours modifié avec succès.")

    def rechercher_cours(self):
        """Méthode pour rechercher un cours"""
        clear_screen()
        print("\n", "*" * 10 , "Rechercher un Cours", "*" * 10 ,"\n")
        code_cours = input("Entrer le code du cours à rechercher : ")
        cours = self.db_manager.read_records(table="cours", condition="code_cours=?", params=(code_cours,))
        if cours:
            for cour in cours:
                print(f"Code du cours: {cour[0]}")
                print(f"Nom du cours: {cour[1]}")
                print(f"Heure de début: {cour[2]}")
                print(f"Heure de fin: {cour[3]}")
                print(f"Session: {cour[4]}")
                print(f"Année académique: {cour[5]}")
        else:
            print("Cours non trouvé.")
        pause_system()

    def _verifier_existence_cours(self, code_cours):
        """Vérifie si un cours avec le code_cours existe déjà."""
        cours = self.db_manager.read_records(table="cours", condition="code_cours = ?", params=(code_cours,))
        return bool(cours)