"""
1   5
 2 4
  3

Printing this pattern using a single loop
"""

n = int(input())

if n%2 == 0:
    print()
else:
    for i in range(1, n//2+1):
        print(" " * (i-1), i, " " * (n-i*2), n-i+1, sep="") # sep="" removes extra spaces
    print(" " * (n//2), n//2+1, sep="")