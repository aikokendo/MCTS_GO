#!/usr/bin/python

import node
import montecarlo
import roles
import board


#create the root
test_node = node.Node('root',1,1, 0, 0, None, [])

#create a child and appending
test_child = node.Node('child1',2,3,0,0,test_node,[])
test_node.children.append(test_child)

#example of backpropagation
test_child.back_propagate(5)

test_child = node.Node('child2',3,4,0,0,test_node,[])
test_node.children.append(test_child)
test_child.back_propagate(1)

#print(test_node.utility)
#print(len(test_node.children))


#state = [[0 for i in range(0,15)] for i in range(0,15)]
#valid_moves_left = []
#for i in range(15):
#    for f in range(15):
#        valid_moves_left.append([i,f])

#print(valid_moves_left)

board_instance = board.Board()
game_roles = roles.Roles([1, 2])
board_instance.add_piece(10,10,game_roles.get_current_ai())
montecarlo.MonteCarlo(board_instance,game_roles)







