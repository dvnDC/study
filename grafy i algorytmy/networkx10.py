import networkx as nx
import numpy as np
from networkx.algorithms import tournament


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
H = nx.from_numpy_matrix(adj_matrix)

arr = tournament.hamiltonian_path(G)

if (not nx.is_connected(H)):
    print("Graf jest niespójny")
else:
    if arr:
        if(G.has_edge(arr[0],arr[-1])):
            print("Graf jest hamiltonowski")
            print(arr)
        else:
            print("Graf jest półhamiltonowski")
    else:
        if(G.has_edge(0,0)):
            print("Graf jest hamiltonowski")
        else:
            print("Graf nie jest hamiltonowski")
