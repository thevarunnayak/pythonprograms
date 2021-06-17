"""
i/p -> 4

o/p ->
a
ab
abc
abcd

Program to print this pattern in a single loop, i.e. O(n) time complexity
"""

n = int(input())
string = "" # Created an empty string

# Now we should generate first n aplhabets
for i in range(1,n+1):
    string += chr(64+i) # chr(65) = A, chr(66) = B,......so on ; and appending it to the empty string
print(string)

for i in range(1,n+1):
    print(string[:i])

"""
print(string[:i]+ " "*((n-i)*2)+string[:i])

to print
A      A
AB    AB
ABC  ABC
ABCDABCD

for i/p 4
"""