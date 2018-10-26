# -*- encoding: utf-8 -*-
from Clases.Menu.Highscores.Fondo import f
from Clases.Menu.Highscores.Text import text
from Clases.Menu.Highscores.Scores import scores
from Clases.Menu.Niveles_menu import niveles_menu
import pygame
class hg(object):
    @staticmethod
    def iniciar():

        pygame.init()
        salir = False
        jugador1 = text()
        jugador2 = text()
        jugador3 = text()
        jugador4 = text()
        screen = pygame.display.set_mode((1280, 700))
        fondo = f()
        lista_scores = []
        for z in range(4):
            a = scores()
            a.cargar(z)
            lista_scores.append(a)
        while not salir:
            for e in pygame.event.get():

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        salir=True


            screen.blit(fondo.image,(0,0))
            screen.blit(jugador1.showNombre(lista_scores[0].nombre), (335, 190))
            screen.blit(jugador1.showPuntaje(lista_scores[0].puntaje), (850, 190))
            screen.blit(jugador2.showNombre(lista_scores[1].nombre), (335, 285))
            screen.blit(jugador2.showPuntaje(lista_scores[1].puntaje), (850, 285))
            screen.blit(jugador3.showNombre(lista_scores[2].nombre), (335, 375))
            screen.blit(jugador3.showPuntaje(lista_scores[2].puntaje), (850, 375))
            screen.blit(jugador4.showNombre(lista_scores[3].nombre), (335, 465))
            screen.blit(jugador4.showPuntaje(lista_scores[3].puntaje), (850, 465))
            pygame.display.flip()
            pygame.time.wait(3)
        if salir:
            niveles_menu.iniciar()
