import pygame,sys
from pygame import *
from Clases.Menu.Selector.Selector import selector
class personaje(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../../imagenes/Menu/Botones/Personaje/rsz_1normal.png')
        self.normal = pygame.image.load('../../imagenes/Menu/Botones/Personaje/rsz_1normal.png')
        self.seleccionado = pygame.image.load('../../imagenes/Menu/Botones/Personaje/rsz_1seleccionado.png')
        self.rect = self.image.get_rect()
        self.rect.y = 330
        self.rect.x = 530


    def toc(self,es):
        if es == 1:
            self.image = self.seleccionado
        elif es == 0:
            self.image=self.normal
    def jugar(self):
        selector.inicio()