a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
L=[a,b,c]
d=max(L)
L.pop(L.index(d))
print(max(L))
