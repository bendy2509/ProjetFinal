# cours.py
from modules.contraintes.contraintes import clear_screen, pause_system, saisir_annee, saisir_duration, saisir_nom_cours, saisir_session
from modules.database.database import Database

class Cours:
    """Gestion des cours"""
    def __init__(self, nom, duration, session, annee, code_cours):
        """Fonction init"""
        self.nom = nom
        self.duration = duration
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
        
        duration = saisir_duration("Veuillez saisir la durée (ex : 2) : ")
        if duration is None:
            return
        
        session = saisir_session()
        if session is None:
            return
        
        annee = saisir_annee()
        if annee is None:
            return

        code_cours = self._generer_code_cours(nom, session, annee)

        if not self.verifier_existence_cours(code_cours):
            cours = Cours(nom, duration, session, annee, code_cours)
            self.db_manager.create_record(
                "cours",
                {
                    "code_cours": cours.code_cours,
                    "nom": cours.nom,
                    "duration": cours.duration,
                    "session": cours.session,
                    "annee": cours.annee
                }
            )
            print("Cours enregistré avec succès.")
        else:
            print("Erreur, un cours avec code existe deja dans la base.")
        pause_system()

    def _generer_code_cours(self, nom, session, annee):
        """Génère un code de cours unique à partir du nom, de la session et de l'année."""
        return f"{nom[:3]}-S{session}-{annee}".upper()

    def afficher_cours(self):
        """Affiche la liste des cours enregistrés."""
        clear_screen()
        print("\t" * 5, "Liste des cours :")
        cours = self.db_manager.read_records("cours")
        print("\n")
        print("\t" * 3, "-" * 75)
        print("\t" * 3, "| {:<13} | {:15} | {:15} | {:<10} | {:<10} |".format("CODE COURS", "NOM", "PROFESSEUR", "DUREE", "SESSION", "ANNEE"))
        print("\t" * 3, "-" * 75)
        for cour in cours:
            if not (cour[2]):
                print("\t" * 3, "| {:<13} | {:15} | {:15} | {:<10} | {:<10} |".format(cour[0], cour[1], "....", cour[3], cour[4], cour[5]))
            else:
                print("\t" * 3, "| {:<13} | {:15} | {:15} | {:<10} | {:<10} |".format(cour[0], cour[1], cour[2], cour[3], cour[4], cour[5]))
            print("\t" * 3, "-" * 75)
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
        print("2. Durée du cours")
        print("3. Session")
        print("4. Année académique")
        print("5. Modifier tout")
        print("0. Annuler")

        choix = input("Votre choix : ")

        if choix == '0':
            print("Modification annulée.")
            return

        nom = cours[0][1]
        duration = cours[0][2]
        session = cours[0][3]
        annee = cours[0][4]

        if choix == '1' or choix == '5':
            nom = saisir_nom_cours()
        if choix == '2' or choix == '5':
            duration = saisir_duration("Saisir la nouvelle durée (ex : 2) : ")
        if choix == '3' or choix == '5':
            session = saisir_session()
        if choix == '4' or choix == '5':
            annee = saisir_annee()

        nouveau_code_cours = self._generer_code_cours(nom, session, annee)

        if nouveau_code_cours != code_cours and self.verifier_existence_cours(nouveau_code_cours):
            print("Erreur : Un autre cours avec ce nouveau code existe déjà.")
            pause_system()
            return

        cours = Cours(nom, duration, session, annee, nouveau_code_cours)
        self.db_manager.update_record(
            table="cours",
            values={
                "code_cours": cours.code_cours,
                "nom": cours.nom,
                "duration": cours.duration,
                "session": cours.session,
                "annee": cours.annee
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
            clear_screen()
            print("\n")
            print("\t" * 3, "-" * 75)
            print("\t" * 3, "| {:<13} | {:15} | {:15} | {:<10} | {:<10} |".format("CODE COURS", "NOM", "PROFESSEUR", "DUREE", "SESSION", "ANNEE"))
            print("\t" * 3, "-" * 75)
            for cour in cours:
                if not (cour[2]):
                    print("\t" * 3, "| {:<13} | {:15} | {:15} | {:<10} | {:<10} |".format(cour[0], cour[1], "....", cour[3], cour[4], cour[5]))
                else:
                    print("\t" * 3, "| {:<13} | {:15} | {:15} | {:<10} | {:<10} |".format(cour[0], cour[1], cour[2], cour[3], cour[4], cour[5]))
                print("\t" * 3, "-" * 75)
        else:
            print("Cours non trouvé.")
        pause_system()

    def ajouter_professeur_au_cours(self, code_cours, code_professeur):
        """
        Ajoute un professeur à un cours après avoir vérifié l'existence du code professeur.

        :param code_cours: Code du cours auquel ajouter le professeur.
        :param code_professeur: Code du professeur à ajouter au cours.
        """
        # Vérifier l'existence du professeur
        professeur_existe = self.db_manager.read_records(
            table="professors", 
            condition="code=?", 
            params=(code_professeur,)
        )
        
        if not professeur_existe:
            print("Erreur : Code professeur non trouvé.")
            pause_system()
            return
        
        # Vérifier l'existence du cours
        cours_existe = self.db_manager.read_records(
            table="cours",
            condition="code_cours=?",
            params=(code_cours,)
        )
        
        if not cours_existe:
            print("Erreur : Code cours non trouvé.")
            pause_system()
            return
        
            # Vérifier si un professeur est déjà assigné à ce cours
        if cours_existe[0]["teacher_code"]:
            print("Erreur : Un professeur est déjà assigné à ce cours.")
            pause_system()
            return
        
        # Mettre à jour le cours avec le code du professeur
        self.db_manager.update_record(
            table="cours",
            values={"teacher_code": code_professeur},
            condition="code_cours=?",
            condition_params=(code_cours,)
        )
        print("Professeur assigné au cours avec succès.")

    def verifier_existence_cours(self, code_cours):
        """Vérifie si un cours avec le code_cours existe déjà."""
        cours = self.db_manager.read_records(table="cours", condition="code_cours = ?", params=(code_cours,))
        return bool(cours)