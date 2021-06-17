# Program to print the following pattern

# It is a combinstion of Pattern 2 & Pattern 4

"""
i/p ->
Ramya

o/p ->
RamyaRamya   # 0 spaces
Ramy  Ramy   # 2 spaces
Ram    Ram   # 4 spaces
Ra      Ra   # 6 spaces
R        R   # 8 spaces
"""

string = input()
a = len(string)

for i in range(a,0,-1):
    print(string[:i],end="")
    print(" " * ((a - i)*2),end="")
    print(string[:i])

"""
for i in range(a,0,-1):
    print(string[:i],end="")
    print(" " * ((a - i)*2),end="")
    print(string[::-1])

To print:
RamyaaymaR
Ramy  ymaR
Ram    maR
Ra      aR
R        R
"""