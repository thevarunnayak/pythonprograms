# Program to calculate bill
# If amt>5000, discount = 15%


"""
Bill amount : 5000.00
Less (-)    :  750.00
            ----------
Net Amount    4250.00
            ----------
"""

product_name = input("Enter the product name: ")
price = int(input("Enter the price: "))
qty = int(input("Enter the quantity: "))
amt = price * qty
discount = 0
if amt >= 5000:
    discount = 0.15*amt
bill_amt = amt - discount
print("Bill Amount : ",float(amt))
print("Less (-)    : ",discount)
print("             -----------")
print("Net Amount  : ", float(bill_amt))
print("             -----------")