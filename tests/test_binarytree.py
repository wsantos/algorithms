#import pytest
from algorithms.datastructure.binarytree import Node



class TestBinaryTree:
    def test_instanciate_node(self):
        node = Node(1)
        node.left = Node(5)
        node.right = Node(3)



