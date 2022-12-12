from utils import *
from tile import Tile


class TilePalette:
    def __init__(self, dict_tilename_id=None):

        # If this tile palette is being loaded from one that already exists
        if dict_tilename_id is not None:
            # Use this set of tiles and maps from tilename to id
            self.dict_tilename_id = dict_tilename_id
        else:
            # If this is a new tilemap, assume the default
            self.dict_tilename_id = TilePalette.load('Tilemap/Tile Palettes/tp_default_palette.json')

        # Stores all the available tiles in a dictionary, accessible by their id, as determined by the palette
        self.tiles = {}
        for tile_file in self.dict_tilename_id.keys():
            tile = Tile.load(tile_file)
            tile.id = self.dict_tilename_id[tile.name]
            self.tiles[tile.id] = tile

    def __getitem__(self, i):
        return self.tiles[i]

    def get_render_info(self):
        surface = pygame.Surface(self.rect.size)
        surface.fill(WHITE)

        return surface, self.rect

    def save(self, filename):
        with open(f'Tilemap/Tile Palettes/tp_{filename}.json', 'w') as outfile:
            json.dump(self.dict_tilename_id, outfile)
            print(f'{outfile.name} saved successfully')

    @staticmethod
    def load(filename):
        with open(f'Tilemap/Tile Palettes/tp_{filename}.json') as json_file:
            data = json.load(json_file)
            tile_palette = TilePalette(data)
            print(f'{json_file.name} loaded successfully')
            return tile_palette
