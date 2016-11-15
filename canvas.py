#!/usr/bin/python

import tkinter
import roles
import random
import time
from tkinter import font
import board
import montecarlo


class CanvasManager:

    def on_canvas_click(self,event):
        if self.canvas_blocked == 0:
            x_board_pos = round((event.x - self.x_offset) / self.square_size)
            y_board_pos = round((event.y - self.y_offset) / self.square_size)
            self.add_piece(x_board_pos,y_board_pos)

    def on_player_selected(self,event):
        if self.first == 0 and self.canvas_blocked == 1:
            if event.x >=485 and event.x<=515:
                self.w.create_rectangle(485,15,515,45, outline='gray')
                self.game_roles = roles.Roles([2, 1])  # human starts   #do not use 0
            else:
                self.w.create_rectangle(525,15,555,45, outline='gray')
                self.game_roles = roles.Roles([1, 2])  # AI starts      #do not use 0
            self.canvas_blocked = 0
            self.state = board.Board()
            self.update_status()
            self.check_ai()



    def __init__(self):
        self.x_offset = 98  # 300px image x center position - (470px image width / 2) + 38px minor image margin up to first line
        self.y_offset = 98  # 300px image y center position - (470px image height / 2) + 38px minor image margin
        self.square_size = 29  # square size
        self.piece_size = self.square_size - 4
        self.number_of_lines = 15
        self.canvas_blocked = 1
        self.first = 0
        self.list_of_pieces = []

        self.top = tkinter.Tk(className="Gomoku! Montecarlo approach!")
        self.w = tkinter.Canvas(self.top, width=600, height=600)
        self.w.pack()
        self.title = self.w.create_text(80, 30, text="GOMOKU!",
                                        font=font.Font(family='Helvetica', size=20, weight='bold'))
        self.subtitle = self.w.create_text(400, 30, text="Please select a player:",
                                        font=font.Font(family='Helvetica', size=12))
        self.obj1 = self.w.create_oval(500 - self.square_size / 2, 30 - +self.piece_size / 2, 500 + self.piece_size / 2,
                                 30 + self.piece_size / 2, fill='Black')
        self.obj2 = self.w.create_oval(540 - self.square_size / 2, 30 - +self.piece_size / 2, 540 + self.piece_size / 2,
                                               30 + self.piece_size / 2, fill='White')
        self.w.tag_bind(self.obj1,'<Double-1>',self.on_player_selected)
        self.w.tag_bind(self.obj2,'<Double-1>',self.on_player_selected)

        photo = tkinter.PhotoImage(file='./board.gif')
        self.status = self.w.create_text(300,550,text="...")

        self.w.create_image(300, 300, image=photo)
        self.w.bind('<Button-1>', self.on_canvas_click)
        self.top.mainloop()

    def add_piece(self,x_board_pos,y_board_pos):
        newx = self.x_offset + (x_board_pos) * self.square_size
        newy = self.y_offset + (y_board_pos) * self.square_size
        if x_board_pos >= 0 and x_board_pos < self.number_of_lines and y_board_pos >= 0 and y_board_pos < self.number_of_lines:
            if self.state.is_valid_move(x_board_pos, y_board_pos):
                obj = self.w.create_oval(newx - self.square_size / 2, newy - +self.piece_size / 2, newx + self.piece_size / 2,
                                               newy + self.piece_size / 2, fill=self.game_roles.get_current_color())
                self.state.add_piece(x_board_pos, y_board_pos, self.game_roles.get_current_ai())  #we are using the same user id as the board pieces
                self.list_of_pieces.append(obj)
                print("[{0}({1},{2})]".format(self.game_roles.get_current_color(),chr(65+x_board_pos),y_board_pos))
                self.top.update()
                self.next_turn()
            else:
                #AI tried to insert in a used place, this shouldnt happen with montecarlo,but could happen in the first turn
                self.check_ai()

    def next_turn(self):
        if(self.state.is_terminal(self.game_roles.get_current_ai())):
            self.got_a_winner()
        else:
            self.first = 1
            self.game_roles.next_player()
            self.canvas_blocked = 0
            self.update_status()
            self.check_ai()

    def update_status(self):
        player_status = "Human"
        if self.game_roles.get_current_ai() == 1:
            player_status = "AI"
        self.w.itemconfig(self.status,
                          text="Player {0} turn ({1})".format(self.game_roles.players[self.game_roles.get_current_player()],
                                                              player_status))
        self.top.update()

    def got_a_winner(self):
        self.w.itemconfig(self.status,
                          text="Player {0} is the WINNER!!!".format(
                              self.game_roles.players[self.game_roles.get_current_player()]))
        self.top.update()

    def check_ai(self):
        if self.game_roles.get_current_ai() == 1:
            self.canvas_blocked = 1
            if self.first == 0 :
                self.add_piece(random.randint(7, 9), random.randint(7, 9))
            else:
                MCTS = montecarlo.MonteCarlo(self.state, self.game_roles)
                move = MCTS.best_next_move()
                x,y = move[0],move[1]
                self.add_piece(x,y)

    def restart_game(self):
        print(self.list_of_pieces)
        for p in self.list_of_pieces:
            self.w.delete(p)
        self.list_of_pieces.clear()
