'''
Binary search tree
'''


class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return '%s=%s' % (self.key, self.value)


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def _as_string(self, node):
        if node is None:
            return ''
        s = (self._as_string(node.left) +
             '%s=%s ' % (node.key, node.value) +
             self._as_string(node.right))
        return s

    def __repr__(self):
        return self._as_string(self.root)

    def _add(self, key, value, node):
        if node is None:
            return Node(key, value)
        elif key >= node.key:
            node.right = self._add(key, value, node.right)
        else:
            node.left = self._add(key, value, node.left)
        return node

    def add(self, key, value):
        self.root = self._add(key, value, self.root)

    def _get(self, key, node):
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key >= node.value:
            return self._get(key, node.right)
        else:
            return self._get(key, node.left)

    def get(self, key):
        return self._get(key, self.root)

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        return node

    def _delete(self, key, node):
        if node is None:
            return
        elif key == node.key:
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                x = self._min(node.right)
                x.right = self._delete_min(node.right)
                x.left = node.left
                node = x

        elif key >= node.key:
            node.right = self._delete(key, node.right)
        else:
            node.left = self._delete(key, node.left)
        return node

    def delete(self, key):
        self._delete(key, self.root)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.add('C', 3)
    bst.add('B', 2)
    bst.add('A', 1)
    bst.add('H', 4)
    bst.add('E', 5)
    print bst
    bst.delete('B')
    print bst
    bst.delete('H')
    print bst
    bst.add('Q', 15)
    bst.add('T', 11)
    print bst
