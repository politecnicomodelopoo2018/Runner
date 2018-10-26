import pygame, sys
from pygame import *
from Niveles.GOD.GOD import GOD


class tres(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../../imagenes/Menu/Botones/Niveles/3/rsz_2normal.png')
        self.normal = pygame.image.load('../../imagenes/Menu/Botones/Niveles/3/rsz_2normal.png')
        self.seleccionado = pygame.image.load('../../imagenes/Menu/Botones/Niveles/3/rsz_2seleccionado.png')
        self.rect = self.image.get_rect()
        self.rect.y = 430
        self.rect.x = 530

    def toc(self, es):
        if es == 2:
            self.image = self.seleccionado
        elif es is not 2:
            self.image = self.normal
    def jugar(self):
        GOD.iniciar()
    def reset(self):
        self.image = pygame.image.load('../../imagenes/Menu/Botones/Niveles/3/rsz_2normal.png')


