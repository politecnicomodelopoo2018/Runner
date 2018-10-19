
class registro(object):
    def __init__(self,h):
        import pygame as pg
        from Clases.Menu.Background import background
        from Clases.Menu.RegistroC.text import puntaje
        from Clases.Menu.Niveles_menu import niveles_menu
        from Clases.DB import db
        from Clases.Menu.Highscores.HS import hg
        screen = pg.display.set_mode((1280, 700))
        font = pg.font.Font(None, 32)
        clock = pg.time.Clock()
        input_box = pg.Rect(500, 300, 140, 32)
        color_inactive = pg.Color('lightskyblue3')
        color_active = pg.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        b = background()
        p = puntaje()
        p.score=h
        self.salir = False

        while not self.salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.salir = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pg.KEYDOWN:
                    if active:
                        if event.key == pg.K_RETURN:
                            a = db.connect("INSERT INTO `mydb`.`Jugador` ( `Nombre`, `Puntaje`) VALUES "
                                           "('%s',%s)" % (text,int(p.score)))
                            self.salir=True
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.blit(b.image, b.rect)
            screen.blit(p.show(p.score), (500, 100))
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pg.draw.rect(screen, color, input_box, 2)
            pg.display.flip()
            clock.tick(30)

        if self.salir:
            a = hg()



