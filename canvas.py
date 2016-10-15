#!/usr/bin/python

import tkinter
import roles
import random
import time


class CanvasManager:

    def on_canvas_click(self,event):
        if self.canvas_blocked == 0:
            x_board_pos = round((event.x - self.x_offset) / self.square_size)
            y_board_pos = round((event.y - self.y_offset) / self.square_size)
            self.add_piece(x_board_pos,y_board_pos)

    def __init__(self,game_roles,state):
        self.x_offset = 96  # 300px image x center position - (460px image width / 2) + 26px minor image margin up to first line
        self.y_offset = 96  # 300px image y center position - (460px image height / 2) + 26px minor image margin
        self.square_size = 27  # square size
        self.piece_size = self.square_size - 2
        self.number_of_lines = 15
        self.canvas_blocked = 0
        self.first = 0
        self.game_roles = game_roles
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

    def add_piece(self,x_board_pos,y_board_pos):
        newx = self.x_offset + (x_board_pos) * self.square_size
        newy = self.y_offset + (y_board_pos) * self.square_size
        if x_board_pos >= 0 and x_board_pos <= self.number_of_lines \
                and y_board_pos >= 0 and y_board_pos <= self.number_of_lines:
            if self.state[y_board_pos][x_board_pos] == 0:
                obj = self.w.create_oval(newx - self.square_size / 2, newy - +self.piece_size / 2, newx + self.piece_size / 2,
                                               newy + self.piece_size / 2, fill=self.game_roles.get_current_color())
                self.state[y_board_pos][x_board_pos] = 1
                print("[{0}({1},{2})]".format(self.game_roles.get_current_color(),chr(65+x_board_pos),y_board_pos))
                self.top.update()
                self.next_turn()

    def next_turn(self):
        self.game_roles.next_player()
        self.first = 1
        self.canvas_blocked = 0
        self.update_status()
        self.check_ai()

    def update_status(self):
        playerstatus = "Human"
        if self.game_roles.get_current_ai() == 1:
            playerstatus = "AI"
        self.w.itemconfig(self.status,
                          text="Player {0} turn ({1})".format(self.game_roles.players[self.game_roles.get_current_player()],
                                                              playerstatus))
        self.top.update()


    def check_ai(self):
        if self.game_roles.get_current_ai() == 1:
            self.canvasblocked = 1
            if self.first == 0 :
                self.add_piece(random.randint(7, 9), random.randint(7, 9))
            else:
                #activate monte carlo
                #add piece as recommended by monte carlo.
                #delete the random below
                time.sleep(2)
                self.add_piece(random.randint(0,15),random.randint(0,15))

