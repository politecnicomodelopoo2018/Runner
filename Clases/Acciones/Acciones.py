class acciones(object):

    def colision(self, sprite):
        return self.rect.colliderect(sprite.rect)