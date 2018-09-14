import pygame
from Clases.player.player import Player
p = Player(300,300)
screen = pygame.display.set_mode((600, 600))

all_sprites = pygame.sprite.Group()
black = (0,0,0)
all_sprites.add(p)
screen.fill(black)
while True:



    all_sprites.draw(screen)
    pygame.display.update()
    pygame.display.flip()
    pygame.time.wait(1)
