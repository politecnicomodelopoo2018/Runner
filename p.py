import pygame, sys
from pygame.locals import *
from Player import  Player
pygame.init()





clock = pygame.time.Clock()

bgOne = pygame.image.load('rsz_1rsz_canvas.png')
bgTwo = pygame.image.load('rsz_1rsz_canvas.png')
tux = pygame.image.load("E58.png")
tux_pos_x = 200
tux_pos_y = 500

screen = pygame.display.set_mode((1000, 1000))
bgOne_x = 0
bgTwo_x = bgOne.get_width()

while True:
    pygame.display.flip()
    screen.blit(bgOne, (bgOne_x, 0))
    screen.blit(bgTwo, (bgTwo_x, 0))
    screen.blit(tux,(tux_pos_x,tux_pos_y))


    pygame.display.update()


    bgOne_x -= 10
    bgTwo_x -= 10

    if bgOne_x  == -1 * bgOne.get_width():
        bgOne_x = bgTwo_x + bgTwo.get_width()
    if bgTwo_x  == -1 * bgTwo.get_width():
        bgTwo_x = bgOne_x + bgOne.get_width()

    for event in pygame.event.get():
        a = 1
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            #sys.exit()
        #if event.type == (event.type == KEYUP and event.key == K_UP):
            for a in range(40):
                tux_pos_y -= 5
                if tux_pos_y == 300:
                        tux_pos_y += 5


    clock.tick(100000)