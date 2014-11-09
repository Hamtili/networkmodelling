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
import matplotlib.pyplot as plt


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
        Graph[v1][v2]['color'] = 'red'
        cost = cost + costEdge
        Tour.append(v1)
    Tour.append(H[-1][1])   
    
    last = Tour[-1]
    first = Tour[0]
    costLastEdge = Graph.get_edge_data(last, first)['weight']
    Graph[first][last]['color'] = 'red'
    Tour.append(first)
    cost = cost + costLastEdge
    print 'Finished TSP calculation in ', time.time() - start_time
    print 'Tour: ', Tour
    print 'Cost: ', cost
    
    x = nx.get_node_attributes(Graph, 'x')
    y = nx.get_node_attributes(Graph, 'y')
    tmp = [x, y]
    pos = {}
    for k in x.iterkeys():
        pos[k] = tuple(d[k] for d in tmp)
    
    edges = Graph.edges()
    colors = [Graph[u][v]['color'] for u,v in edges]
    nx.draw(Graph, pos, edges=edges, edge_color=colors)
    plt.show()

    
