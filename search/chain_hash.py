'''
Hash which implements separate chaining.
'''


class SequentialSearchArray(object):

    def __init__(self):
        self.keys = []
        self.values = []

    def __len__(self):
        return len(self.keys)

    def add(self, key, value):
        self.keys.append(key)
        self.values.append(value)

    def items(self):
        return zip(self.keys, self.values)

    def get(self, key):
        for i, k in enumerate(self.keys):
            if k == key:
                return self.values[i]
        return None


class SeparateChainingHash(object):

    def __init__(self, n):
        self.n = n
        self.arrays = [SequentialSearchArray() for i in range(0, n)]

    def __repr__(self):
        items = []
        for array in self.arrays:
            items.extend(array.items())
        return repr(items)

    def depth_range(self):
        lengths = [len(a) for a in self.arrays]
        return min(lengths), max(lengths)

    def hash(self, val):
        return (hash(val) & 0x7fffffff) % self.n

    def add(self, key, val):
        h = self.hash(key)
        self.arrays[h].add(key, val)

    def get(self, key):
        h = self.hash(key)
        return self.arrays[h].get(key)


if __name__ == '__main__':
    sch = SeparateChainingHash(3)
    sch.add(4, 'a')
    sch.add(5, 'b')
    sch.add(9, 'c')
    sch.add(15, 'd')
    sch.add(24, 'e')
    sch.add(17, 'y')
    print sch
    print sch.depth_range()
