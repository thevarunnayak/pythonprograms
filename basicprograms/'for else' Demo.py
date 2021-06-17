# for else Demo:
# Program to check if the entered number is prime number or not

n = int(input())
if (n==0):
    print("Neither Prime nor Composite")
else:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")