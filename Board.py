from tkinter import *
from Enums import *

class Board:

    def __init__(self, canvasClickCallback, resetGame, setDiffEasy, setDiffHard, width, height):

        master = Tk()

        self.canvasWidth = width
        self.canvasHeight = height
        self.minimumSpace = 5
        self.columnHeight = self.canvasHeight / 3
        self.columnWidth = self.canvasWidth / 3
        self.gameBoard = Canvas(master,
                                width=self.canvasWidth,
                                height=self.canvasHeight)

        self.gameBoard.bind("<Button-1>", canvasClickCallback)
        self.drawBaseBoard()
        self.gameBoard.pack()

        self.menubar = Menu(master)
        master.config(menu = self.menubar)

        self.menuPCPlayer = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Schwierigkeitsgrad", menu=self.menuPCPlayer)
        self.menuPCPlayer.add_command(label="Einfach", command=setDiffEasy)
        self.menuPCPlayer.add_command(label="Schwierig", command=setDiffHard)

        self.menubar.add_command(label="Neues Spiel", command=resetGame)
 

    def resetBoard(self):
        self.gameBoard.delete("all")
        self.drawBaseBoard()
        self.gameBoard.pack()

    def drawSigns(self, field, player):
        if player == Figures.circle:
            self.drawCircle(field)
        else:
            self.drawCross(field)

    def drawBaseBoard(self):
        self.drawParallelLines()
        self.drawVerticalLines()

    def drawParallelLines(self):
        y = int(self.columnHeight)
        self.gameBoard.create_line(0, y, self.canvasWidth, y, fill="#476042")
        self.gameBoard.create_line(0, y + self.columnHeight, self.canvasWidth, y + self.columnHeight, fill="#476042")

    def drawVerticalLines(self):
        y = int(0)
        self.gameBoard.create_line(self.columnWidth, y, self.columnWidth, self.canvasHeight, fill="#476042")
        self.gameBoard.create_line(2 * self.columnWidth, y, 2 * self.columnWidth, self.canvasHeight, fill="#476042")

    def drawCross(self, field):
        startEndCoordinates = self.computeStartEndCoordinates(field)
        self.gameBoard.create_line(startEndCoordinates[Coordinates.startX], startEndCoordinates[Coordinates.startY],
                                   startEndCoordinates[Coordinates.endX], startEndCoordinates[Coordinates.endY])
        self.gameBoard.create_line(startEndCoordinates[Coordinates.startX], startEndCoordinates[Coordinates.endY],
                                   startEndCoordinates[Coordinates.endX], startEndCoordinates[Coordinates.startY])


    def drawCircle(self, field):
        startEndCoordinates = self.computeStartEndCoordinates(field)
        self.gameBoard.create_oval(startEndCoordinates[Coordinates.startX], startEndCoordinates[Coordinates.startY],
                                   startEndCoordinates[Coordinates.endX], startEndCoordinates[Coordinates.endY])

    def computeStartEndCoordinates(self, field):
        startEndCoordinates = [0, 0, 0, 0]
        startEndCoordinates[Coordinates.startX] = field[0] * self.columnWidth + self.minimumSpace
        startEndCoordinates[Coordinates.endX] = (field[0] + 1) * self.columnWidth - self.minimumSpace
        startEndCoordinates[Coordinates.startY] = field[1] * self.columnHeight + self.minimumSpace
        startEndCoordinates[Coordinates.endY] = (field[1] + 1) * self.columnHeight - self.minimumSpace

        return startEndCoordinates
