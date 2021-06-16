from math import inf

line = input()
line = line.split(" ")
getLen = len(line)
matryca = []
matryca.append(line)

for i in range(getLen - 1):
    line = input()
    line = line.split(" ")
    matryca.append(line)
for i in range(getLen):
    for j in range(getLen):
        matryca[i][j] = int(matryca[i][j])

poczatek = int(input()) -1

def minOdleglosc(odleglosc, kolejka):

    minimum = inf
    minimum_index = -1

    for i in range(len(odleglosc)):
        if odleglosc[i] < minimum and i in kolejka:
            minimum = odleglosc[i]
            minimum_index = i
    return minimum_index

def dijkstra(graf, poczatek):
    wiersze = len(graf)
    kolumny = len(graf[0])

    odleglosci = [inf] * wiersze

    rodzic = [-1] * wiersze

    odleglosci[poczatek] = 0

    kolejka = []
    for i in range(wiersze):
        kolejka.append(i)

    while kolejka:

        u = minOdleglosc(odleglosci, kolejka)

        kolejka.remove(u)

        for i in range(kolumny):

            if graf[u][i] and i in kolejka:
                if odleglosci[u] + graf[u][i] < odleglosci[i]:
                    odleglosci[i] = odleglosci[u] + graf[u][i]
                    rodzic[i] = u

    return odleglosci

sciezki = dijkstra(matryca, poczatek)

for i in range(len(sciezki)):
    if i == len(sciezki) - 1:
        print(i+1, "=", sciezki[i], end=" ")
    else:
        print(i+1, "=", sciezki[i])