marked_price= int(input("Enter price=>"))
if marked_price>=10000:
    print("discount 20%",marked_price*20/100)
elif marked_price>7000<=10000:
    print("discount 15%",marked_price*15/100)
elif marked_price>=7000:
    print("discount 10%",marked_price*10/100)
else:
    print("not discount")