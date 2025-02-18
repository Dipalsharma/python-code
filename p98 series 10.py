n=int(input("entre limit="))
t=0
for i in range(2,n+1,2):
    print(i,end=" x ")
    t=t+i
print("\nTotal = ", t)