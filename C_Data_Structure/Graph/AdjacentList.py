

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def setparent(self, parent):
        self.parent = parent
    def setkey(self, key):
        self.key = key
class Edge():
    def __init__(self, data, cost):
        self.data = data
        self.cost = cost

class Graph():
    def __init__(self, V):
        self.vertices = V
        self.graph = [None] * self.vertices
        self.graphlist = []

    
    def AddEdge(self, src, dest):
        NewNode = Node(dest)
        NewNode.next = self.graph[src]
        self.graph[src] = NewNode

        NewNode2 = Node(src)
        NewNode2.next = self.graph[dest]
        self.graph[dest] = NewNode2
    
    def AddCostEdge(self, src, dest, cost):
        NewEdge = Edge(dest, cost)
        NewEdge.next = self.graph[src]
        self.graph[src] = NewEdge
        self.graphlist.append(NewEdge)

        NewEdge = Edge(src , cost)
        NewEdge.next = self.graph[dest]
        self.graph[dest] = NewEdge
    def PrintGraph(self):
        for v in range(len(self.graph)):
            temp = self.graph[v]
            
            if temp:
                print(f"Vertex {v}: ",end="")
                print(f"->{temp.data}",end="")
                while temp.next:
                    
                    temp = temp.next
                    print(f"->{temp.data}",end="")
                print("")
            else:
                print(f"Vertex {v}:")

    def getVertices(self):
        return self.graphlist        
    

    def getAdjacentNode(self,index):
        neighbors = []
        neighborlist = self.graph[index]
        if neighborlist:
            neighbors.append({neighborlist.data:neighborlist.cost})
            while neighborlist.next:
                neighborlist = neighborlist.next
                neighbors.append({neighborlist.data:neighborlist.cost})
        return neighbors

if __name__ == '__main__':
    test = Graph(6)
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

    test.PrintGraph()
