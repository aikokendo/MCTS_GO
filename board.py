#!/usr/bin/python
import re

class Board:

    def __init__(self):
        #Creates the Board with an Matrix of 15x15 with values of 0 and an empty action set
        self.matrix = [[0 for i in range(0,15)] for i in range(0,15)]
        self.last_x = -1
        self.last_y = -1
        self.moves = 0
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
        self.moves = self.moves + 1

    def remove_action(self, x, y):
        self.actions.discard((x,y))

    def is_terminal(self, n):
        #   0 not terminal,
        #   1 tie,
        #   2 won
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

    def check_threat(self): #2 is Human, 1 is AI
        #Check if enemy has a winning move
        possible_threats = ["([1][2]{4}[0])","(^[2]{4}[0])", "([2]{3}[0][2])", "([2][0][2]{3})", "([2]{2}[0][2]{2})","([0][2]{4}([0-1]|$))"]
        threat_counters= [5,4,3,1,2,0]
        expressions = [self.get_row_expression(1,0), self.get_row_expression(0,1), self.get_row_expression(1,1), self.get_row_expression(1,-1)] #Horizontal, Vertical, Diagonal1, Diagonal2
        expr_adding = [(1,0),(0,1),(1,1),(1,-1)]
        for i in range(len(expressions)):
            for j in range(len(possible_threats)):
                result = re.search(possible_threats[j],expressions[i][0])
                if result != None:
                    print("Found threat")
                    x_result = expressions[i][1][0] + (result.span()[0] * expr_adding[i][0]) + (threat_counters[j] * expr_adding[i][0])
                    y_result = expressions[i][1][1] + (result.span()[0] * expr_adding[i][1]) + (threat_counters[j] * expr_adding[i][1])
                    return (x_result, y_result)
        return None
        #Open Three Regex /([0][2]{3}[0])/g
        #Four Regex /([0]?[2]{4}[0]?)/g
        #Split Three /([0][2]{2}[0][2][0])/g
        #Split Three /([0][2][0][2]{2}[0])

    def get_row_expression(self, x_add, y_add):
        x = self.last_x
        y = self.last_y
        start_xy = None
        expr = str(self.matrix[x][y])
        #Iterates Left
        for i in range(1,15):
            if self.is_index_in_bounds(x - (i*x_add),y - (i*y_add)):
                expr = str(self.matrix[x - (i*x_add)][y - (i*y_add)]) + expr
                start_xy = ((x - (i*x_add)),(y - (i*y_add)))
            else:
                break
        #Iterates Right
        for i in range(1,15):
            if self.is_index_in_bounds(x + (i*x_add),y + (i*y_add)):
                expr = expr + str(self.matrix[x + (i*x_add)][y + (i*y_add)])
            else:
                break
        return (expr, start_xy)



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

    def log_matrix(self):
        for i in self.matrix:
            row = ""
            for j in i:
                if(j == 0):
                    row += "[ ]"
                if(j == 1):
                    row += "[X]"
                if(j == 2):
                    row += "[O]"
            print(row)
    def log_matrix_with_actions(self):
        for index_x, i in enumerate(self.matrix):
            row = ""
            for index_y, j in enumerate(i):
                if(j == 0):
                    if (index_x,index_y) in self.actions:
                        row += "[A]"
                    else:
                        row += "[ ]"
                if(j == 1):
                    row += "[X]"
                if(j == 2):
                    row += "[O]"
            print(row)
