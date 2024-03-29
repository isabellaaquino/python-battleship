from enum import Enum
from typing import List
from tile import Tile, TileState


class ShipType(Enum):
    PORTA_AVIOES = 5
    NAVIOS_TANQUE = 4
    CONTRATORPEDEIRO = 3
    SUBMARINO = 2

class Ship:

    def __init__(self, type: ShipType) -> None:
        self.player = None # Player attribute starts as None because it'll be set in the future after checking if the board is valid
        self.type = type
        self.tiles = []

    def get_tiles(self) -> List[Tile]:
        return self.tiles

    def set_tiles(self, tiles: List[Tile]) -> None:
        self.tiles = tiles

    def get_type(self) -> ShipType:
        return self.type

    def set_player(self, player: 'Player'):
        self.player = player
    
    @property
    def is_alive(self) -> bool:
        # Check if all the tiles were hit
        tiles_states = [tile.get_state().name for tile in self.get_tiles()]
        # The quantity of hit tiles is the same of the ship size
        return tiles_states.count(TileState.HIT.name) != ShipType[self.get_type()].value

