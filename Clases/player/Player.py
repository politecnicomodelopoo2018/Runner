import pygame,sys
from pygame import *

class player(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('imagenes/Player/Player.png')
        self.muerto=False
        self.maximo=100
        self.rect = self.image.get_rect()
        self.rect.y=300
        self.rect.x = 300
        self.GRAVEDAD = 0.05
        self.dy = 0


    def colision(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def salto(self,key):
        if self.dy == 0:
            if key[K_UP]:
                self.dy = -3.5
        else:
            self.rect.y += self.dy
            self.dy += self.GRAVEDAD
            if self.rect.y > 300:
                self.dy = 0
                self.rect.y = 300

