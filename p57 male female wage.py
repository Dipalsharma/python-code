age= int(input("Enter age=>"))
gender= input("Enter gender=>")
if age>=18 and age<30:
    if gender=="male":
     print("male wage==700")
    else:
      print("female==750")
elif age>=30 and age<=40:
    if gender=="male":
        print("male wage==800")
    else:
        print("female wage==850")

