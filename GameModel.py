from Enums import *

class GameModel:
    def __init__(self, currentPlayer):
        self.playfield = self.getNewPlayfield()
        self.freeFields = []
        self.freeFields = self.getNewFreeField()
        self.currentPlayer = currentPlayer
        self.playFieldWidth = 300
        self.playfieldHeight = 300
        self.currentField = [0, 0]
        self.gameOver = False


    def resetGame(self):
        self.gameOver = False
        self.freeFields = self.getNewFreeField()
        self.playfield = self.getNewPlayfield()
        self.currentField = [0, 0]

    def changeCurrentPlayer(self):
        self.currentPlayer = (self.currentPlayer + 1) % 2

    def getNewFreeField(self):
        field = []
        for i in range(3):
            for j in range(3):
                field += [[i,j]]

        return field

    def getNewPlayfield(self):
        newList = []
        for i in range(3):
            newPartList = []
            for j in range(3):
                newPartList += [2]
            newList += [newPartList]

        return newList

    def getClickedField(self, x, y):
        xIndex = self.calcCoordinateIndex(x)
        yIndex = self.calcCoordinateIndex(y)

        return [xIndex, yIndex]

    def calcCoordinateIndex(self, value):
        coordValue = 0
        for i in range(3):
            if value > i * (self.playFieldWidth / 3):
                coordValue = i
        
        return coordValue

    def isFieldFree(self, field):
        if self.freeFields.count(field) > 0:
            return True
        else:
            return False
    
    def placeMark(self, field):
        self.playfield[field[0]][field[1]] = self.currentPlayer
        self.freeFields.remove(field)
        self.currentField = field

    def executePlayerTurn(self, x, y):
        field = self.getClickedField(x, y)
        
        if self.isFieldFree(field):
           self.placeMark(field)
           return True
        else:
            return False

    def checkIfGameOver(self):
        if len(self.freeFields) == 0 or self.gameOver:
            self.gameOver = True
            return True
        else:
            return False

    def checkIfCurrentPlayerWon(self):
        if self.checkDiagonals() or self.checkVerticals() or self.checkHorizontals():           
            self.gameOver = True
            return True
        
        return False

    def checkVerticals(self):
        for i in range(3):
            if self.playfield[i][0] == self.currentPlayer:
                if self.checkLine(0, 1, [i,0]):
                    return True

        return False        

    def checkHorizontals(self):
        for i in range(3):
            if self.playfield[0][i] == self.currentPlayer:
                if self.checkLine(1, 0, [0, i]):
                    return True

        return False

    def checkDiagonals(self):
        if self.checkLine(1, 1, [0, 0]) or self.checkLine(-1, 1, [2, 0]):
            return True

        return False

    def checkLine(self, x, y, field):
        marks = 0
        for i in range(3):
            if self.playfield[field[0]][field[1]] == self.currentPlayer:
                marks += 1
            field[0] += x
            field[1] += y

        if marks == 3:
            return True
        
        return False
