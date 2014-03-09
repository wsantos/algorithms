#encode: utf-8
import sys

MAX_INT = sys.maxint
MIN_INT = -sys.maxint - 1


def is_bst(node, min=MIN_INT, max=MAX_INT):
    print node, min, max

    if node.key < min or node.key > max:
        return False

    if node.left is None and node.right is None:
        return True

    left = is_bst(node.left, MIN_INT, node.key)
    right = is_bst(node.right, node.key, MAX_INT)

    print left, right

    if not left or not right:
        return False

    return True
