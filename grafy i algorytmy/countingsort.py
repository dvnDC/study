import itertools
import numpy as np

class CountingSort():

    def __init__(self):
        self.word_ascii_dict = {}
        self.word_full_ascii_dict = {}
        self.word_len_dict = {}
        self.ascii_array = []
        self.ascii_array_full = []
        self.matrix_ascii = 0
        self.matrix_out = 0
        self.matrix_final = 0
        self.last_pos = []

        self.getInput()
        self.fillWithZeros()
        self.createArrayFromDictList()
        self.createMatrix()
        self.startCountingSort()
        print(''.join(str(i) for i in self.convertToString()))

    def convertToString(self):
        output = []
        index = len(self.word_len_dict.keys())
        letter = max(self.word_len_dict.values())
        for row in range(index):
            for column in range(letter):
                if not (row == index-1 and  column == letter-1):
                    output.append((chr(self.tmp_matrix[row][column])))
            if row<index-1:
                output.append(" ")
        output.append(chr(int(self.tmp_matrix[-1][-1])).format)

        return output

    def fillWithZeros(self):
        for word, ascii_arr in self.word_ascii_dict.items():
            while len(self.word_ascii_dict[word]) < max(self.word_len_dict.values()):
                self.word_ascii_dict[word].append(0)
        for word, ascii_arr in self.word_full_ascii_dict.items():
            while len(self.word_full_ascii_dict[word]) < max(self.word_len_dict.values()):
                self.word_full_ascii_dict[word].append(0)

    def createArrayFromDictList(self):
        for key, value in (itertools.chain.from_iterable([itertools.product((k,), v) for k, v in self.word_ascii_dict.items()])):
            self.ascii_array.append(value)
        for key, value in (itertools.chain.from_iterable([itertools.product((k,), v) for k, v in self.word_full_ascii_dict.items()])):
            self.ascii_array_full.append(value)


    def getInput(self):
        arr = input().split()
        arr_len = len(arr)
        for word in range(arr_len):
            ascii_arr = [ord(word_ascii) for word_ascii in arr[word].upper()]
            ascii_arr_full = [ord(word_ascii) for word_ascii in arr[word]]
            self.word_ascii_dict[arr[word]] = ascii_arr
            self.word_full_ascii_dict[arr[word]] = ascii_arr_full
            self.word_len_dict[arr[word]] = len(arr[word])

    def createMatrix(self):
        index = len(self.word_len_dict.keys())
        letter = max(self.word_len_dict.values())
        self.matrix_ascii = np.zeros([index, letter], dtype=int)
        self.matrix_out = np.zeros([index, letter], dtype=int)
        self.matrix_final = np.zeros([index, letter], dtype=int)
        self.tmp_matrix = np.zeros([index, letter], dtype=int)
        i = 0
        for row in range(index):
            for column in range(letter):
                self.matrix_ascii[row][column] = self.ascii_array[i]
                self.matrix_final[row][column] = self.ascii_array_full[i]
                i += 1



    def countingSort(self, A, k):
        position = []
        self.last_pos = []
        output = [0] * len(A)

        freq = [0] * k

        for i in A:
            freq[i] = freq[i] + 1

        total = 0
        for i in range(k):
            oldCount = freq[i]
            freq[i] = total
            total += oldCount


        for i in A:
            output[freq[i]] = i
            position.append(freq[i])
            freq[i] = freq[i] + 1

        for row in range(len(position)):
            self.matrix_out[position[row]] = self.matrix_ascii[row]
            self.tmp_matrix[position[row]] = self.matrix_final[row]


    def startCountingSort(self):
        index = len(self.word_len_dict.keys())
        letter = max(self.word_len_dict.values())
        # self.matrix_out = self.matrix_ascii
        for column in range((letter-1),-1,-1):
            arr = self.matrix_ascii[:,column]
            self.countingSort(arr, 128)
            for row in range(index):
                self.matrix_ascii[row] = self.matrix_out[row]
                self.matrix_final[row] = self.tmp_matrix[row]






if __name__ == "__main__":
    CountingSort()




