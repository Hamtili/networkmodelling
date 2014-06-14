'''
Created on Jun 14, 2014

@author: marc
'''
import copy

def mst(Graph):
    V = set(Graph.nodes())
    s = min(V)
    e = dict.fromkeys(V,float('NaN'))
    d = dict.fromkeys(V,float('Inf'))
    d[s] = 0
    S = set()
    ET = set()
    
    while S != V:
        VS = V - S
        tmp = copy.copy(d)
        map(tmp.__delitem__, S)
        u = min(tmp,key=tmp.get)
        S = S | set(u)
        nodes = set(Graph.neighbors(u)) & VS
        for v in nodes:
            edge = Graph.get_edge_data(u,v)
            if edge['weight'] < d[v]:
                d[v] = edge['weight']
                e[v] = (u,v)
                
    Vs = V - set(s)           
    for v in Vs:
        ET.add(e[v])
    return ET
        
    