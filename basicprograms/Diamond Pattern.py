# Program to print the following pattern

# Combination of patterns 1,2,3,4

"""
i/p ->
Ramya

o/p ->
RamyaRamya
Ramy  Ramy
Ram    Ram
Ra      Ra
R        R
Ra      Ra
Ram    Ram
Ramy  Ramy
RamyaRamya
"""

string = input()
l = len(string)

for i in range(l,0,-1):
    print(string[:i] + " "*((l-i)*2) + string[:i][::-1])
for i in range(2,l+1):
    print(string[:i] + " " * ((l - i) * 2) + string[:i][::-1])