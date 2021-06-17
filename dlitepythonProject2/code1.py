n = int(input("Enter a positive integer in the range [0,100]: "))

if n == 0:
    print("0")
elif 0 < n <= 100:
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:

        print("Not Weird")
else:
    print()
