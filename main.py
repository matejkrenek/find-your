# game modules
from game import Game

# player modules
from game.player import Player

# map modules
from game.map import Map
from game.map.room import Room

map = Map("Mapa hry", 
    Room("Hlavní hala", [
        Room("kuchyně", [
            Room("Jindrův dvůr", [

            ]),
            Room("Ozynov", [

            ]),
        ]),
        Room("postelová místnost", [
            Room("chlíveček", [

            ]),
            Room("prdelov", [

            ]),
        ]),
        Room("koupelna", [
            Room("pokojiček", [

            ])
        ]),
    ])
)

map.print()
