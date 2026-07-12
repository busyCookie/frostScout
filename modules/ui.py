#handles user inputs and outputs.

# external imports
import os

# local imports
from modules.gameManager import GameMode, WordState

class UI():
    def __init__(self):
        pass

    def _parse_inputs(self, inputs: list) -> list:
        inputs_list = inputs.split(".")

        i: int = 0
        while i < len(inputs_list):
            before_list = inputs_list[:i]
            current_list = inputs_list[i].split(",")
            after_list = inputs_list[i+1:]

            inputs_list = before_list
            inputs_list.extend(current_list)
            inputs_list.extend(after_list)
            i += 1

        i: int = 0
        while i < len(inputs_list):
            before_list = inputs_list[:i]
            current_list = inputs_list[i].split(";")
            after_list = inputs_list[i+1:]

            inputs_list = before_list
            inputs_list.extend(current_list)
            inputs_list.extend(after_list)
            i += 1

        return inputs_list

    # gets player inputs and parses them into commands that can be later validated and process by game manager
    def get_player_commands(self) -> list:
        inputs: list = []
        inputs = input("your word is my command: \n")

        commands = self._parse_inputs(inputs)

        return commands

    def refresh(self):
        os.system('cls||clear')

    def update(self, gm):
        print("new screen")
        print(f"Current game mode: {gm.get_current_mode()}")

        updates = gm.give_updates()
        print(f"Updates since last turn:\n")
        for update in updates:
            print(f"* {update}")
        print(f"Current world state {gm.get_current_world()}")
