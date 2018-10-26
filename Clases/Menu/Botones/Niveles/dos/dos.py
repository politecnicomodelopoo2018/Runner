import pygame, sys
from pygame import *
from Niveles.Medio.Medio import medio


class dos(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../../imagenes/Menu/Botones/Niveles/2/rsz_1normal(1).png')
        self.normal = pygame.image.load('../../imagenes/Menu/Botones/Niveles/2/rsz_1normal(1).png')
        self.seleccionado = pygame.image.load('../../imagenes/Menu/Botones/Niveles/2/rsz_1seleccionado(1).png')
        self.rect = self.image.get_rect()
        self.rect.y = 330
        self.rect.x = 530

    def toc(self, es):
        if es == 1:
            self.image = self.seleccionado
        elif es is not 1:
            self.image = self.normal
    def jugar(self):
        b = medio()
    def reset(self):
        self.image = pygame.image.load('../../imagenes/Menu/Botones/Niveles/2/rsz_1normal(1).png')
