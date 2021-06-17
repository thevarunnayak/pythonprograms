# Program to print the following pattern

# It is a combinstion of Pattern 1 & Pattern 3

"""
i/p ->
Ramya

o/p ->
R        R
Ra      Ra
Ram    Ram
Ramy  Ramy
RamyaRamya
"""

string = input()
a= len(string)

for i in range(a):
    print(string[:i+1], end="")
    print(" "*((a-i-1)*2),end = "") # Printing Space, end="" specifies that next print() should be in same line
    print(string[:i+1])

"""
for i in range(a):
    print(string[:i+1],end="")
    print(" " * ((a - i)*2),end="")
    print(string[i::-1])

To print:
R        R  # 8 spaces
Ra      aR  # 6 spaces
Ram    maR  # 4 spaces
Ramy  ymaR  # 2 spaces
RamyaaymaR  # 0 spaces
"""