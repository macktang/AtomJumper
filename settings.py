'''
Mack Tang
Final Project
This project is a jumping platformer game that is planned
to be playable by humans and machine learning
'''

# settings.py serves as many parameters
# that can be imported in


WIDTH = 384

HEIGHT = 683

SPAWN_HEIGHT = -708
# -683 - 25

FPS = 60

GATE_WIDTH = WIDTH / 3

FONT_NAME = 'arial'

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

# # Starting platforms
# PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
#                  (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
#                  (125, HEIGHT - 350, 100, 20),
#                  (350, 200, 100, 20),
#                  (175, 100, 50, 20)]