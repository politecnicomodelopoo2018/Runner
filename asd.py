# -*- encoding: utf-8 -*-
import pygame
from pygame import QUIT, K_LEFT, K_RIGHT, K_UP

screen = pygame.display.set_mode((800, 800))
salir = False

bgOne = pygame.image.load('rsz_1rsz_canvas.png')
color_negro = (0, 0, 0)
color_rojo = (200, 0, 0)

tux = pygame.image.load("E58.png")
# variables del personaje
personaje = pygame.Rect((0, 0, 30, 30))
dy = 0
x = 40
y = 600 - tux.get_height()
GRAVEDAD = 0.02

# linea horizontal que representa el suelo
pos_suelo = 600

while not salir:
    pygame.display.flip()
    screen.blit(bgOne, (0, 0))

    # Actualización de eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            salir = True

    # Actualización del personaje
    key = pygame.key.get_pressed()

    # animación de salto
    if dy == 0:               # si está en el suelo..."
        if key[K_UP]:
            dy = -2
    else:
        y += dy                  # empuja el personaje hacia abajo
        dy += GRAVEDAD           # y acelera su caida

        if y > pos_suelo - tux.get_height():        # detiene la caida en el suelo
            dy = 0
            y = pos_suelo - tux.get_height()

    # aplica la posición al personaje
    #personaje.bottom = int(y)
    #personaje.centerx = int(x)

    # Actualización gráfica
    #screen.fill((200, 200, 200))

    #screen.fill(color_rojo, personaje)
    screen.blit(tux, (int(x), int(y)))
    pygame.draw.line(screen, color_negro, (0, pos_suelo), (800, pos_suelo))
    pygame.display.update()
    pygame.display.flip()




    # Espera un instante
    pygame.time.wait(1)