lst = []
n = int(input("Enter number of elements : "))
for j in range(0, n):
    ele = int(input())
    lst.append(ele)
print(lst)
i = 1
if i < n:
    while i < n and lst[i] > lst[i - 1]:
        i += 1
    while i < n and lst[i] == lst[i - 1]:
        i += 1
    while i < n and lst[i] < lst[i - 1]:
        i += 1
    print("yes")
else:
    print("no")
