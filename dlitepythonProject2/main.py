# Program to determine if the given year is a leap year or not

a = int(input("Enter the year: "))

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
else:
    print("NO")

