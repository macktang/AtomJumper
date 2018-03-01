'''
Mack Tang
Final Project
This project is a jumping platformer game that is planned
to be playable by humans and machine learning
'''


import pygame as pg
from game import Game


g = Game()

while g.running:
    g.new()
    g.run()

pg.quit()