import pygame
import os

pygame.init()

WIDTH, HEIGHT = 900, 500
FLOOR = 410
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
VEL = 4
HADOUKEN_VEL = 7
MAX_HADOUKENS = 1

Y_GRAVITY = 1
JUMP_HEIGHT = 19

FIRST_CHARACTER_HIT = pygame.USEREVENT + 1
SECOND_CHARACTER_HIT = pygame.USEREVENT + 2

HADOUKEN_DAMAGE = 15
PUNCH_DAMAGE = 10
KICK_DAMAGE = 10

FONT_PLAYER = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 20)
FONT_CHARACTER = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 20)
FONT_GAME_OVER = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 80)
FONT_WINNER = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 40)

RED = (255, 0, 0)
ORANGE = (255, 117, 26)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)