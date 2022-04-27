import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Game")

WHITE = (255, 0, 255)

FPS = 60
VEL = 5

ME = pygame.transform.scale(pygame.image.load(os.path.join('static', 'moiDetoure.png')), (100, 130))
CURSED_GOAT = pygame.transform.scale(pygame.image.load(os.path.join('static', 'cursedGoat-removedBg.png')), (110, 125))

def drawWindow(me, cursedGoat):
    WIN.fill(WHITE)
    WIN.blit(ME, (me.x, me.y))
    WIN.blit(CURSED_GOAT, (cursedGoat.x, cursedGoat.y))
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

def main():
    me = pygame.Rect(200, 100, 100, 130)
    cursedGoat = pygame.Rect(500, 100, 110, 125)

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        meMovements(keys_pressed, me)
        cursedGoatMovements(keys_pressed, cursedGoat)

        drawWindow(me, cursedGoat)

    pygame.quit()

if __name__ == "__main__":
    main()