n = int(input())
for i in range(n):
    a, b, K = (map(int, input().split()))
    if a >= b:
        print(K // b)
    else:
        print(K // a)
