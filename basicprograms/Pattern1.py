# Program to print the following pattern
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
# Number of rows depends on the string length

string = input()
length = len(string)

# Iterations

for i in range(length):
    print(string[:i+1])