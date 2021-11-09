from game.helpers import writer
import shutil
import os

class Room:
    _game = None
    DIRECTION = {
        "left": {
            "name": "left",
            "3": "vlevo",
            "4": "doleva",
        },
        "right": {
            "name": "right",
            "3": "vpravo",
            "4": "doprava",
        },
        "straight": {
            "name": "straight",
            "3": "rovně",
            "4": "rovně"
        },
    }

    def __init__(self, name, data = {}, rooms = [], direction = None):
        self.name = name
        self.data = data
        self.children = []
        self.parent = None

        if direction:
            self.direction = self.DIRECTION[direction]
        else:
            self.direction = None

        for room in rooms:
            self.add_room(room)
    
    def add_room(self, room):
        room.parent = self
        self.children.append(room)

    def doors_direction(self):
        string = ""

        for child in self.children:
            if child.direction:
                string += child.direction["3"] + ", "

        return string

    def is_valid_direction(self, string):
        exist = False

        for child in self.children:
            if child.direction and child.direction["name"].lower() == string.lower():
                exist = True
            
            if exist:
                return True

    def find_room(self, string):
        for child in self.children:
            if child.direction and child.direction["name"].lower() == string.lower():
                return child
            
                
    def intro(self, screenplay = None):
        if not screenplay:
            screenplay = self.data["screenplay"]
            

        if(isinstance(screenplay, list)):
            for phrase in screenplay:
                formated_phrase = phrase.format(rooms = len(self.children), rooms_directions=self.doors_direction(), player = self._game._player.name).center(shutil.get_terminal_size().columns)

                writer(formated_phrase, 0.05)
                if phrase in self.data["input"]:
                    eval(self.data["input"][phrase])
        else:
            print("screenplay parameter has to be type of list")
    
    def get_level(self):
        level = 0
        _parent = self.parent

        while _parent:
            level += 1
            _parent = _parent.parent
        
        return level

    def set_game(self, game):
        self._game = game
        self._game.set_game_to_rooms(self)
        
    def print_map(self): 
        direction = ""

        if self.direction:
            direction += " ["
            direction += self.direction["name"]
            direction += "]"

        name = self.name + f'{direction}'
        prefix = "".ljust(int((shutil.get_terminal_size().columns / 2 - 8) + (self.get_level() * 3)))

        print(prefix + name)
        if self.children:
            for child in self.children:
                child.print_map()