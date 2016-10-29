#!/usr/bin/python

import math

class Node:

    def __init__(self, state, visits, utility, parent, children):
        self.state = state
        self.visits = visits
        self.utility = utility
        self.parent = parent
        self.children = children

    def best_child(self):
        score = 0
        result = self
        for i in self.children:
            new_score = i.utility + math.sqrt(math.log(i.visits)/self.visits)
            if new_score > score:
                score = new_score
                result = i
        return result
