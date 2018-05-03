'''
Mack Tang
Final Project
This project is a jumping platformer game that is planned
to be playable by humans and machine learning
'''

import pygame as pg
from settings import *
from inputs.joystick import Joysticks
from player import Player
from inputs import keyboard

from plat import Plat

import random

from os import path

from collections import deque


# The game class is used to take off some of the work from
# the code in __main.py__, and is the highest hierarchy class.
# The game class holds all pygame classes, platform class, and
# player class.
class Game():

    #Game Constructor
    # initializes pygame, game window size
    # clock, instantiates joystick class,
    # sets screen size
    def __init__(self):

        pg.init()
        self.size = [WIDTH, HEIGHT]
        self.clock = pg.time.Clock()
        self.sticks = Joysticks()
        self.screen = pg.display.set_mode(self.size)
        self.running = True

        self.font_name = pg.font.match_font(FONT_NAME)

        self.score = 0

        self.bot_active = False # store whether bot or human will play

        self.load_data()

        self.d = deque()

    # loads in wav files from sound folder (snd)
    def load_data(self):
        self.dir = path.dirname(__file__)
        self.snd_dir = path.join(self.dir, 'snd')
        self.coin_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Pickup_Coin18.wav'))
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Powerup13.wav'))
        self.death_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Explosion6.wav'))

    # show the start screen and accompanying text,
    # pause to wait for user key or mouse press
    def show_start_screen(self):
        self.screen.fill(WHITE)
        self.draw_text("AtomJumper", 48, BLACK, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Use left and right arrows to move", 22, BLACK, WIDTH / 2, HEIGHT / 2)
        self.draw_text("press any key to play! or Click Mouse to activate bot", 22, BLACK, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    # wait for any key to be pressed or mouse click
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    waiting = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    waiting = False
                    self.bot_active = True


    # instantiates sprite groups
    # instantiates player
    # generates first gate
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.scoring = pg.sprite.Group()
        self.player = Player(WIDTH, HEIGHT)
        self.all_sprites.add(self.player)

        self.player_height = WIDTH

        self.last_gate_player_height = 0

        self.font_name = pg.font.match_font(FONT_NAME)

        self.genFirstGate(-40)

    # the main game loop
    # reads in keyboard events
    # updates all sprites
    # draws all sprites
    # ticks game clock
    def run(self):
        self.playing = True

        if self.bot_active == True:
            # self.center_future = 0
            # self.d.append(-1)
            # print list(self.d)
            while self.playing:
                # will leave event listener on, so timing is same.
                # human player could disrupt bot, but is not meant to
                self.events()
                self.bot_events()
                # print "db passed bot event handler"
                self.update()
                self.draw()
                self.clock.tick(FPS)
                # put bot code here!

        elif self.bot_active == False:
            while self.playing:
                self.events()
                self.update()
                self.draw()
                self.clock.tick(FPS)
                # self.frameCount += 1

    # function reads in events
    # such as keyboard presses
    # or joystick moves and reacts to these events
    def events(self):
        events = pg.event.get()
        for event in events:
            keyboard.readKeyboard(self.player, event)
            self.sticks.listenJoystick(self.player, event)
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
                # sys.exit()

    # event handler for the bot, replaces keyboard event listener
    def bot_events(self):
        if (self.d[0] != -1): # if the leftmost item is not equal to -1
            # if self.player.pos.y >= (HEIGHT - 270):
                if self.player.rect.centerx >= self.d[0]:
                    self.player.jump(self.player.LEFT)
                elif self.player.rect.centerx < self.d[0]:
                    self.player.jump(self.player.RIGHT)

        else:
            # if self.player.pos.y >= (HEIGHT - 270):
                self.player.jump(self.player.LEFT)

    # game update function
    # updates all sprites, checks for collisions
    # scrolls window, deletes old gates
    def update(self):
        # print self.player_height

        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)


        if hits:
            # print "collision"
            self.score = 0
            self.death_sound.play()
            self.d.clear()
            self.playing = False
            # self.player.pos.y = hits[0].rect.top + 1
            # self.player.vel.y = 0

        if self.player.rect.top <= HEIGHT / 2:
            self.player.pos.y += abs(self.player.vel.y)
            self.player_height += abs(self.player.vel.y)

            # for s in self.scoring:
            #     if s.rect.top >= HEIGHT:
            #         self.score += 1

            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)

                if plat.rect.top >= HEIGHT:
                    plat.kill()

        for plat_score in self.scoring:
            if self.player.rect.bottom <= plat_score.rect.top:
                self.score += 1
                try:
                    self.d.popleft() #update bot aim to the next gate
                except IndexError:
                    print "tried to pop from an empty deque, supressing error"
                self.coin_sound.play()
                self.scoring.remove(plat_score)


                # if plat.rect.top >= HEIGHT:
                #     if pg.sprite.Group.has(self.scoring,plat):
                #         self.score += 1
                #         self.coin_sound.play()
                #
                #     plat.kill()


        if (self.player_height > (self.last_gate_player_height + WIDTH)):
            # print "new gate will be generated"
            self.generateGate(SPAWN_HEIGHT)
            self.last_gate_player_height = self.player_height


        if self.player.rect.top >= HEIGHT:
            self.score = 0
            self.d.clear()
            self.playing = False

    # input: offset to generate gate at
    # this function generates a gate at the specified location
    def generateGate(self, offset):

        randomGateStart = random.randrange(10, WIDTH - 10 - GATE_WIDTH)
        pa = Plat(0, offset, randomGateStart, 40)
        self.platforms.add(pa)
        self.scoring.add(pa)
        self.all_sprites.add(pa)

