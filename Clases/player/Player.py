import pygame,sys
from pygame import *

class player(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('imagenes/Player/Player.png')
        self.muerto=False
        self.saltando=False
        self.maximo=100
        self.quieto=True
        self.bajando=False
        self.rect = self.image.get_rect()
        self.rect.y=300
        self.rect.x = 300

    def saltar(self):
        self.saltando=True
        self.quieto=False
        self.bajando=False

        if self.rect.y >= self.maximo:
            self.bajando= True
            self.saltando=False


        if self.bajando is False:

            for i in range(20):
                if i <= 10:
                    self.rect.y -= 0.5
                elif i > 10:
                    self.rect.y += 0.5

        if self.bajando:
            self.rect.y -= 15
