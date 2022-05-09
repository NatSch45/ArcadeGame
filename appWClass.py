import pygame
from pygame import mixer
import datetime as DT

from scripts.surfaces import *
from scripts.consts import *

from scripts.classes.player import Player
from scripts.classes.ryu import Ryu
from scripts.classes.ken import Ken
import RPi.GPIO as GPIO

#ken
BUTTON_PIN = 33 #jump
BUTTON_PIN_3 = 31 #stoop
BUTTON_PIN_4 = 23 #punch
BUTTON_PIN_6 = 21 #kick

#ryu
BUTTON_PIN_13 = 10 #jump
BUTTON_PIN_10 = 8 #stoop
BUTTON_PIN_5 = 24 #punch
BUTTON_PIN_7 = 22 #kick
BUTTON_PIN_12 = 16 #right

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(BUTTON_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(BUTTON_PIN_5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


mixer.init()
pygame.init()

pygame.display.set_caption("Arcade Game")

def drawWindow(players):
    WIN.blit(BGSF, (0, 0)) # Draw background image

    for player in players:
        textPlayer = FONT_PLAYER.render(player.name, True, BLACK)
        textCharacter = FONT_CHARACTER.render(player.character.name, True, GREY)
        textGameOver = FONT_GAME_OVER.render("GAME OVER", True, WHITE)

        if Player.isGameOver :
            WIN.blit(textGameOver, (WIDTH/2 - textGameOver.get_width()/2, HEIGHT/2 - textGameOver.get_height()/2))
            textWinner = FONT_WINNER.render(f'{players[0].name} wins !' if players[1].character == Player.isGameOver else f'{players[1].name} wins !', True, GREY)
            WIN.blit(textWinner, (WIDTH/2 - textWinner.get_width()/2, HEIGHT/2 - textWinner.get_height()/2 + 70))
            break

        textPos = 10 if player.name == "Player 1" else 730
        WIN.blit(textPlayer, (textPos, 10))
        WIN.blit(textCharacter, (textPos, 40))
        
        player.character.displayLifebar()
        WIN.blit(player.character.drawing, (player.character.surface.x, player.character.surface.y)) # Draw Character
        #* pygame.draw.rect(WIN, (255,0,0), player.character.surface, 2) # Draw character's hitbox

        for hadouken in player.character.hadoukens:
            if player.character.direction: # RIGHT DIRECTION HADOUKEN
                WIN.blit(HADOUKEN, (hadouken.x + 10, hadouken.y - 5))
            else: # LEFT DIRECTION HADOUKEN
                WIN.blit(REVERSE_HADOUKEN, (hadouken.x + 10, hadouken.y - 5))

    pygame.display.update()

def main():
    players = [Player("Player 1")]
    players[0].setCharacter(Ryu(150, 215, 46*2, 92*2)) # (posX, posY, width, height)

    twoPlayers = True
    if twoPlayers :
        players.append(Player("Player 2"))
        players[1].setCharacter(Ken(650, 215, 47*2, 92*2)) # (posX, posY, width, height)

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        event = None
        
        #if event.type == pygame.KEYDOWN:
        for player in players:
            c = player.character
            if ((GPIO.input(BUTTON_PIN_5) == GPIO.HIGH and GPIO.input(BUTTON_PIN_7) == GPIO.HIGH) if c.isFirst else ( GPIO.input(BUTTON_PIN_4) == GPIO.HIGH and GPIO.input(BUTTON_PIN_6) == GPIO.HIGH)) and len(c.hadoukens) < MAX_HADOUKENS and not c.jumping:
                hadouken = pygame.Rect(c.surface.x + c.surface.width + 35 if c.direction else c.surface.x - 50, 245, 28*2, 26*2)
                c.hadoukens.append(hadouken)
                c.setStartHadouken(DT.datetime.now())
                hadoukenSound = mixer.Sound('static/sound/hadouken.wav')
                hadoukenSound.play()
                    
            if GPIO.input(BUTTON_PIN_5) == GPIO.HIGH if c.isFirst else GPIO.input(BUTTON_PIN_4) == GPIO.HIGH and DT.datetime.now() > c.getStartPunch() + DT.timedelta(seconds=0.3): # PUNCH
                c.attacking = True
                c.replace = "Punch"
                c.setStartPunch(DT.datetime.now())

            if GPIO.input(BUTTON_PIN_7) == GPIO.HIGH if c.isFirst else GPIO.input(BUTTON_PIN_6) == GPIO.HIGH and DT.datetime.now() > c.getStartKick() + DT.timedelta(seconds=0.3): # KICK
                c.attacking = True
                c.replace = "Kick"
                c.setStartKick(DT.datetime.now())

            if GPIO.input(BUTTON_PIN_13) == GPIO.HIGH if c.isFirst else GPIO.input(BUTTON_PIN) == GPIO.HIGH and not GPIO.input(BUTTON_PIN_10) == GPIO.HIGH: # JUMP
                c.jumping = True

        for player in players:
            opponent = players[1].character if player.name == "Player 1" else players[0].character
            player.character.jumps(opponent)
            player.character.movements(keys_pressed)
            player.character.handleHadoukens(opponent)

        drawWindow(players)

    pygame.quit()

if __name__ == "__main__":
    main()