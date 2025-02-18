n=int(input("entre limit="))
t=0
for i in range(n,0,-1):
    print(i,end=" + ")
    t=t+i
print("\nTotal = ", t)