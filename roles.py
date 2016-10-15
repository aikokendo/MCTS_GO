#!/usr/bin/python
import random


class Roles:

    def __init__(self,players,colors,player_ai):
        self.players = players
        self.colors = colors
        self.player_ai = player_ai #1 if the player is to be played by AI, #2 if the player is a human.
        self.current_player = random.randint(0,len(players)-1)

    def get_current_player(self):
        return self.current_player

    def get_current_color(self):
        return self.colors[self.current_player]

    def next_player(self):
        if self.current_player == len(self.players)-1:
            self.current_player = 0
        else:
            self.current_player += 1

    def get_current_ai(self):
        return self.player_ai[self.current_player]

