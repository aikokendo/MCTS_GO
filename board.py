#!/usr/bin/python


class Board:

    def __init__(self):
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
        self.last_x = x
        self.last_y = y 

    def check_add_action(self,x,y):
        if is_index_in_bounds(self,x,y)
            if self.matrix[x][y] == 0
                self.actions.append((x,y))

    def is_index_in_bounds(self,x,y):
        if (x <= 14 and x >= 0) and (y <= 14 and y >= 0)
            return True
        return False

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
            and (self.matrix[lx + (i * x_add)][ly + [(i * y_add)]] == n)
                k ++
                if k >= 5
                    return True
            else
                k = 0
        return False
