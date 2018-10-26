# -*- encoding: utf-8 -*-
from Clases.player.Player import player
from Clases.Vidas.Vida import vida
from Clases.Enemigo.Enemigo import enemigo
from Clases.Text.Text import score
from Clases.Obstaculo.Obstaculo import obstaculo
from Clases.Menu.Registro import registro
from Clases.DB import db
from Clases.Menu.Highscores.New_high import new
from Clases.Menu.Highscores.Scores import scores
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
n = new()

pygame.display.set_caption("Boke Games")
screen = pygame.display.set_mode((1280, 700))
all_sprites = pygame.sprite.Group()
all_sprites.add(p,v,en,n)
pos_suelo=300+240
dy = 0
Negro = (0, 0, 0)
Blanco = (255, 255, 255)
Gris = (200, 200, 200)

class medio(object):
    def __init__(self):
        self.salir = False
        self.perdio = False
        en.reset()
        v.reset()
        S.reset()
        p.reset()
        n.mayor = False
        n.reset()
        high = scores.cargar()
        while not self.salir:

            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.salir = True

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_DOWN:
                        p.Agacharse(True)

                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_DOWN:
                        p.Pararse(True)
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_KP0:
                                    S.score+=2000


            v.fuera_pantalla()
            v.moverse(2)
            key = pygame.key.get_pressed()
            p.salto(key)

            if p.colision(v):
                v.fuera()
                S.score +=100
                if S.score > high[0].puntaje:
                    n.mayor=True
            if p.colision(en):
                self.salir = True
                self.perdio = True

            en.moverse(2)
            en.fuera_pantalla()
            screen.fill(Gris)
            all_sprites.draw(screen)
            pygame.draw.line(screen, Negro, (0, pos_suelo), (1280, pos_suelo))
            screen.blit(S.show(S.score), (5, 10))
            en.cambiar_sprite(en.estado)
            v.cambiar_sprite(v.estado)
            p.cambiar_sprite()
            n.cambiar_sprite(n.estado)
            pygame.display.flip()
            pygame.time.wait(2)


        if self.salir:
            if self.perdio:
                registro.inicio(S.score)
                en.fuera_pantalla()