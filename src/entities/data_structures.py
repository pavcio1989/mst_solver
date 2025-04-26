from src.entities.edges import Edge
from collections import defaultdict


class IndexedMinPQ:
    def __init__(self, n):
        self.N: int = n
        self.key: list = [None for i in range(self.N)]
        self.key_edges: list = [None for i in range(self.N)]
        self.pq: list = [None for i in range(self.N+1)]
        self.qp: list = [None for i in range(self.N)]
        self.total: int = 0

    def insert(self, i: int, edge: Edge, key):
        assert type(i) is int
        if i >= self.N:
            raise IndexError('index is out of the range of IndexedMinPQ.')
        if self.key[i] is not None:
            raise IndexError('index is already in the IndexedMinPQ.')
        self.total += 1
        self.key_edges[i] = edge
        self.key[i] = key
        self.pq[self.total] = i
        self.qp[i] = self.total
        self.__swim(self.total)

    def __swim(self,i):
        parent_i = i//2

        while parent_i > 0:
            key = self.key[self.pq[i]]
            parent_key = self.key[self.pq[parent_i]]
            if parent_key < key:
                break
            self.pq[i], self.pq[parent_i] = self.pq[parent_i], self.pq[i]
            self.qp[self.pq[i]] , self.qp[self.pq[parent_i]] = self.qp[self.pq[parent_i]],self.qp[self.pq[i]]
            i = parent_i
            parent_i = i // 2

    def delete_min(self):
        if not self.is_empty():
            out_index: int = self.pq[1]
            out_key: float = self.key[self.pq[1]]
            out_edge: Edge = self.key_edges[self.pq[1]]

            self.key[self.pq[1]] = None
            self.key_edges[self.pq[1]] = None
            self.qp[self.pq[1]] = None
            self.pq[1] = self.pq[self.total]
            self.qp[self.pq[1]] = 1
            self.pq[self.total] = None
            self.total -= 1
            self.__sink(1)
            return out_index, out_key, out_edge
        raise IndexError('IndexedMinPQ is Empty')

    def __sink(self, i):
        child_i = i * 2
        if child_i <= self.total:
            key = self.key[self.pq[i]]
            child_key = self.key[self.pq[child_i]]
            other_child = child_i + 1
            if other_child <= self.total:
                other_child_key =  self.key[self.pq[other_child]]
                if other_child_key < child_key:
                    child_i = other_child
                    child_key = other_child_key
            if child_key < key:
                self.pq[i], self.pq[child_i] = self.pq[child_i], self.pq[i]
                self.qp[self.pq[i]], self.qp[self.pq[child_i]] = self.qp[self.pq[child_i]], self.qp[self.pq[i]]
                self.__sink(child_i)

    def is_empty(self):
        return self.total == 0

    def contains(self, i):
        return self.key[i] is not None

    def decrease_key(self, i: int, edge: Edge, key):
        if i < 0 or i > self.N:
            raise IndexError('index i is not in the range')
        if self.key[i] is None:
            raise IndexError('index i is not in the IndexedMinPQ')
        assert type(i) is int

        if key < self.key[i]:
            self.key[i] = key
            self.key_edges[i] = edge
            self.__swim(self.qp[i])

    def increase_key(self, i, key):
        if i < 0 or i > self.N:
            raise IndexError('index i is not in the range')
        if self.key[i] is None:
            raise IndexError('index i is not in the IndexedMinPQ')
        assert type(i) is int
        assert key > self.key[i]
        self.key[i] = key
        self.__sink(self.qp[i])


class UnionFind:
    size: int = 0
    component_size = defaultdict()
    id = defaultdict()
    num_of_components = 0

    def __init__(self, size):
        if size < 0:
            raise Exception("Negative size is not allowed.")
        self.size = size
        self.num_of_components = size

        for i in range(size):
            self.component_size[i] = 1
            self.id[i] = i

    def find(self, p: int):
        # Find the root of component p
        root = self.id[p]
        while self.id[root] != root:
            root = self.id[root]

        # Compress the path leading back to the root.
        while p != root:
            _next = self.id[p]
            self.id[p] = root
            p = _next

        return root

    # Return whether the elements 'p' and 'q' are in the same components/set.
    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)

    # Unify the components/sets containing elements 'p' and 'q'
    def unify(self, p: int, q: int):

        if self.connected(p, q):
            return

        root_1 = self.find(p)
        root_2 = self.find(q)

        if self.component_size[root_1] < self.component_size[root_2]:
            self.component_size[root_2] += self.component_size[root_1]
            self.id[root_1] = root_2
            self.component_size[root_1] = 0
        else:
            self.component_size[root_1] += self.component_size[root_2]
            self.id[root_2] = root_1
            self.component_size[root_2] = 0

        self.num_of_components -= 1