<<<<<<< HEAD
        self.center_future = randomGateStart + settings.GATE_WIDTH/2
        print "gate center target updated"
=======
        # self.center_future = randomGateStart + GATE_WIDTH/2
        self.d.append(randomGateStart + GATE_WIDTH/2)
>>>>>>> 03efef7ddd547f47cce147398d062bc69d28d690

        pb = Plat(randomGateStart + GATE_WIDTH, offset,
                  WIDTH - GATE_WIDTH - randomGateStart, 40)
        self.platforms.add(pb)
        self.all_sprites.add(pb)

        brick_a_start = random.randrange(randomGateStart,randomGateStart + GATE_WIDTH)
        brick_a_height = random.randrange(13,13+GATE_WIDTH)
        ba = Plat(brick_a_start,SPAWN_HEIGHT-brick_a_height,25,25) #generate brick between 13 to gate height up
        self.platforms.add(ba)
        self.all_sprites.add(ba)

        brick_b_start = random.randrange(randomGateStart,randomGateStart + GATE_WIDTH)
        brick_b_height = random.randrange(randomGateStart,randomGateStart + GATE_WIDTH)
        bb = Plat(brick_b_start,SPAWN_HEIGHT+brick_b_height,25,25)
        self.platforms.add(bb)
        self.all_sprites.add(bb)

    def genFirstGate(self,offset):
        randomGateStart = random.randrange(10, WIDTH - 10 - GATE_WIDTH)
        pa = Plat(0, offset, randomGateStart, 40)
        self.platforms.add(pa)
        self.scoring.add(pa)
        self.all_sprites.add(pa)

        # self.center_future = randomGateStart + GATE_WIDTH/2
        self.d.append(randomGateStart + GATE_WIDTH/2)
        # self.d.popleft() #delete initial "-1" in queue

        pb = Plat(randomGateStart + GATE_WIDTH, offset,
                  WIDTH - GATE_WIDTH - randomGateStart, 40)
        self.platforms.add(pb)
        self.all_sprites.add(pb)

    # draws screen background, draws score,
    # sprites, and renders display
    def draw(self):
        self.screen.fill(WHITE)

        self.all_sprites.draw(self.screen)

        self.draw_text(str(int(self.score)), 22, BLACK, WIDTH / 2, 15)

        pg.display.flip()

    # draws text at the specified location
    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)