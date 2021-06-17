# Program to find unique elements of a list
# Program to generate a list which contains unique elements

list1 = input().split()
unique_elements = []

for element in list1:
    if element not in unique_elements:
        unique_elements.append(element)

print(unique_elements)

# Here, the o/p elements are in order.