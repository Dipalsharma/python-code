n=int(input("entre limit="))
t=0
c=0
for i in range(1,n+1):
  if i % 7==0:
    print(i,end=" + ")
    c = c + 1
    t = t + i
print("\nTotal = ", t, " Count = ", c)