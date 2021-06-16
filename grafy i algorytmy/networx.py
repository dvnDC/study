import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

G.add_edge(0,1)
G.add_edge(0,4)
G.add_edge(1,5)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(2,5)
G.add_edge(3,4)
G.add_edge(3,5)

H = G
H.remove_node(0)
H.remove_node(4)


plt.figure(1, figsize=(10.24,5.76))
nx.draw(H,node_size=4,with_labels=1)
plt.show()

print(G.nodes())