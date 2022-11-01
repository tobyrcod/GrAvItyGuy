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
        # Add some tiles for testing
        self.tile_grid[4][9] = 1
        self.tile_grid[5][9] = 2
        self.tile_grid[6][9] = 2
        self.tile_grid[7][9] = 1
        self.tile_grid[8][9] = 2
        self.tile_grid[9][9] = 1
        self.tile_grid[10][9] = 2

        self.tile_grid[16][9] = 1
        self.tile_grid[17][9] = 2
        self.tile_grid[18][9] = 1
        self.tile_grid[19][9] = 2
        self.tile_grid[20][9] = 2
        self.tile_grid[21][9] = 1
        self.tile_grid[22][9] = 2


        self.tile_grid[4][2] = 1
        self.tile_grid[5][2] = 2
        self.tile_grid[6][2] = 2
        self.tile_grid[7][2] = 1
        self.tile_grid[8][2] = 2
        self.tile_grid[9][2] = 1
        self.tile_grid[10][2] = 2
        self.tile_grid[11][2] = 1
        self.tile_grid[12][2] = 2
        self.tile_grid[13][2] = 2
        self.tile_grid[14][2] = 1
        self.tile_grid[15][2] = 2
        self.tile_grid[23][2] = 1
        self.tile_grid[24][2] = 2
        self.tile_grid[25][2] = 1
        self.tile_grid[26][2] = 2
        self.tile_grid[27][2] = 2
        self.tile_grid[28][2] = 1
        self.tile_grid[29][2] = 2

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
