'''
Depth-first graph traversal.
'''


class UndirectedGraph(object):

    def __init__(self):
        self.v = {}  # map vertices to neighbors

    def add(self, x, y):
        self.v.setdefault(x, set()).add(y)
        self.v.setdefault(y, set()).add(x)

    def adj(self, x):
        return self.v[x]


def depth_first_search(graph, current=None, visited=None):
    if visited is None:
        visited = set()
    if current is None:
        current = graph.v.keys()[0]
    visited.add(current)
    order = [current]
    for v in graph.adj(current):
        if v not in visited:
            order.extend(depth_first_search(graph, v, visited))
    return order


if __name__ == '__main__':
    g = UndirectedGraph()
    g.add('a', 'b')
    g.add('b', 'c')
    g.add('c', 'e')
    g.add('c', 'f')
    g.add('c', 'g')
    g.add('g', 'h')
    print depth_first_search(g)
