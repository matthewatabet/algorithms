import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import bst


def _validate(node):
    if node is None:
        return True, None, None

    l_valid, l_min, l_max = _validate(node.left)
    r_valid, r_min, r_max = _validate(node.right)

    valid = l_valid and r_valid
    if valid:
        if l_max is not None:
            valid = valid and l_max < node.key
        if r_max is not None:
            valid = valid and r_max >= node.key
    return valid, min(r_min, node.key), max(r_max, node.key)


def validate(tree):
    return _validate(tree.root)[0]


if __name__ == '__main__':
    tree = bst.BinarySearchTree()
    tree.add('X', 1)
    tree.add('B', 2)
    tree.add('Q', 3)
    tree.add('A', 2)
    print validate(tree)

    # Concoct an invalid tree.
    tree = bst.BinarySearchTree()
    tree.root = bst.Node('G', 2)
    tree.root.left = bst.Node('B', 3)
    tree.root.left.right = bst.Node('C', 4)
    tree.root.left.left = bst.Node('X', 5)

    print validate(tree)
