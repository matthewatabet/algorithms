'''
Depth first paths.
'''


class Graph(object):

    def __init__(self):
        self.v = {}

    def add(self, v, w):
        self.v.setdefault(v, set()).add(w)
        self.v.setdefault(w, set()).add(v)

    def adj(self, v):
        return self.v[v]


def depth_first_paths(g, v=None, memo=None, edges=None):
    if v is None:
        v = g.v.keys()[0]
    if memo is None:
        memo = set()
    memo.add(v)
    for w in g.adj(v):
        if w not in memo:
            edges[w] = v
            depth_first_paths(g, w, memo=memo, edges=edges)


if __name__ == '__main__':
    g = Graph()
    g.add(0, 2)
    g.add(0, 1)
    g.add(2, 1)
    g.add(2, 3)
    g.add(2, 4)
    g.add(3, 4)
    g.add(3, 5)
    g.add(5, 0)
    edges = {}
    depth_first_paths(g, edges=edges)
    print edges
