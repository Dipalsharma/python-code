print("Press + for addition")
print("Press - for subtraction")
print("Press * for multiplication")
print("Press / for division")
op=input("Enter option for calculation=>")
if op=="+":
    no1 = int(input("Enter no =>"))
    no2 = int(input("Enter no =>"))
    print("addition of 2 number =",no1+no2)
elif op=="-":
    no1 = int(input("Enter no =>"))
    no2 = int(input("Enter no =>"))
    print("sub 2 number =", no1-no2)
elif op =="*":
    no1 = int(input("Enter no =>"))
    no2 = int(input("Enter no =>"))
    print("mul of 4 number  =", no1*no2)
elif op =="/":
    no1 = int(input("Enter no =>"))
    no2 = int(input("Enter no =>"))
    print("div of 5 number  =", no1/no2)
else:
    print("Wrong opt")