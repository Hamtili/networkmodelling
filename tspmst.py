'''
Created on Jun 14, 2014

@author: marc
'''
from mst import mst
from eulercycle import euler
import networkx as nx
import copy

def tspmst(Graph):
    ET = mst(Graph)
    ETd = copy.deepcopy(ET)
    for v1, v2, e in ETd: 
        e['id'] = e['id'] + '.5'
    dmst = ET + ETd
    T = nx.MultiGraph()
    T.add_edges_from(dmst)
    C = euler(T)
    print 'spanning tree:', ET
    print 'Euler cycle: ', C
    
