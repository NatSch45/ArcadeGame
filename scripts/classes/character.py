import pygame
from scripts.surfaces import *
from scripts.consts import *
import datetime as DT

class character:
    def __init__(self, defaultPosX, defaultPosY, standWidth, standHeight) -> None:
        self.drawing = None
        self.defaultXPos = defaultPosX
        self.defaultYPos = defaultPosY
        self.standWidth = standWidth
        self.standHeight = standHeight
        self.surface = pygame.Rect(defaultPosX, defaultPosY, standWidth, standHeight)
        self.name = None
        pass

    def getStandDrawing(self):
        return None
    def getStoopDrawing(self):
        return None
    def getJumpDrawing(self):
        return None
    def getStaticPunchDrawing(self):
        return None
    def getHdkPosDrawing(self):
        return None

    def movements(self, keys_pressed, jumping):

        if keys_pressed[pygame.K_q] and self.surface.x - VEL > 0 and self.drawing != self.getHdkPosDrawing(): # LEFT
            if keys_pressed[pygame.K_s]:
                self.surface.x -= 2
            else:
                self.surface.x -= VEL - 1

        if keys_pressed[pygame.K_d] and self.surface.x + VEL + self.surface.width < WIDTH and self.drawing != self.getHdkPosDrawing(): # RIGHT
            if keys_pressed[pygame.K_s]:
                self.surface.x += 2
            else:
                self.surface.x += VEL

        if keys_pressed[pygame.K_s] and not jumping and self.drawing != self.getHdkPosDrawing(): # STOOP
            self.surface.y = 280
            self.drawing = self.getStoopDrawing()
        elif self.drawing == self.getHdkPosDrawing():
            self.surface.y = 233
        elif self.drawing == self.getStaticPunchDrawing():
            self.surface.x += 2
            self.surface.y = 225
        elif not jumping:
            self.surface.y = self.defaultYPos
            
        pass
        
    
    def jumps(self, jumping, yVelocity, startHadouken, startPunch):

        if jumping: # JUMP
            self.surface.y -= yVelocity
            yVelocity -= Y_GRAVITY
            if yVelocity < -JUMP_HEIGHT:
                jumping = False
                yVelocity = JUMP_HEIGHT
            self.drawing = self.getJumpDrawing()
        elif DT.datetime.now() < startHadouken + DT.timedelta(seconds=0.3):
            self.drawing = self.getHdkPosDrawing()
        elif DT.datetime.now() < startPunch + DT.timedelta(seconds=0.2):
            self.drawing = self.getStaticPunchDrawing()
        else:
            self.drawing = self.getStandDrawing()
        
        
        return (jumping, yVelocity)


    """
    Methods available in inherited classes :
    - getStandDrawing()
    - getStoopDrawing()
    - getJumpDrawing()
    - getStaticPunchDrawing()
    - getHdkPosDrawing()
    """