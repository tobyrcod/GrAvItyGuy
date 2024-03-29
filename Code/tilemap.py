import pygame
from tile import Tile
from tilepalette import TilePalette
from utils import *


class Tilemap:  # currently indexed with [x][y]

    def __init__(self, width: int, height: int, cell_size: int):
        self.width, self.height = width, height
        self.cell_size = cell_size
        self.size = pygame.Vector2(width * cell_size, height * cell_size)

        # Tile palette to handle which tiles are available to place
        self.tile_palette = TilePalette.load('default_palette')

        # A 2D array of indexes of tiles as determined by the tile_palette
        # Initially all -1 to indicate an empty cell
        self.tile_grid = [[-1 for y in range(height)] for x in range(width)]

        self.is_dirty = True
        self.surface = None
        self.rects = []

    def clean_tilemap(self):
        # TODO: specify if a specific tile changed or if we need to recalculate the entire surface
        # TODO: make tile_rects only contain the rects that are on the screen for efficiency boost when checking for collisions
        # if adding new tile: blit the rect to the old surface
        print('is dirty')
        surface = pygame.Surface(self.size).convert_alpha()  # makes the parts of the surface we don't draw to
        # transparent
        rects = []

        # Start to draw the tilemap
        for x in range(self.width):
            # for every row in the column
            for y in range(self.height):
                # If there is something in this tile
                value = self.tile_grid[x][y]
                if value != -1:
                    # Draw it
                    rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                    rects.append(rect)
                    # Get the tile
                    tile = self.tile_palette[value]
                    sprite = pygame.transform.scale(tile.get_sprite(neighbours=self.get_neighbours(x, y)), rect.size)
                    # Draw to screen
                    surface.blit(sprite, rect)

        self.is_dirty = False
        self.surface = surface
        self.rects = rects

    def get_render_info(self):
        # TODO: Cache the tilemap and only recreate the surface if any new tiles are placed
        if self.is_dirty:
            self.clean_tilemap()

        return self.surface, (0, 0)

    def position_to_coord(self, position: pygame.Vector2):
        return pygame.Vector2(int(position.x // self.cell_size), int(position.y // self.cell_size))

    def get_neighbours(self, x, y):
        return {
            'up': -1 if not self.is_valid_coord(x, y - 1) else self.tile_grid[x][y - 1],
            'left': -1 if not self.is_valid_coord(x - 1, y) else self.tile_grid[x - 1][y],
            'right': -1 if not self.is_valid_coord(x + 1, y) else self.tile_grid[x + 1][y],
            'down': -1 if not self.is_valid_coord(x, y + 1) else self.tile_grid[x][y + 1],
        }

    def is_valid_coord(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def set_tile(self, x: int, y: int, value: int):
        if not self.is_valid_coord(x, y):
            return

        self.tile_grid[int(x)][int(y)] = value
        self.is_dirty = True

    def floodfill(self, x: int, y: int, value: int, depth=0):
        if depth >= 10:
            return

        if not self.is_valid_coord(x, y) or self.tile_grid[int(x)][int(y)] != -1:
            return

        self.set_tile(x, y, value)

        self.floodfill(x - 1, y, value, depth+1)
        self.floodfill(x + 1, y, value, depth+1)
        self.floodfill(x, y - 1, value, depth+1)
        self.floodfill(x, y + 1, value, depth+1)

    def clear(self):
        self.tile_grid = [[-1 for y in range(self.height)] for x in range(self.width)]
        self.is_dirty = True

    def save_level(self, filename: str):
        ext = 'tm'
        json_tilemap = {}

        for x in range(self.width):
            # for every row in the column
            for y in range(self.height):
                # If there is something in this tile
                value = self.tile_grid[x][y]
                if value != -1:
                    if x in json_tilemap:
                        json_tilemap[x][y] = value
                    else:
                        json_tilemap[x] = {y: value}

        with open(f'Tilemap/Levels/{filename}.{ext}', 'w') as outfile:
            json.dump(json_tilemap, outfile)
            print(f'{outfile.name} saved successfully')

    def load_level(self, filename: str):
        ext = 'tm'

        with open(f'Tilemap/Levels/{filename}.{ext}') as json_file:
            json_tilemap = json.load(json_file)

            tile_grid = [[-1 for y in range(self.height)] for x in range(self.width)]
            for x, ys in json_tilemap.items():
                for y, value in ys.items():
                    tile_grid[int(x)][int(y)] = value

            self.tile_grid = tile_grid
            self.is_dirty = True

            print(f'{json_file.name} loaded successfully')

