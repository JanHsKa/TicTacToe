from tkinter import *
from Enums import *

class Board:

    def __init__(self, canvasClickCallback):

        master = Tk()

        self.canvasWidth = 300
        self.canvasHeight = 300
        self.minimumSpace = 5
        self.columnHeight = self.canvasHeight / 3
        self.columnWidth = self.canvasWidth / 3
        self.gameBoard = Canvas(master,
                                width=self.canvasWidth,
                                height=self.canvasHeight)

        self.gameBoard.bind("<Key>", self.key)
        self.gameBoard.bind("<Button-1>", canvasClickCallback)
        y = int(self.columnHeight)
        self.gameBoard.pack()

    def key(self, event):
        print ("pressed", repr(event.char))

    def drawSigns(self, event):

        print ("clicked at", event.x, event.y)

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


newBoard = Board(lambda a : a)
newBoard.drawBaseBoard()
newBoard.drawCircle([0, 2])
newBoard.drawCross([1, 2])
mainloop()
