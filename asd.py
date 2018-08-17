import pygame
from pygame.locals import *
import sys

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


def main():
    bgOne = pygame.image.load('canvas.png')
    bgTwo = pygame.image.load('canvas.png')
    tux_pos_x = 0
    tux_pos_y = 0
    bgOne_x = 0
    bgTwo_x = bgOne.get_width()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Boke games")
    fondo = pygame.image.load("akinfeev-celebration-1.jpg").convert()
    tux = pygame.image.load("E58.png").convert_alpha()
    background_size = fondo.get_size()
    background_rect = fondo.get_rect()
    screen = pygame.display.set_mode(background_size)
    screen.blit(fondo, (0, 0))
    screen.blit(tux, (tux_pos_x, tux_pos_y))
    pygame.display.flip()

    while True:

        tux_pos_x = tux_pos_x + 1
        pygame.display.flip()
        screen.blit(bgOne, (bgOne_x, 0))
        screen.blit(bgTwo, (bgTwo_x, 0))
        screen.blit(tux, (tux_pos_x, tux_pos_y))
        pygame.display.update()
        if tux_pos_x == 820:
            tux_pos_x = 0
        if bgOne_x == -1 * bgOne.get_width():
            bgOne_x = bgTwo_x + bgTwo.get_width()
        if bgTwo_x == -1 * bgTwo.get_width():
            bgTwo_x = bgOne_x + bgOne.get_width()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                sys.exit()



if __name__ == "__main__":
    main()



