no= int(input("Enter no=>"))
if no%2==0:
    if no>=2 and no<=5:
        print("not weird")
    elif no>=6 and no<=20:
        print("weird")
    elif no>21:
        print("not weird")
else:
     print("weird")
