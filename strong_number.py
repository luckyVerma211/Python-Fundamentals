Num = int(input(" Please Enter any Number: "))
Sum = 0
Temp = Num

while(Temp > 0):
    Factorial = 1
    i = 1
    Reminder = Temp % 10

    while(i <= Reminder):
        Factorial = Factorial * i
        i = i + 1

    print("\n Factorial of %d = %d" %(Reminder, Factorial))
    Sum = Sum + Factorial
    Temp = Temp // 10

print("\n Sum of Factorials of a Given Number %d = %d" %(Num, Sum))
    
if (Sum == Num):
    print(" %d is a Strong Number" %Num)
else:
    print(" %d is not a Strong Number" %Num)