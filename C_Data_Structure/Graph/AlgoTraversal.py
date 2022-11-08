from AdjacentList import Graph
from queue import Queue

class DataNode():
    def __init__(self):
        
        self.color = "white"
        self.d = float("inf")
        self.parent = None

def BFSAlgo(G,s):
    DataNodes = []
    for idx in range(8):
        DataNodes.append(DataNode())

    StartNode = DataNodes[s]
    StartNode.color = "grey"
    StartNode.distance = 0

    Q = Queue() 
    Q.put(s)
    cost = 0

    while (not Q.empty()):
        cur = Q.get()
        cost += 1
        print(f"Current Node:{cur}")
        for v in G.getAdjacentNode(cur):
            idx = list(v.keys())[0]
            
            n = DataNodes[idx] 
            if n.color == "white":
                n.color = "grey"
                n.distance = cost
                n.parent = cur
                Q.put(idx)
        
        DataNodes[cur].color = "black"

    return DataNodes

if __name__ == '__main__':
    g = Graph(8)
    g.AddCostEdge(0,1,1)
    g.AddCostEdge(1,5,1)
    g.AddCostEdge(0,4,1)
    g.AddCostEdge(2,5,1)
    g.AddCostEdge(5,6,1)
    g.AddCostEdge(2,6,1)
    g.AddCostEdge(2,3,1)
    g.AddCostEdge(3,6,1)
    g.AddCostEdge(3,7,1)
    g.AddCostEdge(6,7,1)

    dn = (BFSAlgo(g,1))
    for num,v in enumerate(dn):
        print(v.color,end=" ")
        print(v.d,end=" ")
        print(v.parent,end="")
        print()