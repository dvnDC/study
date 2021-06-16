import numpy as np


matrix_size = int(input())
if not matrix_size <= 0:
    zeros_matrix = np.zeros((matrix_size, matrix_size), dtype=int)
    for y in range(matrix_size):
            print(*zeros_matrix[y], sep=' ')
else:
    print("BLAD")


