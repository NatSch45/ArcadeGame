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
        player.character.displayLifebar(WIN)
        fontPlayer = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 20)
        fontCharacter = pygame.font.Font(os.path.join('static/font', 'ARCADE_N.TTF'), 20)
        textPlayer = fontPlayer.render(player.name, True, (255, 255, 255))
        textCharacter = fontCharacter.render(player.character.name, True, (200, 200, 200))
        textPos = 10 if player.name == "Player 1" else 730
        WIN.blit(textPlayer, (textPos, 10))
        WIN.blit(textCharacter, (textPos, 40))

        WIN.blit(player.character.drawing, (player.character.surface.x, player.character.surface.y)) # Draw Character

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
            
            if event.type == pygame.KEYDOWN:
                for player in players:
                    c = player.character
                    if event.key == (pygame.K_LCTRL if c.isFirst else pygame.K_RSHIFT) and len(c.hadoukens) < MAX_HADOUKENS and not c.jumping:
                        hadouken = pygame.Rect(c.surface.x + c.surface.width + 35 if c.direction else c.surface.x - 50, 245, 33*2, 33*2)
                        c.hadoukens.append(hadouken)
                        c.setStartHadouken(DT.datetime.now())
                        hadoukenSound = mixer.Sound('static/sound/hadouken.wav')
                        hadoukenSound.play()
                    
                    if event.key == (pygame.K_SPACE if c.isFirst else pygame.K_EXCLAIM) and DT.datetime.now() > c.getStartPunch() + DT.timedelta(seconds=0.3): # PUNCH
                        c.attacking = True
                        c.replace = "Punch"
                        c.setStartPunch(DT.datetime.now())

                    if event.key == (pygame.K_LALT if c.isFirst else pygame.K_RCTRL) and DT.datetime.now() > c.getStartKick() + DT.timedelta(seconds=0.3): # KICK
                        c.attacking = True
                        c.replace = "Kick"
                        c.setStartKick(DT.datetime.now())

                    if event.key == (pygame.K_z if c.isFirst else pygame.K_UP) and not keys_pressed[pygame.K_s]: # JUMP
                        c.jumping = True

        for player in players:
            player.character.jumps()
            player.character.movements(keys_pressed)
            player.character.handleHadoukens()

        drawWindow(players)

    pygame.quit()

if __name__ == "__main__":
    main()