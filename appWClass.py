import pygame
from pygame import mixer
import datetime as DT

from scripts.surfaces import *
from scripts.consts import *

from scripts.classes.player import Player
from scripts.classes.ryu import Ryu
from scripts.classes.ken import Ken
from scripts.classes.geki import Geki
from scripts.classes.eagle import Eagle

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
            WIN.blit(LOGO, (WIDTH/2 - LOGO.get_width()/2, HEIGHT/2 - LOGO.get_height()/2 - 155))
            WIN.blit(textGameOver, (WIDTH/2 - textGameOver.get_width()/2, HEIGHT/2 - textGameOver.get_height()/2))
            textWinner = FONT_WINNER.render(f'{players[0].name} wins !' if players[1].character == Player.isGameOver else f'{players[1].name} wins !', True, GREY)
            WIN.blit(textWinner, (WIDTH/2 - textWinner.get_width()/2, HEIGHT/2 - textWinner.get_height()/2 + 70))
            break

        textPos = 10 if player.name == "Player 1" else 730
        WIN.blit(textPlayer, (textPos, 10))
        WIN.blit(player.character.getNameDrawing(), (textPos, 40))
        
        player.character.displayLifebar()
        WIN.blit(player.character.drawing, (player.character.surface.x, player.character.surface.y)) # Draw Character
        #* pygame.draw.rect(WIN, (255,0,0), player.character.surface, 2) # Draw character's hitbox

        for hadouken in player.character.hadoukens:
            WIN.blit(player.character.getProjectileDrawing(), (hadouken.x + 10, hadouken.y - 5))

    pygame.display.update()

def game(players):
    
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
                        hadouken = None
                        hadouken = pygame.Rect(c.surface.x + c.surface.width + 35 if c.direction else c.surface.x - 50, 245 if player.character.name != "Geki" else 300, 28*2, 26*2)
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
            opponent = players[1].character if player.name == "Player 1" else players[0].character
            player.character.jumps(opponent)
            player.character.movements(keys_pressed)
            player.character.handleHadoukens(opponent)

        drawWindow(players)

def pickChar(focusPlayer, isFirst):
    xPos = 150 if isFirst else 650
    c = None
    if focusPlayer[0] == 1:
        c = Ryu(xPos, 215, 46*2, 92*2)
    elif focusPlayer[1] == 1:
        c = Ken(xPos, 215, 47*2, 92*2)
    elif focusPlayer[2] == 1:
        c = Geki(xPos, 215, 56*2, 92*2)
    elif focusPlayer[3] == 1:
        c = Eagle(xPos, 215, 48*2, 93*2)

    return c

