#!/usr/bin/python


class Node:

    def __init__(self, state, visits, utility, parent, children):
        self.state = state
        self.visits = visits
        self.utility = utility
        self.parent = parent
        self.children = children

