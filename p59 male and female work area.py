age= int(input("Enter age=>"))
gender= input("Enter gender=>")
if gender=="female":
     print("female==she will work only in urban area")
elif age>=20 and age<=40:
  if gender=="male":
        print("male==he work anywhere")
  else:
        print("not only single area")
elif age>40 and age<=60:
    if gender == "male":
        print("male==he will work in only urban area")
    else:
        print("not allowed in anywhere")
else:
    print("ERROR")
