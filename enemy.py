
import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self, width, height,x,y):


        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load("gandalfhoodedition.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.width = width
        self.height = height