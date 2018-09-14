import pygame
from Clases.player.player import Player
p = Player(400,400)
screen = pygame.display.set_mode((600, 600))

all_sprites = pygame.sprite.Group()
black = (0,0,0)
all_sprites.add(p)
while True:

    screen.fill(black)

    all_sprites.draw(screen)



