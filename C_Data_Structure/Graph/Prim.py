from AdjacentList import Graph

def PrimAlgo(G, s):
    '''Find minimum spanning tree using Prim's Algorithm G denotes graph and s denotes start'''
    VerticesList = []
    for v in range((N)):
        VerticesList.append({'key':float("inf"),"parent":None})
    
    VerticesList[s]['key'] = 0

    # Use Heap/FibHeap to Boost
    PriorityQ = [{num:s['key']} for num, s in enumerate(VerticesList)]    

    while PriorityQ:
        # extract min
        minima =  float("inf")
        index = None
        for num, ele in enumerate(PriorityQ):
            key = list(ele.values())[0]
            if key < minima:
                index = num
                minima = key
        pop = list( PriorityQ[index].keys() )[0]
        print("Priority Queue Dequeue",pop)
        PriorityQ.pop(index)
        neighbors = G.getAdjacentNode(index)
        for n in neighbors:
            node = list(n.keys())[0]
            cost = list(n.values())[0]
            Qeles = [list(s.keys())[0] for s in PriorityQ]
            #print(node)
            Origcost = [list(s.values())[0] for s in PriorityQ if list(s.keys())[0] == node]
            #print(f"Updated Node{node} Cost {cost}")
            #print(PriorityQ)
            if Origcost:
                Origcost = Origcost[0]
                if (node in Qeles) and (cost < Origcost):
                    
                    #print(f"Node:{node}, Cost:{cost}")
                    for idx, ele in enumerate(PriorityQ):
                        if list( ele.keys() )[0] == node:
                            PriorityQ[idx] = {node:cost}
                            
                    VerticesList[node]['key'] = cost
                    VerticesList[node]['parent'] = pop


if __name__ == '__main__':
    N = 6
    test = Graph(N)
    test.AddCostEdge(0,1,16)
    test.AddCostEdge(0,5,21)
    test.AddCostEdge(0,4,19)
    test.AddCostEdge(1,2,5)
    test.AddCostEdge(1,3,6)
    test.AddCostEdge(1,5,11)
    test.AddCostEdge(2,3,10)
    test.AddCostEdge(3,5,14)
    test.AddCostEdge(3,4,18)
    test.AddCostEdge(4,5,33)
    PrimAlgo(test,1)