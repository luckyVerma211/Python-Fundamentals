A=eval(input("Enter the list of numbers:"))
n=len(A)
print("Before Swapping List:",A)

for i in range(n-1):
    for j in range(i+1,n):
        if A[i]<A[j]:
            temp=A[i]
            A[i]=A[j]
            A[j]=temp

print("After Swapping List:",A)
