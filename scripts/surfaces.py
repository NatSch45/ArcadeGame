import pygame
import os
from scripts.consts import WIDTH, HEIGHT

IMG_DIR = 'static/img'
MULTIPLIER = 2

#* LOGO
LOGO = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Logo.png')), (222*1.5, 104*1.5))
#* BACKGROUND STREET FIGHTER HD
BGSF = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'bgsfhd.jpg')), (WIDTH, HEIGHT))

#* RYU CHARACTER SURFACES
RYU_NAME = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuName.png')), (63*MULTIPLIER, 16*MULTIPLIER))
# RIGHT DIRECTED (default)
RYU_STAND = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuStand.png')), (46*MULTIPLIER, 92*MULTIPLIER))
RYU_JUMP = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuJump.png')), (36*MULTIPLIER, 64*MULTIPLIER))
RYU_STOOP = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuStoop.png')), (47*MULTIPLIER, 63*MULTIPLIER))
RYU_STATIC_PUNCH = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuStaticPunch.png')), (75*MULTIPLIER, 92*MULTIPLIER))
RYU_STATIC_KICK = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuStaticKick.png')), (89*MULTIPLIER, 84*MULTIPLIER))
RYU_HADOUKEN = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/RyuHdk.png')), (85*MULTIPLIER, 89*MULTIPLIER))
# LEFT DIRECTED (reverse)
RYU_STAND_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/ReverseRyuStand.png')), (46*MULTIPLIER, 92*MULTIPLIER))
RYU_JUMP_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/ReverseRyuJump.png')), (36*MULTIPLIER, 64*MULTIPLIER))
RYU_STOOP_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/ReverseRyuStoop.png')), (47*MULTIPLIER, 63*MULTIPLIER))
RYU_STATIC_PUNCH_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/ReverseRyuStaticPunch.png')), (75*MULTIPLIER, 92*MULTIPLIER))
RYU_STATIC_KICK_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/ReverseRyuStaticKick.png')), (89*MULTIPLIER, 84*MULTIPLIER))
RYU_HADOUKEN_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ryu/ReverseRyuHdk.png')), (85*MULTIPLIER, 89*MULTIPLIER))

#* KEN CHARACTER SURFACES
KEN_NAME = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenName.png')), (63*MULTIPLIER, 16*MULTIPLIER))
# RIGHT DIRECTED (default)
KEN_STAND = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenStand.png')), (47*MULTIPLIER, 92*MULTIPLIER))
KEN_JUMP = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenJump.png')), (36*MULTIPLIER, 64*MULTIPLIER))
KEN_STOOP = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenStoop.png')), (47*MULTIPLIER, 63*MULTIPLIER))
KEN_STATIC_PUNCH = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenStaticPunch.png')), (74*MULTIPLIER, 92*MULTIPLIER))
KEN_STATIC_KICK = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenStaticKick.png')), (89*MULTIPLIER, 84*MULTIPLIER))
KEN_HADOUKEN = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/KenHdk.png')), (85*MULTIPLIER, 89*MULTIPLIER))
# LEFT DIRECTED (reverse)
KEN_STAND_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/ReverseKenStand.png')), (47*MULTIPLIER, 92*MULTIPLIER))
KEN_JUMP_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/ReverseKenJump.png')), (36*MULTIPLIER, 64*MULTIPLIER))
KEN_STOOP_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/ReverseKenStoop.png')), (47*MULTIPLIER, 63*MULTIPLIER))
KEN_STATIC_PUNCH_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/ReverseKenStaticPunch.png')), (74*MULTIPLIER, 92*MULTIPLIER))
KEN_STATIC_KICK_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/ReverseKenStaticKick.png')), (89*MULTIPLIER, 84*MULTIPLIER))
KEN_HADOUKEN_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ken/ReverseKenHdk.png')), (85*MULTIPLIER, 89*MULTIPLIER))

#* GEKI CHARACTER SURFACES
GEKI_NAME = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/GekiName.png')), (63*MULTIPLIER, 16*MULTIPLIER))
# RIGHT DIRECTED (default)
GEKI_STAND = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/GekiStand.png')), (56*MULTIPLIER, 92*MULTIPLIER))
GEKI_JUMP = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/GekiJump.png')), (46*MULTIPLIER, 64*MULTIPLIER))
GEKI_STOOP = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/GekiStoop.png')), (48*MULTIPLIER, 64*MULTIPLIER))
GEKI_STATIC_PUNCH = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/GekiStaticPunch.png')), (96*MULTIPLIER, 91*MULTIPLIER))
GEKI_STATIC_KICK = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/GekiStaticKick.png')), (96*MULTIPLIER, 92*MULTIPLIER))
GEKI_HADOUKEN = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/GekiShourikenPos.png')), (56*MULTIPLIER, 64*MULTIPLIER))
# LEFT DIRECTED (reverse)
GEKI_STAND_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/ReverseGekiStand.png')), (56*MULTIPLIER, 92*MULTIPLIER))
GEKI_JUMP_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/ReverseGekiJump.png')), (46*MULTIPLIER, 64*MULTIPLIER))
GEKI_STOOP_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/ReverseGekiStoop.png')), (48*MULTIPLIER, 64*MULTIPLIER))
GEKI_STATIC_PUNCH_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/ReverseGekiStaticPunch.png')), (96*MULTIPLIER, 91*MULTIPLIER))
GEKI_STATIC_KICK_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/ReverseGekiStaticKick.png')), (96*MULTIPLIER, 92*MULTIPLIER))
GEKI_HADOUKEN_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'geki/ReverseGekiShourikenPos.png')), (56*MULTIPLIER, 64*MULTIPLIER))

#* PROJECTILE SURFACES
HADOUKEN = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Hadouken.png')), (28*MULTIPLIER, 26*MULTIPLIER))
HADOUKEN_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ReverseHadouken.png')), (28*MULTIPLIER, 26*MULTIPLIER))
SHURIKEN = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Shuriken.png')), (8*MULTIPLIER, 8*MULTIPLIER))
SHURIKEN_REVERSE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'ReverseShuriken.png')), (8*MULTIPLIER, 8*MULTIPLIER))