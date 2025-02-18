bmi= float(input("Enter bmi=>"))
if bmi<18.5:
    print("you are under weight")
elif bmi>=18.5 and bmi<24.9:
    print("you are normal weight")
elif bmi>=25 and bmi<29.9:
    print("you are over weight")
elif bmi>=30:
    print("you are obese")
else:
    print("ERROR")
    