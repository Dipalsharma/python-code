while True:
    print("Press 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    op=int(input("Enter option for calculation=>"))
    if op==1:
        no1 = int(input("Enter no =>"))
        no2 = int(input("Enter no =>"))
        print("addition of 2 number =",no1+no2)
    elif op==2:
        no1 = int(input("Enter no =>"))
        no2 = int(input("Enter no =>"))
        print("sub 2 number =", no1-no2)
    elif op ==3:
        no1 = int(input("Enter no =>"))
        no2 = int(input("Enter no =>"))
        print("mul of 4 number  =", no1*no2)
    elif op ==4:
        no1 = int(input("Enter no =>"))
        no2 = int(input("Enter no =>"))
        print("div of 5 number  =", no1/no2)
    elif op == 5:
        print("error")
        break
    else:
        print("Wrong opt")