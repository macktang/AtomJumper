import pygame as pg
import settings
from inputs.joystick import Joysticks
from player import Player
from inputs import keyboard

from plat import Plat

import random

class Game():
    def __init__(self):

        pg.init()
        self.size = [settings.GAME_WIDTH, settings.GAME_HEIGHT]
        self.clock = pg.time.Clock()
        self.sticks = Joysticks()
        self.screen = pg.display.set_mode(self.size)
        self.running = True

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(settings.GAME_WIDTH, settings.GAME_HEIGHT)
        self.all_sprites.add(self.player)

        # for platform in settings.PLATFORM_LIST:
        #     p = Plat(*platform)
        #     self.all_sprites.add(p)
        #     self.platforms.add(p)

        # self.gateStart = random.randrange(20,settings.GAME_WIDTH - 20 - settings.GATE_WIDTH)
        self.lastGate = -50
        self.GateCount = 0

        self.generateGate(-50)
        self.generateGate(-50-settings.GAME_WIDTH)
        # self.generateGate(-50-settings.GAME_WIDTH-settings.GAME_WIDTH)

        # p1 = Plat(0,-50,self.gateStart, 25)
        # self.platforms.add(p1)
        # self.all_sprites.add(p1)
        #
        # p2 = Plat(self.gateStart+settings.GATE_WIDTH, -50,
        #           settings.GAME_WIDTH - settings.GATE_WIDTH - self.gateStart, 25)
        # self.platforms.add(p2)
        # self.all_sprites.add(p2)

        # p1 = Plat(0,settings.GAME_HEIGHT-40,settings.GAME_WIDTH, 30)
        # self.platforms.add(p1)
        # self.all_sprites.add(p1)
        #
        # p2 = Plat(settings.GAME_WIDTH * 3/4,settings.GAME_HEIGHT/2, 200, 30)
        # self.platforms.add(p2)
        # self.all_sprites.add(p2)

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(settings.FPS)

    def update(self):
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)

        if hits:
            # self.player.rect.midbottom[1] = hits[0].rect.top + 1
            # self.player.rect.midbottom[0] = hits[0].rect.top
            self.player.pos.y = hits[0].rect.top + 1
            self.player.vel.y = 0
            # print hits[0].rect.top
            # print hits[0].rect.top + 1

        if self.player.rect.top <= settings.GAME_HEIGHT / 2:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)

                if plat.rect.top >= settings.GAME_HEIGHT:
                    plat.kill()

                    self.GateCount -= 1

                    print self.GateCount


    def generateGate(self, offset):

        randomGateStart = random.randrange(20, settings.GAME_WIDTH - 20 - settings.GATE_WIDTH)
        pa = Plat(0, offset, randomGateStart, 25)
        self.platforms.add(pa)
        self.all_sprites.add(pa)

        pb = Plat(randomGateStart + settings.GATE_WIDTH, offset,
                  settings.GAME_WIDTH - settings.GATE_WIDTH - randomGateStart, 25)
        self.platforms.add(pb)
        self.all_sprites.add(pb)

        self.GateCount += 2
        print self.GateCount



    def events(self):
        events = pg.event.get()
        for event in events:
            keyboard.readKeyboard(self.player, event)
            self.sticks.listenJoystick(self.player, event)
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
                # sys.exit()

    def draw(self):
        self.screen.fill(settings.GRAY)

        self.all_sprites.draw(self.screen)

        pg.display.flip()
