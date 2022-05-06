import pygame
import os
from scripts.consts import WIDTH, HEIGHT

#* BACKGROUND STREET FIGHTER HD 
BGSF = pygame.transform.scale(pygame.image.load(os.path.join('static/img', 'bgsfhd.jpg')), (WIDTH, HEIGHT))

#* RYU CHARACTER SURFACES
RYU_STAND = pygame.transform.scale(pygame.image.load(os.path.join('static/img', 'RyuStand.png')), (57*2, 105*2))
RYU_JUMP = pygame.transform.scale(pygame.image.load(os.path.join('static/img', 'RyuJump.png')), (42*2, 69*2))
RYU_STOOP = pygame.transform.scale(pygame.image.load(os.path.join('static/img', 'RyuStoop.png')), (53*2, 71*2))
RYU_STATIC_PUNCH = pygame.transform.scale(pygame.image.load(os.path.join('static/img', 'RyuStaticPunch.png')), (79*2, 97*2))
RYU_HADOUKEN = pygame.transform.scale(pygame.image.load(os.path.join('static/img', 'RyuHdk.png')), (88*2, 92*2))

#* KEN CHARACTER SURFACES

#* HADOUKEN
HADOUKEN = pygame.transform.scale(pygame.image.load(os.path.join('static/img', 'hadouken.png')), (33*2, 33*2))