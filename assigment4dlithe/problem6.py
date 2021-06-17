s = input().split()
word, N = input().split()
count = s.count(word)
i = 0
index = -1
while count > 0:
    index = s.index(word, index + 1)
    i += 1

    if i == int(N):
        s.pop(index)
        break
    count -= 1
print(s)
