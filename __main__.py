import pygame as pg
from game import Game


g = Game()

while g.running:
    g.new()
    g.run()

pg.quit()