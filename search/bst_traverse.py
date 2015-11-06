'''
Non-recursive traversal of a binary search tree.
'''


class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return '%s=%s ' % (self.key, self.value)


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def _add(self, node, key, value):
        if node is None:
            return Node(key, value)
        elif key >= node.key:
            node.right = self._add(node.right, key, value)
        else:
            node.left = self._add(node.left, key, value)
        return node

    def add(self, key, value):
        self.root = self._add(self.root, key, value)


def inorder(tree, func):

    stack = []
    current = tree.root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        if stack:
            current = stack.pop()
            func(current)
            current = current.right


if __name__ == '__main__':
    def pr(n):
        print str(n)
    bst = BinarySearchTree()
    bst.add('c', 1)
    bst.add('a', 2)
    bst.add('z', 3)
    bst.add('e', 4)
    inorder(bst, pr)
