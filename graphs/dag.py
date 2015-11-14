'''
Check a directed graph for cycles.
'''


class DAG(object):

    def __init__(self):
        self.connections = {}

    def add(self, v, w):
        '''
        Add a connection between v and w.
        '''
        self.connections.setdefault(v, set()).add(w)

    def adj(self, v):
        return self.connections.get(v, [])

    def cycle(self, v=None, visited=None, stack=None):
        '''
        Returns True if the graph contains a cycle.
        '''
        if v is None:
            v = self.connections.keys()[0]
        if visited is None:
            visited = set()
        if stack is None:
            stack = set()
        visited.add(v)
        stack.add(v)
        cycle = False
        for w in self.adj(v):
            if w not in visited:
                cycle = cycle or self.cycle(w, visited=visited, stack=stack)
            elif w in stack:
                return True
        stack.remove(v)
        return cycle

if __name__ == '__main__':
    dag = DAG()
    dag.add('a', 'b')
    dag.add('b', 'c')
    dag.add('c', 'd')
    dag.add('c', 'e')
    print dag.cycle()

    dag = DAG()
    dag.add('a', 'b')
    dag.add('a', 'c')
    dag.add('c', 'd')
    dag.add('d', 'a')
    print dag.cycle()
