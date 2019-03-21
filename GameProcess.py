from Board import *


class GameProcess:
    def __init__(self):
        self.play = Board(self.canvasClickCallback)
        playfield = [[0,0,0]] * 3
        currentPlayer = 0
        

    def canvasClickCallback(self, event):
        pass
    
