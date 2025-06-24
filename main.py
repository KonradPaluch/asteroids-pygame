import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, \
    ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, \
    ASTEROID_SPAWN_RATE, FRAMERATE
from player import Player


def main():
    _ = pygame.init()

    dt = 0
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(
        [SCREEN_WIDTH, SCREEN_HEIGHT],
        pygame.SCALED)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        _ = screen.fill(("black"))
        player.draw(screen)
        pygame.display.flip()

        tick_time = clock.tick(FRAMERATE)
        dt = tick_time / 1000

if __name__ == "__main__":
    main()
