# Program to calculate the simple interest

P = int(input("Enter the principal amount: "))
T = float(input("Enter the number of years: "))
R = float(input("Enter the interest rate: "))
SI = (P*T*R)/100
print("Simple Interest = ", round(SI, 3))