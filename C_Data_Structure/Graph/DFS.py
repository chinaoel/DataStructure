from AdjacentMatrix import Graph
from queue import Queue

def DFS(G, start):
    global visit_vertex
    visit_vertex[start] = True
    print(f"Visit Vertex {start}")
    for num , row in enumerate( G.matrix[start] ):
        if row == 1:
            if not visit_vertex[num]:
                DFS(G,num)


def BFS(G, start):
    global visit_vertex
    visit_vertex[start] = True
    # start point enqueue
    Q = Queue()
    Q.put(start)
    while Q.qsize() != 0:
        vertex = Q.get()
        
        
        for num , row in enumerate( G.matrix[vertex] ):
            #print(f"vertex {num}, row: {G.matrix[vertex]}")
            if row == 1:
                if not visit_vertex[num]:
                    visit_vertex[vertex] = True
                    print(f"Visit vertex {num}")
                    Q.put(num)



    


if __name__ == '__main__':
    N = 8
    visit_vertex = [False]*N
    G = Graph(N)
    G.AddEdge(0,1)
    G.AddEdge(0,2)
    G.AddEdge(1,3)
    G.AddEdge(1,4)
    G.AddEdge(2,5)
    G.AddEdge(2,6)
    G.AddEdge(3,7)
    G.AddEdge(4,7)
    G.AddEdge(5,7)
    G.AddEdge(6,7)
    BFS(G, 0)
    print(visit_vertex)
    
