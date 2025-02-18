month= int(input("Enter month=>"))
year= int(input("Enter year=>"))
if month==1:
    print("january has 31 day")
elif month==2:
    if year % 4 == 0:
        print("february has 29 days",year)
    else:
        print("february has 28 days")
elif month==3:
    print("march has 31 day")
elif month==4:
    print("april has 30 days")
elif month==5:
    print("may has 31 days")
elif month==6:
    print("june has 30 days")
elif month==7:
    print("july has 31 days")
elif month==8:
    print("august has 31 days")
elif month==9:
    print("september has 30 days")
elif month==10:
    print("october has 31 days")
elif month==11:
    print("november has 30 days")
elif month==12:
    print("december has 31 days")
else:
    print("not exist")