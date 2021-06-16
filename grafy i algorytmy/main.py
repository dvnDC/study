# A 65 a 97 space 32
#  heap
#  dla k Left: 2*k+1
#        Right: 2*k+2


scan_input_array = ""
input_array_ascii = []
sorted_input_array_ascii = []
output_string = ""
word_length = 0
words_count = 1


def changeToString():
    global output_string
    for arrayNr in range(len(arr)):
        if (arrayNr != 0):
            output_string = output_string + " " + str(arr[arrayNr])
        else:
            output_string = output_string + str(arr[arrayNr])
    output_string = output_string.lower()


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


scan_input_array = input()
scan_input_array = scan_input_array.upper()
input_array_length = len(scan_input_array)
for arrayNr in range(input_array_length):
    asciiNr = ord(scan_input_array[arrayNr])
    input_array_ascii.append(asciiNr)
    if (asciiNr == 32):
        words_count += 1
        if (word_length == 0):
            word_length = arrayNr

sortedArray = []
sortedString = ""
for n in range(words_count):
    for l in range(word_length):
        sortedString += chr(input_array_ascii[l+((word_length+1)*n)])
    sortedArray.append(sortedString)
    sortedString = ""

word_number = word_length + 1

arr = sortedArray
heapSort(arr)
changeToString()
print(output_string)

# def switchWords(wordlength, word1_pos, word2_pos):
#     for letterNr in range(wordlength):
#         input_array_ascii[word1_pos + letterNr],input_array_ascii[word2_pos + letterNr] = input_array_ascii[word2_pos + letterNr],input_array_ascii[word1_pos + letterNr]
#
#
# def compareWords(wordlength, word1_pos, word2_pos):
#     for letterNr in range(wordlength):
#         if (input_array_ascii[word1_pos+letterNr] > input_array_ascii[word2_pos+letterNr]):
#             switchWords(wordlength, word1_pos, word2_pos)