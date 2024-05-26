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

    def add_room(self, room):
        self.rooms.append(room)

    def __repr__(self):
        return f"Bâtiment(nom={self.name}, Nombre_etage={self.floors}, {self.rooms})"

class BuildingManager(Database):
    def __init__(self, db_file):
        super().__init__(db_file)

    def add_building(self, building):
        clear_screen()
        try:
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
        except sqlite3.IntegrityError:
            print(f"Le Batiment '{building.name}' existe déjà.")
        pause_system()

    def update_building_name(self, old_name, new_name):
        clear_screen()
        try:
            succes = self.update_record("buildings", {"name": new_name}, f"name='{old_name}'")
            if len(succes) > 0:
                print(f"Le nom du batiment '{old_name}' est remplacé par '{new_name}'.")
            else:
                print(f"Le nom {old_name} est introuvable.")
        except sqlite3.IntegrityError:
            print(f"Le Batiment '{new_name}' existe déjà.")
        pause_system()

    def update_building_floors(self, name, new_floors):
        clear_screen()
        self.update_record("buildings", {"floors": new_floors}, f"name='{name}'")
        print(f"L'étage du batiment '{name}' a été mis à jour par {new_floors} étages.")
        pause_system()

    def delete_building(self, name):
        self.delete_record("buildings", f"name='{name}'")
        clear_screen()
        print(f"Le batiment '{name}' a été supprimé avec succès.")
        pause_system()

    def list_buildings(self):
        i = 1
        clear_screen()
        print("Liste des batiments et les salles :")
        buildings = self.read_records("buildings")
        for building in buildings:
            print(f"ID : {building[0]}, Nom Batiment : {building[1]}, Nombre d'étages : {building[2]}")
            i = self.list_rooms(building[0], i+1)
        pause_system()

    def list_rooms(self, building_id, i=2):
        rooms = self.read_records("rooms", condition=f"building_id={building_id}")
        for room in rooms:
            print(f" Salle (Etage: {room[2]}, Numéro: {room[3]}, Type: {room[4]}, Capacité: {room[5]})")
        return i+1
        

    def add_room_to_building(self, building_name, room):
        clear_screen()
        building = self.read_records("buildings", columns=["id"], condition=f"name='{building_name}'")
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
            print(f"La salle '{room.number}' a été ajouté dans le batiment '{building_name}' avec succès.")
        else:
            print(f"Pas de batiment avec le nom '{building_name}'.")
        pause_system()
