#table
def table():
    n = int(input("entre table number="))
    i = 1
    while i <= 10:
        print(n, "-", i, "-", n * i)
        i = i + 1
table()



#odd or even number
def oddeven():
    no = int(input("Enter no=>"))
    if no % 2 == 0:
        print(no,"no is even")
    else:
        print(no,"no is odd")
oddeven()



#positive and negative number
def positiv_negative():
    no = int(input("Enter no=>"))
    if no%2==0:
        print("positive")
    else:
        print("negative")
positiv_negative()



#max 3 values
def max():
    a = int(input("Enter no1 =>"))
    b = int(input("Enter no2 =>"))
    c = int(input("Enter no3 =>"))
    if a>b and a>c:
        print("no1 is greater")
    elif b>a and b>c:
        print("no2 is greater")
    elif c>a and c>b:
        print("no3 is greater")
    else:
        print("error")

max()



#fectorial
def fec():
    n = int(input("entre limit="))
    t = 0
    for i in range(1, n + 1):
        print(i, end=" + ")
        t = t + i
    print("\nTotal = ", t)
fec()


#square
def square():
    no1 = int(input("Enter no1 =>"))
    print("squre =", no1 * no1)
square()


#qube
def qube():
    no2 = int(input("Enter no2 =>"))
    print("qube =", no2 * no2 * no2)
qube()

#tringel
def tri():
    height = int(input("Enter height =>"))
    base = int(input("Enter base =>"))
    print("area of tringel=", height * base * 0.5)
tri()


#circle
def circle():
    r = int(input("Enter r =>"))
    print("circle =", 3.14 * r * r)
circle()
