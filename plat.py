'''
Mack Tang
Final Project
This project is a jumping platformer game that is planned
to be playable by humans and machine learning
'''

import pygame as pg
import settings


# Platform class, inherits from pygame sprite class
class Plat(pg.sprite.Sprite):

    # Spawn in platform
    # Inputs: x and y coordinate for top left corner of platform,
    # desired width and height of platform
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(settings.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y