import pygame, sys ,time
from pygame.locals import *

pygame.init()



clock = pygame.time.Clock()

bgOne = pygame.image.load('rsz_1rsz_canvas.png')
bgTwo = pygame.image.load('rsz_1rsz_canvas.png')
tux = pygame.image.load("E58.png")

dy = 0
x = 40
y = 800 - tux.get_height()
GRAVEDAD = 0.02
pos_suelo = 800

jump = False
fall = False

screen = pygame.display.set_mode((1000, 1000))
bgOne_x = 0
bgTwo_x = bgOne.get_width()



while True:
    pygame.display.flip()
    screen.blit(bgOne, (bgOne_x, 0))
    screen.blit(bgTwo, (bgTwo_x, 0))
    screen.blit(tux, (int(x), int(y)))

    pygame.display.update()


    bgOne_x -= 10
    bgTwo_x -= 10

    if bgOne_x  == -1 * bgOne.get_width():
        bgOne_x = bgTwo_x + bgTwo.get_width()
    if bgTwo_x  == -1 * bgTwo.get_width():
        bgTwo_x = bgOne_x + bgOne.get_width()

    for e in pygame.event.get():
        if e.type == QUIT:
            salir = True

            # Actualización del personaje
    key = pygame.key.get_pressed()

    # animación de salto
    if dy == 0:  # si está en el
        if key[K_UP]:
            dy = -2.5
    else:
        y += dy  # empuja el p
        dy += GRAVEDAD  # y acelera s

        if y > pos_suelo - tux.get_height():
            dy = 0
            y = pos_suelo - tux.get_height()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            sys.exit()




    clock.tick(100000)