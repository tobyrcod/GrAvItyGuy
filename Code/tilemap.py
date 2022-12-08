import pygame

from utils import *


class Tilemap:  # currently indexed with [x][y]

    dict_index_color = {
        1: RED,
        2: GREEN
    }

    def __init__(self, width: int, height: int, cell_size: int):
        self.width, self.height = width, height
        self.cell_size = cell_size
        self.size = pygame.Vector2(width * cell_size, height * cell_size)

        self.tile_grid = [[-1 for y in range(height)] for x in range(width)]
        self.tile_grid[1][1] = 1
        self.tile_grid[5][-1] = 2

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
                    pygame.draw.rect(
                        surface=surface,
                        color=self.dict_index_color[value],
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
        return pygame.Vector2(position.x // self.cell_size, position.y // self.cell_size)
