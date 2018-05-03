'''
Mack Tang
Final Project
This project is a jumping platformer game that is planned
to be playable by humans and machine learning
'''

import pygame as pg
import physics

import settings

from os import path

#shorten usage of pygame vector object
vec = pg.math.Vector2

# the player class inherits from the sprite class
# and holds all information to the player sprite
# and jumping attributes. It also contains
# the update function, which updates the player sprite.
class Player(pg.sprite.Sprite):

    # this should be an enum eventually
    LEFT = 0
    RIGHT = 1
    CENTER = 2
    INHERIT = 3
    # JUMPAMOUNT = 1.5
    JUMPAMOUNT = 2.0


    # Constructor
    # inputs: game width and height (for spawning in center)
    def __init__(self, width, height):

        self.pos = vec(settings.WIDTH / 2, settings.HEIGHT * 2 / 3)
        self.vel = vec(0,0)

        # pg.sprite.Sprite.__init__(self)
        # self.image = pg.image.load("atom_12.png")
        # self.rect = self.image.get_rect()
        #
        # self.rect.center = self.pos
        #
        self.width = width
        self.height = height

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((25, 25))
        self.image.fill(settings.GREEN)
        self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # self.pos = vec(WIDTH / 2, HEIGHT / 2)
        # self.vel = vec(0, 0)
        # self.acc = vec(0, 0)

        self.player_load_data()

    # loads in player sounds from snd folder
    def player_load_data(self):
        self.dir = path.dirname(__file__)
        self.snd_dir = path.join(self.dir, 'snd')
        # self.coin_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Pickup_Coin18.wav'))
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Jump3_low_volume.wav'))
        # self.death_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Explosion6.wav'))

    # inputs: mode, which can be 0, 1, or 2,
    # which make player jump left, right, or center (straight up)
    def jump(self,mode):

        # self.vel.y = -6.5
        self.vel.y = -10.5
        direct = 1
        if mode == self.LEFT:
            direct = -1
        elif mode == self.CENTER:
            direct = 0
        # elif mode == self.INHERIT:
        #     direct =
        self.vel.x = self.JUMPAMOUNT * direct
        # self.jump_sound.play()
        # removed jump sound for now due to inability to play sounds quickly after another

    # returns player velocity vector
    def getSpeed(self):
        return [self.vel.x,self.vel.y]

    # Applies gravity to player,
    # Updates player position based on speed,
    # Teleports player to opposite side
    # if they move off left or right.
    def update(self):
        # print "about to update velocity"
        physics.updateVelocity(self.vel, 0, .4)  # gravitational pull

        # physics.updateVelocity(self.vel, self.vel.x * -0.01, 0) # friction
        # physics.addFriction(self.vel,-0.9)

        self.pos = self.pos + self.vel

        # wrap screen from left to right
        # by teleporting player
        if self.pos.x > self.width:
            self.pos.x = 0

        if self.pos.x < 0:
            self.pos.x = self.width

        self.rect.midbottom = self.pos

