"""
Module pour gérer les salles dans un bâtiment.
"""
from modules.contraintes.contraintes import pause_system
from modules.database.database import Database

class Room:
    """
    Classe représentant une salle.
    """
    def __init__(self, number, room_type, room_floor, statut, capacity=60):
        """
        Initialise une nouvelle salle.

        :param number: Numéro de la salle.
        :param room_type: Type de la salle (salle de cours, salle virtuelle, labo).
        :param room_floor: Étage où se trouve la salle.
        :param capacity: Capacité de la salle (nombre de places).
        """
        self.number = number
        self.room_type = room_type
        self.room_floor = room_floor
        self.capacity = capacity
        self.statut = statut

    def __repr__(self):
        """
        Représentation en chaîne de caractères de la salle.

        :return: Description textuelle de la salle.
        """
        return f"Salle {self.number} (type={self.room_type}, capacité={self.capacity}, statut={self.statut})"

class RoomManager:
    """
    Classe pour gérer les opérations liées aux salles dans la base de données.
    """
    def __init__(self, DB_FILE):
        """
        Initialise le gestionnaire de salles avec la base de données.

        :param DB_FILE: Chemin vers le fichier de base de données SQLite.
        """
        self.db = Database(DB_FILE)

    def add_room(self, building_name, room):
        """
        Ajoute une salle à un bâtiment.

        :param building_name: Nom du bâtiment.
        :param room: Objet Room représentant la salle à ajouter.
        """
        building = self.db.read_records("buildings", columns=["id"], condition="name=?", params=(building_name,))
        if building:
            building_id = building[0][0]
            if not self.room_exists(room.number):
                self.db.create_record("rooms", {
                    "number": room.number,
                    "building_id": building_id,
                    "floor": room.room_floor,
                    "type": room.room_type,
                    "capacity": room.capacity,
                    "statut": room.statut
                })
                print(f"La salle '{room.number}' a été ajoutée dans le bâtiment '{building_name}' avec succès.")
            else:
                print(f"La salle '{room.number}' existe déjà dans le bâtiment '{building_name}'.")
        else:
            print(f"Pas de bâtiment avec le nom '{building_name}'.")
        pause_system()

    def list_rooms(self, building_name):
        """
        Liste toutes les salles d'un bâtiment.

        :param building_name: Nom du bâtiment.
        """
        building = self.db.read_records("buildings", columns=["id"], condition=f"name='{building_name}'")
        if building:
            building_id = building[0][0]
            rooms = self.db.read_records("rooms", condition=f"building_id={building_id}")
            if rooms:
                print(f"Salles dans le bâtiment '{building_name}':")
                for room in rooms:
                    print(f"Salle {room[0]}, Type: {room[3]}, Capacité: {room[4]}, Statut: {room[5]}")
            else:
                print(f"Aucune salle trouvée dans le bâtiment '{building_name}'.")
        else:
            print(f"Pas de bâtiment avec le nom '{building_name}'.")

    def update_room_disponibility(self, room_number, disponibility):
        """
        Met à jour la disponibilité d'une salle.

        :param room_number: Numéro de la salle.
        :param disponibility: Nouvelle disponibilité de la salle.
        """
        if self.room_exists(room_number):
            self.db.update_record("rooms", {"disponibility": disponibility}, "number='{room_number}'")
            print(f"La disponibilité de la salle '{room_number}' a été mise à jour.")

    def room_exists(self, room_number):
        """
        Vérifie si une salle existe déjà dans un bâtiment pour un étage donné.

        :param room_number: ID de la salle.
        """
        room = self.db.read_records("rooms", condition="number=?", params=(room_number,))
        return len(room) > 0

    def delete_room_from_building(self, room_number):
        """
        Supprime une salle d'un bâtiment.

        :param room_number: Numéro(ID) de la salle à supprimer.
        """
        try:        
            # Vérifier si la salle existe dans le bâtiment
            room = self.db.read_records("rooms", condition="number=?", params=(room_number))
            if not room:
                print(f"La salle '{room_number}' n'existe pas.")
                return

            # Supprimer la salle
            self.db.delete_record(table="rooms", condition="number=?", params=(room[0][0],))
            print(f"La salle '{room_number}' a été supprimée avec succès.")

        except:
            print("Erreur lors de la suppression de la salle")
        finally:
            pause_system()

