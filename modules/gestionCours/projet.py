# from os import system
from datetime import datetime
from databases import DBManager
from menu import menu_cours

class Cours:
    """Gestion des cours"""
    def __init__(self, db_manager, nom, debut, fin, session, annee, code_cours):
        """Fonction init"""
        self.db_manager = db_manager
        self.nom = nom
        self.debut = debut
        self.fin = fin
        self.session = session
        self.annee = annee
        self.code_cours = code_cours

class Manager:
    """Gestion des fonctions"""

    def __init__(self, db_manager):
        """Fonction init"""
        self.db_manager = db_manager

    def enregistrer_cours(self):
        """Méthode pour enregistrer un cours"""
        print("\n", "*" * 10 , "Enregistrer Cours" , "*" * 10 ,"\n")
        nom = input("Nom du cours : ")
        debut = input("Heure de debut (ex : 2) : ")
        fin = input("Heure de la fin (ex : 2) : ")
        session = input("Session (1 ou 2) : ")
        annee = input("Année académique : ")
        code_cours = f"{nom}-session{session}-{annee}".upper()

        try:
            debut = int(debut)
        except ValueError:
            print("Erreur : Veuillez entrer une valeur entiere pour l'heure de début. Réessayer svp...\n")
            return

        try:
            fin = int(fin)
        except ValueError:
            print("Erreur : Veuillez entrer une valeur entiere pour l'heure de la fin du cours. Réessayer svp...\n")
            return

        try:
            session = int(session)
        except ValueError:
            print("Erreur : Veuillez entrer une valeur entiere pour la session. Réessayer svp...\n")
            return

        try:
            annee = int(annee)
        except ValueError:
            print("Erreur : Veuillez entrer une valeur entiere pour l'année'. Réessayer svp...\n")
            return

        if debut < 0 or fin < 0 or debut >= 24 or fin >= 24:
            print("Erreur : L'heure de début et de fin doit être entre 0 et 23.\n")
            return
        if fin <= debut:
            print("Erreur : L'heure de fin doit être après l'heure de début.\n")
            return
        if session not in [1, 2]:
            print("Erreur : La session doit être 1 ou 2.\n")
            return
        if annee < 2000 or annee > datetime.now().year:
            print("Erreur : L'année académique doit être entre 2000 et l'année actuelle.\n")
            return

        self.db_manager.execute_query(
            "INSERT INTO cours (code_cours, nom, debut, fin, session, annee) VALUES (?, ?, ?, ?, ?, ?)",
            (code_cours, nom, debut, fin, session, annee)
        )
        print("Cours enregistré avec succès.")

    def afficher_cours(self):
        """Méthode pour afficher les cours"""
        print("\n", "*" * 10 , "Liste des Cours" , "*" * 10 ,"\n")
        cours = self.db_manager.execute_query("SELECT * FROM cours")
        for cour in cours:
            print(cour)

    def modifier_cours(self):
        """Méthode pour modifier un cours"""
        print("\n", "*" * 10 , "Modifier un Cours", "*" * 10 ,"\n")
        code_cours = input("Entrer le code du cours à modifier : ")
        cours = self.db_manager.execute_query("SELECT * FROM cours WHERE code_cours = ?", (code_cours,))
        if not cours:
            print("Cours non trouvé.")
            return

        nom = input("Nom du cours (laisser vide pour ne pas modifier) : ") or cours[0][1]
        debut = input("Heure de début (laisser vide pour ne pas modifier) : ")
        fin = input("Heure de fin (laisser vide pour ne pas modifier) : ")
        session = input("Session (1 ou 2) (laisser vide pour ne pas modifier) : ")
        annee = input("Année académique (laisser vide pour ne pas modifier) : ")

        debut = int(debut) if debut else cours[0][2]
        fin = int(fin) if fin else cours[0][3]
        session = int(session) if session else cours[0][4]
        annee = int(annee) if annee else cours[0][5]
        code_cours = f"{nom}-session{session}-{annee}".upper()
        
        self.db_manager.execute_query(
            "UPDATE cours SET nom = ?, debut = ?, fin = ?, session = ?, annee = ?, code_cours = ?",
            (nom, debut, fin, session, annee, code_cours)
        )
        print("Cours modifié avec succès.")

    def rechercher_cours(self):
        """Méthode pour rechercher un cours"""
        print("\n", "*" * 10 , "Rechercher un Cours", "*" * 10 ,"\n")
        code_cours = input("Entrer le code du cours à rechercher : ")
        cours = self.db_manager.execute_query("SELECT * FROM cours WHERE code_cours = ?", (code_cours,))
        if cours:
            for cour in cours:
                print(cour)
        else:
            print("Cours non trouvé.")

# Initialisation de la base de données
db_manager1 = DBManager("cours.db")

# Affichage du menu et gestion des cours
manager = Manager(db_manager1)
menu_cours(manager)
