# Program to print the following pattern

# Combination of patterns 1,2,3,4

"""
i/p ->
Ramya

o/p ->
R        R
Ra      Ra
Ram    Ram
Ramy  Ramy
RamyaRamya
Ramy  Ramy
Ram    Ram
Ra      Ra
R        R

"""

string = input()
l = len(string)

for i in range(1,l):
    print(string[:i] + " "*((l-i)*2) + string[:i][::-1])

for i in range(l,0,-1):
    print(string[:i] + " "*((l-i)*2) + string[:i][::-1])