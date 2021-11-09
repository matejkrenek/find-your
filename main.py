# game modules
from game import Game

# player modules
from game.player import Player

# map modules
from game.map import Map
from game.map.room import Room

game = Game("Hra", {
    "screenplay": [
        "Nazdar Gandalfe...",
        "Oh, ty nejsi gandalf",
        "Nebo ano?",
        "Já nevím",
        "Hele víš ty co?",
        "Radši mi řekni jak se jmenuješ:",
        "Dobře, budu tě tedy nazývat tímto hloupím jménem",
        "Předem se ti ale omlouvám...",
        "Neumím skloňovat",
        "Matěj mě to nenaučil",
        "{player} být hodný",
        "{player} za moment dostat mapu",
        "Víš proč?",
        "Vidím ti to totiž na očích",
        "Oh, ano",
        "Máš neskuteční hlad",
        "Takže...",
        "Víš kam se musíš dostat?",
        "Je to tak",
        "Do kuchyně",
        "Ale nevím jestli tam pro tebe něco zbylo",
        "Tady je ta mapa {player}",
        "Radši si ji pořádně prohlédni",
        "Stačí jedna chyba a jedeš znovu",
        "A věř mi...",
        "Nechceš toto vidět znova"

    ],
    "input": {
        "Radši mi řekni jak se jmenuješ:": "self._player.ask_name()",
        "Tady je ta mapa {player}": "self._map.print()",
    }
})
game.map(
    Map("Mapa hry", 
        Room("Rozcestník", {
                "screenplay": [
                    "Tak hele",
                    "Jsou tady {rooms} dveře",
                    "Viděl jsi mapu...",
                    "Byl by jsi fakt ňouma, kdyby jsi něco pokazil {player}",
                ],
                "input": {
                    "Byl by jsi fakt ňouma, kdyby jsi něco pokazil {player}": "self._game.select_direction()"
                }
            }, 
            [
            Room("Mordor", {
                "screenplay": [
                    "Tak hele...",
                    "Tohle jsme si nedomluvili",
                    "Vždyť jsi říkal, že nejsi Gandalf",
                    "Chceš snad do Temné věže?",
                    "Tak to jsi si asi spletl Hru",
                    "Čus...",
                ],
                "input": {
                    "Čus...": "self._game.stop()"
                }
            }, [
                Room("Temná věž", {}, [], "left"),
                Room("Hora stínu", {}, [], "right"),
                Room("Jezero Nurnen", {}, [], "straight"),
            ], "left"),
            Room("Varna", {
                "screenplay": [
                    "Jesse...",
                    "Hej Jesse...",
                ],
                "input": {
                    "Hej Jesse...": "self._game.stop()"
                }
            }, [
                Room("Sklad", {}, [], "straight"),
                Room("Chlaďák na Metamfetamin", {}, [], "left"),
            ], "right"),
            Room("Koupelna", {
                "screenplay": [
                    "Je pravda, že sprchu by jsi potřeboval {player}",
                    "Kvůli tomu tady ale nejsi",
                    "Takže...",
                    "Kam teď?",
                ],
                "input": {
                    "Kam teď?": "self._game.select_direction()"
                }
            }, [
                Room("Pokoj na spaní pro osamocené", {
                    "screenplay": [
                        "Cítíš se sám {player}?",
                        "A ospále",
                        "Hele, ani se ti nedivím, když hraješ tuto hru"
                    ],
                    "input": {
                        "Hele, ani se ti nedivím, když hraješ tuto hru": "self._game.stop()"
                    }
                }, [], "straight"),
                Room("Plavací hala", {
                    "screenplay": [
                        "dneska není čtvrtek..."
                    ],
                    "input": {
                        "dneska není čtvrtek...": "self._game.stop()"
                    }
                }, [], "left"),
                Room("Kuchyně", {
                    "screenplay": [
                        "{player}...",
                        "Ty tu maturitu možná i uděláš",
                        "Nevěřil jsem, že to dokážeš",
                        "...",
                        "...",
                        "Ups",
                        "Nic tady není co?",
                        "R.I.P.",
                    ],
                    "input": {
                        "R.I.P.": "self._game.finish()"
                    }
                }, [], "right"),
            ], "straight"),
        ])
))

game.player(Player("idk"))
if __name__ == "__main__":
    game.start()