print("*"*40)
print("COMPOUND INTEREST CALCULATOR")
print("*"*40)
p=int(input("Enter the Principal amount:"))
r=float(input("Enter the rate of interest:"))
t=float(input("Enter the Time period:"))
am=p*(1+r/100)**t
ci=am-p
print("*"*40)
print("The total interest is:",round(ci,2))
print("The total amount is:",round(am,2))
print("*"*40)