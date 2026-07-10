#handles user inputs and outputs.

# external imports
import os

# local imports
from modules.gameManager import GameMode, WordState

class UI():
    def __init__(self):
        pass

    def get_inputs(self) -> list:
        inputs: list = []

        command = input("your word is my command:")

        inputs.append(command)

        return inputs

    def refresh(self):
        os.system('cls||clear')

    def update(self, game_state, world_state):
        print("new screen")
        print(game_state)
        print(world_state)
