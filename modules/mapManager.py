# This module defines location entities to handle world geography and traversal

# external imports

# local imports
from modules.actor import Actor

class MapManager():
    def __init__(self, *args, **kwargs):
        pass

    def generate_map(self, seed, player):

        scenes: list = []

        scenes.append(Scene(
            "camp",
            "You are standing at abandoned camp, which is hiding form frozen winds under a giant sharp rock formation."))

        scenes.append(Scene(
            "ruined building",
            "You are looking at stone ruins of a small building. Probably it was someone's home, before the long winters came."))

        locations: list = []
        locations.append(Location(
            "solitary rock",
            scenes))

        for scene in locations[0].scenes:
            console.log(f"index: {locations[0].scenes.index(scene)}")

        #locations[0]._connect_scenes(locations[0].scenes[0], "east", locations[0].scenes[1])
        #locations[0]._connect_scenes(locations[0].scenes[1], "west", locations[0].scenes[0])

        worldMap = WorldMap("frolstaland", locations, scenes[0])
        worldMap._launch_player(player)

    def load_map(self, file):
        pass

# Contains a list of locations - different wapoints, settlements and home city.
class WorldMap():
    def __init__(self, name, locations, start_scene):
        self.name = name
        self.locations: list = locations
        self.start_scene = start_scene

    def _connect_locations(self, location1, location2):
        pass

    def _launch_player(self, player):
        for location in self.locations:
            for scene in location.scenes:
                for actor in scene.actors:
                    if actor._is_player():
                        raise Exception("Player already present in the game world")

        self.start_scene._add_actor(player)

# locations consist from specific scenes.
class Location():
    def __init__(self, name, world = None, scenes = []) -> None:
        self.name = name
        self.world = world
        # scenes contained in location
        self.scenes = scenes
        # connections to other locations reachable from the location
        self.passages: list = []

    def _add_scene(self, scene) -> None:
        if scene not in self.scenes:
            self.scenes.append(scene)

        if scene.parent != self:
            scene

    def _connect_scenes(scene1, direction, scene2):
        if scene1 in self.scenes and scene2 in self.scenes:
            scene1._add_transition(direction, scene2)

class Scene():
    def __init__(self, name, description = "NOWHERE", interactable = [], actors = [], items = []):
        self.name = name
        self.parent = None
        self.description: str = description
        self.interactable : list = interactable
        self.actors: list = actors
        self.items: list = items
        self.tags: list = []
        self.transitions: dict = {}

    def _add_transition(direction, scene) -> None:
        self.transition[direction] = scene

    def _add_actor(self, new_actor) -> None:
        self.actors.append(new_actor)

    def _remove_actor(self, actor) -> None:
        if actor in self.actors:
            self.actors.remove(actor)

class Passage():
    # potantially will have some kind of fiel for traversal event genreation logic, but not rn
    def __init__(self, location1, location2, diffcuty, distance):
        self.locations = [location1, location2]
        self.diffcuty = diffcuty
        self.distance = distance
