from decimal import Decimal, getcontext, ROUND_HALF_UP
import numpy as np
from collections import defaultdict


class Graph():

    def __init__(self):
        ### Graph data
        self.adjacency_list = defaultdict(list)
        self.adjacency_matrix = 0

        self.n_vertices = 0
        self.parents = {}
        self.size = {}

        ### Rounding options (decimal)
        dc = getcontext()
        dc.rounding = ROUND_HALF_UP

        ### Actions
        self.loadAdjacencyList()
        self.printGraphData()


    def printAdjMatrix(self, adjacency_matrix):
        matrix_size = len(adjacency_matrix[0])
        for y in range(matrix_size):
            print(*adjacency_matrix[y], sep=' ')

    def printAdjList(self, adjacency_list):
        for vertex, edge in adjacency_list.items():
            if type(edge) != int:
                print(vertex, *edge, sep=' ')
            else:
                print(vertex, edge)

    def loadAdjacencyList(self):
        row_data = input().split()
        while row_data:
            try:
                self.adjacency_list[row_data[0]] = row_data[1:]
                row_data = input().split()
                self.n_vertices += 1
            except EOFError:
                break

    def loadAdjacencyMatrix(self):
        row_data = input().split()
        matrix_size = len(row_data)
        matrix_output = np.empty([matrix_size, matrix_size], dtype=int)
        for row in range(matrix_size):
            for column in range(matrix_size):
                matrix_output[row][column] = row_data[column]
            if row < matrix_size - 1:
                row_data = input().split()
        self.adjacency_matrix = matrix_output
        return matrix_output

    def loadVertexCheck(self):
        vertex = int(input())
        adjacency_vertices = []
        if vertex <= 0 or vertex > len(self.adjacency_matrix):
            print("BŁĄD")
        else:
            for column in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[vertex-1][column] == 1:
                    adjacency_vertices.append(int(column+1))
        return adjacency_vertices

    def checkVerticesDegree(self):
        vertices_dgr = []
        for vertex, edge in self.adjacency_list.items():
            vertices_dgr.append(len(self.adjacency_list[vertex]))
        return vertices_dgr

    def loadNewVertex(self):
        vertex_new_row = input().split()
        vtx = []
        for column in range(len(vertex_new_row)-1):
            vtx.append(int(vertex_new_row[column]))
        new_row = np.array(vtx)
        self.adjacency_matrix = np.vstack([self.adjacency_matrix, new_row])
        vtx.append(int(vertex_new_row[-1]))
        self.adjacency_matrix = np.c_[self.adjacency_matrix,vtx]

    def checkAverageEdgesList(self):
        vertex_max = len(self.adjacency_list)
        edges_max = 0
        for vertex, edge in self.adjacency_list.items():
            edges_max += len(edge)
        return (edges_max / vertex_max)

    def checkDegreeEdgesOut(self, adjacency_list):
        max_vertex = int(list(adjacency_list.keys())[-1])
        degree_array = []
        for vertex, edge in adjacency_list.items():
            counter = 0
            for vtx in range(max_vertex):
                for edgenr in range(len(edge)):
                    if (list(adjacency_list.keys())[vtx]) == edge[edgenr]:
                        counter += 1
            degree_array.append(len(edge))
        return degree_array

    def checkMatrixEdgesIn(self, adjacency_matrix):
        matrix_size = len(adjacency_matrix[0])
        degree_array = []
        for column in range(matrix_size):
            counter = 0
            for row in range(matrix_size):
                if adjacency_matrix[row][column] == 1:
                    counter += 1
            degree_array.append(counter)
        return degree_array

    def convertAdjacencyMatrixToList(self, adjacency_matrix):
        matrix_size = len(adjacency_matrix[0])
        vertex = 1
        for row in range(matrix_size):
            for column in range(matrix_size):
                if adjacency_matrix[row][column] != 0:
                    self.append_value(self.adjacency_list, vertex, column + 1)
            if vertex not in self.adjacency_list.keys():
                self.adjacency_list[vertex] = ''
            vertex += 1

    def convertAdjacencyListToMatrix(self, adjacency_list):
        row_data = list(adjacency_list.keys())[-1]
        keys_length = len(list(adjacency_list.keys()))
        matrix_size = int(row_data)
        matrix_output = np.zeros([matrix_size, matrix_size], dtype=int)
        for vertex, edge in adjacency_list.items():
            if int(vertex) > keys_length:
                break
            for edgenr in range(len(edge)):
                matrix_output[int(vertex)-1][(int(edge[edgenr]))-1] = 1
        return matrix_output

    def deleteVertex(self):
        vertex = int(input())
        if vertex <= 0 or vertex > len(self.adjacency_matrix):
            print("BŁĄD")
        else:
            self.adjacency_matrix = np.delete(self.adjacency_matrix, vertex-1, 0)
            self.adjacency_matrix = np.delete(self.adjacency_matrix, vertex-1, 1)
            self.printAdjMatrix(self.adjacency_matrix)

    def checkGraphExists(self, vertices_degree):
        while True:
            vertices_degree = sorted(vertices_degree, reverse=True)
            if int(vertices_degree[0]) == 0 and vertices_degree[len(vertices_degree) - 1] == 0:
                return True
            vertex = int(vertices_degree[0])
            vertices_degree = vertices_degree[1:]
            if vertex > len(vertices_degree):
                return False
            for i in range(vertex):
                vertices_degree[i] = int(vertices_degree[i])
                vertices_degree[i] -= 1
                if vertices_degree[i] < 0:
                    return False

    def printDecimal(self, float_number):
        d = Decimal(float_number)
        d = round(d, 2)
        if d%2 != 1:
            print(Decimal(d).normalize())
        else:
            print("{:.1f}".format(d))

    def append_value(self, dict_obj, key, value):
        if key in dict_obj:
            if not isinstance(dict_obj[key], list):
                dict_obj[key] = [dict_obj[key]]
            dict_obj[key].append(value)
        else:
            dict_obj[key] = value

    def checkIfCompleteGraph(self, number_of_edges):
        max_vtx = len(self.adjacency_list.keys())
        return number_of_edges == (max_vtx*(max_vtx-1))/2

    def checkIfGraphIsPath(self):
        max_nodes = []
        for vertex, edge in self.adjacency_list.items():
            max_nodes.append(max(self.adjacency_list[vertex]))
        for i in range((len(max_nodes)-2),0,-1):
            if not (int(max_nodes[i])-int(max_nodes[i-1])) == 1:
                return False
        return True

    def checkIfGraphIsTree(self):
        for vertex in self.adjacency_list.keys():
            neighbours = len(self.adjacency_list[vertex])
            if neighbours > 3:
                return False
        return True

    def checkIfGraphIsCycle(self, edges, vertexes, vertex_degree):
        last_vtx = str(len(self.adjacency_list.keys()))
        values_len = len(self.adjacency_list["1"])
        if edges >= vertexes:
            if int(self.adjacency_list["1"][values_len-1]) == int(last_vtx):
                if int(self.adjacency_list[last_vtx][0]) == 1:
                    for vtx in vertex_degree:
                        if vtx < 2:
                            return False
                    return True
        else:
            return False

    def printGraphData(self):
        ilosc_wierzcholkow = len(self.adjacency_list.keys())
        ilosc_krawedzi = 0
        for vertex in self.adjacency_list.keys():
            ilosc_krawedzi += len(self.adjacency_list[vertex])
        ilosc_krawedzi = int(ilosc_krawedzi / 2)
        stopnie_wierzcholkow = self.checkVerticesDegree()
        sredni_stopien = self.checkAverageEdgesList()
        last_ans = True
        print("Ilość wierzchołków:", ilosc_wierzcholkow)
        print("Ilość krawędzi:", ilosc_krawedzi)
        print("Stopnie wierzchołków:", *stopnie_wierzcholkow, sep=' ')
        if not sredni_stopien % 1 != 0:
            print("Średni stopień:", "{:.0f}".format(sredni_stopien))
        else:
            print("Średni stopień:", sredni_stopien)
        if self.checkIfGraphIsPath():
            print("Jest to ścieżka.")
            last_ans = False
        if self.checkIfCompleteGraph(ilosc_krawedzi):
            print("Jest to graf pełny.")
            last_ans = False
        elif self.checkIfGraphIsCycle(ilosc_krawedzi, ilosc_wierzcholkow, stopnie_wierzcholkow):
            print("Jest to cykl.")
            last_ans = False
        elif self.checkIfGraphIsTree():
            print("Jest to drzewo.")
            last_ans = False
        if last_ans:
            print("Graf nie należy do żadnej z podstawowych klas.")



if __name__ == "__main__":
    Graph()
