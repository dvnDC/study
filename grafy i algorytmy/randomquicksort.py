import random

def quicksort(array, start_index, stop_index):
    if len(array) == 1:
        return array
    if (start_index < stop_index):
        pivotindex = partitionrandom(array, start_index, stop_index)
        quicksort(array, start_index, pivotindex - 1)
        quicksort(array, pivotindex + 1, stop_index)

def partitionrandom(array, start_index, stop_index):
    random_pivot = random.randrange(start_index, stop_index)
    array[start_index], array[random_pivot] = array[random_pivot], array[start_index]
    return partition(array, start_index, stop_index)


def partition(array, start_index, stop_index):
    pivot = start_index
    i = start_index + 1
    for j in range(start_index + 1, stop_index + 1):
        if array[j] <= array[pivot]:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    array[pivot], array[i - 1] = array[i - 1], array[pivot]
    pivot = i - 1
    return pivot


input_array = input().split()
input_array_length = len(input_array)
quicksort(input_array, 0, input_array_length - 1) #array, start index, stop index(last array's element)
print(*input_array, sep=' ')
#O(n log n), najgorszy pojedynczy przypadek dochodzi do O(n^2)