import networkx as nx
import numpy as np

def loadAdjacencyMatrix():
    row_data = input().split()
    matrix_size = len(row_data)
    matrix_output = np.empty([matrix_size, matrix_size], dtype=int)
    for row in range(matrix_size):
        for column in range(matrix_size):
            matrix_output[row][column] = row_data[column]
        if row < matrix_size - 1:
            row_data = input().split()
    return matrix_output

adj_matrix = loadAdjacencyMatrix()

G = nx.from_numpy_matrix(adj_matrix)

distance = []
for n in G:
    a = nx.shortest_path_length(G, source=0, target=n)
    distance.append(a)
print(*distance)