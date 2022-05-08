class Player:
    nbrOfPlayers = 0

    def __init__(self, name) -> None:
        self.name = name
        self.character = None
        self.nbrOfWin = 0
        Player.nbrOfPlayers += 1
        pass

    def setCharacter(self, newCharacter):
        self.character = newCharacter
    
    def addWin(self):
        self.nbrOfWin += 1
    
    def resetWin(self):
        self.nbrOfWin = 0