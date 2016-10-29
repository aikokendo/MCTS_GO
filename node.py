#!/usr/bin/python

import math

class Node:

    def __init__(self, state, visits, utility, parent, children):
        self.state = state
        self.visits = visits
        self.utility = utility
        self.parent = parent
        self.children = children
        self.best_child_score = 0


    def best_child(self):
        score = 0
        result = None
        for i in self.children:
            new_score = i.utility + math.sqrt(math.log(i.visits)/self.visits)
            if new_score > score:
                score = new_score
                result = i
            if result == None:
                result = i
        self.best_child_score = score
        return result

    def back_propagate(self,score):
        self.visits += 1
        self.utility += score
        if self.parent is not None:
            self.parent.back_propagate(score)