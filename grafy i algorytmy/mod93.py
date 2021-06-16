L = {}
while True:
    try:
        line = input()
        # if(not line):
        #     break
        h = line.split()
        h2 = []
        [h2.append(int(j)) for j in h[1:]]
        L[int(h[0])] = h2
    except EOFError:
        break

E = []
for i in L:
    for j in L[i]:
        if(not (i, j) in E):
            if (not (j, i) in E):
                E.append((i, j))

R = {}
for i in E:
    R[i] = []

for a, b in R.keys():
    for c, d in R.keys():
        if(not(a == c and b == d)):
            if((d == a and c in L[a]) or (c == b and d in L[b]) or (a == c and d in L[a]) or (b == d and c in L[b])):
                R[(a, b)].append((c, d))

for i in R:
    print(i, end=' ')
    R[i].sort(key=lambda x: x[0])
    print(*R[i])