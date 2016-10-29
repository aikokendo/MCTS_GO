#!/usr/bin/python


class Board:

    def __init__(self):
        #Creates the Board with an Matrix of 15x15 with values of 0 and an empty action set
        self.matrix = [[0 for i in range(0,15)] for i in range(0,15)]
        self.last_x = -1
        self.last_y = -1
        self.actions = set()

    def add_piece(self,x ,y, n):
        self.matrix[x][y] = n
        self.check_add_action(x+1,y)
        self.check_add_action(x-1,y)
        self.check_add_action(x,y+1)
        self.check_add_action(x,y-1)
        self.check_add_action(x+1,y+1)
        self.check_add_action(x+1,y-1)
        self.check_add_action(x-1,y+1)
        self.check_add_action(x-1,y-1)
        self.actions.discard((x,y))
        self.last_x = x
        self.last_y = y

    def remove_action(self, x, y):
        self.actions.discard((x,y))

    def is_terminal(self, n):
        #   0 not terminal,
        #   1 tie,
        #   2 won
        is_terminal = False
        is_terminal = self.check_row(n, self.last_x - 4, self.last_y, 1, 0) #LEFT TO RIGHT
        if(is_terminal): return 2
        is_terminal = self.check_row(n,self.last_x, self.last_y - 4, 0, 1) #DOWN TO UP
        if(is_terminal): return 2
        is_terminal = self.check_row(n,self.last_x - 4,self.last_y - 4,1,1) # DOWN LEFT TO UP RIGHT
        if(is_terminal): return 2
        is_terminal = self.check_row(n,self.last_x - 4,self.last_y + 4,1,-1) # UP LEFT TO DOWN RIGHT
        if(is_terminal): return 2
        if len(self.actions) == 0:
            return 1
        return 0

    def check_row(self,n, lx, ly, x_add, y_add):
        k = 0
        for i in range(9):
            x = lx + (i* x_add)
            y = ly + (i * y_add)
            if self.is_index_in_bounds(x,y) and (self.matrix[x][y] == n):
                k += 1
                if k >= 5: return True
            else:
                k = 0
        return False

    def check_add_action(self,x,y):
        if self.is_index_in_bounds(x, y) and self.is_valid_move(x,y):
            self.actions.add((x,y))

    def is_index_in_bounds(self,x,y):
        return ((x <= 14 and x >= 0) and (y <= 14 and y >= 0))

    def has_actions(self):
        return len(self.actions) > 0

    def is_valid_move(self,x,y):
        return self.matrix[x][y] == 0
