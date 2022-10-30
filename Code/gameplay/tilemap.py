from utils import *


class Tilemap:  # currently indexed with [x][y]

    dict_index_color = {
        1: RED,
        2: GREEN
    }

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.size = pygame.Vector2(WIDTH, HEIGHT)

        self.grid_size = math.ceil(self.size.y / height)
        self.grid = [[-1 for y in range(height)] for x in range(width)]
        self.grid[0][1] = 1
        self.grid[3][2] = 2

    def get_render_info(self):
        surface = pygame.Surface(self.size).convert_alpha()  # makes the parts of the surface we don't draw to
        # transparent

        # Start to draw the tilemap
        for x in range(self.width):
            # If this column is off the screen, we don't need to render it or any other column
            if x * self.grid_size >= self.size.x:
                break

            # for every row in the column
            for y in range(self.height):
                # If there is something in this tile
                value = self.grid[x][y]
                if value != -1:
                    # Draw it
                    pygame.draw.rect(
                        surface=surface,
                        color=self.dict_index_color[value],
                        rect=(x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size)
                    )

        return surface, (0, 0)
