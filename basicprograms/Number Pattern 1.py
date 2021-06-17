# Program to print the foll pattern

"""
i/p ->
5

o/p ->
1
12
123
1234
12345

Analysis:
Row  Column
1    1
2    12
3    123
4    1234
5    12345

No.of columns in a row depends on row number
"""
# Method 1:
"""
n = int(input())

for r in range(1,n+1):
    for c in range(1,r+1):
        print(c, end="")
    print()                # Print new line
"""

# Method 2:
n = int(input())

for r in range(0,n+1):
    print(*range(1,r+1),sep="")

"""
if print statement was like print(*range(1,r+1)),if i/p was 5; o/p would be:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

sep = "" gives no separation b/w numbers
"""