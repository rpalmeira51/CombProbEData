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

def test_excessess(components,graph, val):
    "Teste pra existencia de excesso apenas menor OU IGUAL a val."
    excessess = []
    
    for component in components:

        temp = 0
        
        for v in component:
            temp += sum(graph[v])
            
        if  temp/2-len(component) > val:
            return False
        
    return True

def prob_calc(n, tries):
    "Benchmark: 100x100 -> 0.8secs "
    cs = []
    for i in range(tries):
        g= generateRandomGraph(n)
        cs += [test_excessess(connected_components(g),g,1)]
    return sum(cs)/tries
