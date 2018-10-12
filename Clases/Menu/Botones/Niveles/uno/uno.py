from Niveles.Facil.Facil import facil
import pygame,sys
from pygame import *

class uno(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../../imagenes/Menu/Botones/Niveles/1/rsz_normal(1).png')
        self.normal = pygame.image.load('../../imagenes/Menu/Botones/Niveles/1/rsz_normal(1).png')
        self.seleccionado = pygame.image.load('../../imagenes/Menu/Botones/Niveles/1/rsz_seleccionado(1).png')
        self.rect = self.image.get_rect()
        self.rect.y = 230
        self.rect.x = 530

    def toc(self,es):
        if es == 0:
            self.image = self.seleccionado
        elif es is not 0:
            self.image=self.normal
    def jugar(self):
        b = facil()

