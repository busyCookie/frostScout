# This module defines all active entities in the game:
# player character/s, hostile and neutral npc/mobs/animals

class Actor():
    def __init__(self,
                 name: str,
                 hp: int,
                 speed: int
                 ) -> None:

        self.name: str = name
        self.current_hp: int = hp
        self.max_hp: int = hp
        self.speed: int = speed

    def get_name() -> str:
        return ""

    def get_hp() -> int:
        return 0

    def get_speed() -> int:
        return 0

    def attack() -> None:
        pass

    def receive_hit() -> None:
        pass

    def heal() -> bool:
        pass


class gameCharacter(Actor):
    def __init__(self,
                 name: str,
                 hp: int,
                 speed: int,
                 talent: int,
                 inventory: list = [],
                 is_player: bool = False
                 ) -> None:

        super().__init__(name, hp, speed)
        self.talent = talent
        self.inventory = inventory
        self.is_player = is_player

    def _is_player(self):
        return self.is_player
