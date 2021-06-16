import networkx as nx

D = eval(input())

G = nx.Graph()
for i in D:
    G.add_node(i)

for i in D:
    for j in D[i]:
        G.add_edge(i, j)

L = []
S = []
for n in G:
    if (G.degree(n) == 1):
        L.append(n)
        l = G.neighbors(n)
        for m in l:
            S.append(m)

S = list(dict.fromkeys(S))
S = list(dict.fromkeys(S))
L.sort()
S.sort()
print("Liście:", *L, end='\n')
print("Supporty: ", end='')
for i in S:
    print(i, end=' ')