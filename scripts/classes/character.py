import pygame
from scripts.surfaces import *
from scripts.consts import *
from scripts.classes.player import Player
import datetime as DT

class Character:
    def __init__(self, defaultPosX, defaultPosY, standWidth, standHeight) -> None:
        self.drawing = self.getStandDrawing()
        self.jumping = False
        self.attacking = False
        self.replace = ""
        self.damageCooldown = DT.datetime.now()
        self.yVelocity = JUMP_HEIGHT
        self.isFirst = Player.nbrOfPlayers == 1
        self.direction = Player.nbrOfPlayers == 1 # True if right directed, left otherwise
        self.defaultXPos = defaultPosX
        self.defaultYPos = defaultPosY
        self.standWidth = standWidth
        self.standHeight = standHeight
        self.surface = pygame.Rect(defaultPosX, defaultPosY, standWidth, standHeight)
        self.maxHp = 100
        self.hp = self.maxHp
        pass

    def movements(self, keys_pressed):

        if (keys_pressed[pygame.K_q] if self.isFirst else keys_pressed[pygame.K_LEFT]) and self.surface.x - VEL > 0 and self.drawing != self.getHdkPosDrawing(): # LEFT
            if keys_pressed[pygame.K_s]:
                self.surface.x -= 2
            else:
                self.surface.x -= (VEL - 1 if self.direction else VEL)

        if (keys_pressed[pygame.K_d] if self.isFirst else keys_pressed[pygame.K_RIGHT]) and self.surface.x + VEL + self.surface.width < WIDTH and self.drawing != self.getHdkPosDrawing(): # RIGHT
            if keys_pressed[pygame.K_s]:
                self.surface.x += 2
            else:
                self.surface.x += (VEL if self.direction else VEL - 1)

        if (keys_pressed[pygame.K_s] if self.isFirst else keys_pressed[pygame.K_DOWN]) and not self.jumping and self.drawing != self.getHdkPosDrawing(): # STOOP
            self.drawing = self.getStoopDrawing()
            self.surface.width, self.surface.height = self.getStoopDrawing().get_width(), self.getStoopDrawing().get_height()
        elif self.drawing == self.getStaticPunchDrawing():
            if self.direction:
                if self.surface.x + self.surface.width < WIDTH:
                    self.surface.x += 1
            else:
                if self.surface.x + self.surface.width > 0:
                    self.surface.x -= 1
        elif self.drawing == self.getStaticKickDrawing():
            if self.direction:
                if self.surface.x + self.surface.width < WIDTH:
                    self.surface.x += 1
            else:
                if self.surface.x + self.surface.width > 0:
                    self.surface.x -= 1
        elif not self.jumping:
            self.surface.y = self.defaultYPos
        
        if not self.jumping:
            self.surface.y = FLOOR - self.drawing.get_height()
            
        pass
        
    
    def jumps(self, opponent):

        if self.jumping: #? JUMP
            self.surface.y -= self.yVelocity
            self.yVelocity -= Y_GRAVITY
            if self.yVelocity < -JUMP_HEIGHT:
                self.jumping = False
                self.yVelocity = JUMP_HEIGHT
            self.drawing = self.getJumpDrawing()
            self.surface.width, self.surface.height = self.getJumpDrawing().get_width(), self.getJumpDrawing().get_height()

        elif DT.datetime.now() < self.startHadouken + DT.timedelta(seconds=0.3): #? HADOUKEN
            self.drawing = self.getHdkPosDrawing()
            self.surface.width, self.surface.height = self.getHdkPosDrawing().get_width(), self.getHdkPosDrawing().get_height()

        elif DT.datetime.now() < self.startPunch + DT.timedelta(seconds=0.2): #? PUNCH
            if self.attacking and not self.direction and self.surface.x > 0 :
                self.surface.x -= 52
                self.attacking = False
            self.drawing = self.getStaticPunchDrawing()
            self.surface.width, self.surface.height = self.getStaticPunchDrawing().get_width(), self.getStaticPunchDrawing().get_height()
            if opponent.surface.colliderect(self.surface) and DT.datetime.now() > self.damageCooldown + DT.timedelta(seconds=0.25):
                pygame.event.post(pygame.event.Event(opponent.hit))
                opponent.getHit(opponent, PUNCH_DAMAGE)
                self.damageCooldown = DT.datetime.now()

        elif DT.datetime.now() < self.startKick + DT.timedelta(seconds=0.2): #? KICK
            if self.attacking and not self.direction and self.surface.x > 0:
                self.surface.x -= 35
                self.attacking = False
            self.drawing = self.getStaticKickDrawing()
            self.surface.width, self.surface.height = self.getStaticKickDrawing().get_width(), self.getStaticKickDrawing().get_height()
            if opponent.surface.colliderect(self.surface) and DT.datetime.now() > self.damageCooldown + DT.timedelta(seconds=0.25):
                pygame.event.post(pygame.event.Event(opponent.hit))
                opponent.getHit(opponent, KICK_DAMAGE)
                self.damageCooldown = DT.datetime.now()

        else: #? STAND
            if self.replace == "Punch" and not self.direction :
                self.surface.x += 52
                self.replace = ""
            elif self.replace == "Kick" and not self.direction :
                self.surface.x += 35
                self.replace = ""
            self.surface.y = self.defaultYPos
            self.drawing = self.getStandDrawing()
            self.surface.width, self.surface.height = self.getStandDrawing().get_width(), self.getStandDrawing().get_height()
    
    def displayLifebar(self):
        lifeBarRect = pygame.Rect(185 if self.isFirst else 460 + (self.maxHp - self.hp) * 2.5, 10, self.hp * 2.5, 30)
        pygame.draw.rect(WIN, GREEN if self.hp > 60 else (ORANGE if self.hp > 30 else RED), lifeBarRect)
        pygame.draw.rect(WIN, BLACK, (185 if self.isFirst else 460, 10, self.maxHp * 2.5, 30), 2)
    
    def getHit(self, opponent, damage):
        if self.hp - damage > 0:
            self.hp -= damage
        else:
            self.hp = 0
            Player.isGameOver = opponent
        

    """
    Methods available in derived classes :
    - getStandDrawing()
    - getStoopDrawing()
    - getJumpDrawing()
    - getStaticPunchDrawing()
    - getStaticKickDrawing()
    - getHdkPosDrawing()
    """