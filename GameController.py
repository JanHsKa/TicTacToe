from Board import *
from GameModel import *
from AIPlayer import *


class GameController:
    def __init__(self):
        self.gameModel = GameModel(0)
        self.aiPlayer = AIPlayer(Figures.circle, self.gameModel)
        self.play = Board(self.canvasClickCallback, self.startNewGame, 
            self.aiPlayer.setDifficultyToEasy, self.aiPlayer.setDifficultyToHard, self.gameModel.playFieldWidth, self.gameModel.playfieldHeight)
        self.aiTurn = False

    def startNewGame(self):
        startPlayer = randint(0,1)
        self.gameModel.resetGame(startPlayer)
        self.play.resetBoard()
        self.aiTurn = startPlayer
        self.executeAITurn()
        
    def executeAITurn(self):
        if self.gameModel.checkIfGameOver() or not self.aiTurn:
            return False

        self.aiPlayer.executeTurn()
        self.play.drawSigns(self.gameModel.currentField, self.gameModel.currentPlayer)

        self.gameModel.checkIfCurrentPlayerWon()
        self.gameModel.changeCurrentPlayer()
        self.aiTurn = False

    def canvasClickCallback(self, event):
        if self.aiTurn or self.gameModel.checkIfGameOver():
            return False

        x = event.x
        y = event.y
        field = [x, y]

        if self.gameModel.executePlayerTurn(field[0], field[1]):
            self.play.drawSigns(self.gameModel.currentField, self.gameModel.currentPlayer)
            self.gameModel.checkIfCurrentPlayerWon()
            self.gameModel.changeCurrentPlayer()
            self.aiTurn = True
            self.executeAITurn()

        return True
    



    
