from utils import *


class Player:

    speed = 20
    swap_impulse = -10

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

        new_position = self.position + self.velocity * delta_time
        if new_position.y < 1:
            new_position.y = 1
            self.velocity.y = 0
        if new_position.y > HEIGHT - self.size.y:
            new_position.y = HEIGHT - self.size.y
            self.velocity.y = 0

        self.position = new_position

    def get_render_info(self):
        surface = pygame.Surface(self.size)
        surface.fill(BLUE)

        return surface, self.position
