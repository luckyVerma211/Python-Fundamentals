def area(l,b):                                              #formal paramater
    area=l*b
    return area
def main():
    lrect=int(input("Enter the length of rectangle:"))
    brect=int(input("Enter the breadth of rectangle:"))
    arearec=area(lrect,brect)                               #actual parameter
    print("Area of rectangle",arearec)

if __name__=='__main__':
    main()


