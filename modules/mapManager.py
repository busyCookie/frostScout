# This module defines location entities to handle world geography and traversal

# external imports

# local imports
from actor import Actor

# Manages a list of locations - different wapoint, settlements and home city. All locations
class WorldMap():
    def __init__(self):
        self.locations: list = []


# locations consist from specific scenes.
class Location():
    def __init__(self, scenes, connections) -> None:
        # scenes contained in location
        self.scenes = scenes
        # connections to other locations reachable from the location
        self.connections: list = connections

class Scene():
    def __init__(self, description, interactable, actors, items, connections):
        self.description: str = description
        self.interactable : list = interactable
        self.actors: list = actors
        self.items: list = items
        self.connections: list = connections

    def _add_actor(self, new_actor) -> None:
        self.actors.extend(new_actor)

    def _remove_actor(self, actor) -> None:
        if actor in self.actors:
            self.actors.remove(actor)

class Connection():
    def __init__(self, to_location, diffcuty, distance)
        self.to_location
