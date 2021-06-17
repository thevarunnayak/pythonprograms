# Program to terminate the iteration
'''
Example 1:

for i in range(10): # 0,1,2,3,4,5,6,7,8,9
    if i%2:         # if i%2 != 0:
        break       # Terminate iteration
    print(i)        # Print the value of i, here 0
'''

# Example 2:
string = 'virat'
for char in string:
    if char in string:
        if char == "t":
            break
        print(char)
'''
string = 'virat'
for _ in string:
    for char in string:
        if char == "r":
            break
        else:
            print(string)
'''