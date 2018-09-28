import pygame, sys
from pygame.locals import *

class text(object):
    myfont = pygame.font.SysFont("monospace", 16)
    def texto(self,text):

        self.scoretext = self.myfont.render("Score {0}".format(text), 1, (0, 0, 0))

