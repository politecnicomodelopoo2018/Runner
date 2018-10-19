import pygame,sys
from pygame import *
from Niveles.Facil.Facil import facil
from Clases.Menu.Niveles_menu import niveles_menu
from Clases.player.Player import player
class ronald(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../../imagenes/Menu/Selector/Botones/Ronaldinho/Normal.png')
        self.normal = pygame.image.load('../../imagenes/Menu/Selector/Botones/Ronaldinho/Normal.png')
        self.seleccionado = pygame.image.load('../../imagenes/Menu/Selector/Botones/Ronaldinho/Seleccionado.png')
        self.rect = self.image.get_rect()
        self.rect.y = 580
        self.rect.x = 865

    def toc(self,es):
        if es == 2:
            self.image = self.seleccionado
        else:
            self.image=self.normal
    def jugar(self):

        player.person='Ronald'