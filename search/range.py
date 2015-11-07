'''
Use inorder traversal to return a range of keys.
'''


class Node(object):

    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def _add(self, node, k, v):
        if node is None:
            return Node(k, v)
        if k > node.k:
            node.right = self._add(node.right, k, v)
        elif k < node.k:
            node.left = self._add(node.left, k, v)
        else:
            node.v = v
        return node

    def add(self, k, v):
        self.root = self._add(self.root, k, v)

    def _range(self, node, min_, max_, result):
        if node is None:
            return
        if node.k >= min_:
            self._range(node.left, min_, max_, result)
        if node.k >= min_ and node.k <= max_:
            result.append(node.k)
        if node.k <= max_:
            self._range(node.right, min_, max_, result)

    def range(self, min_, max_):
        result = []
        self._range(self.root, min_, max_, result)
        return result


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.add(5, 'a')
    bst.add(3, 'b')
    bst.add(6, 'c')
    bst.add(8, 'd')
    bst.add(1, 'e')
    bst.add(9, 'f')
    bst.add(4, 'g')
    print bst.range(3, 6)
