n = int(input())
arr = map(int, input().split())
arr = list(set(list(arr)))
a = len(arr)
arr = sorted(arr)
print(arr[a - 2])
