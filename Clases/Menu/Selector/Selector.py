# -*- encoding: utf-8 -*-
from Clases.Menu.Selector.Fondo import f
from Clases.Menu.Highscores.Text import text
from Clases.DB import db
import pygame
class selector(object):
    def __init__(self):

        pygame.init()
        self.salir = False
        screen = pygame.display.set_mode((1280, 700))
        fondo = f()

        while not self.salir:
            for e in pygame.event.get():

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.salir=True


            screen.blit(fondo.image,(0,0))
            pygame.display.flip()
            pygame.time.wait(3)
