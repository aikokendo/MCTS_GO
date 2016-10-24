#!/usr/bin/python
import node
import datetime


class MonteCarlo:

    def __init__(self,state):
        # create the root
        v0 = node.Node(state, None, None, 0, 0, None, [])
        start_time = datetime.datetime.now()
        while (datetime.datetime.now() - start_time).seconds < 8:
            #v1 = self.select(v0)
            #score = self.simulate(v1.state)
            #v1.back_propagate(score)
        #return x, y


    def select(self):
        return 1
        #select node for expansion based on the visit count.

    def expand(self):
        a=1
        #expand a selectd node by all the possible actions it has available.

    def simulate(self):
        a=1
        #simulate player movements up to getting a winner. Assign a value to the result (depthcharge)
        #use simulate to best guess how much valuable a branch is.

    def back_propagation(self):
        a=1
        #update parents based on children simulate results

