from utils import *
from gameplay import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("grAvIty guy")
clock = pygame.time.Clock()


def draw(win):
    win.fill(BG_COLOR)

    pygame.display.update()


def main():

    player = Player()

    run = True
    while run:
        # Go to the next frame
        clock.tick(FPS)
        # Get all the events that happen this frame
        events = pygame.event.get()
        # Respond to the pygame events this frame
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                break

        draw(WIN)

    pygame.quit()


if __name__ == "__main__":
    main()
