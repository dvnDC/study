
file = open("C:\\Users\dvn\\Desktop\\3700.txt", "r")
data = (file.read()).split()
hashtab = {}
mod = int(input())
sum = 0

for word in data:
    for char in word:
        sum = sum + ord(char)
    value = sum // mod
    if value in hashtab.keys():
        hashtab[value].append(word)
    else:
        hashtab[value] = []
        hashtab[value].append(word)
    sum = 0

print(hashtab)