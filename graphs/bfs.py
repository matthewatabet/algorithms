'''
Breadth-first search.
'''

class Graph(object):

    def __init__(self):
        self.v = {}

    def add(self, v, w):
        self.v.setdefault(v, set()).add(w)
        self.v.setdefault(w, set()).add(v)

    def adj(self, v):
        return self.v[v]


def breadth_first_search(g):

    memo = set()
    edges = {}
    stack = [g.v.keys()[0]]
    memo.add(stack[0])

    while stack:
        v = stack.pop()
        for w in g.adj(v):
            if w not in memo:
                memo.add(w)
                edges[w] = v
                stack.append(w)
    return edges


if __name__ == '__main__':
    g = Graph()
    g.add(1, 2)
    g.add(1, 3)
    g.add(1, 4)
    g.add(4, 5)
    g.add(5, 3)
    g.add(5, 2)
    print breadth_first_search(g)
