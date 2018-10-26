# -*- encoding: utf-8 -*-
from Clases.Menu.Selector.Fondo import f
from Clases.Menu.Highscores.Text import text
from Clases.DB import db
from Clases.Menu.Selector.Ronald.Boton import ronald
from Clases.Menu.Selector.Logic.Boton import logic
from Clases.Menu.Selector.Indiana.Boton import jones
from Clases.player.Player import player
import pygame
class selector(object):
    @staticmethod
    def inicio():
        estado = 0
        r = ronald()
        l = logic()
        j = jones()
        ro = player()
        ro.rect.x=865
        l_image=pygame.image.load('../../imagenes/Player/Logic/Normal.png')
        j_image=pygame.image.load('../../imagenes/Player/Normal.png')
        all_sprites = pygame.sprite.Group()
        all_sprites.add(r,l,j,ro)
        ro.person='Ronald'
        pygame.init()
        salir = False
        screen = pygame.display.set_mode((1280, 700))
        fondo = f()

        while not salir:
            ro.cambiar_sprite()
            for e in pygame.event.get():

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RIGHT:
                       if estado is not 2:
                            estado+=1

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                       if estado is not 0:
                            estado-=1

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                       if estado is not 0:
                            if estado is 0:
                                j.jugar()
                            if estado is 1 :
                                l.jugar()
                            if estado is 2:
                                r.jugar()


                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        from Clases.Menu.Menu import menu
                        menu.iniciar()



            r.toc(estado)
            l.toc(estado)
            j.toc(estado)
            screen.blit(fondo.image,(0,0))
            screen.blit(l_image, (540 , 300))
            screen.blit(j_image, (225, 300))
            all_sprites.draw(screen)
            pygame.display.flip()
            pygame.time.wait(50)