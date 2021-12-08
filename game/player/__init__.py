from game.map.room import Room

import shutil

class Player:
    def __init__(self, name:str) -> None:
        self.__name = name

    def ask_name(self) -> None:
        prefix = "".ljust(int(shutil.get_terminal_size().columns / 2) - 5)
        name = input(prefix)

        self.__name = name

    def name(self) -> str:
        return self.__name

    def get_name(self) -> str:
        return self.__name

    def move(self, room:Room) -> None:
        self.position = room
        room.intro()
