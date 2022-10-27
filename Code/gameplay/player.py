from utils import *


class Player:

    speed = 20
    swap_impulse = -30

    def __init__(self, width, height):
        self.size = pygame.Vector2(width, height)
        self.position = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        print('Created a player instance')

    def jump(self):
        self.velocity.y = self.swap_impulse
        print('jump')

    def update(self, delta_time):
        self.velocity.y += GRAVITY * delta_time
        self.position += self.velocity * delta_time

    def get_render_info(self):
        surface = pygame.Surface(self.size)
        surface.fill(BLUE)

        return surface, self.position
