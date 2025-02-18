sugar_level= int(input("Enter sugar level=>"))
if sugar_level>=80 and sugar_level<=100:
    print("sugar level is low")
elif sugar_level>100:
    print("sugar level normal")
else:
    print("error")