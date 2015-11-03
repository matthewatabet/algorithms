'''
Binary search tree
'''


class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


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
        elif node.value >= node.value:
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

    def _delete(self, key, node):
        if node is None:
            return
        elif key == node.key:
           pass
        elif key >= node.key:
            node.right = self._delete(key, node.right)
        else:
            node.left = self._delete(key, node.left)

    def delete(self, key):
        self._delete(key, self.root)


bst = BinarySearchTree()
bst.add('C', 3)
bst.add('B', 2)
bst.add('A', 1)
print bst
print bst.get('A')
print bst.get('B')
