from utils import *
from gameplay import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("grAvIty guy")
clock = pygame.time.Clock()


def main():

    player = Player(width=20, height=20)
    tilemap = Tilemap(width=100, height=10)

    run = True
    while run:
        # Go to the next frame and save how long it has been since the last frame
        delta_time = clock.tick(FPS) / 1000
        # Get all the events that happen this frame
        events = pygame.event.get()

        # Respond to the pygame events this frame
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        player.update(delta_time)

        draw(WIN, player, tilemap)

    pygame.quit()


def draw(win: pygame.display, player: Player, tilemap: Tilemap):

    win.fill(BG_COLOR)

    tilemap_surface, tilemap_position = tilemap.get_render_info()
    win.blit(tilemap_surface, tilemap_position)

    player_surface, player_position = player.get_render_info()
    win.blit(player_surface, player_position)

    pygame.display.update()


if __name__ == "__main__":
    main()
