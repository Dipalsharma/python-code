print("Press Y for aere of tringel")
print("Press X for aere of circle")
op=input("Enter option =>")
if op=="Y":
    height = int(input("Enter height =>"))
    base = int(input("Enter base =>"))
    print("tringel =",height*base*0.5)
elif op=="X":
    r= int(input("Enter r =>"))
    print("circle =",3.14*r*r)
else:
    print("Wrong opt")