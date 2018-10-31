import pygame,sys
from pygame import *

class player(pygame.sprite.Sprite):
    person = 'Jones'  # Jones,Logic,Ronald

    def __init__(self):
        super().__init__()

        self.image=pygame.image.load('../../imagenes/Player/Normal.png')
        self.sprites = {'Jones':[pygame.image.load('../../imagenes/Player/Normal.png'),
                                pygame.image.load('../../imagenes/Player/1(2).png')],
                        'Logic':[pygame.image.load('../../imagenes/Player/Logic/Normal.png'),
                                pygame.image.load('../../imagenes/Player/Logic/1.png')],
                        'Ronald':[pygame.image.load('../../imagenes/Player/Ronaldinho/1.png'),
                                  pygame.image.load('../../imagenes/Player/Ronaldinho/2.png'),
                                   pygame.image.load('../../imagenes/Player/Ronaldinho/3.png'),
                                    pygame.image.load('../../imagenes/Player/Ronaldinho/4.png'),
                                     pygame.image.load('../../imagenes/Player/Ronaldinho/5.png'),
                                      pygame.image.load('../../imagenes/Player/Ronaldinho/6.png'),
                                        pygame.image.load('../../imagenes/Player/Ronaldinho/7.png'),
                                         pygame.image.load('../../imagenes/Player/Ronaldinho/8.png'),
                                          pygame.image.load('../../imagenes/Player/Ronaldinho/9.png'),
                                            pygame.image.load('../../imagenes/Player/Ronaldinho/10.png'),
                                             pygame.image.load('../../imagenes/Player/Ronaldinho/11.png'),
                                              pygame.image.load('../../imagenes/Player/Ronaldinho/12.png')]}

        self.maximo=100
        self.rect = self.image.get_rect()
        self.rect.y=317
        self.rect.x = 300
        self.GRAVEDAD = 0.1 # Para el nivel GOD 0.1 , para el resto 0.05
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
                self.dy = -5 # Para el nivel GOD 5 , para el resto -3.5
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
    def cambiar_sprite(self):
        if self.estado <len(self.sprites[self.person]):
            self.image=self.sprites[self.person][self.estado]
            self.estado+=1
        if self.estado == len(self.sprites[self.person]):
            self.estado=0
    def fuera_pantalla(self):
        if self.rect.x <= -100:
            return True

    def reset(self):
        self.rect.y = 317
        self.rect.x = 300
        self.estado = 0






