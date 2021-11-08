class Map:
    def __init__(self, data):
        self.data = data
        self.rooms = []

    def add_room(self, room):
        room.parent = self
        self.rooms.append(room)

    def print_map(self):
        pass

class Room:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None