'''
Mack Tang
Final Project
This project is a jumping platformer game that is planned
to be playable by humans and machine learning
'''

import pygame as pg
import settings
from inputs.joystick import Joysticks
from player import Player
from inputs import keyboard

from plat import Plat

import random

from os import path


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
        self.size = [settings.GAME_WIDTH, settings.GAME_HEIGHT]
        self.clock = pg.time.Clock()
        self.sticks = Joysticks()
        self.screen = pg.display.set_mode(self.size)
        self.running = True

        self.font_name = pg.font.match_font(settings.FONT_NAME)

        self.score = 0

        self.bot_active = False # store whether bot or human will play

        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        self.snd_dir = path.join(self.dir, 'snd')
        self.coin_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Pickup_Coin18.wav'))
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Powerup13.wav'))
        self.death_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Explosion6.wav'))


    def show_start_screen(self):
        self.screen.fill(settings.WHITE)
        self.draw_text("AtomJumper",48,settings.BLACK,settings.GAME_WIDTH/2,settings.GAME_HEIGHT/4)
        self.draw_text("Use left and right arrows to move",22,settings.BLACK,settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2)
        self.draw_text("press any key to play! or Click Mouse to activate bot",22,settings.BLACK,settings.GAME_WIDTH/2,settings.GAME_HEIGHT*3/4)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(settings.FPS)
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
        self.player = Player(settings.GAME_WIDTH, settings.GAME_HEIGHT)
        self.all_sprites.add(self.player)

        self.player_height = settings.GAME_WIDTH

        self.last_gate_player_height = 0

        self.font_name = pg.font.match_font(settings.FONT_NAME)

    # the main game loop
    # reads in keyboard events
    # updates all sprites
    # draws all sprites
    # ticks game clock
    def run(self):
        self.playing = True

        if self.bot_active == True:
            self.center_future = 0
            while self.playing:
                # will leave event listener on, so timing is same.
                # human player could disrupt bot, but is not meant to
                self.events()
                self.bot_events()
                # print "db passed bot event handler"
                self.update()
                self.draw()
                self.clock.tick(settings.FPS)
                # put bot code here!

        elif self.bot_active == False:
            while self.playing:
                self.events()
                self.update()
                self.draw()
                self.clock.tick(settings.FPS)
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
        if (self.center_future != 0):
            # if self.player.pos.y >= (settings.GAME_HEIGHT - 270):
                if self.player.pos.x >= self.center_future:
                    self.player.jump(self.player.LEFT)
                elif self.player.pos.x < self.center_future:
                    self.player.jump(self.player.RIGHT)

        else:
            # if self.player.pos.y >= (settings.GAME_HEIGHT - 270):
                self.player.jump(self.player.LEFT)

    # game update function
    # updates all sprites, checks for collisions
    # scrolls window, deletes old gates
    def update(self):
        # print self.player_height

        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)




        if hits:
            print "collision"
            self.score = 0
            self.death_sound.play()
            self.playing = False
            # self.player.pos.y = hits[0].rect.top + 1
            # self.player.vel.y = 0

        if self.player.rect.top <= settings.GAME_HEIGHT / 2:
            self.player.pos.y += abs(self.player.vel.y)
            self.player_height += abs(self.player.vel.y)

            # for s in self.scoring:
            #     if s.rect.top >= settings.GAME_HEIGHT:
            #         self.score += 1

            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)

                if plat.rect.top >= settings.GAME_HEIGHT:
                    if pg.sprite.Group.has(self.scoring,plat):
                        self.score += 1
                        self.coin_sound.play()

                    plat.kill()


        if (self.player_height > (self.last_gate_player_height + settings.GAME_WIDTH)):
            # print "new gate will be generated"
            self.generateGate(settings.SPAWN_HEIGHT)
            self.last_gate_player_height = self.player_height


        if self.player.rect.top >= settings.GAME_HEIGHT:
            self.score = 0
            self.playing = False

    # input: offset to generate gate at
    # this function generates a gate at the specified location
    def generateGate(self, offset):

        randomGateStart = random.randrange(10, settings.GAME_WIDTH - 10 - settings.GATE_WIDTH)
        pa = Plat(0, offset, randomGateStart, 40)
        self.platforms.add(pa)
        self.scoring.add(pa)
        self.all_sprites.add(pa)

        self.center_future = randomGateStart + settings.GATE_WIDTH/2

        pb = Plat(randomGateStart + settings.GATE_WIDTH, offset,
                  settings.GAME_WIDTH - settings.GATE_WIDTH - randomGateStart, 40)
        self.platforms.add(pb)
        # self.scoring.add(pb)
        self.all_sprites.add(pb)

        brick_a_start = random.randrange(randomGateStart,randomGateStart + settings.GATE_WIDTH)
        brick_a_height = random.randrange(13,13+settings.GATE_WIDTH)
        ba = Plat(brick_a_start,settings.SPAWN_HEIGHT-brick_a_height,25,25) #generate brick between 13 to gate height up
        self.platforms.add(ba)
        self.all_sprites.add(ba)
        # brick_b_start = random.randrange()

        brick_b_start = random.randrange(randomGateStart,randomGateStart + settings.GATE_WIDTH)
        brick_b_height = random.randrange(randomGateStart,randomGateStart + settings.GATE_WIDTH)
        bb = Plat(brick_b_start,settings.SPAWN_HEIGHT+brick_b_height,25,25)
        self.platforms.add(bb)
        self.all_sprites.add(bb)



        # brick_top = Plat()

        # self.GateCount += 2
        # print self.GateCount

    # draws screen background, draws score,
    # sprites, and renders display
    def draw(self):
        self.screen.fill(settings.WHITE)

        self.all_sprites.draw(self.screen)

        self.draw_text(str(int(self.score)),22,settings.BLACK,settings.GAME_WIDTH/2,15)

        pg.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)