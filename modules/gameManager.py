# This module defines main entety that handles state of the game world

# external imports
from enum import Enum

# local imports
from modules.actor import Actor, gameCharacter
from modules.mapManager import MapManager

# definitions
ACTIONS = {
    "QUIT": ["exit", "exit game", "quit", ":q"],
    "LOOK": ["look at", "look"],
    "MOVE": ["move", "go"]}

ACTIONS_LOOKUP = {
    alias: action
    for action, aliases in ACTIONS.items()
    for alias in aliases
    }

class GameMode(Enum):
    EXIT = "exit"
    MENU = "system_menu"
    GAME = "in_game"
    DIALOG = "in_dialog"

class WordState():
    def __init__(self):
        self.player = None
        self.current_world = None
        self.current_location = None
        self.current_scene = None

#Game Manager
class GameManager():
    def __init__(self):
        self.mode = GameMode.EXIT
        self.world_state = WordState()
        self.actions: list = []
        self.updates: list = []
        self.history: list = []

    def start(self):
        self.mode = GameMode.MENU
        player = gameCharacter("Lusor Novus", 10, 10, 0, [{"ration", 3}, {"sword", 1}], True)

        mapManager = MapManager()
        mapManager.generate_map(0, player)

    def update(self):
        for action in self.actions:
            # process the action
            self.updates.append(action)
            if action == "QUIT":
                self.mode = GameMode.EXIT

        match self.mode:
            case GameMode.MENU:
                self.mode = GameMode.GAME

    def generate_actions(self, commands: list) -> None:
        commands.reverse()

        self.actions: list = []
        while len(commands) > 0:
            command = commands.pop()

            command.split()

            action = ACTIONS_LOOKUP.get(command[0])
            self.actions.append(action)

    def get_current_mode(self):
        return self.mode

    def get_current_world(self):
        return self.world_state

    def give_updates(self):

        tmp_bfr: list = self.updates.copy()
        self.updates.clear()
        self.history.extend(tmp_bfr)

        return tmp_bfr
