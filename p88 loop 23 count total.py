n=int(input("entre limit="))
c=0
t=0
for i in range(1,n+1):
  if i % 2==0:
    print(i)
    c=c+1
    t=t+i
print("Total = ",t," Count = ",c)

