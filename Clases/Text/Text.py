import pygame, sys
from pygame.locals import *


class score(object):

    def __init__(self):
        self.score = 0
        self.myfont = pygame.font.SysFont("monospace", 16)
        self.scoretext = self.myfont.render("Score = "+str(self.score), 1, (0,0,0))
