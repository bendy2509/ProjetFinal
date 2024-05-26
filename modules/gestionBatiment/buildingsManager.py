# gestionBatiment/buildingsManager.py

import sqlite3
from modules.contraintes.contraintes import clear_screen, pause_system
from modules.database.database import Database

class Room:
    def __init__(self, number, room_type, room_floor, capacity=60):
        self.number = number
        self.room_type = room_type
        self.capacity = capacity
        self.room_floor = room_floor

    def __repr__(self):
        return f"Salle {self.number} (etage={self.room_floor}, type={self.room_type}, capacité={self.capacity})"

class Building:
    def __init__(self, name, floors=3, rooms=None):
        self.name = name
        self.floors = floors
        self.rooms = rooms if rooms is not None else []

    def __repr__(self):
        return f"Bâtiment(nom={self.name}, Nombre_etage={self.floors}, {self.rooms})"

class BuildingManager(Database):
    def __init__(self, db_file):
        super().__init__(db_file)

    def add_building(self, building):
        clear_screen()
        if not self.is_building_exist(building.name):
            self.create_record("buildings", {"name": building.name, "floors": building.floors})
            # Récupérer l'ID du bâtiment nouvellement inséré
            building_id = self.execute_query("SELECT last_insert_rowid()")[0][0]
            for room in building.rooms:
                self.create_record("rooms", {
                    "building_id": building_id,
                    "floor": room.room_floor,
                    "number": room.number,
                    "type": room.room_type,
                    "capacity": room.capacity,
                    "disponibility": "disponible"
                })
            print(f"Le batiment '{building.name}' a été ajouté avec succès.")
        else:
            print(f"Le Batiment '{building.name}' existe déjà.")
        pause_system()

    def is_building_exist(self, building_name):
        """Vérifie si un bâtiment avec un nom spécifique existe déjà."""
        building = self.read_records("buildings", columns=["id"], condition="name=?", params=(building_name,))
        return len(building) > 0
    
    def update_building_name(self, old_name, new_name):
        clear_screen()
        if not self.is_building_exist(old_name) and not self.is_building_exist(new_name):
            self.update_record("buildings", {"name": new_name}, f"name='{old_name}'")
            #print(succes)
            #pause_system()
            print(f"Le nom du batiment '{old_name}' est remplacé par '{new_name}'.")
        else:
            print(f"Erreur !! Le Batiment '{new_name}' existe déjà ou  le batiment '{old_name}' est introuvable.")
        pause_system()

    def delete_building(self, name):
        if self.is_building_exist(name):
            building = self.read_records(table="buildings", condition=f"name=?", params=(name,))
            if len(building) > 0:
                building_id = building[0][0]
                self.delete_record(table='rooms', condition=f"building_id={building_id}")
            
            self.delete_record("buildings", f"name='{name}'")
            clear_screen()
            print(f"Le batiment '{name}' a été supprimé avec succès.")
        else:
            print("Ce batiment n'existe pas dans la base !")
        pause_system()

    def list_buildings(self):
        clear_screen()
        print("Liste des batiments et les salles :")
        buildings = self.read_records("buildings")
        for building in buildings:
            print(f"ID : {building[0]}, Nom Batiment : {building[1]}, Nombre d'étages : {building[2]}")
            self.list_rooms(building[0])
        pause_system()

    def list_rooms(self, building_id):
        rooms = self.read_records("rooms", condition=f"building_id={building_id}")
        for room in rooms:
            print(f" Salle (Etage: {room[2]}, Numéro: {room[3]}, Type: {room[4]}, Capacité: {room[5]})")

    def add_room_to_building(self, building_name, room):
        """Pour ajouter une salle dans un batiment"""
        clear_screen()
        if self.is_room_exist(building_name, room.room_floor, room.number):
            print(f"La salle '{room.number}' existe déjà dans le bâtiment '{building_name}' à l'étage {room.room_floor}.")
        else:
            building = self.read_records("buildings", columns=["id"], condition="name=?", params=(building_name,))
            if building:
                building_id = building[0][0]
                self.create_record("rooms", {
                    "building_id": building_id,
                    "floor": room.room_floor,
                    "number": room.number,
                    "type": room.room_type,
                    "capacity": room.capacity,
                    "disponibility": "disponible"
                })
                print(f"La salle '{room.number}' a été ajoutée dans le bâtiment '{building_name}' avec succès.")
            else:
                print(f"Aucun bâtiment trouvé avec le nom '{building_name}'.")
        pause_system()

    def is_room_exist(self, building_name, room_floor, room_number):
        """Vérifie si une salle avec un numéro spécifique existe déjà dans un bâtiment pour un même étage."""
        building = self.read_records("buildings", columns=["id"], condition="name=?", params=(building_name,))
        if building:
            building_id = building[0][0]
            condition = "building_id=? AND floor=? AND number=?"
            params = (building_id, room_floor, room_number)
            existing_room = self.read_records("rooms", columns=["id"], condition=condition, params=params)
            return len(existing_room) > 0
        return False