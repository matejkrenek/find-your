import time

from game.map.room import Room

class Map:
    def __init__(self, name, origin:Room = None):
        self.__name = name
        self.__origin = origin

    def room(self, value:Room) -> Room:
        self.__origin = value

        return self.__origin

    def get_origin(self) -> Room:
        return self.__origin

    def name(self) -> str:
        return self.__name

    def get_name(self) -> str:
        return self.__name

    def print(self):
        time.sleep(0.5)
        print("\n")
        if self.__origin:
            self.__origin.print_map()
        print("\n")
        time.sleep(1)
