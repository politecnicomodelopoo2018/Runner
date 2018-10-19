import pygame, sys
from pygame.locals import *


class text(object):

    def __init__(self):
        self.score = 0
        self.myfont = pygame.font.SysFont("monospace", 40)
        self.Color=(0,0,0)
    def showNombre(self,Nombre):
        scoretext = self.myfont.render(str(Nombre), 1, self.Color)
        return(scoretext)
    def showPuntaje(self,Puntaje):
        scoretext = self.myfont.render(str(Puntaje), 1, self.Color)
        return(scoretext)
    def reset(self):
        self.score = 0
