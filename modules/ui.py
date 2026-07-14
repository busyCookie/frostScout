#handles user inputs and outputs.

# external imports
import os

# local imports
from modules.gameManager import GameMode, WordState

class UI():
    def __init__(self):
        pass

    def _parse_inputs(self, inputs_list: list, separator: str):
        work_list: list = []
        index: int = 0

        while index < len(inputs_list):
            current_split: list = inputs_list[index].split(separator)
            work_list.extend(current_split)

            index += 1

        for index in range(0, len(work_list)):
            item = work_list[index]
            item = item.strip()
            item = item.lower()
            work_list[index] = item

        return work_list

    def _get_commands(self, inputs: list) -> list:

        separators: list = [".", ";", ",", "and"]
        work_list = inputs

        for separator in separators:
            work_list = self._parse_inputs(work_list, separator)

        return work_list

    # gets player inputs and parses them into commands that can be later validated and process by game manager
    def get_player_commands(self) -> list:
        inputs = input("your word is my command: \n")
        inputs = [inputs]

        commands = self._get_commands(inputs)

        return commands

    def refresh(self):
        os.system('cls||clear')

    def update(self, gm):
        print("------------------------------")
        print("new screen")
        print(f"Current game mode: {gm.get_current_mode()}")

        updates = gm.give_updates()
        print(f"Updates since last turn:")
        for update in updates:
            print(f"* {update}")
        print(f"Current world state {gm.get_current_world()}")
        #print("\n")
