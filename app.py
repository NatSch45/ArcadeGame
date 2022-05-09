import pygame
from pygame import mixer
import datetime as DT
from scripts.surfaces import *
from scripts.consts import *

mixer.init()

pygame.display.set_caption("Arcade Game")

ryuSurface = RYU_JUMP


def drawWindow(ryu, hadoukens):
    WIN.blit(BGSF, (0, 0)) # Draw background image
    WIN.blit(ryuSurface, (ryu.x, ryu.y)) # Draw Ryu

    for hadouken in hadoukens:
        WIN.blit(HADOUKEN, (hadouken.x + 10, hadouken.y - 5))

    pygame.display.update()

def ryuMovements(keys_pressed, ryu, jumping):
    global ryuSurface

    if keys_pressed[pygame.K_q] and ryu.x - VEL > 0 and ryuSurface != RYU_HADOUKEN: # LEFT
        if keys_pressed[pygame.K_s]:
            ryu.x -= 2
        else:
            ryu.x -= VEL - 1

    if keys_pressed[pygame.K_d] and ryu.x + VEL + ryu.width < WIDTH and ryuSurface != RYU_HADOUKEN: # RIGHT
        if keys_pressed[pygame.K_s]:
            ryu.x += 2
        else:
            ryu.x += VEL

    if keys_pressed[pygame.K_s] and not jumping and ryuSurface != RYU_HADOUKEN: # STOOP
        ryu.y = 280
        ryuSurface = RYU_STOOP
    elif ryuSurface == RYU_HADOUKEN:
        ryu.y = 233
    elif ryuSurface == RYU_STATIC_PUNCH:
        ryu.x += 2
        ryu.y = 225
    elif not jumping:
        ryu.y = 215

def handleJump(jumping, yVelocity, ryu, startHadouken, startPunch):
    global ryuSurface

    if jumping: # JUMP 
        ryu.y -= yVelocity
        yVelocity -= Y_GRAVITY
        if yVelocity < -JUMP_HEIGHT:
            jumping = False
            yVelocity = JUMP_HEIGHT
        ryuSurface = RYU_JUMP
    elif DT.datetime.now() < startHadouken + DT.timedelta(seconds=0.3):
        ryuSurface = RYU_HADOUKEN
    elif DT.datetime.now() < startPunch + DT.timedelta(seconds=0.2):
        ryuSurface = RYU_STATIC_PUNCH
    else:
        ryuSurface = RYU_STAND
    
    
    return (jumping, yVelocity)

def handleHadoukens(hadoukens):
    for hadouken in hadoukens:
        hadouken.x += HADOUKEN_VEL
        if hadouken.x > WIDTH:
            hadoukens.remove(hadouken)

def main():
    global ryuSurface

    ryu = pygame.Rect(150, 215, 57*2, 105*2)
    hadoukens = []
    startHadouken = DT.datetime.now() - DT.timedelta(seconds=0.5)
    startPunch = DT.datetime.now() - DT.timedelta(seconds=0.5)

    clock = pygame.time.Clock()
    run = True

    jumping = False
    yVelocity = JUMP_HEIGHT

    while run:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(hadoukens) < MAX_HADOUKENS and not jumping:
                    hadouken = pygame.Rect(ryu.x + ryu.width, 245, 28*2, 26*2)
                    hadoukens.append(hadouken)
                    startHadouken = DT.datetime.now()
                    hadoukenSound = mixer.Sound('static/sound/hadouken.wav')
                    hadoukenSound.play()
                
                if event.key == pygame.K_SPACE and DT.datetime.now() > startPunch + DT.timedelta(seconds=0.3):
                    startPunch = DT.datetime.now()

                if event.key == pygame.K_z and not keys_pressed[pygame.K_s]:
                    jumping = True

        jumping, yVelocity = handleJump(jumping, yVelocity, ryu, startHadouken, startPunch)

        ryuMovements(keys_pressed, ryu, jumping)
        handleHadoukens(hadoukens)

        drawWindow(ryu, hadoukens)

    pygame.quit()

if __name__ == "__main__":
    main()