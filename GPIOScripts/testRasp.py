import pygame
import os
import RPi.GPIO as GPIO
import datetime as DT

BUTTON_PIN = 33
BUTTON_PIN_1 = 35
BUTTON_PIN_2 = 37
BUTTON_PIN_3 = 31

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(BUTTON_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Game")

FPS = 60
VEL = 4
HADOUKEN_VEL = 7
MAX_HADOUKENS = 1

Y_GRAVITY = 1
JUMP_HEIGHT = 19

BGSF = pygame.transform.scale(pygame.image.load(os.path.join('../static', 'bgsfhd.jpg')), (WIDTH, HEIGHT))
RYU_STAND = pygame.transform.scale(pygame.image.load(os.path.join('../static', 'RyuStand.png')), (57*2, 105*2))
RYU_JUMP = pygame.transform.scale(pygame.image.load(os.path.join('../static', 'RyuJump.png')), (42*2, 69*2))
RYU_STOOP = pygame.transform.scale(pygame.image.load(os.path.join('../static', 'RyuStoop.png')), (53*2, 71*2))
RYU_STATIC_PUNCH = pygame.transform.scale(pygame.image.load(os.path.join('../static', 'RyuStaticPunch.png')), (79*2, 97*2))
RYU_HADOUKEN = pygame.transform.scale(pygame.image.load(os.path.join('../static', 'RyuHdk.png')), (88*2, 92*2))
HADOUKEN = pygame.transform.scale(pygame.image.load(os.path.join('../static', 'Hadouken.png')), (33*2, 33*2))
ryuSurface = RYU_JUMP

RYU_HIT = pygame.USEREVENT + 1

def drawWindow(ryu, hadoukens):
    WIN.blit(BGSF, (0, 0)) # Draw background image
    WIN.blit(ryuSurface, (ryu.x, ryu.y)) # Draw Ryu

    for hadouken in hadoukens:
        WIN.blit(HADOUKEN, (hadouken.x + 10, hadouken.y - 5))

    pygame.display.update()

def ryuMovements(keys_pressed, ryu, jumping):
    global ryuSurface

    if GPIO.input(BUTTON_PIN_2) == GPIO.HIGH and ryu.x - VEL > 0 and ryuSurface != RYU_HADOUKEN: # LEFT
        if keys_pressed[pygame.K_s]:
            ryu.x -= 2
        else:
            ryu.x -= VEL - 1

    if GPIO.input(BUTTON_PIN_1) == GPIO.HIGH and ryu.x + VEL + ryu.width < WIDTH and ryuSurface != RYU_HADOUKEN: # RIGHT
        if keys_pressed[pygame.K_s]:
            ryu.x += 2
        else:
            ryu.x += VEL

    if GPIO.input(BUTTON_PIN) == GPIO.HIGH and not jumping and ryuSurface != RYU_HADOUKEN: # STOOP
        ryu.y = 280
        ryuSurface = RYU_STOOP
    elif ryuSurface == RYU_HADOUKEN:
        ryu.y = 233
    elif not jumping:
        ryu.y = 215

def handleHadoukens(ryu, hadoukens):
    global ryuSurface
    for hadouken in hadoukens:
        hadouken.x += HADOUKEN_VEL
        if hadouken.x > WIDTH:
            hadoukens.remove(hadouken)

def main():
    global ryuSurface

    ryu = pygame.Rect(150, 215, 57*2, 105*2)
    hadoukens = []
    lastHadouken = DT.datetime.now() - DT.timedelta(seconds=0.5)

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
            
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_z and not keys_pressed[pygame.K_s]:
                    #jumping = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(hadoukens) < MAX_HADOUKENS and not jumping:
                    hadouken = pygame.Rect(ryu.x + ryu.width, 245, 33*2, 33*2)
                    hadoukens.append(hadouken)
                    lastHadouken = DT.datetime.now()


                #if event.key == pygame.K_z and not keys_pressed[pygame.K_s]:
                    #jumping = True


                if event.key == pygame.K_z and not keys_pressed[pygame.K_s]:
                    jumping = True


        if GPIO.input(BUTTON_PIN_3) == GPIO.HIGH and not GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            jumping = True
            
        if jumping:
            ryu.y -= Y_VELOCITY
            Y_VELOCITY -= Y_GRAVITY
            if Y_VELOCITY < -JUMP_HEIGHT:
                jumping = False
                yVelocity = JUMP_HEIGHT
            ryuSurface = RYU_JUMP
        elif DT.datetime.now() > lastHadouken + DT.timedelta(seconds=0.3):
            ryuSurface = RYU_STAND
        else:
            ryuSurface = RYU_HADOUKEN

        ryuMovements(keys_pressed, ryu, jumping)
        handleHadoukens(ryu, hadoukens)

        drawWindow(ryu, hadoukens)

    pygame.quit()

if __name__ == "__main__":
    main()