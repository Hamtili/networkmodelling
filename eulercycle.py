'''
Created on Jun 14, 2014

@author: marc
'''
from collections import Counter

import math
import networkx as nx
import copy

def explore(v, Graph, AdjList, cur):
    e = cur[v]
    u = AdjList[Graph.nodes().index(v)][e % Graph.degree(v) / 2]
    C = [v, int(e), u]
    cur[v] = cur[v] + 1
    
    while u != v:
        e = cur[u]
        w = AdjList[Graph.nodes().index(u)][e % Graph.degree(u) / 2]
        C.extend((int(e), w))
        u = w
    
    return {'C': C, 'cur': cur}
    
def eulercycle(Graph):
    V = Graph.nodes()
    AdjList = Graph.adjacency_list()
    cur = dict.fromkeys(V, 1)
    
    C = [V[0]]
    v = V[0]
    i = 0
    run = True
    
    while run == True:
        print 'v: ', v
        while cur[v] <= Graph.degree(v) / 2:
            Explore = explore(v, Graph, AdjList, cur)
            Cadd = Explore['C']
            cur = Explore['cur']
            oldIndex = C.index(v)
            C[oldIndex:oldIndex] = Cadd
            C.pop(oldIndex + len(Cadd))
            print 'C: ', C
        i = i + 1
        print 'i: ', i
        v = C[2 * i - i]
        print 'v: ', v
        
        print 'V in C:', (len(C) + 1) / 2
        if (len(C) + 1) / 2 == i:
            run = False
            
    return C

def euler(Graph):
    K = []
    L = []
    V = Graph.nodes()
    used = dict.fromkeys(V, False)
    
    indexOld = 0
    
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
        [K.insert(i + index + indexOld, item) for i, item in enumerate(C)]
        indexOld = e[u] + indexOld
        
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
    
    

