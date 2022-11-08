from AdjacentMatrix import Graph
import numpy as np
from DisjointSet import DisjointSet
def KruskalAlgo(G, s):
    '''Find Minimum Spanning Tree using Kruskal Algorithm'''
    # find the minima edge
    spanning_tree_edge = 0
    matrix = G.matrix.copy()
    path_set = set()

    while spanning_tree_edge < (G.GetVerticesCount() -1):
        minima = float("inf")
        minima_indices = (None, None)
        for i in range(len(matrix)):
            for j in range((i)):
                if matrix[i][j] < minima:
                    minima = matrix[i][j]
                    minima_indices = (i,j)
        # (i, j) is the minima edge cost of all matrix
        i, j = minima_indices
        matrix[i][j] = np.inf
        matrix[j][i] = np.inf

        if DS.find(i) != DS.find(j):
            path_set.add((i,j))
            spanning_tree_edge += 1
            DS.union(i,j)
            #print(i,j)
        print(path_set)
    return path_set



if __name__ == '__main__':
    test = Graph(7,weight=True)
    DS = DisjointSet([s for s in range(7)])
    test.CostMatrix(0,1,28)
    test.CostMatrix(0,5,10)
    test.CostMatrix(1,2,16)
    test.CostMatrix(1,6,14)
    test.CostMatrix(2,3,12)
    test.CostMatrix(3,4,22)
    test.CostMatrix(3,6,18)
    test.CostMatrix(4,6,24)
    test.CostMatrix(4,5,25)
    test.PrintMatrix()
    KruskalAlgo(test,1)
