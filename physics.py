#dah
# import pygame as pg

# vec = pg.math.Vector2

# Inputs: player velocity vector, acceleration in x and y direction
def updateVelocity(vel, ax, ay):

    #update vector
    vel.y = ay + vel.y
    vel.x = ax + vel.x

# def addFriction(vel,muFriction):
#     vel = vel + vel * muFriction
