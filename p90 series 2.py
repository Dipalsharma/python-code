n=int(input("entre limit="))
t=0
for i in range(1,n+1):
    print(i*i,end=" + ")
    t = t + i*i
print("\nTotal = ", t)