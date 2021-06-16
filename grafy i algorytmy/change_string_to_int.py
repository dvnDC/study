input_string = input()
input_list = input_string.split()
map_object = map(int, input_list)
output_list = list(map_object)
output_list = output_list[::-1]
print(*output_list, sep=' ')
