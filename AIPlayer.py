from GameModel import *
from copy import *
from random import *

class AIPlayer():
    def __init__(self, figure, gameModel):
        self.figure = figure
        self.gameModel = gameModel
        self.istActive = False
        self.optimalField = [0, 0]
        self.turnCount = 10
        self.easyDifficulty = True

    def executeTurn(self):
        if self.easyDifficulty:
            self.randomChoice()
        else:
            self.findBestChoice()

        self.gameModel.placeMark(self.optimalField)
        self.turnCount = 10

    def setDifficultyToEasy(self):
        self.easyDifficulty = True

    def setDifficultyToHard(self):
        self.easyDifficulty = False

    def randomChoice(self):
        self.optimalField = self.gameModel.freeFields[randint(0, len(self.gameModel.freeFields) - 1)]

    def findBestChoice(self):
        if self.checkIfMiddleIsFree():
            self.optimalField = [1, 1]
        elif self.checkForCorners():
            corners = [[0, 0], [2, 0], [0, 2], [2, 2]]
            self.optimalField = corners[randint(0,3)]
        else:
            path = []
            for i in self.gameModel.freeFields:
                self.calculateAllPosibilities(deepcopy(self.gameModel), i, i, 0, deepcopy(path))

    def checkIfMiddleIsFree(self):
        if self.gameModel.freeFields.count([1,1]) > 0:
            return True

        return False

    def checkForCorners(self):
        if self.gameModel.turnCount < 2:
            return True

        return False

    def calculateAllPosibilities(self, newGameModel, startField, field, turnCount, path):
        newGameModel.placeMark(field)
        path.append(field)
        turnCount += 1

        if turnCount > 6:
            return False

        if newGameModel.checkIfCurrentPlayerWon():
            self.updateOptimalField(newGameModel.currentPlayer, turnCount, startField, path)
        elif newGameModel.checkIfGameOver():
            self.updateOptimalField(newGameModel.currentPlayer, turnCount + 1, startField, path)
        else:
            newGameModel.changeCurrentPlayer()

            for i in newGameModel.freeFields:
                self.calculateAllPosibilities(deepcopy(newGameModel), startField, i, turnCount, deepcopy(path))

    def updateOptimalField(self, currentPlayer, turnCount, startField, path):
        if currentPlayer == self.figure:
            if turnCount < self.turnCount:
                self.optimalField = startField
                self.turnCount = turnCount
        else:
            if turnCount < self.turnCount:
                self.optimalField = path[1]
                self.turnCount = turnCount



