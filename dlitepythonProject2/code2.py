# Program to arrange 4 integers in descending order.

a, b, c, d = map(int, input().split())  # Take 4 values in a single line and convert to int

n = [a, b, c, d]
asc = sorted(n)
print(asc[3], ">", asc[2], ">", asc[1], ">", asc[0])
