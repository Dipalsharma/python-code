while True:
    print("Press A for PIZZA")
    print("Press B for fries")
    print("Press C for donuts")
    print("Press D for burger")
    op = input("Enter option =>")
    if op == "A":
        print("480$")
        pizza = int(input("Enter pizza qty =>"))
        print("pizza price =", pizza * 480)
    elif op == "B":
        print("380$")
        frice = int(input("Enter fries qty =>"))
        print("fries price =", frice * 380)
    elif op == "C":
        print("250$")
        donuts = int(input("Enter donuts qty =>"))
        print("donuts price =", donuts * 250)
    elif op == "D":
        print("150$")
        burger = int(input("Enter burger qty =>"))
        print("burger price =", burger * 250)
    elif op =="E":
        print("error")
        break
    else:
        print("Wrong opt")