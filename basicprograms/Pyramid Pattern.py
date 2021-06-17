"""
   1
  212
 32123
4321234

Program to print this in a single loop

Time complexity is O(n)

If there are 2 loops, time complexity is O(n^2)
"""

n = int(input())

for i in range(1,n+1):
    print(" "*(n-i),*range(i,1,-1),*range(1,i+1,1),sep="")