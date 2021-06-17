list1 = list(map(int,input().split()))
sq_list = [element * element if element % 2 == 0 else element for element in list1]
print(sq_list)