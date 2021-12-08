from game.helpers import writer
import shutil
import os

class Room:
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

        if(rooms):
            for room in rooms:
                self.add_room(room)
    
    def room(self, room):
        room.parent = self
        self.children.append(room)

        return room

    def doors_direction(self):
        string = ""

        for child in self.children:
            if child.direction:
                string += child.direction["3"] + ", "

        return string

    def is_valid_name(self, string):
        exist = False

        for child in self.children:
            if child.direction and child.name.lower() == string.lower():
                exist = True
            
            if exist:
                return True

    def find_room(self, string):
        for child in self.children:
            if child.name and child.name.lower() == string.lower():
                return child
            
                
    def intro(self, screenplay = None):
        if not screenplay:
            screenplay = self.data["screenplay"]            

        if(isinstance(screenplay, list)):
            for phrase in screenplay:
                formated_phrase = phrase.format(rooms = len(self.children), rooms_directions=self.doors_direction(), player = self._game._player.get_name()).center(shutil.get_terminal_size().columns)
                writer(formated_phrase, 0.05)
                if phrase in self.data["input"]:
                    eval(self.data["input"][phrase])

                    if screenplay.index(phrase) == len(screenplay) - 1:
                        if self.children:
                            self._game.select_direction()
                        else:
                            self._game._player.move(self.parent)

                if screenplay.index(phrase) == len(screenplay) - 1 and phrase not in self.data["input"]:
                    self._game.select_direction()
        else:
            return
    
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

    def ask_questions(self, context):
        os.system("cls")
        for item in context:
            question = item["question"]
            options = item["options"]
            answear = item["answear"]

            writer(question.center(shutil.get_terminal_size().columns), 0.05)

            for option in options:
                print(f"[{options.index(option) + 1}] {option}".center(shutil.get_terminal_size().columns))
        
            prefix = "".ljust(int(shutil.get_terminal_size().columns / 2) - 3)
            choice = int(input(prefix))

            if choice - 1 == answear:
                self._game._player.score[self.name]+=1
            else:
                print("špatná odpověď".center(shutil.get_terminal_size().columns))
                print(f"spravna odpoved je {answear + 1}".center(shutil.get_terminal_size().columns))

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