class Map:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin
        
    def print(self):
        print("-------------------------")
        print("\t" + self.name)
        print("-------------------------")
        if self.origin:
            self.origin.print_map()
