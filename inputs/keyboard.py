#guy.jump

import pygame as pg

def readKeyboard(player,event):

    if event.type == pg.KEYDOWN:

        if event.key == pg.K_LEFT:
            player.jump(player.LEFT)
        elif event.key == pg.K_RIGHT:
            # print "db 1"
            player.jump(player.RIGHT)
        elif event.key == pg.K_UP:
            player.jump(player.CENTER)