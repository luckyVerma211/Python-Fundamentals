st=[]
def Push(st,val):
    if len(st)>10:
        print("Overflow")
    else:
        st.append(val)
def Pop(st):
    if len(st)==0:
        print("Underflow")
    else:
        val1=st.pop()
        print("Deleted element is:",val1)
def Peek(st):
    print("Top most element is:",st[len(st)-1])

while True:
    print("Press 1 - Push")
    print("Press 2 - Pop")
    print("Press 3 - Peek")
    print("Press 4 - Display")
    print("Press 5 - Quit")
    n = int(input("Enter your choice : "))
    if n == 1:
        val = input("Enter a value to be inserted : ")
        Push(st,val)
    elif n == 2:
        Pop(st)
    elif n == 3:
        Peek(st)
    elif n == 4:
        print(st)
    else:
        break
