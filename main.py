# game modules
from game import Game

# player modules
from game.player import Player

# map modules
from game.map import Map
from game.map.room import Room

game = Game("Hra", {
    "screenplay": [
        "ahoj, {player}."
    ],
    "input": {
        "nejprve mi řekni jak se jmenuješ ty šupáku": "self._player.ask_name()"
    }
})
game.map(
    Map("Mapa hry", 
        Room("Hlavní hala", {
                "screenplay": [
                    "Ok, jsi na začátku jsou tady {rooms} místnost/místnosti",
                ],
                "input": {
                    "Ok, jsi na začátku jsou tady {rooms} místnost/místnosti": "self._game.select_direction()"
                }
            }, 
            [
            Room("kuchyně", {
                "screenplay": [
                    "kuchyně",
                ],
                "input": {}
            }, [
                Room("Jindrův dvůr", {}, [], "left"),
                Room("Ozynov", {}, [], "right"),
            ], "left"),
            Room("postelová místnost", {
                "screenplay": [
                    "postelová místnost",
                ],
                "input": {}
            }, [
                Room("chlíveček", {}, [], "straight"),
                Room("prdelov", {}, [], "left"),
            ], "right"),
            Room("koupelna", {
                "screenplay": [
                    "koupelna",
                ],
                "input": {}
            }, [
                Room("pokojiček", {}, [], "straight")
            ], "straight"),
        ])
    )
)
game.player(Player("hrač 1"))

if __name__ == "__main__":
    game.start()