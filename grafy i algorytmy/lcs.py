one = input()
two = input()

pLen = len(one)-1
dLen = len(two)-1

tab = [[-1 for i in range(dLen + 1)] for i in range(pLen + 1)]

def memoLCS(X, Y, m, n, c):

    if m == -1 or n == -1:
        return 0

    if c[m][n] > -1:
        return c[m][n]

    if X[m] == Y[n]:
        c[m][n] = memoLCS(X, Y, m - 1, n - 1, c) + 1
    else:
        c[m][n] = max(memoLCS(X, Y, m, n - 1, c), memoLCS(X, Y, m - 1, n, c))

    return c[m][n]

print(memoLCS(one, two, pLen, dLen, tab))