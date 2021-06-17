s2 = input("enter the string 2:")
s1 = input("enter the string 1 :")
M = len(s1)
N = len(s2)
for i in range(N - M + 1):

    for j in range(M):
        if s2[i + j] != s1[j]:
            break

    if j + 1 == M:
        print("no")
    else:
        print("yes")
