import time

class Map:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def print(self):
        time.sleep(0.5)
        print("\n")
        if self.origin:
            self.origin.print_map()
        print("\n")
        time.sleep(1)
