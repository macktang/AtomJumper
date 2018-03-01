import pygame as pg
from vector import Vector
import physics

import settings

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    LEFT = 0
    RIGHT = 1
    CENTER = 2
    INHERIT = 3
    JUMPAMOUNT = 1.5

    def __init__(self, width, height):

        # self.vector = Vector(0,0)
        self.pos = vec(10,10)
        self.vel = vec(0,0)

        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("dude.png")
        self.rect = self.image.get_rect()

        self.rect.center = self.pos

        self.width = width
        self.height = height

        # self.pos = self.rect.midbottom

    def jump(self,mode):
        self.vel.y = -6.5
        direct = 1
        if mode == self.LEFT:
            direct = -1
        elif mode == self.CENTER:
            direct = 0
        # elif mode == self.INHERIT:
        #     direct =
        self.vel.x = self.JUMPAMOUNT * direct

    def getSpeed(self):
        return [self.vel.x,self.vel.y]

    def update(self):
        # print "about to update velocity"
        physics.updateVelocity(self.vel, 0, .3)  # gravitational pull
        # physics.updateVelocity(self.vel, self.vel.x * -0.01, 0) # friction
        # physics.addFriction(self.vel,-0.9)

        self.pos = self.pos + self.vel

        if self.pos.x > self.width:
            self.pos.x = 0

        if self.pos.x < 0:
            self.pos.x = self.width

        # portal in floor to ceiling
        # if self.pos.y > settings.GAME_HEIGHT:
        #     self.pos.y = 0

        # self.rect = self.rect.move(self.vel)
        self.rect.midbottom = self.pos

