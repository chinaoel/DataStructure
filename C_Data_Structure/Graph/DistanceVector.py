from AdjacentMatrix import Graph

MAX_Route = 16
# MAX Routing Number in RIP Protocol

def DistanceVector(G):
    #initialize 0 (no link edge)  as infinite distance
    cost_matrix = G.matrix
    for i in range(len(cost_matrix)):
        for j in range(len(cost_matrix)):
            if cost_matrix[i][j] == 0 and (i != j):
                cost_matrix[i][j] = MAX_Route
            
    print("Before Communicating with Adjacent Router",cost_matrix)
    
    for vertex in range(len(cost_matrix)):
        # vertex x shares its vector
        connect = GetConnectedNode(cost_matrix[vertex])
        for con in connect:
            cost = cost_matrix[vertex,con]
            updated_cost_matrix_con = Relax(cost_matrix[vertex],cost_matrix[con],cost)
            cost_matrix[con] = updated_cost_matrix_con
    print("After Communicating with Adjacent Router\n",cost_matrix)
    
def Relax(cost_vector1, cost_vector2,cost):
    for i in range(len(cost_vector2)):
        if ((cost_vector1[i] + cost) < cost_vector2[i]):
            cost_vector2[i] = cost_vector1[i] + cost
    return cost_vector2

def GetConnectedNode(cost_matrix):
    return [num for num, s in enumerate(cost_matrix) if s != MAX_Route]

if __name__ == '__main__':
    G = Graph(7)
    G.AddEdge(0,1)
    G.AddEdge(0,2)
    G.AddEdge(0,4)
    G.AddEdge(0,5)
    G.AddEdge(1,2)
    G.AddEdge(2,3)
    G.AddEdge(3,6)
    G.AddEdge(5,6)
    G.PrintMatrix()
    DistanceVector(G)