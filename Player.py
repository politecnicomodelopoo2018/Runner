class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('rsz_1rsz_coin_-_new_super_mario_bros.png')
        self.rect = self.image.get_rect()
        self.rect.center = (300,300)

    def update(self):
        self.rect.x += 5


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

all_sprites.draw(screen)