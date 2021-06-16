import networkx as nx

def hamilton(G):
    F = [(G, [list(G.nodes())[0]])]
    n = G.number_of_nodes()
    while F:
        graph, path = F.pop()
        confs = []
        neighbors = (node for node in graph.neighbors(path[-1]) if node != path[-1])
        for neighbor in neighbors:
            conf_p = path[:]
            conf_p.append(neighbor)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g,conf_p))
        for g, p in confs:
            if(len(p) == n):
                return p
            else:
                F.append((g,p))
    return None

M = []
n = 0

while True:
    try:
        line = input()
        if(not line):
            break
        M.append([])
        h = line.split()
        [M[n].append(int(j)) for j in h]
        n += 1
    except EOFError:
        break

G = nx.Graph()
for i in range(n):
    G.add_node(i)

for i in range(n):
    for j in range(n):
        if(M[i][j] != 0):
            G.add_edge(i,j)

if (not nx.is_connected(G)):
    print("Graf jest niespójny")
else:
    pth = hamilton(G)
    if(pth != None):
        if(G.has_edge(pth[0],pth[-1])):
            print("Graf jest hamiltonowski")
        else:
            print("Graf jest półhamiltonowski")
    else:
        if(n == 1 and G.has_edge(0,0)):
            print("Graf jest hamiltonowski")
        else:
            print("Graf nie jest hamiltonowski")