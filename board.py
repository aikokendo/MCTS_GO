#!/usr/bin/python


class Board:

    def __init__(self, matrix, last_x, last_y):
        self.matrix = matrix
        self.last_x = last_x
        self.last_y = last_y

    def add_piece(self,x,y):

    def is_terminal(self, n):
        is_terminal = False
        is_terminal = self.check_row(n, last_x - 4, last_y, 1, 0) #LEFT TO RIGHT
        if(is_terminal) return True
        is_terminal = self.check_row(n,last_x, last_y - 4, 0, 1) #DOWN TO UP
        if(is_terminal) return True
        is_terminal = self.check_row(n,last_x - 4,last_y - 4,1,1) # DOWN LEFT TO UP RIGHT
        if(is_terminal) return True
        is_terminal = self.check_row(n,last_x - 4,last_y + 4,1,-1) # UP LEFT TO DOWN RIGHT
        if(is_terminal) return True

    def check_row(self,n, lx, ly, x_add, y_add):
        k = 0
        for i in range(9):
            if ((lx + (i* x_add)) <= 14 and (lx + (i* x_add)) >= 0 )
            and ((ly + (i* y_add)) <= 14 and (ly + (i* y_add)) >= 0 )
            and (matrix[lx + (i * x_add)][ly + [(i * y_add)]] == n)
                k ++
                if k >= 5
                    return True
            else
                k = 0
        return False
