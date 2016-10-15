#!/usr/bin/python
import random

class roles:

    def __init__(self,players,colors):
        self.players = players
        self.colors = colors
        self.currentPlayer = random.randint(0,len(players)-1)

    def get_current_player(self):
        return self.currentPlayer

    def get_current_color(self):
        return self.colors[self.currentPlayer]

    def next_player(self):
        if self.currentPlayer == len(self.players)-1:
            self.currentPlayer = 0
        else:
            self.currentPlayer += 1


