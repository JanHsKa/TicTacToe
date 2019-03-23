from Board import *
from GameModel import *
from AIPlayer import *


class GameController:
    def __init__(self):
        self.gameModel = GameModel(0)
        self.play = Board(self.canvasClickCallback, self.startNewGame, self.gameModel.playFieldWidth, self.gameModel.playfieldHeight)
        self.aiPlayer = AIPlayer(1, self.gameModel)

    def startNewGame(self):
        self.gameModel.resetGame()
        self.play.resetBoard()
        
    
    def canvasClickCallback(self, event):
        if self.gameModel.checkIfGameOver():
            return False

        x = event.x
        y = event.y
        field = [x, y]
    
        if self.gameModel.executePlayerTurn(field[0], field[1]):
            self.play.drawSigns(self.gameModel.currentField, self.gameModel.currentPlayer)
            self.gameModel.checkIfCurrentPlayerWon()
            self.gameModel.changeCurrentPlayer()

        return True
    



    
