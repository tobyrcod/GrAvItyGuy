import pygame
from tile import Tile
from tilepalette import TilePalette
from utils import *


class Tilemap:  # currently indexed with [x][y]

    def __init__(self, width: int, height: int, cell_size: int):
        self.width, self.height = width, height
        self.cell_size = cell_size
        self.size = pygame.Vector2(width * cell_size, height * cell_size)

        green_tile = Tile('green', (0, 255, 0))
        self.tile_palette = TilePalette([green_tile])
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
                    # Get the tile
                    tile = self.tile_palette[value]
                    rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                    rects.append(rect)
                    pygame.draw.rect(
                        surface=surface,
                        color=tile.color,
                        rect=rect
                    )

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

    def set_tile(self, x: int, y: int, value):
        self.tile_grid[int(x)][int(y)] = value
        self.is_dirty = True

    def clear(self):
        self.tile_grid = [[-1 for y in range(self.height)] for x in range(self.width)]
        self.is_dirty = True

    def save(self, filename: str):
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

        with open(f'{filename}.{ext}', 'w') as outfile:
            json.dump(json_tilemap, outfile)
            print(f'{outfile.name} saved successfully')

    def load(self, filename: str):
        ext = 'tm'

        with open(f'{filename}.{ext}') as json_file:
            json_tilemap = json.load(json_file)

            tile_grid = [[-1 for y in range(self.height)] for x in range(self.width)]
            for x, ys in json_tilemap.items():
                for y, value in ys.items():
                    tile_grid[int(x)][int(y)] = value

            self.tile_grid = tile_grid
            self.is_dirty = True

            print(f'{json_file.name} loaded successfully')

