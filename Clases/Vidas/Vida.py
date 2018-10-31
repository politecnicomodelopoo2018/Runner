import pygame,sys
from pygame import *

class vida(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('../../imagenes/Vidas/1.png')
        self.sprites=[pygame.image.load('../../imagenes/Vidas/1.png'),pygame.image.load('../../imagenes/Vidas/2.png'),
                      pygame.image.load('../../imagenes/Vidas/3.png'),pygame.image.load('../../imagenes/Vidas/4.png'),
                      pygame.image.load('../../imagenes/Vidas/5.png'),pygame.image.load('../../imagenes/Vidas/6.png')]
        self.muerto=False
        self.quieto=True
        self.moviendose=True
        self.rect = self.image.get_rect()
        self.rect.y=100
        self.rect.x = 500
        self.estado=0

    def moverse(self,plus):
        self.rect.x -= 4+plus
    def fuera_pantalla(self):
        if self.rect.x <= -200:
            self.fuera()
    def fuera(self):
        self.rect.x=1400

    def colision(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def cambiar_sprite(self):
        if self.estado <len(self.sprites):
            self.image=self.sprites[self.estado]
            self.estado+=1
        if self.estado == len(self.sprites):
            self.estado=0

    def reset(self):
        self.rect.y = 100
        self.rect.x = 500
        self.estado = 0





