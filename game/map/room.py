class Room:
    def __init__(self, name, rooms = []):
        self.name = name
        self.children = []
        self.parent = None

        for room in rooms:
            self.add_room(room)
    
    def add_room(self, room):
        room.parent = self
        self.children.append(room)

    def get_level(self):
        level = 0
        _parent = self.parent

        while _parent:
            level += 1
            _parent = _parent.parent
        
        return level
        
    def print_map(self):
        spaces = "  " * self.get_level() * 1
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.name)

        if self.children:
            for child in self.children:
                child.print_map()