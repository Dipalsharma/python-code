cs= int(input("Enter cs mark=>"))
java= int(input("Enter java mark=>"))
dbms= int(input("Enter dbms mark=>"))
python= int(input("Enter python mark=>"))
total=cs+java+dbms+python
print("your total marks is==>",cs+java+dbms+python)
if total>80:
    print("//you are pass//.")
else:
    print("//you are fail.//")