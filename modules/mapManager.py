# This module defines location entities to handle world geography and traversal

# external imports

# local imports
from actor import Actor

class MapManager(self)
    def __init__(self, *args, **kwargs):
        pass

    def generate_map(self, seed, player):

        scenes: list = []

        scenes[0] = new Scene(
            "camp",
            "You are standing and abandoned campt, hidden form frozen winds under a giant sharp rock formation.")

        scenes[0]._add_actor(player)
        scenes[1] = new Scene(
            "ruined building",
            "You are looking at stone rouing of small building, probably someone's hom before the long winters came.")

        locations: list = []
        locations[0] = new Location(
            "solitary rock",
            scenes)

        locations[0]._connect_scenes(locations[0].scene[0], "east", locations[0].scene[1], "west")

        worldMap = new WolrdMap(locations)

    def load_map(self, file):
        pass

    def put_player()

# Contains a list of locations - different wapoints, settlements and home city.
class WorldMap():
    def __init__(self, locations):
        self.locations: list = locations

    def _connect_locations(self, location1, location2):
        pass

# locations consist from specific scenes.
class Location():
    def __init__(self, name, scenes = []) -> None:
        self.name = name
        # scenes contained in location
        self.scenes = scenes
        # connections to other locations reachable from the location
        self.passages: list = []

    def _add_scene(self, scene) -> None:
        if scene not in self.scenes:
            self.scenes.append(scene)

    def _connect_scenes(scene1, direction12, scene2, direction21):
        if scene1 in self.scenes and scene2 in self.scenes:
            scene1._add_transition(direction12, scene2)
            scene2._add_transition(direction21, scene1)

class Scene():
    def __init__(self, description = "NOWHERE", interactable = [], actors = [], items = []):
        self.name = name
        self.description: str = description
        self.interactable : list = interactable
        self.actors: list = actors
        self.items: list = items
        self.transitions: dict = {}

    def _add_transition(direction, scene) -> None:
        self.transition[direction] = scene

    def _add_actor(self, new_actor) -> None:
        self.actors.extend(new_actor)

    def _remove_actor(self, actor) -> None:
        if actor in self.actors:
            self.actors.remove(actor)

class Passage():
    # potantially will have some kind of fiel for traversal event genreation logic, but not rn
    def __init__(self, location1, location2, diffcuty, distance)
        self.locations = [location1, location2]
        self.diffcuty = diffcuty
        self.distance = distance
