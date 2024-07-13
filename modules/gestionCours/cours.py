# cours.py
from modules.contraintes.contraintes import (
    afficher_affiches, clear_screen,
    pause_system, saisir_annee, saisir_duration, saisir_faculte,
    saisir_nom_cours, saisir_session
)
from modules.database.database import Database

class Cours:
    """Gestion des cours"""
    def __init__(self, nom, faculte, duration, session, annee, code_cours):
        """Fonction init"""
        self.nom = nom
        self.faculte = faculte
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
        print("\n", "=" * 20 , "Enregistrement d'un Cours" , "=" * 20 ,"\n")
        nom = saisir_nom_cours()
        if nom is None:
            return
        
        fac = saisir_faculte()
        if fac is None:
            return
        
        duration = saisir_duration("Veuillez saisir la durée du cours (q pour quitter) : ")
        if duration is None:
            return
        
        session = saisir_session()
        if session is None:
            return

        annee = saisir_annee()
        if annee is None:
            return

        code_cours = self._generer_code_cours(nom, session, fac, annee)

        if not self.verifier_existence_cours(code_cours):
            cours = Cours(nom, fac, duration, session, annee, code_cours)
            self.db_manager.create_record(
                "cours",
                {
                    "code_cours": cours.code_cours,
                    "nom": cours.nom,
                    "faculte": cours.faculte,
                    "duration": cours.duration,
                    "session": cours.session,
                    "annee": cours.annee
                }
            )
            print("Cours enregistré avec succès.")
        else:
            print("Erreur, un cours avec code existe deja dans la base.\n")
        pause_system()

    def cours_assignes_ou_non(self, assigner):
        """
        Pour afficher les cours qui sont assignés ou non

        :param assigner: un boolean qui doit etre True pour les cours assignés,\
        False dans le cas contraire
        """
        cours = self.db_manager.read_records("cours")
        print("\n")

        data = []
        for cour in cours:
            if not cour[3] and not assigner:
                data.append(
                    {"CODE COURS": cour[0], "NOM DU COURS": cour[1],"FACULTE": cour[2], \
                     "PROFESSEUR": cour[3], "DUREE": cour[4], "SESSION": cour[5], "ANNEE": cour[6]}
                )
            if cour[3] and assigner:
                data.append(
                    {"CODE COURS": cour[0], "NOM DU COURS": cour[1],"FACULTE": cour[2], \
                     "PROFESSEUR": cour[3], "DUREE": cour[4], "SESSION": cour[5], "ANNEE": cour[6]}
                )
        afficher_affiches(data=data, valeur_vide="...")
        pause_system()

    def _generer_code_cours(self, nom, session, fac, annee):
        """Génère un code de cours unique à partir du nom, de la session et de l'année."""
        return f"{nom[:3]}-{fac[0:3]}-S{session}-{annee}".upper()

    def afficher_cours(self):
        """Affiche la liste des cours enregistrés."""
        clear_screen()
        print("\t" * 5, "Liste des cours :")
        cours = self.db_manager.read_records("cours")
        print("\n")

        data = []
        for cour in cours:
            data.append(
                {"CODE COURS": cour[0], "NOM DU COURS": cour[1],"FACULTE": cour[2], \
                 "PROFESSEUR": cour[3], "DUREE": cour[4], "SESSION": cour[5], "ANNEE": cour[6]}
            )
        afficher_affiches(data=data, valeur_vide="...")

        pause_system()

    def modifier_cours(self):
        """Modifie un cours existant dans la base de données."""
        clear_screen()
        print("\n", "=" * 10 , "Modifier un Cours" , "=" * 10 ,"\n")

        code_cours = input("Entrer le code du cours à modifier : ")
        cours = self.db_manager.read_records(table="cours", condition="code_cours=?", params=(code_cours,))
        if not cours:
            print("Erreur : Cours non trouvé.")
            pause_system()
            return
        
        data = []
        for cour in cours:
            data.append(
                {"CODE COURS": cour[0], "NOM DU COURS": cour[1],"FACULTE": cour[2], \
                 "PROFESSEUR": cour[3], "DUREE": cour[4], "SESSION": cour[5], "ANNEE": cour[6]}
            )
        afficher_affiches(data=data, valeur_vide="...")

        print("Sélectionnez ce que vous voulez modifier : ")
        print("1. Nom du cours")
        print("2. La faultés")
        print("3. Durée du cours")
        print("4. Session")
        print("5. Année académique")
        print("6. Modifier tout")
        print("0. Annuler ou une autre touche pour quitter")

        choix = input("Votre choix : ")
        clear_screen()
        nom, fac, prof, duration, session, annee = cours[0][1:7]

        modificateurs = {
            '1': lambda: saisir_nom_cours(),
            '2': lambda: saisir_faculte(),
            '3': lambda: saisir_duration("Saisir la nouvelle durée (q pour quitter) : "),
            '4': lambda: saisir_session(),
            '5': lambda: saisir_annee(),
            '6': lambda: (
                saisir_nom_cours(),
                saisir_faculte(),
                saisir_duration("Saisir la nouvelle durée (q pour quitter) : "),
               saisir_session(),
               saisir_annee()
            )
        }

        if choix in modificateurs:
            result = modificateurs[choix]()
            if choix == '6':
                nom, fac, duration, session, annee = result

            else:
                if not result:
                    return
                if choix == '1':
                    nom = result
                elif choix == '2':
                    fac = result
                elif choix == '3':
                    duration = result
                elif choix == '4':
                    session = result
                elif choix == '5':
                    annee = result
        else:
            print("Modification annulée.\n")
            return
        
        if nom is None:
            nom = cours[0][1]
            return 
        if fac is None:
            fac = cours[0][2]
            return 
        if prof is None:
            prof = cours[0][3]
            return 
        if duration is None:
            duration = cours[0][4]
            return 
        if session is None:
            session = cours[0][5]
            return 
        if annee is None:
            annee = cours[0][6]
            return 

        nouveau_code_cours = self._generer_code_cours(nom, session, fac, annee)
        if nouveau_code_cours != code_cours and self.verifier_existence_cours(nouveau_code_cours):
            print("Erreur : Un autre cours avec ce nouveau code existe déjà.")
            pause_system()
            return

        cours = Cours(nom, fac, duration, session, annee, nouveau_code_cours)
        self.db_manager.update_record(
            table="cours",
            values={
                "code_cours": cours.code_cours,
                "nom": cours.nom,
                "teacher_code": prof,
                "faculte": cours.faculte,
                "duration": cours.duration,
                "session": cours.session,
                "annee": cours.annee
            },
            condition="code_cours=?",
            condition_params=(code_cours,)
        )

        # Vérifiez si le code du cours existe dans la table schedules
        schedules_exist = self.db_manager.read_records(
            table="schedules",
            condition="cours_id=?",
            params=(code_cours,)
        )

        if schedules_exist:
            # Mise à jour du code du cours dans la table schedules
            self.db_manager.update_record(
                table="schedules",
                values={"code_cours": nouveau_code_cours},
                condition="code_cours=?",
                condition_params=(code_cours,)
            )
        
        print("Cours modifié avec succès.")
        pause_system()

    def rechercher_cours(self):
        """Méthode pour rechercher un cours"""
        clear_screen()
        print("\n", "=" * 10 , "Rechercher un Cours", "=" * 10 ,"\n")
        code_cours = input("Entrer le code du cours à rechercher : ")
        cours = self.db_manager.read_records(table="cours", \
        condition="code_cours=?", params=(code_cours,))
        if cours:
            data = []
            for cour in cours:
                data.append(
                    {"CODE COURS": cour[0], "NOM DU COURS": cour[1],"FACULTE": cour[2], \
                     "PROFESSEUR": cour[3], "DUREE": cour[4], "SESSION": cour[5], "ANNEE": cour[6]}
                )
            afficher_affiches(data=data, valeur_vide="...")
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
        if cours_existe[0][3]:
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
        cours = self.db_manager.read_records(table="cours", \
        condition="code_cours = ?", params=(code_cours,))
        return bool(cours)