'''
Created on Jun 14, 2014

@author: marc
'''
from mst import mst
from eulercycle import euler
import networkx as nx
import copy
import collections
from __builtin__ import False

def tspmst(Graph):
    ET = mst(Graph)
    ETd = copy.deepcopy(ET)
    for v1, v2, e in ETd: 
        e['id'] = e['id'] + '.5'
    dmst = ET + ETd
    T = nx.MultiGraph()
    T.add_edges_from(dmst)
    C = euler(T)
    
    print 'MSTnx:', nx.minimum_spanning_tree(Graph).edges()
    print 'MST: ', ET

    H = []
    visited = collections.OrderedDict() 
        
    for v1,v2, id in C:
        visited[v1] = False
        
    skip = False
    skipUntil = 'N'
    
    print 'Euler: ', C
    
    for edge in C:
        if skip == True and edge[0] != skipUntil:
            continue
        
        elif skip == True and edge[0] == skipUntil:
            skip = False
            skipUntil = 'N'
        
        if any('False' in str(v) for v in visited.values()):
            if visited[edge[0]] == False or visited[edge[1]] == False:
                H.append(edge)
                visited[edge[0]] = True
                visited[edge[1]] = True
            else:
                shortcut = [k for k,v in visited.iteritems() if v == False]
                v1 = edge[0]
                minCost = float('Inf')
                minCostV = shortcut[0]
                for v2 in shortcut:
                    cost = Graph.get_edge_data(v1,v2)['weight']
                    if cost < minCost:
                        minCost = cost
                        minCostV = v2

                H.append((edge[0],minCostV,'id 0'))
                visited[minCostV] = True
                skip = True
                skipUntil = minCostV
        else: 
            break
    
    Tour = []
    cost = 0
    for v1, v2, id in H:
        Tour.append((v1,v2))
        cost = cost + Graph.get_edge_data(v1,v2)['weight']
    
    last = Tour[-1][1]
    first = Tour[0][0]
    Tour.append((last,first))
    cost = cost + Graph.get_edge_data(last,first)['weight']
    print 'Tour: ', Tour
    print 'Cost: ', cost
    
