### Objekty
- (typeof game.map) Mapa:
    - properties:
        - nazev mapy
        - všechny místnosti (typeof game.map.room)
    - actions:
        - přidání místnosti (typeof game.map.room)
        - zobrazení mapy
    - (typeof game.map.room) Místnost:
        - properties:
            - název místnost
            - texty pro místnost
            - obsah místnosti
            - směr
            - všechny pod místnosti  (typeof game.map.room)
        - actions:
            - přidání pod místnosti (typeof game.map.room)
- (typeof game.player) Hráč:
    - properties:
        - nazev hráče
        - inventář
        - pozice na mapě
    - actions:
        - změna pozice na mapě
        - zobrazení inventáře
        - 
- (typeof game) Hra:
    - properties:
        - nazev hry
        - hráč ve hře
        - mapa hry
    - actions:
        - intro hry
        - start hry
        - stop hry
