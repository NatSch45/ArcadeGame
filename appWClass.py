import pygame
from pygame import mixer
import datetime as DT
from scripts.surfaces import *
from scripts.consts import *
from scripts.classes.ryu import ryu

mixer.init()

pygame.display.set_caption("Arcade Game")

def drawWindow(c1):
    WIN.blit(BGSF, (0, 0)) # Draw background image
    WIN.blit(c1.drawing, (c1.surface.x, c1.surface.y)) # Draw Ryu

    for hadouken in c1.hadoukens:
        WIN.blit(HADOUKEN, (hadouken.x + 10, hadouken.y - 5))

    pygame.display.update()

def main():
    c1 = ryu(150, 215, 57*2, 105*2) # (posX, posY, width, height)
    startHadouken = DT.datetime.now() - DT.timedelta(seconds=0.5)
    startPunch = DT.datetime.now() - DT.timedelta(seconds=0.5)
    jumping = False
    yVelocity = JUMP_HEIGHT

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(c1.hadoukens) < MAX_HADOUKENS and not jumping:
                    hadouken = pygame.Rect(c1.surface.x + c1.surface.width, 245, 33*2, 33*2)
                    c1.hadoukens.append(hadouken)
                    startHadouken = DT.datetime.now()
                    hadoukenSound = mixer.Sound('static/sound/hadouken.wav')
                    hadoukenSound.play()
                
                if event.key == pygame.K_SPACE and DT.datetime.now() > startPunch + DT.timedelta(seconds=0.3):
                    startPunch = DT.datetime.now()

                if event.key == pygame.K_z and not keys_pressed[pygame.K_s]:
                    jumping = True

        jumping, yVelocity = c1.jumps(jumping, yVelocity, startHadouken, startPunch)
        c1.movements(keys_pressed, jumping)
        c1.handleHadoukens()

        drawWindow(c1)

    pygame.quit()

if __name__ == "__main__":
    main()