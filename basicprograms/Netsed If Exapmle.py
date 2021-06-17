# Program to check whether if the given number is divisible by 2 & 3

a=int(input("Enter a number: "))

if a%2 == 0:
    if a%3 == 0:
        print(a, "is divisible by 2 & 3.")
    else:
        print(a, "is divisible by 2, not by 3.")
elif a%3 == 0:
    print(a, "is divisible by 3, not by 2.")
else:
    print(a, "is not divisible by both 2 & 3.")