print("Press Y for area of triangle")
print("Press X for area of circle")
op=input("Enter option =>")
if op=="Y":
    height = int(input("Enter height =>"))
    base = int(input("Enter base =>"))
    print("triangle =",height*base*0.5)
elif op=="X":
    r= int(input("Enter r =>"))
    print("circle =",3.14*r*r)
else:
    print("Wrong opt")

