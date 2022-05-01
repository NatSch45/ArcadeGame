import pygame
import os
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import datetime as DT
from time import sleep

BUTTON_PIN = 38

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Game")

WHITE = (100, 20, 200)

FPS = 60
VEL = 5
BULLET_VEL = 7

ME_HIT = pygame.USEREVENT + 1
CURSED_GOAT_HIT = pygame.USEREVENT + 2

ME = pygame.transform.scale(pygame.image.load(os.path.join('static', 'moiDetoure.png')), (100, 130))
CURSED_GOAT = pygame.transform.scale(pygame.image.load(os.path.join('static', 'cursedGoat-removedBg.png')), (110, 125))

def drawWindow(me, cursedGoat, bulletsMe, bulletsCursedGoat):
    WIN.fill(WHITE)
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
        elif bullet.x < 0:
            bulletsCursedGoat.remove(bullet)
    

def main():
    me = pygame.Rect(200, 100, 100, 130)
    cursedGoat = pygame.Rect(500, 100, 110, 125)
    bulletsMe = []
    bulletsCursedGoat = []

    lastCall = DT.datetime.now()
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            if lastCall and DT.datetime.now() > lastCall + DT.timedelta(seconds=0.5):
                bullet = pygame.Rect(me.x + me.width, me.y + me.height//2 - 2, 10, 5)
                bulletsMe.append(bullet)
                lastCall = DT.datetime.now()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_LCTRL and len(bulletsMe) < 3:
                #     bullet = pygame.Rect(me.x + me.width, me.y + me.height//2 - 2, 10, 5)
                #     bulletsMe.append(bullet)
                
                if event.key == pygame.K_RCTRL and len(bulletsCursedGoat) < 3:
                    bullet = pygame.Rect(cursedGoat.x, cursedGoat.y + cursedGoat.height//2 - 2, 10, 5)
                    bulletsCursedGoat.append(bullet)


        handleBullets(bulletsMe, bulletsCursedGoat, me, cursedGoat)
        
        keys_pressed = pygame.key.get_pressed()
        meMovements(keys_pressed, me)
        cursedGoatMovements(keys_pressed, cursedGoat)

        drawWindow(me, cursedGoat, bulletsMe, bulletsCursedGoat)

    pygame.quit()

if __name__ == "__main__":
    main()