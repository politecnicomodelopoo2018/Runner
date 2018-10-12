import pygame
from Clases.Menu.Background import background
from Clases.Menu.Botones.Niveles.uno.uno import uno
from Clases.Menu.Botones.Niveles.dos.dos import dos
from Clases.Menu.Botones.Niveles.tres.tres import tres
pygame.init()

b = background()
uno = uno()
dos = dos()
tres = tres()
screen = pygame.display.set_mode((1280, 700))
all_sprites = pygame.sprite.Group()
all_sprites.add(uno,dos,tres)

class niveles_menu(object):
    def __init__(self):
        estado = 0
        self.salir = False
        while not self.salir:
            uno.toc(estado)
            dos.toc(estado)
            tres.toc(estado)
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_DOWN:
                        if estado == 0 or estado == 1:
                                estado+=1
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_UP:
                            if estado == 1 or estado == 2:
                                estado-=1
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_RETURN:
                            if estado == 0:
                                uno.jugar()
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_RETURN:
                            if estado == 1:
                                dos.jugar()
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_RETURN:
                            if estado == 2:
                                tres.jugar()
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_ESCAPE:
                            self.salir = True
            screen.blit(b.image, b.rect)
            all_sprites.draw(screen)
            pygame.display.flip()
            pygame.time.wait(3)