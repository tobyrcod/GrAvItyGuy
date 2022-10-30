import pygame

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

    def move(self, move_amount: pygame.Vector2, collisions):
        new_position = self.position + move_amount
        new_position = self.clamp_to_screen(new_position)
        self.position = new_position

    def clamp_to_screen(self, position):
        if position.y < 1:
            position.y = 1
            self.velocity.y = 0
        if position.y > HEIGHT - self.size.y:
            position.y = HEIGHT - self.size.y
            self.velocity.y = 0

        return position

    def update(self, delta_time, collisions):
        # Get the position the player would move to with its current velocity
        move_amount = self.velocity * delta_time

        # Apply constraints to that position (collisions)
        self.move(move_amount=move_amount, collisions=collisions)

    def get_render_info(self):
        surface = pygame.Surface(self.size)
        surface.fill(BLUE)

        return surface, self.position
