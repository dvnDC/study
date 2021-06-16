import networkx as nx


# wczytanie pierwszej lini wiedzac ze macierz sasiedztwa jest N x N
line = input()
line = line.split(" ")
getLen = len(line)
matryca = []
matryca.append(line)

# wczytanie pozostałych lini
for i in range(getLen - 1):
    line = input()
    line = line.split(" ")
    matryca.append(line)

# zamiana str to int
for i in range(getLen):
    for j in range(getLen):
        matryca[i][j] = int(matryca[i][j])

#zmiana w slownik
slownik = {}
for i in range(len(matryca)):
    temp = []
    for j in range(len(matryca[i])):
        if matryca[i][j] != 0:
            temp.append(j)
    slownik[i] = temp

G = nx.from_dict_of_lists(slownik)
odl = []
for i in range(len(matryca)):
    a= nx.shortest_path_length(G, source=0, target=i)
    odl.append(a)
print(*odl)