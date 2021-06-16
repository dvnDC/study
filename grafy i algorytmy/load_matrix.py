import numpy as np

def loadInput():
    input_string = input().split()
    return input_string

def checkLength(input):
    input_length = len(input)
    return input_length

def makeMatrix():
    full_row_input = loadInput()
    matrix_columns = checkLength(full_row_input)
    matrix_rows = matrix_columns
    matrix_output = np.empty([matrix_rows, matrix_columns], dtype=int)
    for row in range(matrix_rows):
        for column in range(matrix_columns):
            matrix_output[row][column] = full_row_input[column]
        if row < matrix_columns-1:
            full_row_input = loadInput()
    return matrix_output

def checkGraphData(matrix_input):
    matrix_size = checkLength(matrix_input)
    vertex_number = matrix_size
    edge_number = 0
    for row in range(matrix_size):
        for column in range(matrix_size):
            if matrix_input[row][column] != 0:
                edge_number += 1
    edge_number = edge_number // 2
    return vertex_number, edge_number

def drawMatrix(matrix_input):
    matrix_size = checkLength(matrix_input)
    for y in range(matrix_size):
        print(*matrix_input[y], sep=' ')

def checkIfDirected(matrix_input):
    matrix_size = checkLength(matrix_input)
    directed_graph = False
    for mirror_mid_place in range(matrix_size):
        for count in range(mirror_mid_place, matrix_size, 1):
            if matrix_input[count][mirror_mid_place] != matrix_input[mirror_mid_place][count]:
                directed_graph = True
                break
    return directed_graph


output_matrix = makeMatrix()
output_matrix_length = checkLength(output_matrix)
if checkIfDirected(output_matrix) == True:
    print("Graf jest skierowany")
else:
    print("Graf jest nieskierowany")