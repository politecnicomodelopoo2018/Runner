import pygame,sys
from pygame import *


class f(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../../imagenes/Menu/Selector/Screen.png')
        self.rect = self.image.get_rect()