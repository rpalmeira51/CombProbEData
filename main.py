import os 
from collections import deque 

def generateRandomGraph(size):
    #graph = [[0]*size]*size
    graph = [ [ 0 for y in range( size ) ] for x in range( size ) ]
    for i in range(size):
        for j in range(i+1,size):
            p = int.from_bytes(os.urandom(4),"big")
            #print(p)
            if(p >= 2**31):
                graph[i][j] = 1
                graph[j][i] = 1

    return graph

def bfs(graph):
    q = deque()
    q.append(0)
    component = [0]
    color = {0:True}
    while (q):
        v = q.popleft()
        for i in range(len(graph)):
            #print(i)
            if(graph[v][i] ==1 and (i not in color)):
                print(i)
                q.append(i)
                component.append(i)
                color[i] = True
    return component


g= generateRandomGraph(5)
print(g)
print(bfs(g))