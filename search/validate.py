import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import bst


def inorder(node, flattened):
    if node is None:
        return
    else:
        inorder(node.left, flattened)
        flattened.append(node.key)
        inorder(node.right, flattened)


def validate_bst(tree):
    # get the inorder traversal
    keys = []
    inorder(tree.root, keys)

    # ensure the inorder values are non-decreasing
    prev = None
    for k in keys:
        if prev is None:
            prev = k
        elif k < prev:
            return False
        else:
            prev = k
    return True


if __name__ == '__main__':
    tree = bst.BinarySearchTree()
    tree.add('X', 1)
    tree.add('B', 2)
    tree.add('Q', 3)
    tree.add('A', 2)
    print validate_bst(tree)
