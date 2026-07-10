# This module defines main entety that handles state of the game world

# external imports
from enum import Enum

# local imports
#from actor import Player

# defenitions
class GameMode(Enum):
    EXIT = "exit"
    MENU = "main_menu"
    GAME = "in_game"

class WordState(Enum):
    UNDEFINED = "primordial chaos"

#Game Manager
class GameManager():
    def __init__(self):
        self.mode = GameMode.EXIT
        self.world_state = WordState.UNDEFINED
        self.actions: list = []

    def start(self):
        self.mode = GameMode.MENU

    def update(self):

        match self.mode:
            case GameMode.MENU:
                self.mode = GameMode.GAME

            case GameMode.GAME:
                self.mode = GameMode.EXIT

    def generate_actions(self, inputs: list) -> None:
        self.actions: list = []
        self.actions.append(inputs.pop())
