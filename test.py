import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Game")

BG_COLOR = (100, 20, 200)

FPS = 60
VEL = 5
BULLET_VEL = 7

Y_GRAVITY = 1
JUMP_HEIGHT = 20

ME = pygame.transform.scale(pygame.image.load(os.path.join('static', 'moiDetoure.png')), (100, 130))
CURSED_GOAT = pygame.transform.scale(pygame.image.load(os.path.join('static', 'cursedGoat-removedBg.png')), (110, 125))
RYU_STAND = pygame.transform.scale(pygame.image.load(os.path.join('static', 'RyuStand.png')), (80, 100))
RYU_JUMP = pygame.transform.scale(pygame.image.load(os.path.join('static', 'RyuJump.png')), (80, 100))
RYU_STOOP = pygame.transform.scale(pygame.image.load(os.path.join('static', 'RyuStoop.png')), (80, 100))

ME_HIT = pygame.USEREVENT + 1
CURSED_GOAT_HIT = pygame.USEREVENT + 2

def drawWindow(me, cursedGoat, bulletsMe, bulletsCursedGoat):
    WIN.fill(BG_COLOR)
    WIN.blit(ME, (me.x, me.y))
    WIN.blit(CURSED_GOAT, (cursedGoat.x, cursedGoat.y))

    for bullet in bulletsMe:
        pygame.draw.rect(WIN, (0, 0, 255), bullet)
    
    for bullet in bulletsCursedGoat:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)

    pygame.display.update()

def meMovements(keys_pressed, me):
    if keys_pressed[pygame.K_q] and me.x - VEL > 0: # LEFT
        me.x -= VEL
    if keys_pressed[pygame.K_d] and me.x + VEL + me.width < WIDTH: # RIGHT
        me.x += VEL
    if keys_pressed[pygame.K_z] and me.y - VEL > 0: # UP
        me.y -= VEL
    if keys_pressed[pygame.K_s] and me.y + VEL + me.height < HEIGHT: # DOWN
        me.y += VEL

def cursedGoatMovements(keys_pressed, cursedGoat):
    if keys_pressed[pygame.K_LEFT] and cursedGoat.x - VEL > 0: # LEFT
        cursedGoat.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and cursedGoat.x + VEL + cursedGoat.width < WIDTH: # RIGHT
        cursedGoat.x += VEL
    if keys_pressed[pygame.K_UP] and cursedGoat.y - VEL > 0: # UP
        cursedGoat.y -= VEL
    if keys_pressed[pygame.K_DOWN] and cursedGoat.y + VEL + cursedGoat.height < HEIGHT: # DOWN
        cursedGoat.y += VEL

def handleBullets(bulletsMe, bulletsCursedGoat, me, cursedGoat):
    for bullet in bulletsMe:
        bullet.x += BULLET_VEL
        if cursedGoat.colliderect(bullet):
            pygame.event.post(pygame.event.Event(CURSED_GOAT_HIT))
            bulletsMe.remove(bullet)
        elif bullet.x > WIDTH:
            bulletsMe.remove(bullet)

    for bullet in bulletsCursedGoat:
        bullet.x -= BULLET_VEL
        if me.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ME_HIT))
            bulletsCursedGoat.remove(bullet)
        elif bullet.x < 0 - bullet.width:
            bulletsCursedGoat.remove(bullet)
    

def main():
    me = pygame.Rect(200, 100, 100, 130)
    cursedGoat = pygame.Rect(500, 100, 110, 125)
    bulletsMe = []
    bulletsCursedGoat = []

    jumping = False
    Y_VELOCITY = JUMP_HEIGHT

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(bulletsMe) < 3:
                    bullet = pygame.Rect(me.x + me.width, me.y + me.height//2 - 2, 10, 5)
                    bulletsMe.append(bullet)
                
                if event.key == pygame.K_RCTRL and len(bulletsCursedGoat) < 3:
                    bullet = pygame.Rect(cursedGoat.x, cursedGoat.y + cursedGoat.height//2 - 2, 10, 5)
                    bulletsCursedGoat.append(bullet)

                if event.key == pygame.K_SPACE:
                    jumping = True
        
        if jumping:
            me.y -= Y_VELOCITY
            Y_VELOCITY -= Y_GRAVITY
            if Y_VELOCITY < -JUMP_HEIGHT:
                jumping = False
                Y_VELOCITY = JUMP_HEIGHT



        handleBullets(bulletsMe, bulletsCursedGoat, me, cursedGoat)
        
        keys_pressed = pygame.key.get_pressed()
        meMovements(keys_pressed, me)
        cursedGoatMovements(keys_pressed, cursedGoat)

        drawWindow(me, cursedGoat, bulletsMe, bulletsCursedGoat)

    pygame.quit()

if __name__ == "__main__":
    main()