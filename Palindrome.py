a=int(input("Enter the number:"))
temp=0
num=a
while num>0:
    d=num%10
    temp=temp*10+d
    num=num//10
if temp==a:
    print(a,"is a Palindrome number!!")
else:
    print(a,"is not a Palindrome number!!")