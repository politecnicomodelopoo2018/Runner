# -*- encoding: utf-8 -*-
from Clases.player.Player import player
from Clases.Vidas.Vida import vida
from Clases.Enemigo.Enemigo import enemigo
from Clases.Text.Text import score
from Clases.Obstaculo.Obstaculo import obstaculo
import pygame
from Clases.Colores import Colores
from Clases.Menu.Registro import registro
from Clases.DB import db
from Clases.Menu.Highscores.New_high import new
from Clases.Menu.Highscores.Scores import scores
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

high = scores.cargar()
n = new()
colorsito = Colores().Gris
pygame.display.set_caption("Boke Games")
screen = pygame.display.set_mode((1280, 700))
all_sprites = pygame.sprite.Group()
all_sprites.add(p,v,en,n)
pos_suelo=300+240
dy = 0

Negro = (0, 0, 0)
Blanco = (255, 255, 255)
Gris = (200, 200, 200)
Verdesungo = (125, 254, 29)
Rojo = (250, 1, 0)
Amarillo = (253, 253, 1)
Rosa = (248, 67, 253)


color = Gris
class GOD(object):
    @staticmethod
    def iniciar():
        co = Colores()
        salir = False
        perdio = False
        estado = 0
        en.reset()
        v.reset()
        S.reset()
        n.mayor = False
        n.reset()
        p.reset()
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
            v.moverse(15)
            key = pygame.key.get_pressed()
            p.salto(key)

            if p.colision(v):
                v.fuera()
                S.score +=100
                if S.score > high[0].puntaje:
                    n.mayor=True
            if p.colision(en):
                en.fuera()
                perdio = True
                salir = True

            if estado == 0:
                estado = 1
                screen.fill(Blanco)
            elif estado == 1:
                estado = 2
                screen.fill(Rojo)
            elif estado == 2:
                estado = 3
                screen.fill(Verdesungo)
            elif estado == 3:
                estado = 4
                screen.fill(Amarillo)
            elif estado == 4:
                estado = 0
                screen.fill(Rosa)


            en.moverse(10)
            en.fuera_pantalla()
            all_sprites.draw(screen)
            pygame.draw.line(screen, co.Negro, (0, pos_suelo), (1280, pos_suelo))
            screen.blit(S.show(S.score), (5, 10))
            en.cambiar_sprite(en.estado)
            v.cambiar_sprite(v.estado)
            p.cambiar_sprite()
            n.cambiar_sprite(n.estado)
            pygame.display.flip()
            pygame.time.wait(3)


        if salir:
            if perdio:
                registro.inicio(S.score)