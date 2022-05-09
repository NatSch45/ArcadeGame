import pygame
import os

pygame.init()

#* WINDOW
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FLOOR = 410

#* ANIMATIONS
FPS = 60
VEL = 4
HADOUKEN_VEL = 7
MAX_HADOUKENS = 1

#* JUMP
Y_GRAVITY = 1
JUMP_HEIGHT = 19

#* USER EVENTS
FIRST_CHARACTER_HIT = pygame.USEREVENT + 1
SECOND_CHARACTER_HIT = pygame.USEREVENT + 2

#* DAMAGES
HADOUKEN_DAMAGE = 15
PUNCH_DAMAGE = 10
KICK_DAMAGE = 10

#* FONTS
FONT_PLAYER = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 20)
FONT_CHARACTER = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 20)
FONT_GAME_OVER = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 80)
FONT_WINNER = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 40)
FONT_BUTTONS = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 50)

#* COLORS
RED = (255, 0, 0)
ORANGE = (255, 117, 26)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)