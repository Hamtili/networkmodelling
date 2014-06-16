'''
Created on Jun 14, 2014

@author: marc
'''
import networkx as nx
from tspmst import tspmst
import argparse

if __name__ == '__main__':
    pass

parser = argparse.ArgumentParser(description='Script for solving the TSP with MST heuristic.')
parser.add_argument('-f','--file', help='File in GEXF format describing the graph',required=True)

args = parser.parse_args();
graphFile = args.file

Graph = nx.read_gexf(graphFile)
print nx.minimum_spanning_tree(Graph).edges()
tspmst(Graph)

