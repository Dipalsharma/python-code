while True:
    print("Press 1 for square")
    print("Press 2 for cube")
    print("PRess 3 for exit")
    op=int(input("Enter op =>"))
    if op==1:
        no=int(input("Enter no ->"))
        print("Square = ",no*no)
    elif op==2:
        no = int(input("Enter no ->"))
        print("Cube = ", no * no * no)
    elif op==3:
        print("bye")
        break
    else:
        print("Wrong opt")