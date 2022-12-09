from utils import *
from tile import Tile


class TilePalette:
    def __init__(self, tiles):
        self.tiles = {}
        for i, tile in enumerate(tiles):
            self.tiles[i + 1] = tile

    def __getitem__(self, i):
        return self.tiles[i]
