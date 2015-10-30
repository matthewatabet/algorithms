class PriorityQueue(object):
    '''
    Zero indexed heap.
    '''

    def __init__(self):
        self.data = []

    def _exchange(self, i, j):
        t = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = t

    def _less(self, i, j):
        return self.data[i] < self.data[j]

    def _promote(self, i):
        while i > 0 and self._less(((i + 1)/2) - 1, i):
            self._exchange(((i + 1)/2) - 1, i)
            i = ((i + 1)/2) - 1

    def _demote(self, i):
        while ((i + 1) * 2) - 1 < len(self.data):
            j = ((i + 1) * 2) - 1
            if (j < len(self.data) - 1 and
                    self._less(j, j+1)):
                j += 1
            if self._less(j, i):
                break
            self._exchange(i, j)
            i = j

    def add(self, x):
        i = len(self.data)
        self.data.append(x)
        self._promote(i)

    def pop(self):
        ret = self.data.pop(0)
        if self.data:
            self._demote(0)
        return ret


def heap_sort(data):
    pq = PriorityQueue()
    for d in data:
        pq.add(d)
    ret = []
    for i in range(0, len(data)):
        ret.append(pq.pop())
    return ret

print heap_sort([4, 2, 13, 12, 9, 2, 9, 9])
print heap_sort([3, 4, 1, 1, 2, 2, 1, 1])
