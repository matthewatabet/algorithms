'''
Arithmetic Binary Search Table.
'''
from math import floor


class ArithmeticBinarySearchTable(object):

    def __init__(self):
        self.keys = []
        self.values = []
        self.max_ = None
        self.min_ = None

    def __repr__(self):
        return repr(zip(self.keys, self.values))

    def _find(self, key, lo, hi):
        if lo >= hi:
            return lo
        # Interpolate keys, rather than simply starting with the midway
        # point.
        k = (key - self.keys[lo]) / (self.keys[hi] - self.keys[lo])
        k = int(floor((k * (hi - lo)) + lo))
        if key == self.keys[k]:
            return k
        elif key > self.keys[k]:
            return self._find(key, k + 1, hi)
        else:
            return self._find(key, lo, k - 1)

    def get(self, key):
        if key > self.max_ or key < self.min_:
            return None
        i = self._find(key, 0, len(self.keys) - 1)
        if self.keys[key] == self.keys[i]:
            return self.values[i]
        return None

    def put(self, key, value):

        i = 0
        # Handle fast putting at either end of the table.
        if key <= self.min_:
            pass  # just insert at 0
        elif key > self.max_:
            i = len(self.keys)
        elif key == self.max_:
            i = len(self.keys) - 1
        else:
            # Perform search
            i = self._find(key, 0, len(self.keys) - 1)

        # Value update.
        if i < len(self.keys) and self.keys[i] == key:
            self.values[i] = value
        else:
            self.keys.insert(i, key)
            self.values.insert(i, value)

        self.max_ = max(self.max_ or key, key)
        self.min_ = min(self.min_ or key, key)


if __name__ == '__main__':
    bst = ArithmeticBinarySearchTable()
    bst.put(4, 'X')
    bst.put(2, 'Y')
    bst.put(5, 'Z')
    bst.put(9, 'Q')
    bst.put(1, 'Z')
    bst.put(9, 'P')
    bst.put(1, 'W')
    print bst
