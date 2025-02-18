print("==(list of name)")
list1=["rahi","mansi","naiya","ragahv","neha"]
print(list1)



print("==(list 0f number)")
list2=[44,55,66,7,9,12,33,44]
print(list2)



print("==(list of max , min , sum , len)")
list3=[52,54,21,63,7,5,3,7]
print(max(list3))
print(min(list3))
print(sum(list3))
print(len(list3))



print("==(list of for loop X value)")
list4=[44,55,66,7,9,12,33,44]
for x in list4:
    print(x)



print("list of for loop max")
list5=[44,55,66,7,9,12,33,44]
for x in list5:
    if x<10:
        print(x)



print("list for append")
import random
n=int(input("Enter limit =>"))
list6=[]
for i in range(1,n+1):
    y=random.randint(1,30)
    list6.append(y)
print(list6)


print("list random append")
import random
n=int(input("Enter limit =>"))
list7=[]
for i in range(1,n+1):
    y=random.randint(1,30)
    list7.append(y)
print(list7)
print("max=",max(list7))
print("sum=",sum(list7))