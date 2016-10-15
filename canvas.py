#!/usr/bin/python

import tkinter
import roles
import random
import time

class canvasManager:


    def on_canvas_click(self,event):
        xboardpos = round((event.x - self.xoffset) / self.squaresize)
        yboardpos = round((event.y - self.yoffset) / self.squaresize)
        self.add_piece(xboardpos,yboardpos)

    def __init__(self,gameroles,state):
        self.xoffset = 96  # 300px image x center position - (460px image width / 2) + 26px minor image margin up to first line
        self.yoffset = 96  # 300px image y center position - (460px image height / 2) + 26px minor image margin
        self.squaresize = 27  # square size
        self.piecesize = self.squaresize - 2
        self.numberoflines = 15
        self.gameroles = gameroles
        self.state = state

        top = tkinter.Tk()
        self.w = tkinter.Canvas(top, width=600, height=600)
        self.w.pack()
        photo = tkinter.PhotoImage(file='./board.png')
        self.w.create_image(300, 300, image=photo)
        self.w.bind('<Button-1>', self.on_canvas_click)

        top.mainloop()

    def add_piece(self,xboardpos,yboardpos):
        newx = self.xoffset + (xboardpos) * self.squaresize
        newy = self.yoffset + (yboardpos) * self.squaresize
        if xboardpos >= 0 and xboardpos <= self.numberoflines and yboardpos >= 0 and yboardpos <= self.numberoflines:
            if self.state[yboardpos][xboardpos] == 0:
                obj = self.w.create_oval(newx - self.squaresize / 2, newy - +self.piecesize / 2, newx + self.piecesize / 2,
                                               newy + self.piecesize / 2, fill=self.gameroles.get_current_color())
                self.state[yboardpos][xboardpos] = 1
                self.next_turn()

    def next_turn(self):
        self.gameroles.next_player()
        if self.gameroles.get_current_ai() == 1:
            print('ai turn')
            #activate monte carlo
            #add piece as recommended by monte carlo.
            #delete the random below
           # time.sleep(2)
           # self.add_piece(random.randint(0,15),random.randint(0,15))
