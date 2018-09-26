import pygame,sys
from pygame import *

class vida(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('imagenes/Vidas/corazon-de-8-bits.png')
        self.muerto=False
        self.quieto=True
        self.moviendose=True
        self.rect = self.image.get_rect()
        self.rect.y=100
        self.rect.x = 500



