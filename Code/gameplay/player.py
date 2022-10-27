from utils import *


class Player:
    def __init__(self, width, height):
        self.size = (width, height)
        self.position = (0, 0)
        print('Created a player instance')

    def get_render_info(self):
        surface = pygame.Surface(self.size)

        surface.fill(BLUE)

        return surface, self.size
