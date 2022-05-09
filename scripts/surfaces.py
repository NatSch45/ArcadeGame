import pygame
import os
from scripts.consts import WIDTH, HEIGHT

IMG_DIR = 'static/img'

#* BACKGROUND STREET FIGHTER HD
BGSF = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'bgsfhd.jpg')), (WIDTH, HEIGHT))

#* RYU CHARACTER SURFACES
# RIGHT DIRECTED (default)
RYU_STAND = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuStand.png')), (46*2, 92*2))
RYU_JUMP = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuJump.png')), (36*2, 64*2))
RYU_STOOP = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuStoop.png')), (47*2, 63*2))
RYU_STATIC_PUNCH = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuStaticPunch.png')), (75*2, 92*2))
RYU_STATIC_KICK = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuStaticKick.png')), (89*2, 84*2))
RYU_HADOUKEN = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuHdk.png')), (85*2, 89*2))
# LEFT DIRECTED (reverse)
RYU_STAND_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/ReverseRyuStand.png')), (46*2, 92*2))
RYU_JUMP_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/ReverseRyuJump.png')), (36*2, 64*2))
RYU_STOOP_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/ReverseRyuStoop.png')), (47*2, 63*2))
RYU_STATIC_PUNCH_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/ReverseRyuStaticPunch.png')), (75*2, 92*2))
RYU_STATIC_KICK_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/ReverseRyuStaticKick.png')), (89*2, 84*2))
RYU_HADOUKEN_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/ReverseRyuHdk.png')), (85*2, 89*2))

#* KEN CHARACTER SURFACES
# RIGHT DIRECTED (default)
KEN_STAND = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenStand.png')), (47*2, 92*2))
KEN_JUMP = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenJump.png')), (36*2, 64*2))
KEN_STOOP = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenStoop.png')), (47*2, 63*2))
KEN_STATIC_PUNCH = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenStaticPunch.png')), (74*2, 92*2))
KEN_STATIC_KICK = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenStaticKick.png')), (89*2, 84*2))
KEN_HADOUKEN = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenHdk.png')), (85*2, 89*2))
# LEFT DIRECTED (reverse)
KEN_STAND_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/ReverseKenStand.png')), (47*2, 92*2))
KEN_JUMP_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/ReverseKenJump.png')), (36*2, 64*2))
KEN_STOOP_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/ReverseKenStoop.png')), (47*2, 63*2))
KEN_STATIC_PUNCH_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/ReverseKenStaticPunch.png')), (74*2, 92*2))
KEN_STATIC_KICK_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/ReverseKenStaticKick.png')), (89*2, 84*2))
KEN_HADOUKEN_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/ReverseKenHdk.png')), (85*2, 89*2))


#* HADOUKEN SURFACES
HADOUKEN = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Hadouken.png')), (28*2, 26*2))
REVERSE_HADOUKEN = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ReverseHadouken.png')), (28*2, 26*2))
