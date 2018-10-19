import pygame
from Clases.Menu.Background import background
from Clases.Menu.Botones.Jugar.Jugar import jugar
from Clases.Menu.Botones.Personaje.Personaje import personaje
from Clases.Menu.Selector.Fondo import f
pygame.init()
salir = False
b = background()
j = jugar()
p = personaje()
screen = pygame.display.set_mode((1280, 700))
all_sprites = pygame.sprite.Group()
all_sprites.add(j,p)
estado = 0
while not salir:
    j.toc(estado)
    p.toc(estado)
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_DOWN:
                if estado == 0:
                    estado+=1
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                if estado == 1:
                    estado-=1
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                salir=True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                if estado == 0:
                    j.jugar()
                elif estado == 1:
                    p.jugar()


    screen.blit(b.image, b.rect)
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.wait(3)