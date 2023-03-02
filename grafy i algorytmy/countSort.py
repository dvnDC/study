class CountSort():
    def __init__(self):
        x = input().split()
        longest = self.checkLongestWord(x)
        xx = self.fillInEmpty(x, longest)
        output = self.radixSort(xx, longest)
        print(output)




    def radixSort(self, arr, longest_word):
        arr2 = []
        for i in range(longest_word -1,-1,-1):
            arr = CountSort(arr,1)
        for i in range(len(arr)):
            arr2.append(arr[i])
        return arr2

    def countSort(self, arr, letter):
        position  = {}
        arr_out = []
        list_of_occurrence = []
        for i in range(len(arr)):
            if arr[i][letter].upper() not in position:
                position[arr[i][letter].upper()] = ord(arr[i][letter].upper())
        for i in range(max(position.values()) + 1):
            list_of_occurrence.append(0)
        for i in range(0, len(arr)):
            list_of_occurrence[position[arr[i]][letter].upper()] = list_of_occurrence[position[arr[i][letter].upper()]] + 1
        for i in range (0, len(arr)):
            arr_out.append(0)
        for i in range(1, len(list_of_occurrence)):
            list_of_occurrence[1] = list_of_occurrence[i] + list_of_occurrence[i-1]
        for i in range(len(arr) - 1, -1, -1):
            arr_out[list_of_occurrence[position[arr[i][letter].upper()]] - 1] = arr[i]
            list_of_occurrence[position[arr[i][letter].upper]] -= 1
        return arr_out


if __name__ == "__main__":
    CountSort()











