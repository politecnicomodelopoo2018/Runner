import pygame,sys
from pygame import *

class enemigo(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagenes/Enemys/rsz_1rsz_mario_fireball.gif')
        self.muerto = False
        self.rect = self.image.get_rect()
        self.rect.y = 445
        self.rect.x = 1300
    def moverse(self):
        self.rect.x -= 3.5
    def fuera_pantalla(self):
        if self.rect.x <= -200:
            self.fuera()
    def fuera(self):
        self.rect.x=1360

