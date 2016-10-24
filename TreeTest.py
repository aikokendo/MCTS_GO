#!/usr/bin/python

import node
import montecarlo


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

print(test_node.utility)
print(len(test_node.children))


montecarlo.MonteCarlo("a")





