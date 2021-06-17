# Program to arrange the 3 integers in the order max > mid > min

a,b,c=input().split()         # The split user inputs are in str form
a=int(a)                      # Converting str to int
b=int(b)
c=int(c)

d=max(a,b,c)
e=min(a,b,c)
f=(a+b+c)-(d+e)
print(d, ">" ,f, ">" ,e)
print(d,f,e,sep=" > ")