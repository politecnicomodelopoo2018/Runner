import pygame,sys
from pygame import *

class vida(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('imagenes/Vidas/1.png')
        self.sprites=[pygame.image.load('imagenes/Vidas/1.png'),pygame.image.load('imagenes/Vidas/2.png'),
                      pygame.image.load('imagenes/Vidas/3.png'),pygame.image.load('imagenes/Vidas/4.png'),
                      pygame.image.load('imagenes/Vidas/5.png'),pygame.image.load('imagenes/Vidas/6.png')]
        self.muerto=False
        self.quieto=True
        self.moviendose=True
        self.rect = self.image.get_rect()
        self.rect.y=100
        self.rect.x = 500
        self.estado=0

    def moverse(self):
        self.rect.x -= 4
    def fuera_pantalla(self):
        if self.rect.x <= -200:
            self.fuera()
    def fuera(self):
        self.rect.x=1400

    def colision(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def cambiar_sprite(self,estado):
        if estado==0:
            self.image=self.sprites[estado]
            self.estado=1
        if estado==1:
            self.image=self.sprites[estado]
            self.estado=2
        if estado==2:
            self.image=self.sprites[estado]
            self.estado=3
        if estado==3:
            self.image=self.sprites[estado]
            self.estado=4

        if estado==4:
            self.image=self.sprites[estado]
            self.estado=5
        if estado==5:
            self.image=self.sprites[estado]
            self.estado=0






