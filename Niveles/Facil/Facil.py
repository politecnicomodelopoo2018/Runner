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
# al comienzo que le pregunte que mapa quiere usar o manejarlo por nivel
# diferentes personajes


from pygame import QUIT, K_LEFT, K_RIGHT, K_UP

class facil(object):

    @staticmethod
    def iniciar():
        from Clases.Text.Text import score
        pygame.init()
        p = player()
        ob = obstaculo()
        v = vida()
        S = score()
        n = new()
        perdio = False
        salir = False
        pygame.display.set_caption("Boke Games")
        screen = pygame.display.set_mode((1280, 700))
        all_sprites = pygame.sprite.Group()
        all_sprites.add(p, v, ob,n)
        pos_suelo = 300 + 240
        dy = 0
        Negro = (0, 0, 0)
        Blanco = (255, 255, 255)
        Gris = (200, 200, 200)
        n.mayor = False
        n.reset()
        high = scores.cargar()
        ob.reset()
        v.reset()
        S.reset()
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
            v.moverse(2)
            key = pygame.key.get_pressed()
            p.salto(key)

            if p.fuera_pantalla():
                salir = True
                perdio = True
            if p.colision(v):
                v.fuera()
                S.score +=100
                if S.score > high[0].puntaje:
                    n.mayor=True

            if p.colision(ob):
                p.nestor_en_bloque()
            ob.moverse()
            ob.fuera_pantalla()
            screen.fill(Gris)
            all_sprites.draw(screen)
            pygame.draw.line(screen, Negro, (0, pos_suelo), (1280, pos_suelo))
            screen.blit(S.show(S.score), (5, 10))
            v.cambiar_sprite()
            p.cambiar_sprite()
            n.cambiar_sprite(n.estado)
            pygame.display.flip()
            pygame.time.wait(2)

        if salir:
            if perdio:
                registro.inicio(S.score)

