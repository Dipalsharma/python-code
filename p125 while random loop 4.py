import random
x=random.randint(1,20)
y=random.randint(1,20)
z=random.randint(1,20)
print("No1 = ",x)
print("No2 = ",y)
print("No2 = ",z)
a=int(input("Enter add =>"))
if a==x+y+z:
    print("Perfect answer")
else:
    print("Wrong answer")