#!/usr/bin/python


class Board:

    def __init__(self, matrix, last_x, last_y):
        self.matrix = matrix
        self.last_x = last_x
        self.last_y = last_y

    def is_terminal(self):
