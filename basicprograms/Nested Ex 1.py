# Program to demonstrate nested for

n = int(input())

for i in range (n):
    for j in range(n):
        print(j," ", end="") # j all in a row
    print()                  # New line