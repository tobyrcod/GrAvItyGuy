from utils import *


class Player:

    speed = 20

    def __init__(self, width, height):
        self.size = pygame.Vector2(width, height)
        self.position = pygame.Vector2(0, 0)
        print('Created a player instance')

    def update(self, delta_time):
        self.position.y += self.speed * delta_time

    def get_render_info(self):
        surface = pygame.Surface(self.size)
        surface.fill(BLUE)

        return surface, self.position
