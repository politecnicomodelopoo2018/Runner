import pygame

class Player(pygame.sprite.Sprite):



    def __init__(self,x,y):

        self.image = pygame.image.load('imagenes/Player/Player.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

