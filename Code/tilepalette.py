from utils import *
from tile import Tile


class TilePalette:
    def __init__(self, dict_tilename_id=None):

        if dict_tilename_id is not None:
            self.dict_tilename_id = dict_tilename_id
        else:
            self.dict_tilename_id = TilePalette.load('tp_default_palette.json')

        self.tiles = {}
        for tile_file in self.dict_tilename_id.keys():
            tile = Tile.load(tile_file)
            self.tiles[self.dict_tilename_id[tile.name]] = tile

    def __getitem__(self, i):
        return self.tiles[i]

    def save(self, filename):
        with open(f'tp_{filename}.json', 'w') as outfile:
            json.dump(self.dict_tilename_id, outfile)
            print(f'{outfile.name} saved successfully')

    @staticmethod
    def load(filename):
        with open(f'tp_{filename}.json') as json_file:
            data = json.load(json_file)
            tile_palette = TilePalette(data)
            print(f'{json_file.name} loaded successfully')
            return tile_palette
