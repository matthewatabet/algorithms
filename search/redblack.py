
class Node(object):

    RED = 'R'
    BLACK = 'B'

    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.color = self.RED
        self.key = key
        self.value = value

    def __repr__(self):
        return '%s=%s(%s)' % (self.key, self.value, self.color)

    def is_red(self):
        return self.color == self.RED


class RedBlackBST(object):

    def __init__(self):
        self.root = None

    def _to_string(self, node):
        if node is None:
            return ''
        return ' '.join([self._to_string(node.left),
                         repr(node),
                         self._to_string(node.right)])

    def __repr__(self):
        return self._to_string(self.root)

    def _is_red(self, node):
        if node is None:
            return False
        return node.color == node.RED

    def _flip_colors(self, node):
        node.color = node.RED
        node.left.color = node.BLACK
        node.right.color = node.BLACK

    def _rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = node.RED
        return x

    def _rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = node.RED
        return x

    def _add(self, node, key, value):
        if node is None:
            return Node(key, value)

        if key > node.key:
            node.right = self._add(node.right, key, value)
        elif key < node.key:
            node.left = self._add(node.left, key, value)
        else:
            node.value = value

        if (self._is_red(node.right)
                and not self._is_red(node.left)):
            node = self._rotate_left(node)
        if (self._is_red(node.left)
                and not self._is_red(node.right)):
            node = self._rotate_right(node)
        if (self._is_red(node.left)
                and self._is_red(node.right)):
            self._flip_colors(node)
        return node

    def add(self, key, value):
        self.root = self._add(self.root, key, value)
        self.root.color = Node.BLACK

if __name__ == '__main__':
    rbbst = RedBlackBST()
    rbbst.add(5, 'a')
    rbbst.add(2, 'b')
    rbbst.add(3, 'c')
    rbbst.add(6, 'd')
    rbbst.add(13, 'e')
    rbbst.add(8, 'f')
    print rbbst
