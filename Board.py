from tkinter import *

class Board:

    def __init__(self):

        master = Tk()

        self.canvasWidth = 300
        self.canvasHeight = 300
        self.columnHeight = self.canvasHeight / 3
        self.columnWidth = self.canvasWidth / 3
        self.w = Canvas(master,
                        width = self.canvasWidth,
                        height = self.canvasHeight)
        self.w.pack()

        y = int(self.columnHeight)

    def drawBaseBoard(self):
        self.drawParallelLines()
        self.drawVerticalLines()

    def drawParallelLines(self):
        y = int(self.columnHeight)
        self.w.create_line(0, y, self.canvasWidth, y, fill="#476042")
        self.w.create_line(0, y + self.columnHeight, self.canvasWidth, y + self.columnHeight, fill="#476042")

    def drawVerticalLines(self):
        y = int(0)
        self.w.create_line(self.columnWidth, y, self.columnWidth, self.canvasHeight, fill="#476042")
        self.w.create_line(2 * self.columnWidth, y, 2 * self.columnWidth, self.canvasHeight, fill="#476042")



newBoard = Board()
newBoard.drawBaseBoard()
mainloop()