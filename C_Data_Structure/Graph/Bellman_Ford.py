from AdjacentMatrix import Graph
import math

def BellmanFord(G,  s , N):
    Dist = G.matrix[s]
    for i in range(N-1):
        for j in range(len(Dist)):
            for k in range(len(Dist)):
                adjacent = G.matrix[k][j]
                if math.isfinite(adjacent):
                    if Dist[j] > (Dist[k] + G.matrix[k][j]):
                        
                        Dist[j] = (Dist[k] + G.matrix[k][j])
    
    print(Dist)






if __name__ == '__main__':
    N = 8
    Parents = [None]*N
    S = [False]*N
    G = Graph(N,Direct=True)
    G.DiCostEdge(1,0,300)
    G.DiCostEdge(2,1,800)
    G.DiCostEdge(3,2,1200)
    G.DiCostEdge(4,3,1500)
    G.DiCostEdge(5,3,1000)
    G.DiCostEdge(4,5,250)
    G.DiCostEdge(5,6,900)
    G.DiCostEdge(6,7,1000)
    G.DiCostEdge(5,7,1400)
    G.DiCostEdge(2,0,1000)
    G.DiCostEdge(7,0,1700)

    #print(G.matrix[4])
    PathCostMatrix  = [float("inf")]*N

    BellmanFord(G, 4, N)