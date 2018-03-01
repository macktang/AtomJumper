#dah
# import pygame as pg

# vec = pg.math.Vector2

def updateVelocity(vel, ax, ay):

    #update vector
    vel.y = ay + vel.y
    vel.x = ax + vel.x

# def addFriction(vel,muFriction):
#     vel = vel + vel * muFriction
