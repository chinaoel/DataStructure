class DisjointSet:
    def __init__(self, elements):
        self.parents = [n for n in elements]
        self.count = len(self.parents)
        
    def find(self, element):
        n = self.parents[element]
        while self.parents[n] != n:
            n = self.parents[n]
        return n
        
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            self.parents[u] = v
            self.count -= 1

    def count_sets(self):
        return self.count