'''
Linear probing hash with lazy delete.
'''


class LinearProbingHash(object):

    def __init__(self, n):
        self.m = 0
        self.n = n
        self.keys = [None] * n
        self.values = [None] * n

    def __repr__(self):
        t = ''
        for k, v in zip(self.keys, self.values):
            if v is None:
                continue
            t += '%s=%s ' % (k, v)
        return t

    def hash(self, key):
        return hash(key) & 0x7fffffff % self.n

    def _resize(self):
        keys = self.keys[:]
        values = self.values[:]
        self.keys = [None] * self.n
        self.values = [None] * self.n
        for key, value in zip(keys, values):
            self.add(key, value)

    def resize(self):
        if self.m > self.n / 2:
            self.n *= 2
            self._resize()
        elif self.m < self.n / 4:
            self.n /= 2
            self._resize()

    def add(self, key, value):
        i = self.hash(key)
        while self.values[i] is not None:
            i += 1
        self.keys[i] = key
        self.values[i] = value
        self.m += 1
        self.resize()

    def delete(self, key):
        i = self.hash(key)
        while (self.keys[i] is not None and
               self.key[i] != key):
            i += 1
        if self.key[i] == key:
            self.values[i] = None
        self.m -= 1
        self.resize()

    def get(self, key):
        i = self.hash(key)
        while (self.keys[i] is not None
               and self.keys[i] != key):
            i += 1
        if self.key[i] == key:
            return self.values[i]
        return None


if __name__ == '__main__':
    h = LinearProbingHash(1)
    h.add(5, 'a')
    h.add(7, 'b')
    h.add(2, 'c')
    h.add(6, 'd')
    h.add(7, 'e')
    h.delete(7)
    print h
