import shutil

class Player:
    def __init__(self, name):
        self.name = name

    def ask_name(self):
        prefix = "".ljust(int(shutil.get_terminal_size().columns / 2) - 5)
        name = input(prefix)

        self.name = name
    
    def move(self, room):
        self.position = room
        room.intro()
