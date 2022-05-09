from scripts.classes.character import Character
from scripts.surfaces import *
from scripts.consts import *
from scripts.classes.player import Player
import datetime as DT

class Geki(Character):
    def __init__(self, defaultPosX, defaultPosY, standWidth, standHeight) -> None:
        self.hadoukens = []
        self.direction = Player.nbrOfPlayers == 1 # True if right directed, left otherwise
        self.hit = FIRST_CHARACTER_HIT if Player.nbrOfPlayers == 1 else SECOND_CHARACTER_HIT

        self.startHadouken = DT.datetime.now() - DT.timedelta(seconds=0.5) # Cooldown for hadouken position animation
        self.startPunch = DT.datetime.now() - DT.timedelta(seconds=0.5) # Cooldown for punch animation
        self.startKick = DT.datetime.now() - DT.timedelta(seconds=0.5) # Cooldown for kick animation

        self.name = "Geki"
        super(Geki, self).__init__(defaultPosX, defaultPosY, standWidth, standHeight)
    
    def handleHadoukens(self, opponent):
        for hadouken in self.hadoukens:
            hadouken.x += (HADOUKEN_VEL if self.direction else -HADOUKEN_VEL)
            if opponent.surface.colliderect(hadouken):
                pygame.event.post(pygame.event.Event(opponent.hit))
                self.hadoukens.remove(hadouken)
                damage = (self.maxHp - self.hp) / 50
                opponent.getHit(opponent, HADOUKEN_DAMAGE * (0.2 if damage <= 0.2 else (1.5 if damage >= 1.5 else damage))) #? The less health points the character has, the harder he shoots, but always in the interval [0.2, 1.5]
            if hadouken.x > WIDTH or hadouken.x < 0 - SHURIKEN.get_width():
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
        return GEKI_STAND if self.direction else GEKI_STAND_REVERSE
    def getStoopDrawing(self):
        return GEKI_STOOP if self.direction else GEKI_STOOP_REVERSE
    def getJumpDrawing(self):
        return GEKI_JUMP if self.direction else GEKI_JUMP_REVERSE
    def getStaticPunchDrawing(self):
        return GEKI_STATIC_PUNCH if self.direction else GEKI_STATIC_PUNCH_REVERSE
    def getStaticKickDrawing(self):
        return GEKI_STATIC_KICK if self.direction else GEKI_STATIC_KICK_REVERSE
    def getHdkPosDrawing(self):
        return GEKI_HADOUKEN if self.direction else GEKI_HADOUKEN_REVERSE
    def getProjectileDrawing(self):
        return SHURIKEN if self.direction else SHURIKEN_REVERSE
    def getNameDrawing(self):
        return GEKI_NAME
    
