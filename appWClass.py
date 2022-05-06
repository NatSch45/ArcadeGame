import pygame
from pygame import mixer
import datetime as DT
import os

from scripts.surfaces import *
from scripts.consts import *

from scripts.classes.player import Player
from scripts.classes.ryu import Ryu
from scripts.classes.ken import Ken

mixer.init()
pygame.init()

pygame.display.set_caption("Arcade Game")

def drawWindow(players):
    WIN.blit(BGSF, (0, 0)) # Draw background image

    for player in players:
        fontPlayer = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 20)
        fontCharacter = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 20)
        textPlayer = fontPlayer.render(player.name, True, (255, 255, 255))
        textCharacter = fontCharacter.render(player.character.name, True, (200, 200, 200))
        WIN.blit(textPlayer, (20, 30))
        WIN.blit(textCharacter, (20, 60))

        WIN.blit(player.character.drawing, (player.character.surface.x, player.character.surface.y)) # Draw Character

        for hadouken in player.character.hadoukens:
            WIN.blit(HADOUKEN, (hadouken.x + 10, hadouken.y - 5))

    pygame.display.update()

def main():
    players = [Player("Player 1")]
    twoPlayers = False
    if twoPlayers :
        players.append(Player("Player 2"))

    players[0].setCharacter(Ryu(150, 215, 57*2, 105*2)) # (posX, posY, width, height)
    
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
                if event.key == pygame.K_LCTRL and len(players[0].character.hadoukens) < MAX_HADOUKENS and not jumping:
                    hadouken = pygame.Rect(players[0].character.surface.x + players[0].character.surface.width, 245, 33*2, 33*2)
                    players[0].character.hadoukens.append(hadouken)
                    players[0].character.setStartHadouken(DT.datetime.now())
                    hadoukenSound = mixer.Sound('static/sound/hadouken.wav')
                    hadoukenSound.play()
                
                if event.key == pygame.K_SPACE and DT.datetime.now() > players[0].character.getStartPunch() + DT.timedelta(seconds=0.3):
                    players[0].character.setStartPunch(DT.datetime.now())
                if event.key == pygame.K_LALT and DT.datetime.now() > players[0].character.getStartKick() + DT.timedelta(seconds=0.3):
                    players[0].character.setStartKick(DT.datetime.now())

                if event.key == pygame.K_z and not keys_pressed[pygame.K_s]:
                    jumping = True

        jumping, yVelocity = players[0].character.jumps(jumping, yVelocity)
        players[0].character.movements(keys_pressed, jumping)
        players[0].character.handleHadoukens()

        drawWindow(players)

    pygame.quit()

if __name__ == "__main__":
    main()