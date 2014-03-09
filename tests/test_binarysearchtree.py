#import pytest
import unittest
from algorithms.datastructure.binarytree import Node
from algorithms.datastructure.binarysearchtree import is_bst



class TestBinaryTree(unittest.TestCase):

    def test_is_binary_search_tree(self):
        node = Node(8)

        ret = is_bst(node)

        self.assertTrue(ret, "BST with only root must return true")


        node.left = Node(3)
        node.right = Node(10)

        node.left.left = Node(1)
        node.left.right = Node(6)

        ret = is_bst(node)

        self.assertTrue(ret, "BST True")



        # Not BST

        node.left = Node(10)
        node.right = Node(3)

        ret = is_bst(node)

        self.assertFalse(ret, "Left node must be less than parent")


