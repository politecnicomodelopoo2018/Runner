import pygame,sys
from pygame import *

class player(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('../../imagenes/Player/Normal.png')
        self.sprites=[pygame.image.load('../../imagenes/Player/Normal.png'),pygame.image.load('../../imagenes/Player/1(2).png')]
        self.muerto=False
        self.maximo=100
        self.rect = self.image.get_rect()
        self.rect.y=317
        self.rect.x = 300
        self.GRAVEDAD = 0.05 # Para el nivel GOD 0.1 , para el resto 0.05
        self.dy = 0
        self.agachado = False
        self.saltando=False
        self.estado=0

    def colision(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def salto(self,key):

        if self.dy == 0:
            if key[K_UP]:
                self.saltando = True
                self.dy = -3.5 # Para el nivel GOD 5 , para el resto -3.5
        else:
            if self.saltando:
                self.rect.y += self.dy
                self.dy += self.GRAVEDAD
                if self.rect.y > 317:
                    self.dy = 0
                    self.rect.y = 317
                    self.saltando = False

    def Agacharse(self,C):
        if C :
            self.agachado = True

        if self.agachado:
            if  self.saltando is False:
                self.image = pygame.image.load('../../imagenes/Player/Agachado.png')
                self.rect.y = 400
    def Pararse(self,C):
        if C:
            self.agachado = False
        if not self.agachado:
            if self.saltando is False:
                self.image = pygame.image.load('../../imagenes/Player/Player.png')
                self.rect.y = 317

    def nestor_en_bloque(self):
        self.rect.x-=4
    def cambiar_sprite(self,estado):
        if estado == 0:
            self.image=self.sprites[estado]
            self.estado=1
        if estado == 1:
            self.image=self.sprites[estado]
            self.estado = 0
    def fuera_pantalla(self):
        if self.rect.x <= -280:
            return True






