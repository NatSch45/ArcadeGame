from scripts.classes.character import Character
from scripts.surfaces import *
from scripts.consts import *
import datetime as DT

class Ryu(Character):
    def __init__(self, defaultPosX, defaultPosY, standWidth, standHeight) -> None:
        self.hadoukens = []

        self.startHadouken = DT.datetime.now() - DT.timedelta(seconds=0.5) # Cooldown for hadouken position animation
        self.startPunch = DT.datetime.now() - DT.timedelta(seconds=0.5) # Cooldown for punch animation
        self.startKick = DT.datetime.now() - DT.timedelta(seconds=0.5) # Cooldown for kick animation

        self.name = "Ryu"
        super().__init__(defaultPosX, defaultPosY, standWidth, standHeight)
    
    def handleHadoukens(self):
        for hadouken in self.hadoukens:
            hadouken.x += HADOUKEN_VEL
            if hadouken.x > WIDTH:
                self.hadoukens.remove(hadouken)

    def getStandDrawing(self):
        return RYU_STAND
    def getStoopDrawing(self):
        return RYU_STOOP
    def getJumpDrawing(self):
        return RYU_JUMP
    def getStaticPunchDrawing(self):
        return RYU_STATIC_PUNCH
    def getStaticKickDrawing(self):
        return RYU_STATIC_KICK
    def getHdkPosDrawing(self):
        return RYU_HADOUKEN
    
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
