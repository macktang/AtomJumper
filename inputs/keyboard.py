'''
Mack Tang
Final Project
This project is a jumping platformer game that is planned
to be playable by humans and machine learning
'''

import pygame as pg

#input: player to move,
# list of all keyboard events
#output: moves player accordingly
# by calling player jump functions
def readKeyboard(player,event):

    if event.type == pg.KEYDOWN:

        if event.key == pg.K_LEFT:
            player.jump(player.LEFT)
        elif event.key == pg.K_RIGHT:
            player.jump(player.RIGHT)
        elif event.key == pg.K_UP:
            player.jump(player.CENTER)