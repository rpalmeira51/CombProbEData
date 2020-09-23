import os 
from collections import deque 
import numpy as np

def generateRandomGraph(n, Multigraph = True):
    
    graph = np.zeros((n,n))
    
    # sorteamos n//2 vezes um numero entre 0 e binom(n,2)[grafo] ou n**2[multigrafo]
    cs  = np.random.randint(0, n*(n-1)/2 - Multigraph*(n*(n-1)/2 - n**2), size=(n//2))    
    for c in cs:
        i,j = divmod(c,n)  # só tem que verificar esse mapa pro caso grafo pra ficar uniforme as arestas.
        graph[i][j] += 1
        graph[j][i] += 1    # somando 1 pra aceitar
    
    return graph


def next_vertix(color,n):
    for k in range(n):
        if k not in color:
            return k
    return False
    
def connected_components(graph):
    
    q = deque()
    components = []
    color = []
    n = len(graph)
    
    while len(color) < n:
        
        v = next_vertix(color,n)
        component = [v]
        q.append(v)
        color.append(v)
        
        while (q):
            v = q.popleft()
                
            for i in range(len(graph)):
                if(graph[v][i] >= 1 and (i not in color)):
                    
                    q.append(i)
                    component.append(i)
                    color.append(i)
                    
        components.append(component)
        
    return components

def check_excessess(components,graph):
    "retorna uma lista com o numero de vértices de cada componente e seus excessos."
    excessess = []
    
    for component in components:
        print(component)
        temp = 0
        for v in component:
            temp += sum(graph[v])
        if temp != 0:    #coloque pra ignorar vértices que não possuem arestas pra diminuir essa lista quando a matriz for mt grande
            excessess += [[len(component),temp/2]]
    return excessess

g= generateRandomGraph(10)
print(g)
print(connected_components(g))

check_excessess(connected_components(g),g)
