'''
Created on Jun 14, 2014

@author: marc
'''
from collections import Counter

import math
import networkx as nx
import copy

def euler(Graph):
    K = []
    L = []
    V = Graph.nodes()
    used = dict.fromkeys(V, False)
    
    Etmp = Graph.edges(data=True)
    E = []
    for v1, v2, e in Etmp:
        first = str(min(int(v1),int(v2)))
        second = str(max(int(v1),int(v2)))
        E.append((first, second, 'id ' + e['id']))
    new = dict.fromkeys(E, True)
    
    IncList = dict.fromkeys(V, [])
    for v in V:
        edges = []
        inc = Graph.edges(v, data=True)
        for v1, v2, d in inc:
            edges.append((v1, v2, 'id ' + d['id']))
        IncList[v] = edges
        
    e = dict.fromkeys(V, float('NaN'))
    
    s = V[0]
    used[s] = True
    L.append(s)
    
    trace(s, IncList, new, K, e, used, L)
    
    while L != []:
        u = L.pop()
        C = []
        trace(u, IncList, new, C, e, used, L)
        index = e[u]

        if len(C) > 0:
            v = C[0][0]
            index = K.index([(v1,v2,id) for v1,v2,id in K if v2 == v][0])
            [K.insert(i + 1 + index , item) for i, item in enumerate(C)]
        
    return K
           
def trace(v, IncList, new, C, e, used, L):
    while IncList[v] != []:
        firstEdge = IncList[v].pop(0)
        first = str(min(int(firstEdge[0]),int(firstEdge[1])))
        second = str(max(int(firstEdge[0]),int(firstEdge[1])))
        sortedFirstEdge = (first,second,firstEdge[2])

        
        if new[sortedFirstEdge] == True:
            C.append(firstEdge)
            
            if math.isnan(e[v]):
                e[v] = C.index(firstEdge)
            
            new[sortedFirstEdge] = False
            v = firstEdge[1]
            
            if used[v] == False:
                L.append(v)
                used[v] = True
    
    

