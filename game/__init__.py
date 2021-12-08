from game.player import Player
from game.map import Map
from game.helpers import writer, fullscreen, font

import time
import os
import sys
import shutil

class Game:
    params = {}
    actions = {}

    def __init__(self, name, data = {}, player:Player = None, map:Map = None):
        self.__name = name
        self.data = data
        self.map(map)
        self.player(player)

        self.init()

    def map(self, map = None):
        if not map:
            return

        if isinstance(map, Map):
            self._map = map

            return self._map
        else:
            print("map parameter has to be type of game.map.Map")

    def set_game_to_rooms(self, room):
        if room.children:
            for child in room.children:
                child.set_game(self)

    def player(self, player = None):
        if not player:
            return
        if isinstance(player, Player):
            self._player = player

            return self._player
        else:
            print("player parameter has to be type of game.player.Player")

    def select_direction(self):
        for child in self._player.position.children:
            if child.direction:
                print(f"{child.name}[{self._player.score[child.name]}/{len(child.data['data']['quiz'])}]".center(shutil.get_terminal_size().columns))
        
        prefix = "".ljust(int(shutil.get_terminal_size().columns / 2) - 3)
        choice = input(prefix)
        
        if self._player.position.is_valid_name(choice):
            room = self._player.position.find_room(choice)
            time.sleep(0.5)
            print("*otevírání dvěří*".center(shutil.get_terminal_size().columns))
            time.sleep(0.5)
            self._player.move(room)
        else:
            print("\n")
            print("Jseš si jistý?".center(shutil.get_terminal_size().columns))
            print("\n")
            self.select_direction()


    def intro(self, screenplay = None):
        if not screenplay:
            screenplay = self.data["screenplay"]

        if(isinstance(screenplay, list)):
            for phrase in screenplay:
                formated_phrase = phrase.format(player = self._player.name()).center(shutil.get_terminal_size().columns)

                writer(formated_phrase, 0.05)
                if phrase in self.data["input"]:
                    eval(self.data["input"][phrase])
        else:
            print("screenplay parameter has to be type of list")

        self.init_player()

        time.sleep(1)
        os.system("cls")

    def init_player(self):
        self._player.score = {}
        origin = self._map.get_origin()

        for room in origin.children:
            self._player.score[room.name] = 0


    def name(self):
        return self.__name

    def screenplay(self):
        return self.data["screenplay"]

    def outro(self):
        time.sleep(1)
        os.system("cls")
        time.sleep(1)
        self.start()

    def start(self):
        origin = self._map.get_origin()
        origin.set_game(self)
        self.set_game_to_rooms(self._map.get_origin())
        self.intro()
        self._player.move(self._map.get_origin())

    def stop(self):
        self.outro()

    def finish(self):
        time.sleep(1)
        os.system("cls")
        time.sleep(1)
        sys.exit(0)

    def room_iterate(self, rooms:list, origin = None, Room = None):
        for idx in range(len(rooms)):      
            room = rooms[idx]  

            new_room = origin.room(Room(room["name"], {
                "screenplay": room["screenplay"],
                "input": room["input"],
                "data": room["data"]
            }, None, room["direction"]))
            

            if "rooms" in room:
                self.room_iterate(room["rooms"], new_room, Room)

    def init(self):
        font()
        fullscreen()
        
        time.sleep(0.5)
        os.system("cls")
