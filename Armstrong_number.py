n=int(input("Enter the number:"))
s=0
a=n
while n>0:
    d=n%10
    s=s+d**3
    n=n//10
if s==a:
    print(a,"is a Armstrong Number!!")
else:
    print(a,"is not a Armstrong Number!!")
