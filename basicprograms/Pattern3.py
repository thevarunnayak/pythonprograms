"""
i/p ->
Ramya

o/p ->
     R
    Ra
  Ram
 Ramy
Ramya
"""

string = input()
a = len(string)

for i in range(a):
    print(" "*(a-i-1),end = "") # Printing Space, end="" specifies that next print() should be in same line
    print(string[:i+1])