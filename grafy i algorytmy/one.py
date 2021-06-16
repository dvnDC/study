from sys import stdin

def create_matrix():
    input = stdin.read()
    data = input.splitlines()
    matrix = []

    for i in range(len(data)):
        matrix.append(data[i].split())

    index = int(matrix[len(matrix) - 1][0])
    del (matrix[len(matrix) - 1])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix, index


def check_data(matrix, index):
    if index > len(matrix) or index < 1:
        return False
    for i in range(len(matrix)):
        if matrix[i][0] != i + 1:
            return False
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j + 1] < 1:
                return False
            if matrix[i][j + 1] > len(matrix):
                return False
    return True


def visit_vertex(data, visited, matrix):
    visited.append(data)
    for i in data['neighbors']:
        if matrix[i - 1] not in visited:
            visit_vertex(matrix[i - 1], visited, matrix)
    return visited


def get_info(matrix, index):
    if not check_data(matrix, index):
        print("BŁĄD")
    else:
        data = get_matrix_dict(matrix)
        order_data = visit_vertex(data[index - 1], [], data)
        order = []
        for value in order_data:
            order.append(str(value['vertex']))
        if len(order) == len(matrix):
            output = "Porządek DFS:"
            for i in order:
                output = output + ' ' + i
            print(output)
            print("Graf jest spójny")
        else:
            print("Graf jest niespójny")


def get_matrix_dict(matrix):
    matrix_dict = []
    for i in range(len(matrix)):
        data = []
        for j in range(len(matrix[i]) - 1):
            data.append(matrix[i][j + 1])
        matrix_dict.append({'vertex': (i + 1), 'neighbors': data})
    return matrix_dict


data, index = create_matrix()
get_info(data, index)