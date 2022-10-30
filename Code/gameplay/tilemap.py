from utils import *


class Tilemap:  # currently indexed with [y][x] NOT [x][y]
    def __init__(self, width: int, height: int):
        self.size = pygame.Vector2(WIDTH, HEIGHT)
        self.grid_size = min(math.floor(self.size.x / width), math.floor(self.size.y / height))
        self.grid = [[-1 for x in range(width)] for y in range(height)]
        print(self.grid, self.grid_size)

    def get_render_info(self):
        surface = pygame.Surface(self.size)
        surface.fill(RED)

        return surface, (0, 0)
