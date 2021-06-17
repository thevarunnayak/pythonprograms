# Problem 6
# Program to remove the Nth occurence of a given word

list1 = input().split()
word, N = input().split()

count = list1.count(word)

i = 0
index = -1

while count > 0:
    index = list1.index(word, index+1)
    i += 1
    if i == int(N):
        list1.pop(index)
        break
    count -= 1
print(list1)