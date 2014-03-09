#encode: utf-8

class Node(object):
    __slots__ = ("left", "right", "key")

    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


    def __repr__(self):
        return "Key: %s (Left: %s - Right: %s)" % (self.key, self.left,
                self.right)
