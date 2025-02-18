n=int(input("entre limit="))
t=0
for i in range(1,n+1,2):
    t = t + i
    print(i, end="  ")
print("\nTotal = ", t)