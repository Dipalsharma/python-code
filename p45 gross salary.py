salary= int(input("//Enter salary=>"))
DA=salary*0.52
HRA=salary*0.10
MR=salary*0.10
ITC=salary*0.5
VA=salary*0.10
PF=salary*1000
gross_salary=salary+DA+HRA+MR+ITC+VA
print("DA==0.52")
print("HRA=0.10")
print("MR==0.10")
print("ITC==0.5")
print("VA==0.10")
print("PF==1000")
print("gross salary==",gross_salary)
print("nrt salary==",gross_salary-PF)