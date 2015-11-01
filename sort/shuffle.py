'''
Shuffle a singly-linked list.
'''

import random


class LinkedList(object):

    def __init__(self, v=None, data=None, i=0):
        self.v = v
        self.n = None
        if data is not None:
            self.v = data[i]
            if i < len(data) - 1:
                self.n = LinkedList(data=data, i=i+1)

    def __repr__(self):
        if self.n is None:
            return repr(self.v)
        return repr(self.v) + ' ' + repr(self.n)

    def __len__(self, n=0):
        if self.n is None:
            return 1
        return 1 + len(self.n)

    def split(self):
        '''
        Split the linked list in half. Return self and the new head of the
        second list.
        '''
        length = len(self)
        if length == 1:
            return self
        mid = length / 2
        node = self
        for i in range(0, mid):
            n = node.n
            if i == mid - 1:
                node.n = None
            node = n
        return self, node

    def extend(self, other):
        '''
        Concatonate other to the end of self.
        '''
        if self.n is None:
            self.n = other
        else:
            self.n.extend(other)
        return self


def shuffle(l):
    '''
    Shuffle linked list l.
    '''
    if len(l) == 1:
        return l
    a, b = l.split()
    a = shuffle(a)
    b = shuffle(b)

    if random.randint(0, 1) == 0:
        a.extend(b)
        return a
    else:
        b.extend(a)
        return b

l = LinkedList(data=[4, 7, 2, 3, 1])
l = shuffle(l)
print l
