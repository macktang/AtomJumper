import unittest

from player import Player

import settings

import pygame as pg

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""



    def test_jump(self):
        '''test jump function of player'''
        pg.init()
        testplayer = Player(settings.GAME_WIDTH, settings.GAME_HEIGHT)

        first_x_velocity = testplayer.vel.x
        first_y_velocity = testplayer.vel.y

        testplayer.jump(0)

        self.assertTrue(testplayer.vel.y - first_y_velocity == -10.5) #y velocity should be updated
        self.assertTrue(testplayer.vel.x - first_x_velocity == testplayer.JUMPAMOUNT * -1) # x velocity should update



if __name__ == '__main__':
    unittest.main()