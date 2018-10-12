import pygame, sys
from pygame.locals import *


class puntaje(object):

    def __init__(self):
        self.score = 0
        self.myfont = pygame.font.SysFont("monospace", 40)
        self.Color=(255,255,255)
    def show(self,score):
        scoretext = self.myfont.render("Score = "+str(score), 1, self.Color)
        return(scoretext)