# Program to calculate simple interest

p=int(input("Enter the principal amount: "))
n=float(input("Enter the number of years: "))
r=float(input("Enter the interest rate: "))
si=(p*n*r)/100
print("Simple Interest = ", round(si,3))