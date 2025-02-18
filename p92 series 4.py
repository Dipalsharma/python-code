n=int(input("entre limit="))
t=0
for i in range(1,n+1):
  if i % 2!=0:
    print(i,end=" + ")
    t = t+i
print("\nTotal = ", t)