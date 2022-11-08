from AdjacentMatrix import Graph
import numpy as np
import math
import time

def Dijkstra(G, s):
    global Q,S
    '''Find the shortest path from one node to all nodes using Dijkstra algorithm'''

    Initialize(G, s)
    Confirmed = set()
    
    Q = []
    for i in range(N):
        Q.append({i:G.matrix[s][i]})
    
    while Q:
        time.sleep(1)
        minima = float("inf")
        for idx, ele in enumerate(Q):
            val = list(ele.values())[0]
            if val < minima:
                minima = val
                key = list(ele.keys())[0]

        for idx, i in enumerate( Q ):
            if list( i.keys() )[0] == key:
                Q.pop(idx)
        print("Queue",Q)
        S[key] = True
        Confirmed.add(key)
        # find node's neighbor
        for num, each in enumerate(G.matrix[key]):
            if math.isfinite(each) and not S[num]:
                Relax(key,num,minima)


def Initialize(G, s):
    global PathCostMatrix
    PathCostMatrix[s] = 0
    

def Relax(key, num, new_path_cost):
    print(f"Relaxing {key} and {num}")
    global Q
    orig_cost = 0
    for i, ele in enumerate(Q):
        if list( ele.keys() )[0] == num:
            orig_cost = list( ele.values() )[0]
            idx = i
    print(f"orig cost{orig_cost}, new_cost{new_path_cost+ G.matrix[key, num]}")

    if (orig_cost) > (new_path_cost + G.matrix[key, num]):
        
        Q[idx] =  {num:(new_path_cost + G.matrix[key, num])}
        Parents[num] = key
    print("Queue after relax", Q)


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

    Dijkstra(G, 4)