'''
Union find algorithm.
'''


class UnionFind(object):

    def __init__(self, n):
        self.parents = range(0, n)
        self.sizes = [1] * n

    def find(self, v):
        '''
        Return the id of the tree which vertex v belongs to.
        '''
        while self.parents[v] != v:
            v = self.parents[v]
        return v

    def union(self, v, w):
        '''
        Add a connection between v and w.
        '''
        v_tree = self.find(v)
        w_tree = self.find(w)

        if v_tree == w_tree:
            return

        v_size = self.sizes[v_tree]
        w_size = self.sizes[w_tree]

        if v_size < w_size:
            self.parents[v_tree] = self.parents[w_tree]
            self.sizes[w_tree] += self.sizes[v_tree]
        else:
            self.parents[w_tree] = self.parents[v_tree]
            self.sizes[v_tree] += self.sizes[w_tree]

    def connected(self, v, w):
        '''
        Returns True if vertices v and w belong to the same graph island.
        '''
        return self.find(v) == self.find(w)


if __name__ == '__main__':
    uf = UnionFind(10)

    uf.union(1, 2)
    uf.union(4, 5)
    uf.union(5, 6)
    uf.union(4, 7)

    print uf.connected(5, 7)
    print uf.connected(1, 2)
    print uf.connected(1, 5)
