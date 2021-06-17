# printing integer triangle
n = int(input())
for i in range(1, n):
    print(int(i * 10 ** i / 9))
