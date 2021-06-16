def loadAdjacencyList():
    node = []
    edge = []
    matrix = []
    row_data = input().split()
    while row_data:
        try:
            node.append(row_data[0])
            edge.append(row_data[1:])
            row_data = input().split()
        except EOFError:
            break
    return node, edge

def convertAdjList(nodes, edges):
    maxNodes = len(nodes)
    matrix = []
    for o in range(maxNodes):
        newArr = []
        for x in range(maxNodes):
            checkNumber = True
            for y in range(len(edges[o])):
                if int(edges[o][y]) == int(x+1) or int(o) == int(x):
                    checkNumber = False
                    break
            if checkNumber:
                newArr.append(x+1)
        matrix.append(newArr)
    return matrix

def makeComplAdjList(adjacency_list):
    complAdjList = {}
    for node in adjacency_list.keys():
        temp_dict = {node: []}
        for edge in range(len(adjacency_list[node])):
            for x in range(len(adjacency_list)):
                if int(edge) != x:
                    temp_dict[node].append(x)
        complAdjList.update(temp_dict)
    return complAdjList


node, edge = loadAdjacencyList()
newArr = convertAdjList(node,edge)
for y in range(len(node)):
    print((y+1),*newArr[y], sep=' ')