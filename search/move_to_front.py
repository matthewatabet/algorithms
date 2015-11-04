'''
Unordered key-value store which uses a move-to-front heuristic. Whenever a key
is retrieved, it's moved to the head of the search array.
'''


class MoveToFront(object):

    def __init__(self):
        self.keys = []
        self.values = []

    def __repr__(self):
        t = ''
        for i in range(0, len(self.keys)):
            t += str(self.keys[i]) + '=' + str(self.values[i]) + ' '
        return t

    def add(self, key, value):
        self.keys.append(key)
        self.values.append(value)

    def get(self, key):
        i = 0
        value = None
        while i < len(self.keys) and self.keys[i] != key:
            i += 1
        if i >= len(self.keys):
            return None
        value = self.values[i]

        # shift left
        for j in range(i, 0, -1):
            self.keys[j] = self.keys[j - 1]
            self.values[j] = self.values[j - 1]
        self.values[0] = value
        self.keys[0] = key

        return value


if __name__ == '__main__':
    mtf = MoveToFront()
    mtf.add('x', 5)
    mtf.add('y', 3)
    mtf.add('z', 2)
    mtf.add('q', 4)
    print mtf
    print mtf.get('q')
    print mtf.get('z')
    print mtf
