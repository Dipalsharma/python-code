import random
x=random.randint(1,10)
print("No = ",x)
a=int(input("Enter square =>"))
if a==x*x:
    print("Perfect")
else:
    print("Wrong answer")