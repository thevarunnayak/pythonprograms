string = input()
l = len(string)

for i in range(0,l):
    print(" "*(i*2) + string[i] + " "*((l-i)*4) + string[i], sep="")

print(" "*12, string[0], sep="")
for i in range(1,l):
    print(" "*((l-i)*2) + string[i] + " "*(i*4) + string[i], sep="")