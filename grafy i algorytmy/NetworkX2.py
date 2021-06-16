# import networkx as nx
# import ast
#
# graph_dict = ast.literal_eval(input())
# G = nx.Graph(graph_dict)
# I = nx.incidence_matrix(G)
# A = nx.adjacency_matrix(G)
#
# print(A.todense())
# print(I.todense())


from sys import stdin
import ast
import networkx as nx
graph_dict = ast.literal_eval(input())
G = nx.Graph(graph_dict)
D = nx.complement(G)
X = nx.adjacency_matrix(D)
K = nx.line_graph(G)
print(X.todense())
print(nx.adjacency_matrix(K).todense())