def characterChoice():
    clock = pygame.time.Clock()
    run = True
    focusPlayer1 = [1, 0, 0, 0]
    focusPlayer2 = [1, 0, 0, 0]
    lastInput = DT.datetime.now()

    while run :
        clock.tick(FPS)

        WIN.fill(BLACK)
        textButton1 = FONT_BUTTONS.render("RYU", True, RED)
        textButton2 = FONT_BUTTONS.render("KEN", True, RED)
        textButton3 = FONT_BUTTONS.render("GEKI", True, RED)
        textButton4 = FONT_BUTTONS.render("EAGLE", True, RED)
        WIN.blit(textButton1, (WIDTH/2 - textButton1.get_width()/2, HEIGHT/2 - 150))
        WIN.blit(textButton2, (WIDTH/2 - textButton2.get_width()/2, HEIGHT/2 - 50))
        WIN.blit(textButton3, (WIDTH/2 - textButton3.get_width()/2, HEIGHT/2 + 50))
        WIN.blit(textButton4, (WIDTH/2 - textButton4.get_width()/2, HEIGHT/2 + 150))

        btnRect1 = None
        btnRect2 = None
        for id, c in enumerate(focusPlayer1):
            if c == 1:
                if id == 0:
                    btnRect1 = pygame.Rect(WIDTH/2 - textButton1.get_width()/2 - 8, HEIGHT/2 - 150 - 8, textButton1.get_width() + 10, textButton1.get_height() + 10)
                elif id == 1:
                    btnRect1 = pygame.Rect(WIDTH/2 - textButton2.get_width()/2 - 8, HEIGHT/2 - 50 - 8, textButton2.get_width() + 10, textButton2.get_height() + 10)
                elif id == 2:
                    btnRect1 = pygame.Rect(WIDTH/2 - textButton3.get_width()/2 - 8, HEIGHT/2 + 50 - 8, textButton3.get_width() + 10, textButton3.get_height() + 10)
                elif id == 3:
                    btnRect1 = pygame.Rect(WIDTH/2 - textButton4.get_width()/2 - 8, HEIGHT/2 + 150 - 8, textButton4.get_width() + 10, textButton4.get_height() + 10)
        
        for id, c in enumerate(focusPlayer2):
            if c == 1:
                if id == 0:
                    btnRect2 = pygame.Rect(WIDTH/2 - textButton1.get_width()/2 - 14, HEIGHT/2 - 150 - 14, textButton1.get_width() + 20, textButton1.get_height() + 20)
                elif id == 1:
                    btnRect2 = pygame.Rect(WIDTH/2 - textButton2.get_width()/2 - 14, HEIGHT/2 - 50 - 14, textButton2.get_width() + 20, textButton2.get_height() + 20)
                elif id == 2:
                    btnRect2 = pygame.Rect(WIDTH/2 - textButton3.get_width()/2 - 14, HEIGHT/2 + 50 - 14, textButton3.get_width() + 20, textButton3.get_height() + 20)
                elif id == 3:
                    btnRect2 = pygame.Rect(WIDTH/2 - textButton4.get_width()/2 - 14, HEIGHT/2 + 150 - 14, textButton4.get_width() + 20, textButton4.get_height() + 20)
                    
        pygame.draw.rect(WIN, RED, btnRect1, 2)
        pygame.draw.rect(WIN, GREEN, btnRect2, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    run = False

                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if DT.datetime.now() > lastInput + DT.timedelta(seconds=0.2):
                        lastInput = DT.datetime.now()
                        players = [Player("Player 1")]
                        players[0].setCharacter(pickChar(focusPlayer1, True)) # (posX, posY, width, height)

                        players.append(Player("Player 2"))
                        players[1].setCharacter(pickChar(focusPlayer2, False)) # (posX, posY, width, height)
                        game(players)
                
                if event.key == pygame.K_s:
                    if DT.datetime.now() > lastInput + DT.timedelta(seconds=0.2):
                        for id, c in enumerate(focusPlayer1):
                            if c == 1:
                                if id != 3:
                                    focusPlayer1[id+1] = 1
                                else:
                                    focusPlayer1[0] = 1
                                focusPlayer1[id] = 0
                                break
                        lastInput = DT.datetime.now()
                        break
                if event.key == pygame.K_z:
                    if DT.datetime.now() > lastInput + DT.timedelta(seconds=0.2):
                        for id, c in enumerate(focusPlayer1):
                            if c == 1:
                                if id != 0:
                                    focusPlayer1[id-1] = 1
                                else:
                                    focusPlayer1[3] = 1
                                focusPlayer1[id] = 0
                                break
                        lastInput = DT.datetime.now()
                        break
                
                if event.key == pygame.K_DOWN:
                    if DT.datetime.now() > lastInput + DT.timedelta(seconds=0.2):
                        for id, c in enumerate(focusPlayer2):
                            if c == 1:
                                if id != 3:
                                    focusPlayer2[id+1] = 1
                                else:
                                    focusPlayer2[0] = 1
                                focusPlayer2[id] = 0
                                break
                        lastInput = DT.datetime.now()
                        break
                if event.key == pygame.K_UP:
                    if DT.datetime.now() > lastInput + DT.timedelta(seconds=0.2):
                        for id, c in enumerate(focusPlayer2):
                            if c == 1:
                                if id != 0:
                                    focusPlayer2[id-1] = 1
                                else:
                                    focusPlayer2[3] = 1
                                focusPlayer2[id] = 0
                                break
                        lastInput = DT.datetime.now()
                        break

        pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    focus = True # True if focus is on PLAY, False if focus is on QUIT
    lastInput = DT.datetime.now()

    while run:
        clock.tick(FPS)

        WIN.fill(BLACK)
        textButton1 = FONT_BUTTONS.render("PLAY", True, RED)
        textButton2 = FONT_BUTTONS.render("QUIT", True, RED)
        WIN.blit(textButton1, (WIDTH/2 - textButton1.get_width()/2, HEIGHT/2 - 80))
        WIN.blit(textButton2, (WIDTH/2 - textButton2.get_width()/2, HEIGHT/2 + 120))
        btnRect = None
        if focus:
            btnRect = pygame.Rect(WIDTH/2 - textButton1.get_width()/2 - 8, HEIGHT/2 - 80 - 8, textButton1.get_width() + 10, textButton1.get_height() + 10)
        else:
            btnRect = pygame.Rect(WIDTH/2 - textButton2.get_width()/2 - 8, HEIGHT/2 + 120 - 8, textButton2.get_width() + 10, textButton2.get_height() + 10)
        pygame.draw.rect(WIN, RED, btnRect, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if DT.datetime.now() > lastInput + DT.timedelta(seconds=0.2):
                        lastInput = DT.datetime.now()
                        if focus:
                            characterChoice()
                        else:
                            run = False
                
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if DT.datetime.now() > lastInput + DT.timedelta(seconds=0.2):
                        focus = not focus
                        lastInput = DT.datetime.now()

        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()