from AdjacentMatrix import Graph

def Floyd_Warshall(G, N):
    Cost = G.matrix.copy()

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if Cost[j][k] > (Cost[j][i] + Cost[i][k]):
                    Cost[j][k] = Cost[j][i] + Cost[i][k]
        
    print(Cost)


if __name__ == '__main__':
    N = 3
    Parents = [None]*N
    S = [False]*N
    G = Graph(N,Direct=True)
    '''
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
    '''
    G.DiCostEdge(0,1,4)
    G.DiCostEdge(1,0,6)
    G.DiCostEdge(1,2,2)
    G.DiCostEdge(0,2,11)
    G.DiCostEdge(2,0,3)

    #print(G.matrix[4])
    PathCostMatrix  = [float("inf")]*N

    Floyd_Warshall(G , N)