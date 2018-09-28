# -*- encoding: utf-8 -*-
from Clases.player.Player import player
from Clases.Vidas.Vida import vida
from Clases.Enemigo.Enemigo import enemigo
import pygame
from pygame import QUIT, K_LEFT, K_RIGHT, K_UP

p = player()
v = vida()
en = enemigo()
screen = pygame.display.set_mode((1280, 700))
all_sprites = pygame.sprite.Group()
all_sprites.add(p,v,en)
BLACK=(0,0,0)
pos_suelo=300+240
GRAVEDAD = 0.05
dy = 0
while True:
    v.fuera_pantalla()
    # Actualización de eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            salir = True
    v.moverse()

    key = pygame.key.get_pressed()
    p.salto(key)
    if p.colision(v):
        v.fuera()
    if p.colision(en):
        en.fuera()
    en.moverse()
    en.fuera_pantalla()
    screen.fill((200, 200, 200))
    all_sprites.draw(screen)
    pygame.draw.line(screen, BLACK, (0, pos_suelo), (1280, pos_suelo))
    pygame.display.flip()
    pygame.time.wait(1)


