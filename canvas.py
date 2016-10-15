#!/usr/bin/python

import tkinter
import roles
import random
import time


class CanvasManager:

    def on_canvas_click(self,event):
        if self.canvasblocked == 0:
            xboardpos = round((event.x - self.xoffset) / self.squaresize)
            yboardpos = round((event.y - self.yoffset) / self.squaresize)
            self.add_piece(xboardpos,yboardpos)

    def __init__(self,gameroles,state):
        self.xoffset = 96  # 300px image x center position - (460px image width / 2) + 26px minor image margin up to first line
        self.yoffset = 96  # 300px image y center position - (460px image height / 2) + 26px minor image margin
        self.squaresize = 27  # square size
        self.piecesize = self.squaresize - 2
        self.numberoflines = 15
        self.canvasblocked = 0
        self.first = 0
        self.gameroles = gameroles
        self.state = state

        self.top = tkinter.Tk(className="Gomoku! Montecarlo approach!")
        self.top.title = "hola"
        self.w = tkinter.Canvas(self.top, width=600, height=600)
        self.w.pack()
        photo = tkinter.PhotoImage(file='./board.png')
        self.status = self.w.create_text(300,50,text="...")
        self.w.create_image(300, 300, image=photo)
        self.w.bind('<Button-1>', self.on_canvas_click)
        self.update_status()
        self.check_ai()
        self.top.mainloop()

    def add_piece(self,xboardpos,yboardpos):
        newx = self.xoffset + (xboardpos) * self.squaresize
        newy = self.yoffset + (yboardpos) * self.squaresize
        if xboardpos >= 0 and xboardpos <= self.numberoflines and yboardpos >= 0 and yboardpos <= self.numberoflines:
            if self.state[yboardpos][xboardpos] == 0:
                obj = self.w.create_oval(newx - self.squaresize / 2, newy - +self.piecesize / 2, newx + self.piecesize / 2,
                                               newy + self.piecesize / 2, fill=self.gameroles.get_current_color())
                self.state[yboardpos][xboardpos] = 1
                self.top.update()
                self.next_turn()

    def next_turn(self):
        self.gameroles.next_player()
        self.first = 1
        self.canvasblocked = 0
        self.update_status()
        self.check_ai()

    def update_status(self):
        playerstatus = "Human"
        if self.gameroles.get_current_ai() == 1:
            playerstatus = "AI"
        self.w.itemconfig(self.status,
                          text="Player {0} turn ({1})".format(self.gameroles.players[self.gameroles.get_current_player()],
                                                              playerstatus))
        self.top.update()


    def check_ai(self):
        if self.gameroles.get_current_ai() == 1:
            self.canvasblocked = 1
            if self.first == 0 :
                self.add_piece(random.randint(7, 9), random.randint(7, 9))
            else:
                #activate monte carlo
                #add piece as recommended by monte carlo.
                #delete the random below
                time.sleep(2)
                self.add_piece(random.randint(0,15),random.randint(0,15))

