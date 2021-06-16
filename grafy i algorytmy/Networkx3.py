import networkx as nx

G = nx.read_adjlist("lista.txt")
nodes_list = []

for v in G:
    if G.degree[v] == 2:
        nodes_list.append(v)

print("Wierzchołki stopnia 2:", *nodes_list, sep=' ')