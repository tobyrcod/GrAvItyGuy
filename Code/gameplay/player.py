from utils import *


class Player:
    vertical_speed = 100

    def __init__(self, width, height):
        self.size = pygame.Vector2(width, height)
        self.position = pygame.Vector2(100, HEIGHT / 2 - height / 2)

        self.gravity_scale = 1
        self.velocity = pygame.Vector2(0, self.gravity_scale * self.vertical_speed)
        print('Created a player instance')

    def jump(self):
        self.gravity_scale *= -1
        self.velocity.y = self.gravity_scale * self.vertical_speed

    def update(self, delta_time):
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
