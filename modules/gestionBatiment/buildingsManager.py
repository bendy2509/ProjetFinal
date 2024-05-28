"""
Module pour gérer les bâtiments et leurs salles associées.
"""
from modules.contraintes.contraintes import clear_screen, pause_system
from modules.database.database import Database
from modules.gestionSalle.roomManager import RoomManager

class Building:
    """
    Classe représentant un bâtiment.
    """
    def __init__(self, name, floors=3, rooms=None):
        """
        Initialise un nouveau bâtiment.

        :param name: Nom du bâtiment.
        :param floors: Nombre d'étages du bâtiment.
        :param rooms: Liste des salles dans le bâtiment.
        """
        self.name = name
        self.floors = floors
        self.rooms = rooms if rooms is not None else []

    def __repr__(self):
        """
        Représentation en chaîne de caractères du bâtiment.

        :return: Description textuelle du bâtiment.
        """
        return f"Bâtiment(nom={self.name}, Nombre_etage={self.floors}, {self.rooms})"

class BuildingManager(Database):
    """
    Classe pour gérer les opérations liées aux bâtiments dans la base de données.
    """
    def __init__(self, DB_FILE):
        """
        Initialise le gestionnaire de bâtiments avec la base de données.

        :param DB_FILE: Chemin vers le fichier de base de données SQLite.
        """
        super().__init__(DB_FILE)
        self.room_manager = RoomManager(DB_FILE)

    def add_building(self, building):
        """
        Ajoute un bâtiment à la base de données.

        :param building: Objet Building représentant le bâtiment à ajouter.
        """
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
            print(f"Le bâtiment '{building.name}' a été ajouté avec succès.")
        else:
            print(f"Le Bâtiment '{building.name}' existe déjà.")
        pause_system()

    def is_building_exist(self, building_name):
        """
        Vérifie si un bâtiment avec un nom spécifique existe déjà.

        :param building_name: Nom du bâtiment à vérifier.
        :return: True si le bâtiment existe, False sinon.
        """
        building = self.read_records("buildings", columns=["id"], condition="name=?", params=(building_name,))
        return len(building) > 0
    
    def update_building_name(self, old_name, new_name):
        """
        Met à jour le nom d'un bâtiment.

        :param old_name: Ancien nom du bâtiment.
        :param new_name: Nouveau nom du bâtiment.
        """
        clear_screen()
        if not self.is_building_exist(old_name) and not self.is_building_exist(new_name):
            self.update_record("buildings", {"name": new_name}, f"name='{old_name}'")
            print(f"Le nom du bâtiment '{old_name}' est remplacé par '{new_name}'.")
        else:
            print(f"Erreur !! Le Bâtiment '{new_name}' existe déjà ou le bâtiment '{old_name}' est introuvable.")
        pause_system()

    def delete_building(self, name):
        """
        Supprime un bâtiment de la base de données.

        :param name: Nom du bâtiment à supprimer.
        """
        if self.is_building_exist(name):
            building = self.read_records(table="buildings", condition=f"name=?", params=(name,))
            if len(building) > 0:
                building_id = building[0][0]
                # Supprimer toutes les salles associées au bâtiment
                self.delete_record(table='rooms', condition=f"building_id={building_id}")
            
            self.delete_record("buildings", f"name='{name}'")
            clear_screen()
            print(f"Le bâtiment '{name}' a été supprimé avec succès.")
        else:
            print("Ce bâtiment n'existe pas dans la base !")
        pause_system()

    def add_room_to_building(self, building_name, room):
        """
        Utilise RoomManager pour ajouter une salle à un bâtiment.

        :param building_name: Nom du bâtiment.
        :param room: Objet Room représentant la salle à ajouter.
        """
        self.room_manager.add_room(building_name, room)

    def list_building_rooms(self, building_name):
        """
        Utilise RoomManager pour lister toutes les salles d'un bâtiment.

        :param building_name: Nom du bâtiment.
        """
        self.room_manager.list_rooms(building_name)

    def list_buildings(self):
        """
        Liste tous les bâtiments et leurs salles associées.
        """
        clear_screen()
        print("Liste des bâtiments et les salles :")
        buildings = self.read_records("buildings")
        for building in buildings:
            print(f"ID : {building[0]}, Nom Bâtiment : {building[1]}, Nombre d'étages : {building[2]}")
            self.list_building_rooms(building[1])
        pause_system()

    def is_room_exist(self, building_name, room_floor, room_number):
        """
        Vérifie si une salle avec un numéro spécifique existe déjà dans un bâtiment pour un même étage.

        :param building_name: Nom du bâtiment.
        :param room_floor: Étage de la salle.
        :param room_number: Numéro de la salle.
        :return: True si la salle existe, False sinon.
        """
        building = self.read_records("buildings", columns=["id"], condition="name=?", params=(building_name,))
        if building:
            building_id = building[0][0]
            condition = "building_id=? AND floor=? AND number=?"
            params = (building_id, room_floor, room_number)
            existing_room = self.read_records("rooms", columns=["id"], condition=condition, params=params)
            return len(existing_room) > 0
        return False
