# Program to print the following pattern

"""
i/p ->
Ramya

o/p ->
Ramya
 Ramy
  Ram
   Ra
    R
"""

string = input()
a = len(string)

for i in range(a,0,-1):
    print(" " * (a - i),end="")
    print(string[:i])