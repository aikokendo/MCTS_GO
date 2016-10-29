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
        if v.state.has_actions():
            return self.expand(v)
        else:
            return v.best_child()
        #select node for expansion based on the visit count.

    def expand(self, v):
        random_action = random.sample(v.state.actions, 1)
        simulated_board = copy.deepcopy(v.state)
        simulated_board.add_piece(random_action[0][0],random_action[0][1],self.roles.get_current_ai())
        v_child = node.Node(simulated_board, 0, 0, v, [])
        v.children.append(v_child)
        v.state.remove_action(random_action[0][0],random_action[0][1])
        return v_child
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

