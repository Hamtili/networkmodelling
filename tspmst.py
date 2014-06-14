'''
Created on Jun 14, 2014

@author: marc
'''
from mst import mst
from eulercycle import eulercycle

def tspmst(Graph):
    ET = mst(Graph)
    ET = ET | ET
    print ET
    
