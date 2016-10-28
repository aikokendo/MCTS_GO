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
        self.root = node.Node(state, 0, 0, None, [])


    def best_next_move(self):
        start_time = datetime.datetime.now()
        while (datetime.datetime.now() - start_time).seconds < 1:
            # v1 = self.select(self.root)
            score = self.simulate(self.root.state)
            self.root.back_propagate(score)
            best_child = self.root.best_child()
            return [best_child.state.last_x,best_child.state.last_y]

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
        simulated_board = copy.deepcopy(state)
        for i in self.roles.player_ai:
            actions = simulated_board.actions
            random_action = random.sample(actions,1)
            simulated_board.add_piece(random_action[0][0],random_action[0][1],i)
            result = simulated_board.is_terminal(i)
            if result == 1:  #tie
                return 0
            if result == 2:
                if i == self.roles.get_current_ai():   #current player won
                    return 50
                else:
                    return -100         #current player lost
        return self.simulate(simulated_board)

         #   1==1
        #return self.simulate(board)


    def get_best_child(self):
        a = 1  #implemented in the node, will delete this function shortly when we fix dependencies