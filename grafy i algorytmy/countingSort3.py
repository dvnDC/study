def countingSort(self, arr):
    position = []

    counts = [0 for i in range(max(arr) + 1)]

    for el in arr:
        counts[el] += 1

    for index in range(1, len(counts)):
        # counts[index] = counts[index - 1] + counts[index]
        counts[index] = counts[index + 1] + counts[index]

    L = [0 for loop in range(len(arr))]
    for el in arr:
        index = counts[el] - 1
        L[index] = el
        # position.append(index)
        counts[el] -= 1
        position.append(counts[el])
    for row in range(len(position)):
        self.matrix_out[position[row]] = self.matrix_ascii[row]

        # litera wartosc, sumowanie liter, potem dodac po kluczach sasiedne wartosci