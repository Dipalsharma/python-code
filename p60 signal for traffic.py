color= input("Enter color of signal=>")
if color=="green":
    print("car is allowed to go")
elif color == "yellow":
    print("car has to wait")
elif color == "red":
    print("car has to stop")
else:
    print("unrecognized")
