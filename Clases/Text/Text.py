import pygame, sys
from pygame.locals import *


class score(object):

    def __init__(self):
        self.score = 0
        self.myfont = pygame.font.SysFont("monospace", 16)
        self.Color=(0,0,0)
    def show(self,score):
        scoretext = self.myfont.render("Score = "+str(score), 1, self.Color)
        return(scoretext)