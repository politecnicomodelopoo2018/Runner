# -*- encoding: utf-8 -*-
from Clases.Menu.Highscores.Fondo import f
from Clases.Menu.Highscores.Text import text
from Clases.DB import db
from Clases.Menu.Niveles_menu import niveles_menu
import pygame
class hg(object):
    def __init__(self):

        pygame.init()
        self.salir = False
        jugador1 = text()
        jugador2 = text()
        jugador3 = text()
        jugador4 = text()
        screen = pygame.display.set_mode((1280, 700))
        fondo = f()
        a = db.connect("select Nombre,Puntaje from Jugador order by Puntaje desc ")
        y = []
        for j in a :
            y.append(j)
        while not self.salir:
            for e in pygame.event.get():

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.salir=True


            screen.blit(fondo.image,(0,0))
            screen.blit(jugador1.showNombre(y[0]['Nombre']), (335, 190))
            screen.blit(jugador1.showPuntaje(y[0]['Puntaje']), (850, 190))
            screen.blit(jugador2.showNombre(y[1]['Nombre']), (335, 285))
            screen.blit(jugador2.showPuntaje(y[1]['Puntaje']), (850, 285))
            screen.blit(jugador3.showNombre(y[2]['Nombre']), (335, 375))
            screen.blit(jugador3.showPuntaje(y[2]['Puntaje']), (850, 375))
            screen.blit(jugador4.showNombre(y[3]['Nombre']), (335, 465))
            screen.blit(jugador4.showPuntaje(y[3]['Puntaje']), (850, 465))
            pygame.display.flip()
            pygame.time.wait(3)
        if self.salir:
            a = niveles_menu
