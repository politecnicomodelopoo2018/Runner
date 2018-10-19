import pygame,sys
from pygame import *

class new(pygame.sprite.Sprite):


    def __init__(self):

        super().__init__()
        self.image=pygame.image.load('../../imagenes/Highscores/New/Nothing.png')
        self.sprites=[pygame.image.load('../../imagenes/Highscores/New/Normal.png'),pygame.image.load('../../imagenes/Highscores/New/80.png'),pygame.image.load('../../imagenes/Highscores/New/60.png')
                      ,pygame.image.load('../../imagenes/Highscores/New/40.png'),pygame.image.load('../../imagenes/Highscores/New/20.png')]
        self.estado=0
        self.rect = self.image.get_rect()
        self.rect.y = 50
        self.rect.x = 500
        self.mayor =False

    def cambiar_sprite(self,estado):
        if self.mayor:
            if estado == 0:
                self.image = self.sprites[estado]
                self.estado = 1
            if estado == 1:
                self.image = self.sprites[estado]
                self.estado = 2
            if estado == 2:
                self.image = self.sprites[estado]
                self.estado = 3
            if estado == 3:
                self.image = self.sprites[estado]
                self.estado = 4
            if estado== 4:
                self.image = self.sprites[estado]
                self.estado = 0
    def reset(self):
        self.image = pygame.image.load('../../imagenes/Highscores/New/Nothing.png')
