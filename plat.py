'''
Mack Tang
Final Project
This project is a jumping platformer game that is planned
to be playable by humans and machine learning
'''

import pygame as pg
import settings

import random


# Platform class, inherits from pygame sprite class
class Plat(pg.sprite.Sprite):

    # Spawn in platform
    # Inputs: x and y coordinate for top left corner of platform,
    # desired width and height of platform
    def __init__(self, x, y, w, h):
        # random_color_num = random.randint(1, 7)
        # if random_color_num == 1: random_color = settings.GREEN
        # elif random_color_num == 2: random_color = settings.WHITE
        # elif random_color_num == 3: random_color = settings.RED
        # elif random_color_num == 4: random_color = settings.BLUE
        # elif random_color_num == 5: random_color = settings.GRAY
        # elif random_color_num == 6: random_color = settings.PURPLE
        # elif random_color_num == 7: random_color = settings.ORANGE

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(settings.LIGHT_BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y