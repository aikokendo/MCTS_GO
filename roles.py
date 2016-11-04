#!/usr/bin/python


class Roles:

    def __init__(self,player_ai):
        self.players = [1,2]
        self.colors = ['Black','White']
        self.player_ai = player_ai #1 if the player is to be played by AI, #2 if the player is a human.
        self.current_player = 0

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


    def player_array_for_montecarlo(self):
        if self.get_current_ai() == self.player_ai[0]:
            return [self.player_ai[1],self.player_ai[0]]
        else:
            return self.player_ai
