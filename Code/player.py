import pygame

from utils import *


class Player:
    vertical_speed = 5

    def __init__(self, width, height):
        size = pygame.Vector2(width, height)
        position = pygame.Vector2(100, HEIGHT / 2 - height / 2)
        self.rect = pygame.Rect(*position, *size)

        self.gravity_scale = 1
        self.velocity = pygame.Vector2(0, self.gravity_scale * self.vertical_speed)

    def jump(self):
        self.gravity_scale *= -1
        self.velocity.y = self.gravity_scale * self.vertical_speed

    def move(self, move_amount: pygame.Vector2, collision_rects):
        collision_types = {'top': False, 'bottom': False, 'left': False, 'right': False}
        rect_after_movement = self.rect
        rect_after_movement.x += move_amount.x
        hit_list = collision_test(rect_after_movement, collision_rects)
        for hit in hit_list:
            if move_amount.x > 0:
                rect_after_movement.right = hit.left
                collision_types['right'] = True
            elif move_amount.x < 0:
                rect_after_movement.left = hit.right
                collision_types['left'] = True
        rect_after_movement.y += move_amount.y
        hit_list = collision_test(rect_after_movement, collision_rects)
        for hit in hit_list:
            if move_amount.y > 0:
                rect_after_movement.bottom = hit.top
                collision_types['bottom'] = True
            elif move_amount.y < 0:
                rect_after_movement.top = hit.bottom
                collision_types['up'] = True

        self.rect = rect_after_movement
        return collision_types

    def update(self, delta_time, tile_rects):
        # TODO: Add delta_time for movement back
        # Get the position the player would move to with its current velocity
        move_amount = self.velocity
        move_amount.x = 2
        # Move the player contained to collisions and get the collisions from the movement
        collisions = self.move(move_amount=move_amount, collision_rects=tile_rects)

    def get_render_info(self):
        surface = pygame.Surface(self.rect.size)
        surface.fill(BLUE)

        return surface, self.rect
