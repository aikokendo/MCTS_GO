#!/usr/bin/python

import tkinter
import random

def onCanvasClick(event):
    xoffset = 96 #300px image x center position - (460px image width / 2) + 26px minor image margin up to first line
    yoffset = 96 #300px image y center position - (460px image height / 2) + 26px minor image margin
    squaresize = 27 #square size
    piecesize = squaresize - 2
    numberoflines = 15

    xboardpos = round((event.x - xoffset) / squaresize)
    yboardpos = round((event.y - yoffset) / squaresize)
    newx = xoffset + (xboardpos)* squaresize
    newy = yoffset + (yboardpos) * squaresize
    print('Got canvas click', event.x, event.y, event.widget,xboardpos,yboardpos,newx,newy,state)
    if xboardpos >= 0 and xboardpos <=numberoflines and yboardpos >=0 and yboardpos <=numberoflines:
        if state[yboardpos][xboardpos] == 0:
            obj = event.widget.create_oval(newx-squaresize/2,newy-+piecesize/2,newx+piecesize/2,newy+piecesize/2, fill="red")
            state[yboardpos][xboardpos] = 1



global state;
state = [[0 for i in range(0,14)] for i in range(0,14)]
top = tkinter.Tk()
w = tkinter.Canvas(top, width=600,height=600)
w.pack()
photo = tkinter.PhotoImage(file = './board.png')
w.create_image(300,300,image=photo)
w.bind('<Button-1>', onCanvasClick)

top.mainloop()


