import os 

def generateRandomGraph(size):
    graph = [[0]*size]*size
    for i in range(size):
        for j in range(size):
            p = int.from_bytes(os.urandom(4),"big")
            if(p >= 2**31):
                graph[i][j] = 0
            else:
                graph[i][j] = 1
    return graph

g= generateRandomGraph(10)
print(g)