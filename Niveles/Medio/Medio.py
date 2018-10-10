# -*- encoding: utf-8 -*-
from Clases.player.Player import player
from Clases.Vidas.Vida import vida
from Clases.Enemigo.Enemigo import enemigo
from Clases.Text.Text import score
from Clases.Obstaculo.Obstaculo import obstaculo
import pygame
from Clases.Colores import Colores
# highscore en bdd
# obstaculos/pozos
# en bdd que se epuedan crear los mapas
# al comienzo que le pregunte que mapa quiere usar o manejarlo por nivel
# diferentes personajes


from pygame import QUIT, K_LEFT, K_RIGHT, K_UP
pygame.init()
p = player()
ob = obstaculo()
v = vida()
en = enemigo()
S = score()
salir = False
pygame.display.set_caption("testing")
screen = pygame.display.set_mode((1280, 700))
all_sprites = pygame.sprite.Group()
all_sprites.add(p,v,en)
pos_suelo=300+240
dy = 0
Negro = (0, 0, 0)
Blanco = (255, 255, 255)
Gris = (200, 200, 200)


while not salir:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                salir = True

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_DOWN:
                p.Agacharse(True)

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_DOWN:
                p.Pararse(True)

    v.fuera_pantalla()
    v.moverse(0)
    key = pygame.key.get_pressed()
    p.salto(key)

    if p.colision(v):
        v.fuera()
        S.score +=100
    if p.colision(en):
        en.fuera()
        salir = True
    en.moverse(0)
    en.fuera_pantalla()
    screen.fill(Gris)
    all_sprites.draw(screen)
    pygame.draw.line(screen, Negro, (0, pos_suelo), (1280, pos_suelo))
    screen.blit(S.show(S.score), (5, 10))
    en.cambiar_sprite(en.estado)
    v.cambiar_sprite(v.estado)
    p.cambiar_sprite(p.estado)
    pygame.display.flip()
    pygame.time.wait(3)


