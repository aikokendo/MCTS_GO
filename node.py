#!/usr/bin/python


class Node:

    def __init__(self, state, x, y, visits, utility, parent, children):
        self.state = state
        self.visits = visits
        self.utility = utility
        self.parent = parent
        self.children = children

    def back_propagate(self,score):
        self.visits += 1
        self.utility += score
        if self.parent is not None:
            self.parent.back_propagate(score)
