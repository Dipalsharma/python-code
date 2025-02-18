age= int(input("Enter age=>"))
if age<12:
    print("you are child")
elif age>=13 and age<=19:
    print("you are teenager")
elif age>=20 and age<=64:
    print("you are adult")
elif age>64:
    print("you are senior")
else:
    print("ERROR")