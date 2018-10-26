import pygame,sys
from pygame import *

class obstaculo(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../../imagenes/Obstaculo/rsz_ñe.png')
        self.muerto = False
        self.rect = self.image.get_rect()
        self.rect.y = 430
        self.rect.x = 1600

    def moverse(self):
        self.rect.x -= 4
    def fuera_pantalla(self):
        if self.rect.x <= -200:
            self.fuera()
    def fuera(self):
        self.rect.x=1360
    def reset(self):
        self.rect.y = 430
        self.rect.x = 1600



