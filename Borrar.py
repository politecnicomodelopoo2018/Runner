# -*- encoding: utf-8 -*-
from Clases.player.Player import player
from Clases.Vidas.Vida import vida
import pygame
from pygame import QUIT, K_LEFT, K_RIGHT, K_UP

p = player()
v = vida()
screen = pygame.display.set_mode((1280, 700))
all_sprites = pygame.sprite.Group()
all_sprites.add(p,v)
BLACK=(0,0,0)
pos_suelo=300+240
GRAVEDAD = 0.05
dy = 0
while True:
    # Actualización de eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            salir = True
    v.rect.x -=3

    # Actualización del personaje
    key = pygame.key.get_pressed()
    if dy == 0:               # si está en el suelo..."
        if key[K_UP]:
            dy = -3.5
    else:
        p.rect.y += dy                  # empuja el personaje hacia abajo
        dy += GRAVEDAD           # y acelera su caida

        if p.rect.y > 300:        # detiene la caida en el suelo
            dy = 0
            p.rect.y = 300

    screen.fill((200, 200, 200))
    all_sprites.draw(screen)
    pygame.draw.line(screen, BLACK, (0, pos_suelo), (1280, pos_suelo))
    pygame.display.flip()
    pygame.time.wait(1)


