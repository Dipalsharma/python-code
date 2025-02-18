print("Press 1 for battery-based toy")
print("Press 2 for key-based toy")
print("Press 3 for electrical charging based toy")
op=int(input("Enter option =>"))
if op==1:
    bill = int(input("bill =>"))
    if bill>=1000:
        amt=bill*10/100
        print("give 10% discount",amt)
        print("final price",bill-amt)
    else:
        print("no discount")
elif op==2:
    bill = int(input("bill =>"))
    if bill>=100:
        amt = bill * 10 / 100
        print("give 5% discount",amt)
        print("final price", bill - amt)
    else:
        print("no discount")
elif op ==3:
    bill = int(input("bill =>"))
    if bill>=500:
        amt = bill * 10 / 100
        print("give 10% discount",amt)
        print("final price", bill - amt)
    else:
        print("no discount")
else:
    print("Wrong opt")



