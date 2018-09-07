import pygame,sys
from pygame import *
import random
from pygame.locals import *
screen = pygame.display.set_mode((600, 600))
screen = pygame.display.set_mode((600, 600))


salir = False
pygame.init()
bgOne = pygame.image.load('rsz_1rsz_canvas.png')
color_negro = (0, 0, 0)
color_rojo = (200, 0, 0)
bgOne = pygame.image.load('rsz_1rsz_canvas.png')
bgTwo = pygame.image.load('rsz_1rsz_canvas.png')
bgOne_x = 0
bgTwo_x = bgOne.get_width()
coin = pygame.image.load('rsz_1rsz_coin_-_new_super_mario_bros.png')
coin2 = pygame.image.load('rsz_1rsz_coin_-_new_super_mario_bros.png')
myfont = pygame.font.SysFont("monospace", 16)
WHITE = (255,255,255)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coiiiin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (0, 300)
        self.Muerto = False

    def bg_one(self,x):
        self.rect.center = (x, 300)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('hiler.png')
        self.rect = self.image.get_rect()
        self.rect.center = (100, 530)
        self.Muerto = False

    def bg_one(self,x):
        self.rect.center = (x, 530)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pl.png')
        self.rect = self.image.get_rect()
        self.rect.center = (40, 423)
        self.rect.x = 40
        self.rect.y = 423
        self.GRAVEDAD = 0.02
        self.dy = 0

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

tux = pygame.image.load("rsz_1rsz_coin_-_new_super_mario_bros.png")
all_sprites = pygame.sprite.Group()
player = Player()
coine = Coin()
ene = Enemy()
all_sprites.add(coine,player,ene)
pos_suelo = 600
score = 0
y_tux = 300
shet = 0
score = 0

vel = 0
while not salir:
    pygame.display.flip()


    screen.blit(bgOne, (bgOne_x, 0))
    screen.blit(bgTwo, (bgTwo_x, 0))
    #screen.blit(tux, (bgOne_x, y_tux))
    all_sprites.draw(screen)


    for e in pygame.event.get():
        if e.type == QUIT:
            salir = True


    key = pygame.key.get_pressed()
    bgOne_x -= 5 + vel
    bgTwo_x -= 5 + vel


    if bgOne_x == -1 * bgOne.get_width():
        bgOne_x = bgTwo_x + bgTwo.get_width()
    if bgTwo_x == -1 * bgTwo.get_width():
        bgTwo_x = bgOne_x + bgOne.get_width()

    coine.bg_one(bgOne_x+shet)
    ene.bg_one(bgOne_x+900)

    if player.dy == 0:
        if key[K_UP]:
            player.dy = -2.5
    else:
        player.rect.y += player.dy
        player.dy += player.GRAVEDAD

        if player.rect.y > (pos_suelo - player.image.get_height()):
            player.dy = 0
            player.rect.y = (pos_suelo - player.image.get_height())

    if player.is_collided_with(coine):
        shet -= 300
        if shet < (-1200):
            shet = -400
        score+=100
    if player.is_collided_with(ene):
        salir = True

    if score > 500:
        vel += 2
    pygame.draw.line(screen, color_negro, (0, pos_suelo), (800, pos_suelo))

    scoretext = myfont.render("Score {0}".format(score), 1, (0, 0, 0))
    screen.blit(scoretext, (5, 10))

    # screen.blit(tux, (int(x), int(y)))

    pygame.display.update()
    pygame.display.flip()
    #print(player.image.get_height(),player.image.get_width())
    #print(score)
    pygame.time.wait(1)