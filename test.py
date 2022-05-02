import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Game")

FPS = 60
VEL = 4
BULLET_VEL = 7

Y_GRAVITY = 1
JUMP_HEIGHT = 19

BGSF = pygame.transform.scale(pygame.image.load(os.path.join('static', 'bgsfhd.jpg')), (WIDTH, HEIGHT))
# ME = pygame.transform.scale(pygame.image.load(os.path.join('static', 'moiDetoure.png')), (100, 130))
# CURSED_GOAT = pygame.transform.scale(pygame.image.load(os.path.join('static', 'cursedGoat-removedBg.png')), (110, 125))
RYU_STAND = pygame.transform.scale(pygame.image.load(os.path.join('static', 'RyuStand.png')), (57*2, 105*2))
RYU_JUMP = pygame.transform.scale(pygame.image.load(os.path.join('static', 'RyuJump.png')), (42*2, 69*2))
RYU_STOOP = pygame.transform.scale(pygame.image.load(os.path.join('static', 'RyuStoop.png')), (53*2, 71*2))
ryuSurface = RYU_JUMP

# ME_HIT = pygame.USEREVENT + 1
# CURSED_GOAT_HIT = pygame.USEREVENT + 2
RYU_HIT = pygame.USEREVENT + 3

def drawWindow(ryu):
    WIN.blit(BGSF, (0, 0)) # Draw background image
    WIN.blit(ryuSurface, (ryu.x, ryu.y)) # Draw Ryu

    pygame.display.update()

def ryuMovements(keys_pressed, ryu, jumping):
    if keys_pressed[pygame.K_q] and ryu.x - VEL > 0: # LEFT
        if keys_pressed[pygame.K_s]:
            ryu.x -= 2
        else:
            ryu.x -= VEL - 1
    if keys_pressed[pygame.K_d] and ryu.x + VEL + ryu.width < WIDTH: # RIGHT
        if keys_pressed[pygame.K_s]:
            ryu.x += 2
        else:
            ryu.x += VEL
    if keys_pressed[pygame.K_s] and not jumping: # STOOP
        ryu.y = 280
        global ryuSurface
        ryuSurface = RYU_STOOP
    elif not jumping:
        ryu.y = 215

def main():
    global ryuSurface

    ryu = pygame.Rect(150, 215, 57*2, 105*2)

    jumping = False
    Y_VELOCITY = JUMP_HEIGHT

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and not keys_pressed[pygame.K_s]:
                    jumping = True
        
        if jumping:
            ryu.y -= Y_VELOCITY
            Y_VELOCITY -= Y_GRAVITY
            if Y_VELOCITY < -JUMP_HEIGHT:
                jumping = False
                Y_VELOCITY = JUMP_HEIGHT
            ryuSurface = RYU_JUMP
        else:
            ryuSurface = RYU_STAND
        
        ryuMovements(keys_pressed, ryu, jumping)

        drawWindow(ryu)

    pygame.quit()

if __name__ == "__main__":
    main()