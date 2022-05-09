from scripts.classes.character import Character
from scripts.surfaces import *
from scripts.consts import *
from scripts.classes.player import Player
import datetime as DT

class Ken(Character):
    def __init__(self, defaultPosX, defaultPosY, standWidth, standHeight) -> None:
        self.hadoukens = []
        self.direction = Player.nbrOfPlayers == 1 # True if right directed, left otherwise
        self.hit = FIRST_CHARACTER_HIT if Player.nbrOfPlayers == 1 else SECOND_CHARACTER_HIT

        self.startHadouken = DT.datetime.now() - DT.timedelta(seconds=0.5) # Cooldown for hadouken position animation
        self.startPunch = DT.datetime.now() - DT.timedelta(seconds=0.5) # Cooldown for punch animation
        self.startKick = DT.datetime.now() - DT.timedelta(seconds=0.5) # Cooldown for kick animation

        self.name = "Ken"
        super().__init__(defaultPosX, defaultPosY, standWidth, standHeight)
    
    def handleHadoukens(self, opponent):
        for hadouken in self.hadoukens:
            hadouken.x += (HADOUKEN_VEL if self.direction else -HADOUKEN_VEL)
            if opponent.surface.colliderect(hadouken):
                pygame.event.post(pygame.event.Event(opponent.hit))
                self.hadoukens.remove(hadouken)
                opponent.getHit(opponent, HADOUKEN_DAMAGE)
            if hadouken.x > WIDTH or hadouken.x < 0 - HADOUKEN.get_width():
                self.hadoukens.remove(hadouken)
    
    def getStartHadouken(self):
        return self.startHadouken
    def getStartPunch(self):
        return self.startPunch
    def getStartKick(self):
        return self.startKick
    
    def setStartHadouken(self, newStartHadouken):
        self.startHadouken = newStartHadouken
    def setStartPunch(self, newStartPunch):
        self.startPunch = newStartPunch
    def setStartKick(self, newStartKick):
        self.startKick = newStartKick

    def getStandDrawing(self):
        return KEN_STAND if self.direction else KEN_STAND_REVERSE
    def getStoopDrawing(self):
        return KEN_STOOP if self.direction else KEN_STOOP_REVERSE
    def getJumpDrawing(self):
        return KEN_JUMP if self.direction else KEN_JUMP_REVERSE
    def getStaticPunchDrawing(self):
        return KEN_STATIC_PUNCH if self.direction else KEN_STATIC_PUNCH_REVERSE
    def getStaticKickDrawing(self):
        return KEN_STATIC_KICK if self.direction else KEN_STATIC_KICK_REVERSE
    def getHdkPosDrawing(self):
        return KEN_HADOUKEN if self.direction else KEN_HADOUKEN_REVERSE
    def getProjectileDrawing(self):
        return HADOUKEN if self.direction else HADOUKEN_REVERSE