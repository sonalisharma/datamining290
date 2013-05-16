import networkx as nx
import numpy as np
G=nx.DiGraph()
G.add_nodes_from([5,2,11,7,9,8,10,3])
G.add_edges_from([(5,11),(11,10),(11,9),(11,2),(7,11),(7,8),(8,9),(3,10),(3,8)])
adjacencymatrix=nx.adjacency_matrix(G)
print adjacencymatrix
nx.write_adjlist(G,"adjacencylist.txt")


