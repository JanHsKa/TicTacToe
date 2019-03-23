from GameModel import*


class AIPlayer():
    def __init__(self, figure, gameModel):
        self.figure = figure
        self.gameModel = gameModel
        self.istActive = False
        print("AIPlayer")

    def executeTurn(self):
        pass

    def findBestChoice(self):
        for i in self.gameModel.freeFields:
            self.calculateAllPosibilities(self.gameModel.freeFields.copy(), 
            self.gameModel.playfield.copy(), i)

    def calculateAllPosibilities(self, freeFields, playField, field):
        pass

    

