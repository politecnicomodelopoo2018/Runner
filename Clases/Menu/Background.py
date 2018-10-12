import pygame,sys
from pygame import *

class background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../../imagenes/Menu/Fondo.png')
        self.rect = self.image.get_rect()