import networkx as nx 
import matplotlib.pyplot as plt
G=nx.DiGraph()

e=[('1','5',1),('2','5',1),('3','5',1),('5','7',1),('4','6',1),('5','8',1),('6','9',1)]
G.add_weighted_edges_from(e)

print(nx.astar_path_length(G,'1','8',heuristic=None,weight='weight' ))
print(nx.astar_path_length(G,'3','5',heuristic=None,weight='weight' ))
print(nx.astar_path_length(G,'4','6',heuristic=None,weight='weight' ))


nx.draw(G)
plt.savefig("path.png")
