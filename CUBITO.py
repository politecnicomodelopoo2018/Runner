# -*- encoding: utf-8 -*-
import pygame
from pygame import QUIT, K_LEFT, K_RIGHT, K_UP

screen = pygame.display.set_mode((320, 240))
salir = False

color_negro = (0, 0, 0)
color_rojo = (200, 0, 0)

# variables del personaje
personaje = pygame.Rect((0, 0, 30, 30))
dy = 0
x = 40
y = 200
GRAVEDAD = 0.02

# linea horizontal que representa el suelo
pos_suelo = 200

while not salir:

    # Actualización de eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            salir = True

    # Actualización del personaje
    key = pygame.key.get_pressed()

    # movimientos horizontales
    if key[K_LEFT]:
        x -= 1
    elif key[K_RIGHT]:
        x += 1

    # animación de salto
    if dy == 0:  # si está en el suelo..."
        if key[K_UP]:
            dy = -2
            print('up')
    else:
        y += dy  # empuja el personaje hacia abajo
        dy += GRAVEDAD  # y acelera su caida

        if y > pos_suelo:  # detiene la caida en el suelo
            dy = 0
            y = pos_suelo
    # aplica la posición al personaje
    personaje.bottom = int(y)
    personaje.centerx = int(x)
    # Actualización gráfica
    screen.fill((200, 200, 200))
    pygame.draw.line(screen, color_negro, (0, pos_suelo), (320, pos_suelo))
    screen.fill(color_rojo, personaje)
    pygame.display.flip()
    # Espera un instante
    pygame.time.wait(1)
