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

G = nx.from_numpy_matrix(adj_matrix, create_using=nx.DiGraph)

out_number = 0
in_number = 0
for n in G:
    if(G.out_degree(n) == 0):
        out_number += 1
    if(G.in_degree(n) == 0):
        in_number += 1
print("Ilość ujść:", out_number)
print("Ilość źródeł:",in_number)