from tkinter import *
master = Tk()

canvas_width = 80
canvas_height = 40
columnHeight = 10
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)

def drawBaseBoard():
    drawParallelLines()
    drawVerticalLines()


def drawParallelLines() :
    w.create_line(0, y, canvas_width, y, fill="#476042")
    w.create_line(0, y + columnHeight, canvas_width, y + columnHeight, fill="#476042")
    w.create_line(0, y + 2 * columnHeight, canvas_width, y + 2 * columnHeight, fill="#476042")

def  drawVerticalLines():
    w.create_line(columnHeight, y, canvas_width, y, fill="#476042")
    w.create_line(0, y + columnHeight, columnHeight, canvas_height, fill="#476042")

drawBaseBoard()
mainloop()