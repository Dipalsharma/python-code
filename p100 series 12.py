n=int(input("entre limit="))
total_even=0
count_even=0
total_odd=0
count_odd=0
for i in range(1,n+1):
  if i % 2==0:
    print(i,"is even")
    total_even=total_even+i
    count_even=count_even+i
  else:
    print(i,"is odd")
    total_odd=total_odd+i
    count_odd=count_odd+i
print("\nTotal odd number = ",total_odd, " Count odd number= ", count_odd)
print("\nTotal even number = ",total_even, " Count even number= ", count_even)