import pygame

from utils import *
from player import Player
from tilemap import Tilemap

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("grAvIty guy")
clock = pygame.time.Clock()

# TODO: Tilemap editing mode
# TODO: UI as a FSM to change what is shown, and what you can press
# TODO: Make scroll_x cleaner


def main():

    mode = 'play'

    player = Player(width=20, height=20)
    tilemap = Tilemap(width=30, height=10, cell_size=HEIGHT/10)

    scroll_x = player.rect.left - 50

    run = True
    while run:
        # Go to the next frame and save how long it has been since the last frame
        delta_time = clock.tick(FPS) / 1000
        # Get all the events that happen this frame
        events = pygame.event.get()

        if mode == 'play':
            tilemap.load('level1')
            # Respond to the pygame events this frame
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.jump()

            player.update(delta_time, tile_rects=tilemap.rects)
            scroll_x = player.rect.left - 50

        if mode == 'edit':
            # Respond to the pygame events this frame
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        tilemap.save('level1')

                    if event.key == pygame.K_l:
                        tilemap.load('level1')

                    if event.key == pygame.K_c:
                        tilemap.clear()

                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.Vector2(pygame.mouse.get_pos())
                    pos.x += scroll_x

                    coord = tilemap.position_to_coord(pygame.Vector2(pos))
                    tilemap.set_tile(coord.x, coord.y, 1)

                if pygame.mouse.get_pressed()[2]:
                    pos = pygame.Vector2(pygame.mouse.get_pos())
                    pos.x += scroll_x

                    coord = tilemap.position_to_coord(pygame.Vector2(pos))
                    tilemap.set_tile(coord.x, coord.y, -1)

        draw(WIN, player, tilemap, scroll_x)

    pygame.quit()


def draw(win: pygame.display, player: Player, tilemap: Tilemap, scroll_x: float):

    win.fill(BG_COLOR)

    tilemap_surface, tilemap_position = tilemap.get_render_info()
    win.blit(tilemap_surface, (0, 0), area=(scroll_x, 0, WIDTH, HEIGHT))

    player_surface, player_rect = player.get_render_info()
    win.blit(player_surface, (player_rect.left - scroll_x, player.rect.top))

    pygame.display.update()


if __name__ == "__main__":
    main()
