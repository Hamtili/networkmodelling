'''
Created on Jun 14, 2014

@author: marc
'''
from mst import mst
from eulercycle import euler
import networkx as nx
import copy
import collections
import time
import cProfile
import re


def tspmst(Graph):
    start_time = time.time()
    ET = mst(Graph)
    print 'Finished MST calculation in ', time.time() - start_time
    ETd = copy.deepcopy(ET)
    for v1, v2, e in ETd: 
        e['id'] = e['id'] + '.5'
    dmst = ET + ETd

    T = nx.MultiGraph()
    T.add_edges_from(dmst)
    start_time = time.time()
    C = euler(T)
    print 'Finished eulercycle calculation in ', time.time() - start_time
    T = []
    ET = []
    ETd = []
    H = []
    visited = collections.OrderedDict() 
        
    for v1, v2, eid in C:
        visited[v1] = False
        
    skip = False
    skipUntil = 'N'
    start_time = time.time()
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
                shortcut = [k for k, v in visited.iteritems() if v == False][0]
                v1 = edge[0]
                H.append((edge[0], shortcut, 'id 0'))
                visited[shortcut] = True
                skip = True
                skipUntil = shortcut
        else: 
            break
    
    Tour = []
    cost = 0
    for v1, v2, eid  in H:
        costEdge = Graph.get_edge_data(v1, v2)['weight']
        cost = cost + costEdge
        Tour.append(v1)
        
    
    last = Tour[-1]
    first = Tour[0]
    costLastEdge = Graph.get_edge_data(last, first)['weight']
    Tour.append(first)
    cost = cost + costLastEdge
    print 'Finished TSP calculation in ', time.time() - start_time
    print 'Tour: ', Tour
    print 'Cost: ', cost

    
