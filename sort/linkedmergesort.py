'''
Bottom up mergesort for linked list.
'''


class LinkedList(object):

    def __init__(self, v=None):
        self.v = v
        self.n = None

    def __repr__(self):
        if self.n is None:
            return repr(self.v)
        else:
            return repr(self.v) + ' => ' + repr(self.n)

    def __len__(self):
        if self.n is None:
            return 1
        return 1 + len(self.n)

    def add(self, v):
        if self.n is None:
            self.n = LinkedList(v)
        else:
            self.n.add(v)

    def split(self):
        mid = len(self) / 2
        l = self
        for i in range(0, mid):
            n = l.n
            if i == mid - 1:
                l.n = None
            l = n
        return self, l

    @classmethod
    def create(cls, data):
        l = LinkedList(data[0])
        for v in data[1:]:
            l.add(v)
        return l


def merge(list_a, list_b):
    '''
    Merge two ordered linked lists.
    '''
    head = None
    current = None
    while list_a or list_b:
        to_add = None
        if list_b is None and list_a is not None:
            to_add = list_a
            list_a = list_a.n
        elif list_a is None and list_b is not None:
            to_add = list_b
            list_b = list_b.n
        elif list_a.v < list_b.v:
            to_add = list_a
            list_a = list_a.n
        else:
            to_add = list_b
            list_b = list_b.n
        if head is None:
            head = to_add
            current = head
        else:
            current.n = to_add
            current = to_add
    return head


def sort(l):
    if len(l) == 1:
        return l
    a, b = l.split()
    a = sort(a)
    b = sort(b)
    return merge(a, b)

l = merge(LinkedList.create([1, 3, 4, 5, 5]),
          LinkedList.create([0, 1, 1, 4]))
print l

print sort(LinkedList.create([6, 2, 2, 5, 3, 2]))
