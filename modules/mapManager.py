# This module defines location entities to handle world geography and traversal

# external imports

# local imports
from actor import Actor

class MapManager(self)
    def __init__(self, *args, **kwargs):
        pass

    def generate_map(self, seed):

        scenes: list = []

        scenes[0] = new Scene(
            "You are standing and abandoned campt, hidden form frozen winds under a giant sharp rock formation")
        scenes[1] = new Scene(
            "You are standing and abandoned campt, hidden form frozen winds under a giant sharp rock formation")


    def load_map(self, file):
        pass


# Contains a list of locations - different wapoints, settlements and home city.
class WorldMap():
    def __init__(self, locations):
        self.locations: list = locations

    def _connect_locations(self, location1, location2):
        pass

# locations consist from specific scenes.
class Location():
    def __init__(self, scenes, connections) -> None:
        # scenes contained in location
        self.scenes = scenes
        # connections to other locations reachable from the location
        self.connections: list = connections

    def _connect_scenes(scene1, scene2, direction12, direction21):
        if scene1 in self.scenes and scene2 in self.scenes:
            scene1._add_transition(direction12, scene2)
            scene2._add_transition(direction21, scene1)

class Scene():
    def __init__(self, description = "NOWHERE", interactable = [], actors = [], items = []):
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
