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

    def saltar(self,suelo):
        self.saltando=True
        self.quieto=False
        self.bajando=False

        if self.rect.y >= self.maximo:
            self.bajando= True
            self.saltando=False


        if self.bajando is False:

            if self.dy == 0:
                self.dy = -2

            else:
                self.rect.y += self.dy
                self.dy += self.GRAVEDAD

                if self.rect.y > suelo:
                    self.dy = 0
                    self.rect.y = suelo

        if self.bajando:
            self.rect.y -= 15
