import pygame
from Clases.player.Player import player
p = player()
screen = pygame.display.set_mode((1280, 700))
all_sprites = pygame.sprite.Group()
black = (0,0,0)
all_sprites.add(p)

while True:

    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.update()
    pygame.display.flip()
    pygame.time.wait(1)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            p.saltar()