"""

"""
from modules.contraintes.contraintes import pause_system
from modules.database.database import Database


class Room:
    def __init__(self, number, room_type, room_floor, capacity=60):
        self.number = number
        self.room_type = room_type
        self.room_floor = room_floor
        self.capacity = capacity

    def __repr__(self):
        return f"Salle {self.number} (etage={self.room_floor}, type={self.room_type}, capacité={self.capacity})"

class RoomManager:
    def __init__(self, db_file):
        self.db = Database(db_file)

    def add_room(self, building_name, room):
        """Ajoute une salle à un bâtiment."""
        building = self.db.read_records("buildings", columns=["id"], condition="name=?", params=(building_name,))
        if building:
            building_id = building[0][0]
            if not self.room_exists(building_id, room.room_floor, room.number):
                self.db.create_record("rooms", {
                    "building_id": building_id,
                    "floor": room.room_floor,
                    "number": room.number,
                    "type": room.room_type,
                    "capacity": room.capacity,
                    "disponibility": "disponible"
                })
                print(f"La salle '{room.number}' a été ajoutée dans le bâtiment '{building_name}' avec succès.")
            else:
                print(f"La salle '{room.number}' au {room.room_floor}e étage existe déjà dans le bâtiment '{building_name}'.")
        else:
            print(f"Pas de bâtiment avec le nom '{building_name}'.")
        pause_system()

    def list_rooms(self, building_name):
        """Liste toutes les salles d'un bâtiment."""
        building = self.db.read_records("buildings", columns=["id"], condition="name=?", params=(building_name,))
        if building:
            building_id = building[0][0]
            rooms = self.db.read_records("rooms", condition="building_id=?", params=(building_id,))
            for room in rooms:
                print(room)
        else:
            print(f"Pas de bâtiment avec le nom '{building_name}'.")

    def update_room_disponibility(self, building_name, floor, room_number, disponibility):
        """Met à jour la disponibilité d'une salle."""
        building = self.db.read_records("buildings", columns=["id"], condition="name=?", params=(building_name,))
        if building:
            building_id = building[0][0]
            self.db.update_record("rooms", {"disponibility": disponibility}, "building_id=? AND floor=? AND number=?", (building_id, floor, room_number))
            print(f"La disponibilité de la salle '{room_number}' au {floor}e étage du bâtiment '{building_name}' a été mise à jour.")
        else:
            print(f"Pas de bâtiment avec le nom '{building_name}'.")

    def room_exists(self, building_id, floor, room_number):
        """Vérifie si une salle existe déjà dans un bâtiment pour un étage donné."""
        room = self.db.read_records("rooms", condition="building_id=? AND floor=? AND number=?", params=(building_id, floor, room_number))
        return len(room) > 0

