import pygame,sys
from pygame import *
from Niveles.Facil.Facil import facil
from Clases.Menu.Niveles_menu import niveles_menu
class jugar(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../../imagenes/Menu/Botones/Jugar/Normal.png')
        self.normal = pygame.image.load('../../imagenes/Menu/Botones/Jugar/Normal.png')
        self.seleccionado = pygame.image.load('../../imagenes/Menu/Botones/Jugar/Seleccionado.png')
        self.rect = self.image.get_rect()
        self.rect.y = 230
        self.rect.x = 530

    def toc(self,es):
        if es == 0:
            self.image = self.seleccionado
        elif es == 1:
            self.image=self.normal
    def jugar(self):

        niveles_menu.iniciar()