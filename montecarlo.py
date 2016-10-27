#!/usr/bin/python
import node
import datetime
import board


class MonteCarlo:

    def __init__(self,state,roles):
        self.roles = roles
        # create the root
        v0 = node.Node(state, None, None, 0, 0, None, [])
        start_time = datetime.datetime.now()
        while (datetime.datetime.now() - start_time).seconds < 8:
            #v1 = self.select(v0)
            #score = self.simulate(v1.state)
            #v1.back_propagate(score)

            #test
            self.simulate(v0.state)
        #return x, y


    def select(self):
        return 1
        #select node for expansion based on the visit count.

    def expand(self):
        a=1
        #expand a selectd node by all the possible actions it has available.

    def simulate(self, board):
        #simulate player movements up to getting a winner. Assign a value to the result (depthcharge)
        #use simulate to best guess how much valuable a branch is.
        if board.is_terminal():
            return 1 #reward()
        for i in self.roles.player_ai:
            #board.find_legals(self.roles.get_current_ai())
            1==1
        return self.simulate(board)

    def back_propagation(self):
        a=1
        #update parents based on children simulate results

