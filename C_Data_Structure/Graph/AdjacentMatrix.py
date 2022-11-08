import numpy as np 

class Graph():
    def __init__(self, v, weight=False, Direct=False):
        self.vertices = v
        if weight:
            self.matrix = np.array(np.ones((v,v)) * np.inf)
            print(type(self.matrix))
        else:
            self.matrix = np.zeros((v,v),dtype=int)
            print(type(self.matrix))
        if Direct:
            self.matrix = np.array(np.ones((v,v)) * np.inf)
            for i in range(self.matrix.shape[0]):
                self.matrix[i][i] = 0


    def AddEdge(self, v1, v2):
        if (v1 > (self.vertices-1)) or (v1 < 0) or  (v2 > (self.vertices-1)) or (v2 < 0):
            print("Index Out Of Range")
            raise IndexError
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1
    
    def CostMatrix(self, v1, v2, weight=10000):
        if (v1 > (self.vertices-1)) or (v1 < 0) or  (v2 > (self.vertices-1)) or (v2 < 0):
            print("Index Out Of Range")
            raise IndexError
        self.matrix[v1][v2] = weight
        self.matrix[v2][v1] = weight

    def DiCostEdge(self, v1, v2, cost):
        self.matrix[v1][v2] = cost
        
    def PrintMatrix(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def GetVerticesCount(self):
        return self.vertices

    def GetNeighbors(self,index):
        return self.matrix[index]
    
if __name__ == '__main__':
    test = Graph(5)
    test.AddEdge(0,1)
    test.AddEdge(2,3)
    test.AddEdge(3,4)
    test.AddEdge(4,0)
    test.PrintMatrix()