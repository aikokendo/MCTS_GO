#!/usr/bin/python
import node
import datetime
import board
import copy
import random
class MonteCarlo:


    def __init__(self,state,roles):
        self.roles = roles
        # create the root
        v0 = node.Node(state, None, None, 0, 0, None, [])
        start_time = datetime.datetime.now()
        while (datetime.datetime.now() - start_time).seconds < 1:
            #v1 = self.select(v0)
            #score = self.simulate(v1.state)
            #v1.back_propagate(score)

            #test
            self.simulate(v0.state)
        #return x, y

    def select(self, v):
        while not v.state.is_terminal():
            if v.state.has_actions():
                self.expand(v)
            else:
                self.get_best_child()
                #if v #is not fully expanded
                #    return expand(v)
                #else
        #select node for expansion based on the visit count.

    def expand(self, v):
        a=1
        #expand a selectd node by all the possible actions it has available.

    def simulate(self, state):
        #simulate player movements up to getting a winner. Assign a value to the result (depthcharge)
        #use simulate to best guess how much valuable a branch is.
        simulated_board = copy.copy(state)
        for i in self.roles.player_ai:
            actions = simulated_board.actions
            random_action = random.sample(actions,1)
            simulated_board.add_piece(random_action[0][0],random_action[0][1],i)
            if simulated_board.is_terminal(i):
                if i == self.roles.get_current_ai():
                    return 10
                else:
                    return -100
        self.simulate(simulated_board)

         #   1==1
        #return self.simulate(board)

    def back_propagation(self):
        a=1
        #update parents based on children simulate results
    def get_best_child(self):
        a = 1