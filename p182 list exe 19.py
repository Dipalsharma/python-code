List_1= [11, 44, 500]
List_2= [77, 44, 11]

common_items = []
for item in List_1:
    if item in List_2:
        common_items.append(item)

print("Common items :", common_items)

