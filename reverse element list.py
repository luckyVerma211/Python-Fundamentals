def list(l):
    for i in range(0,len(l)-1,2):
        l[i],l[i+1]=l[i+1],l[i]
    return l
        
a=eval(input("Enter the list:"))
print(list(a))