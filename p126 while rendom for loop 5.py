import random
perfect_answer_count=0
wrong_answer_count=0

for i in range(1,6):
    no1=random.randint(1,10)
    no2=random.randint(1,10)
    print("No1 =",no1," No2 =",no2)
    a=int(input("Enter add =>"))
    if a==no1+no2:
        print("Perfect answer")
        perfect_answer_count=perfect_answer_count+1
    else:
        print("Wrong answer")
        wrong_answer_count = wrong_answer_count + 1

print("perfect answer==",perfect_answer_count)
print("wrong answer==",wrong_answer_count)






