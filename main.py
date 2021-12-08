from game import Game
from game.player import Player
from game.map import Map
from game.map.room import Room

from game_config import GAME, PLAYER, MAP, ROOMS

game:Game = Game(GAME.name, {"screenplay": GAME.screenplay, "input": GAME.input})
player:Player = game.player(Player(PLAYER.name))
map:Map = game.map(Map(MAP.name))
rooms:list[Room] = game.room_iterate(ROOMS, map, Room)

if __name__ == "__main__":
    game.start()