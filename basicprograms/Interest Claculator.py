# Program to calculate interest (Compound Interest)

principal = int(input("Enter the principal amount: "))
rate = float(input("Rate of interest: "))
years = float(input("Number of years: "))

print("1. Simple Interest")
print("2. Compund Interest")
choice = int(input("Enter your choice: "))

if choice == 1:
    interest = principal * rate * years / 100
else:
    interest = (principal * (1 + rate/100)**years) - principal

print("Interest = ",interest)