
import networkx as nx
import numpy as np

def loadMatrix():
    row_data = input().split()
    matrix_size = len(row_data)
    matrix_output = np.empty([matrix_size, matrix_size], dtype=int)
    for row in range(matrix_size):
        for column in range(matrix_size):
            matrix_output[row][column] = row_data[column]
        if row < matrix_size - 1:
            row_data = input().split()
    return matrix_output

matrix = loadMatrix()
G = nx.from_numpy_matrix(matrix)

arr = []
length = dict(nx.all_pairs_dijkstra_path_length(G))
for i in G:
    for j in G:
        arr.append(length[i][j])
print(max(arr))