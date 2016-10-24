#!/usr/bin/python

import node

#create the root
test_node = node.Node('root', 0, 0, None, [])

#create a child and appending
test_child = node.Node('child1',0,0,test_node,[])
test_node.children.append(test_child)

#example of backpropagation
test_child.back_propagate(5)

test_child = node.Node('child2',0,0,test_node,[])
test_node.children.append(test_child)
test_child.back_propagate(1)

print(test_node.utility)
print(len(test_node.children))







