#!/usr/bin/python
import random

class roles:

    def __init__(self,players,colors,playerAI):
        self.players = players
        self.colors = colors
        self.playerAI = playerAI #1 if the player is to be played by AI, #2 if the player is a human.
        self.currentPlayer = random.randint(0,len(players)-1)

    def GetCurrentPlayer(self):
        return self.currentPlayer

    def GetCurrentColor(self):
        return self.colors[self.currentPlayer]

    def NextPlayer(self):
        if self.currentPlayer == len(self.players)-1:
            self.currentPlayer = 0
        else:
            self.currentPlayer += 1

    def GetCurrentAI(self):
        return self.playerAI[self.currentPlayer]

