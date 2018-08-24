import pygame,sys
from pygame import QUIT, K_UP

screen = pygame.display.set_mode((800, 800))
salir = False

bgOne = pygame.image.load('rsz_1rsz_canvas.png')
color_negro = (0, 0, 0)
color_rojo = (200, 0, 0)
bgOne = pygame.image.load('rsz_1rsz_canvas.png')
bgTwo = pygame.image.load('rsz_1rsz_canvas.png')
bgOne_x = 0
bgTwo_x = bgOne.get_width()
coin = pygame.image.load('rsz_1rsz_coin_-_new_super_mario_bros.png')
coin2 = pygame.image.load('rsz_1rsz_coin_-_new_super_mario_bros.png')
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('rsz_1rsz_coin_-_new_super_mario_bros.png')
        self.rect = self.image.get_rect()
        self.rect.center = (300, 300)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('rsz_e58.png')
        self.rect = self.image.get_rect()
        self.rect.center = (0, 300)


tux = pygame.image.load("rsz_e58.png")
all_sprites = pygame.sprite.Group()
player = Coin()
all_sprites.add(player)
dy = 0
y_coin = 300
x = 40
y = 600 - tux.get_height()
GRAVEDAD = 0.02


pos_suelo = 600

while not salir:
    pygame.display.flip()
    screen.blit(bgOne, (bgOne_x, 0))
    screen.blit(bgTwo, (bgTwo_x, 0))
    all_sprites.draw(screen)
    #screen.blit(coin, (bgOne_x, y_coin))


    for e in pygame.event.get():
        if e.type == QUIT:
            salir = True


    key = pygame.key.get_pressed()

    bgOne_x -= 10
    bgTwo_x -= 10


    if bgOne_x == -1 * bgOne.get_width():
        bgOne_x = bgTwo_x + bgTwo.get_width()
    if bgTwo_x == -1 * bgTwo.get_width():
        bgTwo_x = bgOne_x + bgOne.get_width()

    if bgOne_x == -1 * coin.get_width():
        bgOne_x = bgTwo_x + coin2.get_width()
    if bgTwo_x == -1 * coin2.get_width():
        bgTwo_x = bgOne_x + coin.get_width()

    if dy == 0:
        if key[K_UP]:
            dy = -3
    else:
        y += dy
        dy += GRAVEDAD

        if y > pos_suelo - tux.get_height():
            dy = 0
            y = pos_suelo - tux.get_height()



    pygame.draw.line(screen, color_negro, (0, pos_suelo), (800, pos_suelo))
    screen.blit(tux, (int(x), int(y)))

    pygame.display.update()
    pygame.display.flip()





    pygame.time.wait(1)