cs= float(input("Enter cs mark=>"))
java= float(input("Enter java mark=>"))
dbms= float(input("Enter dbms mark=>"))
python= float(input("Enter python mark=>"))
total=cs+java+dbms+python
print("your total marks is==>",cs+java+dbms+python)
if total>85:
    print("//you got A grade//.")
elif total>70:
    print("//you got B grade.//")
elif total>25:
    print("//you got c grade.//")
elif total<25:
    print("you are fail")
else:
    print("not exist")