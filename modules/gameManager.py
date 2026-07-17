# This module defines main entety that handles state of the game world

# external imports
from enum import Enum

# local imports
from actor import Actor, Player

# defenitions
ACITIONS = {
    "QUIT": ["exit", "exit game", "quit", ":q"],}

class GameMode(Enum):
    EXIT = "exit"
    MENU = "system_menu"
    GAME = "in_game"

class WordState(Enum):
    UNDEFINED = "primordial chaos"

#Game Manager
class GameManager():
    def __init__(self):
        self.mode = GameMode.EXIT
        self.world_state = WordState.UNDEFINED
        self.actions: list = []
        self.updates: list = []
        self.history: list = []

    def start(self):
        self.mode = GameMode.MENU

    def update(self):
        for action in self.actions:
            # process the action
            self.updates.append(action)
            if action == "exit game":
                self.mode = GameMode.EXIT

        match self.mode:
            case GameMode.MENU:
                self.mode = GameMode.GAME

    def generate_actions(self, commands: list) -> None:
        commands.reverse()

        self.actions: list = []
        while len(commands) > 0:
            self.actions.append(commands.pop())

    def get_current_mode(self):
        return self.mode

    def get_current_world(self):
        return self.world_state

    def give_updates(self):

        tmp_bfr: list = self.updates.copy()
        self.updates.clear()
        self.history.extend(tmp_bfr)

        return tmp_bfr
