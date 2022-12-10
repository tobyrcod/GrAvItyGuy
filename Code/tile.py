import pygame.image
from utils import *


class Tile:
    def __init__(self, name: str, sprite_path: str):
        self.name = name
        self.sprite_path = sprite_path

    def get_sprite(self, tile_grid=None):
        return pygame.image.load(f'Assets/Sprites/{self.sprite_path}')

    def save(self, type='base'):
        with open(f'Tilemap/Tiles/tile_{self.name}.json', 'w') as outfile:
            json.dump({
                'name': self.name,
                'sprite_path': self.sprite_path,
                'type': type
            }, outfile)
            print(f'{outfile.name} saved successfully')

    @staticmethod
    def load(filename):
        with open(f'Tilemap/Tiles/tile_{filename}.json') as json_file:
            tile_data = json.load(json_file)
            params = list(tile_data.values())[:-1]
            match tile_data['type']:
                case 'smart':
                    tile = SmartTile(*params)
                case _:
                    tile = Tile(*params)
            print(f'{json_file.name} loaded successfully')
            return tile


class SmartTile(Tile):
    def __init__(self, name: str, sprite_path: str):
        super().__init__(name, sprite_path)
        # sprite path: a tile set of all the sprites this tile an take

    def save(self, **kwargs):
        super().save('smart')

    def get_sprite(self, tile_grid=None):
        if tile_grid is None:
            return  super().get_sprite() # Return the center piece of the tileset

        print('smart')
        sprite_sheet = super().get_sprite()
        return sprite_sheet
