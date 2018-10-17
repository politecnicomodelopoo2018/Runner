# -*- encoding: utf-8 -*-
from Clases.player.Player import player
from Clases.Vidas.Vida import vida
from Clases.Enemigo.Enemigo import enemigo
from Clases.Text.Text import score
from Clases.Obstaculo.Obstaculo import obstaculo
from Clases.Menu.Registro import registro
import pygame
from Clases.Colores import Colores
# highscore en bdd
# obstaculos/pozos
# al comienzo que le pregunte que mapa quiere usar o manejarlo por nivel
# diferentes personajes


from pygame import QUIT, K_LEFT, K_RIGHT, K_UP

class facil(object):


    def __init__(self):
        from Clases.Text.Text import score
        pygame.init()
        p = player()
        ob = obstaculo()
        v = vida()
        S = score()
        self.perdio = False
        self.salir = False
        pygame.display.set_caption("Boke Games")
        screen = pygame.display.set_mode((1280, 700))
        all_sprites = pygame.sprite.Group()
        all_sprites.add(p, v, ob)
        pos_suelo = 300 + 240
        dy = 0
        Negro = (0, 0, 0)
        Blanco = (255, 255, 255)
        Gris = (200, 200, 200)
        ob.reset()
        v.reset()
        S.reset()
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

            v.fuera_pantalla()
            v.moverse(0)
            key = pygame.key.get_pressed()
            p.salto(key)

            if p.fuera_pantalla():
                self.salir = True
                self.perdio = True
            if p.colision(v):
                v.fuera()
                S.score +=100
            if p.colision(ob):
                p.nestor_en_bloque()
            ob.moverse()
            ob.fuera_pantalla()
            screen.fill(Gris)
            all_sprites.draw(screen)
            pygame.draw.line(screen, Negro, (0, pos_suelo), (1280, pos_suelo))
            screen.blit(S.show(S.score), (5, 10))
            v.cambiar_sprite(v.estado)
            p.cambiar_sprite(p.estado)
            pygame.display.flip()
            pygame.time.wait(3)

        if self.salir:
            if self.perdio:
                r = registro(S.score)

