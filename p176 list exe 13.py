sample_list = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
greater_than_value = int(input("Enter greater than value: "))
result = []
for num in sample_list:
    if num > greater_than_value:
        result.append(num)
print("Elements greater than", greater_than_value, ":",* result)