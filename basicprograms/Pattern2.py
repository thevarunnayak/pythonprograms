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

# Number of rows depends on the string length

string = input()
length = len(string)

# Iterations

for i in range(length,0,-1):
    print(string[:i])