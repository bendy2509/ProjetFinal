"""
Modules pour la gestion d'horaires des salles
"""
from modules.contraintes.contraintes import clear_screen, pause_system, saisir_duration
from modules.database.database import Database
from modules.gestionCours.course_manager import Course_Manager
from modules.gestionSalle.roomManager import RoomManager

class Schedule_Manager:
    """Gestion des horaires des salles"""

    def __init__(self, db_file):
        self.db_manager = Database(db_file)
        self.roomManager = RoomManager(db_file)
        self.course_manager = Course_Manager(db_file)

    def ajouter_horaire(self):
        """Ajoute un horaire pour une salle"""
        clear_screen()
        print("\n", "*" * 10 , "Ajouter Horaire" , "*" * 10 ,"\n")
        salle = input("Numéro de la salle : ")
        if not self.roomManager.room_exists(salle):
            print("Erreur : Salle non trouvée.")
            pause_system()
            return
        
        jour = input("Jour (lundi, mardi, etc.) : ").lower()
        debut = saisir_duration("Durée (ex : 3) : ")
        code_cours = input("Code du cours : ")

        if not self.course_manager.verifier_existence_cours(code_cours):
            print("Erreur : Cours non trouvé.")
            pause_system()
            return
        
        cours = self.db_manager.read_records(
            table='cours',
            condition="code_cours=?",
            params=(code_cours,)
        )
        fin = debut + cours[0][3]

        if self.verifier_disponibilite(salle, jour, debut, fin):
            print(f"La salle {salle} est occupée de {debut}h00 à {fin}h00 le {jour}.")
            pause_system()
            return

        self.db_manager.create_record(
            "schedules",
            {
                "room_number": salle,
                "jour": jour,
                "debut": debut,
                "fin": fin,
                "cours_id": code_cours
            }
        )
        print("Horaire ajouté avec succès.")

    def afficher_horaire(self, salle):
        """
        Affiche l'horaire d'une salle sous forme de tableau.

        :param salle: Numéro ou identifiant de la salle dont on veut afficher l'horaire.
        """
        jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]
        heures = range(8, 19)  # Horaires de 8h à 18h
        horaire = {heure: {jour: "" for jour in jours} for heure in heures}

        horaires = self.db_manager.read_records(
            table="schedules",
            condition="room_number=?",
            params=(salle,)
        )

        # Remplissage de l'horaire avec les données de la base de données
        for entry in horaires:
            jour, debut, fin, cours = entry[2], entry[3], entry[4], entry[5]
            for heure in range(debut, fin):
                horaire[heure][jour] = cours

        # Affichage de l'horaire
        clear_screen()
        if len(horaires) > 0:
            print("\n", "*" * 10 , f"Horaire de la salle {salle}" , "*" * 10 ,"\n")
            print("Heure | " + "\t | ".join(jours))
            print("-" * 50)
            for heure in heures:
                cours_par_jour = [horaire[heure][jour] for jour in jours]
                print(f"{heure:02d}h  | " + "\t | ".join(cours_par_jour))

            print("\n" + "-" * 50)
            print("Légende :")
            print("- Heures indiquées sans cours sont disponibles.")
            print("- Cours indiqués sont occupés à cette heure.")
        else:
            print("Aucune horaire trouvée.")
        
        pause_system()

    def verifier_disponibilite(self, salle, jour, debut, fin):
        """
        Vérifie si une salle est disponible à un horaire donné.

        Cette méthode interroge la base de données pour vérifier si la salle spécifiée est libre 
        pendant une plage horaire donnée. La vérification est faite en comparant les horaires 
        d'occupation existants avec l'horaire demandé.

        :param salle: Numéro ou identifiant de la salle à vérifier.
        :param jour: Jour de la semaine pour lequel vérifier la disponibilité (ex. 'lundi').
        :param debut: Heure de début de l'occupation demandée (en format 24 heures, par exemple 9 pour 9h00).
        :param fin: Heure de fin de l'occupation demandée (en format 24 heures, par exemple 11 pour 11h00).

        :return: True si la salle est occupée pendant la plage horaire donnée, False sinon.

        Les conditions vérifiées sont :
        - Si la salle est déjà occupée avant l'heure de début demandée mais se libère pendant ou après l'heure de début demandée.
        - Si la salle est occupée avant ou à l'heure de fin demandée mais se libère pendant ou après l'heure de fin demandée.
        
        Exemple d'utilisation :
        ```
        if self.verifier_disponibilite('A101', 'lundi', 9, 11):
            print("La salle A101 est occupée de 9h00 à 11h00 le lundi.")
        else:
            print("La salle A101 est disponible de 9h00 à 11h00 le lundi.")
        ```
        """
        horaires = self.db_manager.read_records(
            table="schedules",
            condition="room_number=? AND jour=? AND ((debut <= ? AND fin > ?) OR (debut < ? AND fin >= ?))",
            params=(salle, jour, debut, debut, fin, fin)
        )
        return bool(horaires)

