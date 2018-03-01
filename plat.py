import pygame as pg
import settings
# from vector import Vector
# import physics

class Plat(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(settings.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y