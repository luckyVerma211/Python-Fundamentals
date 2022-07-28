print("*"*40)
print("SIMPLE INTEREST CALCULATOR")
print("*"*40)
p=int(input("Enter the Principal amount:"))
r=float(input("Enter the rate of interest:"))
t=float(input("Enter the Time period:"))
si=p*r*t/100
am=si+p
print("*"*40)
print("The total interest is:",round(si,2))
print("The total amount is:",round(am,2))
print("*"*40)