from scripts.classes.character import character
from scripts.surfaces import *
from scripts.consts import *

class ryu(character):
    def __init__(self, defaultPosX, defaultPosY, standWidth, standHeight) -> None:
        self.hadoukens = []
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
    def getHdkPosDrawing(self):
        return RYU_HADOUKEN
