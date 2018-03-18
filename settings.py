'''
Mack Tang
Final Project
This project is a jumping platformer game that is planned
to be playable by humans and machine learning
'''

# settings.py serves as many parameters
# that can be imported in


GAME_WIDTH = 384

GAME_HEIGHT = 683

FPS = 60

GATE_WIDTH = GAME_WIDTH / 3

# Colors in RGB tuple form
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (156,196,252)
LIGHT_GREEN = (0,155,155)
PURPLE = (204,0,204)
ORANGE = (255,153,0)

GRAY = (150, 150, 150)

FONT_NAME = "arial"

# # Starting platforms
# PLATFORM_LIST = [(0, GAME_HEIGHT - 40, GAME_WIDTH, 40),
#                  (GAME_WIDTH / 2 - 50, GAME_HEIGHT * 3 / 4, 100, 20),
#                  (125, GAME_HEIGHT - 350, 100, 20),
#                  (350, 200, 100, 20),
#                  (175, 100, 50, 20)]