a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
if a>b:
    hi=a
else:
    hi=b
while(True):
    if((hi%a==0) and(hi%b==0)):
         print("The LCM is:",hi)
         break
    hi+=1


