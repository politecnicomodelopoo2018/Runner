import pygame,sys
from pygame import *

class enemigo(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagenes/Enemys/1.png')
        self.muerto = False
        self.rect = self.image.get_rect()
        self.rect.y = 445
        self.rect.x = 1300
        self.estado=0
        #self.sprites=(pygame.image.load('imagenes/Enemys/1.png'),pygame.image.load('imagenes/Enemys/2.png'))


    def moverse(self):
        self.rect.x -= 3.5
    def fuera_pantalla(self):
        if self.rect.x <= -200:
            self.fuera()
    def fuera(self):
        self.rect.x=1360


